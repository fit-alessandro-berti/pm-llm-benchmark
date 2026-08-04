#!/usr/bin/env python3
"""
Embed answer files from ../answers/ using OpenAI's text-embedding-3-large model.

Reads OPENAI_API_KEY from the environment. Writes one JSON file per answer
(a list of floats) into ./output/, preserving the answer basename.

Uses only the standard library and the `requests` package. Processes up to
MAX_WORKERS files concurrently.
"""

from __future__ import annotations

import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
ANSWERS_DIR = REPO_ROOT / "answers"
OUTPUT_DIR = SCRIPT_DIR / "output"

# Best general-purpose OpenAI embedding model (highest quality).
MODEL = "text-embedding-3-large"
API_URL = "https://api.openai.com/v1/embeddings"

# Max concurrent API requests.
MAX_WORKERS = 100

# text-embedding-3-large accepts at most 8192 tokens. Without a tokenizer we
# keep the last ~16000 characters (~2 chars/token), which stays under the limit
# for typical English/technical text.
MAX_INPUT_CHARS = 16_000

# HTTP behaviour
REQUEST_TIMEOUT_S = 120
MAX_RETRIES = 5
RETRY_BASE_DELAY_S = 2.0

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_print_lock = threading.Lock()


def log(msg: str) -> None:
    with _print_lock:
        print(msg, flush=True)


def require_api_key() -> str:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.stderr.write(
            "error: OPENAI_API_KEY environment variable is not set\n"
        )
        sys.exit(1)
    return key


def list_answer_files() -> list[Path]:
    if not ANSWERS_DIR.is_dir():
        sys.stderr.write(f"error: answers directory not found: {ANSWERS_DIR}\n")
        sys.exit(1)
    files = sorted(
        p for p in ANSWERS_DIR.iterdir() if p.is_file() and p.suffix == ".txt"
    )
    if not files:
        sys.stderr.write(f"error: no .txt answer files in {ANSWERS_DIR}\n")
        sys.exit(1)
    return files


def output_path_for(answer_path: Path) -> Path:
    # Corresponding file: same stem, JSON array of floats.
    return OUTPUT_DIR / f"{answer_path.stem}.json"


def read_answer_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace").strip()
    if len(text) > MAX_INPUT_CHARS:
        # Keep the trailing portion (conclusions / final answer tend to land here).
        text = text[-MAX_INPUT_CHARS:]
    return text


def embed_text(session: requests.Session, api_key: str, text: str) -> list[float]:
    """Call the OpenAI embeddings API with basic retry on rate limits / 5xx."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "input": text,
    }

    last_error: Exception | str | None = None
    for attempt in range(MAX_RETRIES):
        try:
            resp = session.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=REQUEST_TIMEOUT_S,
            )
        except requests.RequestException as exc:
            last_error = exc
            delay = RETRY_BASE_DELAY_S * (2 ** attempt)
            log(f"  network error ({exc}); retry in {delay:.1f}s")
            time.sleep(delay)
            continue

        if resp.status_code == 200:
            data = resp.json()
            try:
                return data["data"][0]["embedding"]
            except (KeyError, IndexError, TypeError) as exc:
                raise RuntimeError(
                    f"unexpected API response shape: {data!r}"
                ) from exc

        # Retryable statuses
        if resp.status_code in (429, 500, 502, 503, 504):
            last_error = f"HTTP {resp.status_code}: {resp.text[:300]}"
            # Honour Retry-After when present.
            retry_after = resp.headers.get("Retry-After")
            if retry_after and retry_after.isdigit():
                delay = float(retry_after)
            else:
                delay = RETRY_BASE_DELAY_S * (2 ** attempt)
            log(f"  {last_error}; retry in {delay:.1f}s")
            time.sleep(delay)
            continue

        raise RuntimeError(
            f"OpenAI API error HTTP {resp.status_code}: {resp.text[:500]}"
        )

    raise RuntimeError(f"failed after {MAX_RETRIES} retries: {last_error}")


# One Session per worker thread (a single Session must not be shared across
# threads for concurrent requests).
_thread_local = threading.local()


def _get_session() -> requests.Session:
    sess = getattr(_thread_local, "session", None)
    if sess is None:
        sess = requests.Session()
        _thread_local.session = sess
    return sess


def process_one(
    api_key: str,
    answer_path: Path,
    skip_existing: bool,
) -> tuple[str, str]:
    """
    Embed a single answer file.

    Returns (status, detail) where status is 'ok' | 'skip' | 'error'.
    """
    out_path = output_path_for(answer_path)
    name = answer_path.name

    if skip_existing and out_path.exists():
        return "skip", name

    try:
        text = read_answer_text(answer_path)
        if not text:
            return "error", f"{name}: empty file"

        embedding = embed_text(_get_session(), api_key, text)

        # Atomic-ish write: temp then rename.
        tmp_path = out_path.with_suffix(out_path.suffix + ".tmp")
        tmp_path.write_text(
            json.dumps(embedding, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        tmp_path.replace(out_path)
        return "ok", f"{name} -> {out_path.name} (dim={len(embedding)})"
    except Exception as exc:  # noqa: BLE001 — surface any failure per file
        return "error", f"{name}: {exc}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    api_key = require_api_key()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    skip_existing = "--force" not in sys.argv
    if "--force" in sys.argv:
        log("re-embedding all files (--force)")

    files = list_answer_files()
    log(
        f"embedding {len(files)} answer file(s) with {MODEL} "
        f"(max {MAX_WORKERS} concurrent workers)"
    )
    log(f"answers: {ANSWERS_DIR}")
    log(f"output:  {OUTPUT_DIR}")

    ok = skip = err = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {
            pool.submit(process_one, api_key, path, skip_existing): path
            for path in files
        }
        for fut in as_completed(futures):
            status, detail = fut.result()
            if status == "ok":
                ok += 1
                log(f"[ok]    {detail}")
            elif status == "skip":
                skip += 1
                log(f"[skip]  {detail}")
            else:
                err += 1
                log(f"[error] {detail}")

    log(f"done: {ok} written, {skip} skipped, {err} errors")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
