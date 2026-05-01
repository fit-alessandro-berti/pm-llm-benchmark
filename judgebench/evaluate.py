import argparse
import csv
import logging
import os
import threading
import time
from concurrent.futures import Future, ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import requests

from benchlib import sanitize_name


OPENROUTER_CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"
RETRY_SLEEP_SECONDS = 15
REQUEST_TIMEOUT_SECONDS = 600
MAX_CONCURRENT_THREADS = 100

# Edit this list to add judges. ("provider/model",) uses OpenRouter by default.
# ("model", {"api_url": "...", "api_key": "...", "additional_payload": {...}}) overrides it.
JUDGE_LLMS: Sequence[Tuple[Any, ...]] = [
    (
        "gpt-5.4",
        {
            "api_url": "https://api.openai.com/v1/responses",
            "api_key": os.environ.get("OPENAI_API_KEY", ""),
            "additional_payload": {"reasoning": {"effort": "medium"}},
        },
    ),
    (
        "gpt-5.4-mini",
        {
            "api_url": "https://api.openai.com/v1/responses",
            "api_key": os.environ.get("OPENAI_API_KEY", ""),
            "additional_payload": {"reasoning": {"effort": "medium"}},
        },
    ),
    (
        "gpt-5.5",
        {
            "api_url": "https://api.openai.com/v1/responses",
            "api_key": os.environ.get("OPENAI_API_KEY", ""),
            "additional_payload": {"reasoning": {"effort": "medium"}},
        },
    ),
    (
        "grok-4.20-0309-reasoning",
        {"api_url": "https://api.x.ai/v1/responses", "api_key": os.environ["GROK_API_KEY"]},
    ),
    (
        "grok-4.20-0309-non-reasoning",
        {"api_url": "https://api.x.ai/v1/responses", "api_key": os.environ["GROK_API_KEY"]},
    ),
    (
        "grok-4-1-fast-reasoning",
        {"api_url": "https://api.x.ai/v1/responses", "api_key": os.environ["GROK_API_KEY"]},
    ),
    (
        "grok-4-fast-reasoning",
        {"api_url": "https://api.x.ai/v1/responses", "api_key": os.environ["GROK_API_KEY"]},
    ),
    (
        "grok-4.3",
        {"api_url": "https://api.x.ai/v1/responses", "api_key": os.environ["GROK_API_KEY"]},
    ),
    (
        "anthropic/claude-opus-4.7",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"], "additional_payload": {"reasoning": {"enabled": True}}}
    ),
    (
        "google/gemini-3.1-pro-preview",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"]}
    ),
    (
        "google/gemini-2.5-pro",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"]}
    ),
    (
        "deepseek/deepseek-v4-pro",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"],
         "additional_payload": {"reasoning": {"enabled": True}}}
    ),
    (
        "deepseek-v4-pro",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"],
         "additional_payload": {"reasoning": {"enabled": False}}}
    ),
    (
        "qwen/qwen3.6-35b-a3b",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"],
         "additional_payload": {"reasoning": {"effort": "low"}}}
    ),
    (
        "qwen/qwen3.6-plus",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"],
         "additional_payload": {"reasoning": {"effort": "low"}}}
    ),
    (
        "moonshotai/kimi-k2.6",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"],
         "additional_payload": {"reasoning": {"effort": "medium"}}}
    ),
    (
        "kimi-k2.6",
        {"api_url": "https://openrouter.ai/api/v1/chat/completions", "api_key": os.environ["OPENROUTER_API_KEY"],
         "additional_payload": {"reasoning": {"enabled": False}}}
    ),
]

STRICT_EVALUATION_TEXT = (
    "Please evaluate with the utmost strictness. Be hypercritical of any inaccuracies, "
    "unclarities, or logical flaws. Even minor issues should result in a significantly "
    "lower score. Only award a very high score if the answer is nearly flawless."
)

_executor = ThreadPoolExecutor(max_workers=MAX_CONCURRENT_THREADS)
_write_lock = threading.Lock()
_logger = logging.getLogger(__name__)


def _load_selected_answers(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"question", "copied_answer_file", "copied_question_file"}
        if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
            raise ValueError(f"Selected answers CSV must contain {sorted(required)}: {path}")
        return [row for row in reader if row.get("copied_answer_file") and row.get("copied_question_file")]


def _build_judge_prompt(question: str, answer: str) -> str:
    return (
        "Given the following question:\n\n"
        f"{question}\n\n"
        "How would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? "
        "Please put the grade at the beginning of the response. "
        f"{STRICT_EVALUATION_TEXT}\n\n"
        f"{answer}"
    )


def _read_text_resilient(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        with path.open("r") as file:
            return file.read()


def _extract_text_from_api_response(response_json: Dict[str, Any], is_responses_api: bool) -> str:
    if not is_responses_api:
        content = response_json["choices"][0]["message"]["content"]
        return content if isinstance(content, str) else str(content)

    output_text = response_json.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text

    output = response_json.get("output")
    if isinstance(output, list):
        chunks: List[str] = []
        for item in output:
            if not isinstance(item, dict):
                continue
            content_items = item.get("content")
            if not isinstance(content_items, list):
                continue
            for content_item in content_items:
                if isinstance(content_item, dict) and isinstance(content_item.get("text"), str):
                    chunks.append(content_item["text"])
        if chunks:
            return "".join(chunks)

    raise ValueError("Could not extract text content from API response.")


def _submit_and_write_with_retries(
    prompt: str,
    destination_path: str,
    llm_model: str,
    api_url: str,
    api_key: str,
    additional_payload: Optional[Dict[str, Any]],
) -> None:
    if not api_key:
        raise ValueError(f"No API key configured for judge {llm_model}.")

    is_responses_api = "/responses" in api_url.lower()
    if is_responses_api:
        payload: Dict[str, Any] = {"model": llm_model, "input": prompt}
    else:
        payload = {"model": llm_model, "messages": [{"role": "user", "content": prompt}]}
    if additional_payload:
        payload.update(additional_payload)

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    attempt = 0
    while True:
        attempt += 1
        started = time.time_ns()
        try:
            response = requests.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
            text = _extract_text_from_api_response(response.json(), is_responses_api)
            if not text.strip():
                raise ValueError("Received empty response from judge.")

            destination = Path(destination_path)
            destination.parent.mkdir(parents=True, exist_ok=True)
            with _write_lock:
                destination.write_text(text, encoding="utf-8")

            elapsed = (time.time_ns() - started) / 10**9
            _logger.info(
                "Completed JudgeBench request | judge=%s destination=%s attempt=%d response_time_s=%.3f",
                llm_model,
                destination_path,
                attempt,
                elapsed,
            )
            return
        except Exception as exc:
            elapsed = (time.time_ns() - started) / 10**9
            _logger.warning(
                "JudgeBench request failed | judge=%s destination=%s attempt=%d response_time_s=%.3f error=%s",
                llm_model,
                destination_path,
                attempt,
                elapsed,
                exc,
            )
            time.sleep(RETRY_SLEEP_SECONDS)


def submit_prompt_to_chat_completions(
    prompt: str,
    destination_path: str,
    llm_model: str,
    api_url: str = OPENROUTER_CHAT_COMPLETIONS_URL,
    api_key: Optional[str] = None,
    additional_payload: Optional[Dict[str, Any]] = None,
) -> Future:
    if api_key is None:
        api_key = os.environ.get("OPENROUTER_API_KEY", "")
    return _executor.submit(
        _submit_and_write_with_retries,
        prompt,
        destination_path,
        llm_model,
        api_url,
        api_key,
        additional_payload,
    )


def _parse_judge_entries(only: Optional[str]) -> Sequence[Tuple[Any, ...]]:
    if only is None:
        return JUDGE_LLMS
    requested = {value.strip() for value in only.split(",") if value.strip()}
    return tuple(entry for entry in JUDGE_LLMS if entry and str(entry[0]) in requested)


def _parse_judge_options(judge_entry: Tuple[Any, ...]) -> Dict[str, object]:
    kwargs: Dict[str, object] = {}
    for option in judge_entry[1:]:
        if option is None:
            continue
        if isinstance(option, dict):
            kwargs.update(option)
            continue
        raise ValueError(f"Unsupported judge option for {judge_entry[0]}: {option!r}")
    return kwargs


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(description="Evaluate JudgeBench reference answers with judge LLMs.")
    parser.add_argument(
        "--selected-csv",
        type=Path,
        default=script_dir / "selected_answers.csv",
        help="CSV produced by select_references.py. Defaults to judgebench/selected_answers.csv.",
    )
    parser.add_argument(
        "--answers-dir",
        type=Path,
        default=script_dir / "answers",
        help="JudgeBench answers directory. Defaults to judgebench/answers.",
    )
    parser.add_argument(
        "--questions-dir",
        type=Path,
        default=script_dir / "questions",
        help="JudgeBench questions directory. Defaults to judgebench/questions.",
    )
    parser.add_argument(
        "--evaluations-dir",
        type=Path,
        default=script_dir / "evaluations",
        help="Output directory for judge evaluation TXT files. Defaults to judgebench/evaluations.",
    )
    parser.add_argument(
        "--only",
        default=None,
        help="Comma-separated exact judge names from JUDGE_LLMS to run.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s - %(message)s")
    logger = logging.getLogger("judgebench.evaluate")

    selected_rows = _load_selected_answers(args.selected_csv)
    judge_entries = _parse_judge_entries(args.only)
    if not judge_entries:
        raise ValueError("No judges selected.")

    args.evaluations_dir.mkdir(parents=True, exist_ok=True)
    pending: List[Tuple[Future, str, str]] = []

    for judge_entry in judge_entries:
        judge_model = str(judge_entry[0])
        judge_key = sanitize_name(judge_model)
        kwargs = _parse_judge_options(judge_entry)

        for row in selected_rows:
            copied_answer_file = row["copied_answer_file"]
            copied_question_file = row["copied_question_file"]
            answer_path = args.answers_dir / copied_answer_file
            question_path = args.questions_dir / copied_question_file

            if not answer_path.is_file():
                logger.warning("Skipping missing answer: %s", answer_path)
                continue
            if not question_path.is_file():
                logger.warning("Skipping missing question: %s", question_path)
                continue

            output_path = args.evaluations_dir / f"{judge_key}_{copied_answer_file}"
            output_path = output_path.with_suffix(".txt")
            if output_path.exists():
                continue

            question_text = _read_text_resilient(question_path)
            answer_text = _read_text_resilient(answer_path)
            judge_prompt = _build_judge_prompt(question_text, answer_text)

            logger.info(
                "Submitting JudgeBench evaluation | judge=%s answer=%s destination=%s",
                judge_model,
                copied_answer_file,
                output_path,
            )
            future = submit_prompt_to_chat_completions(
                prompt=judge_prompt,
                destination_path=str(output_path),
                llm_model=judge_model,
                **kwargs,
            )
            pending.append((future, judge_model, copied_answer_file))

    if pending:
        logger.info("Submitted %d JudgeBench requests. Waiting for completion.", len(pending))
        for future, judge_model, copied_answer_file in pending:
            future.result()
            logger.info("Finished JudgeBench evaluation | judge=%s answer=%s", judge_model, copied_answer_file)

    logger.info("All done.")


if __name__ == "__main__":
    main()
