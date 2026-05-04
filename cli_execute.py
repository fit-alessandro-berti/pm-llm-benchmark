#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict


REPO_ROOT = Path(__file__).resolve().parent
MODELS_CONFIG_PATH = REPO_ROOT / "models_config.json"

PROVIDER_API_URLS = {
    "openrouter": "https://openrouter.ai/api/v1/",
    "openai": "https://api.openai.com/v1/",
    "google": "https://generativelanguage.googleapis.com/v1beta/",
    "claude": "https://api.anthropic.com/v1/",
    "anthropic": "https://api.anthropic.com/v1/",
    "grok": "https://api.x.ai/v1/",
    "x-ai": "https://api.x.ai/v1/",
    "mistral": "https://api.mistral.ai/v1/",
    "deepinfra": "https://api.deepinfra.com/v1/openai/",
    "qwen": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/",
    "nvidia": "https://integrate.api.nvidia.com/v1/",
    "perplexity": "https://api.perplexity.ai/",
    "groq": "https://api.groq.com/openai/v1/",
}

PROVIDER_API_KEY_ENVS = {
    "openrouter": "OPENROUTER_API_KEY",
    "openai": "OPENAI_API_KEY",
    "google": "GOOGLE_API_KEY",
    "claude": "ANTHROPIC_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "grok": "GROK_API_KEY",
    "x-ai": "GROK_API_KEY",
    "mistral": "MISTRAL_API_KEY",
    "deepinfra": "DEEPINFRA_API_KEY",
    "qwen": "QWEN_API_KEY",
    "nvidia": "NVIDIA_API_KEY",
    "perplexity": "PERPLEXITY_API_KEY",
    "groq": "GROQ_API_KEY",
}

PROVIDER_API_KEY_FILES = {
    "openrouter": "../api_openrouter.txt",
    "openai": "../api_openai.txt",
    "google": "../api_google.txt",
    "claude": "../api_anthropic.txt",
    "anthropic": "../api_anthropic.txt",
    "grok": "../api_grok.txt",
    "x-ai": "../api_grok.txt",
    "mistral": "../api_mistral.txt",
    "deepinfra": "../api_deepinfra.txt",
    "qwen": "../api_qwen.txt",
    "nvidia": "../api_nvidia.txt",
    "perplexity": "../api_perplexity.txt",
    "groq": "../api_groq.txt",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Execute pm-llm-benchmark for one target model.")
    parser.add_argument("model_name", help="Model alias to benchmark.")
    parser.add_argument("--provider", default="openrouter", help="Model provider. Defaults to openrouter.")
    parser.add_argument("--base-model", help="Underlying API model. Defaults to model_name.")
    parser.add_argument("--alias", help="Alias used inside the benchmark. Defaults to model_name.")
    parser.add_argument("--api-url", help="Override API URL.")
    parser.add_argument("--api-key-env", help="Environment variable containing the API key.")
    parser.add_argument("--api-key-file", help="Path to a file containing the API key.")
    parser.add_argument("--reasoning-effort", help="Optional reasoning effort.")
    parser.add_argument("--thinking-tokens", type=int, help="Optional Anthropic thinking token budget.")
    parser.add_argument("--temperature", type=float, help="Optional sampling temperature.")
    parser.add_argument("--max-tokens", type=int, help="Optional max token cap.")
    parser.add_argument("--system-prompt", help="Optional system prompt.")
    parser.add_argument("--add-prompt", help="Optional prompt suffix.")
    parser.add_argument("--payload-json", help="JSON object merged into added_to_payload.")
    parser.add_argument("--tools-json", help="JSON payload for the manual tools field.")
    parser.add_argument("--config-json", help="Extra JSON object merged into the config.")
    parser.add_argument("--config-file", help="Path to a JSON file merged into the config.")
    parser.add_argument(
        "--skip-git-reset-clean",
        action="store_true",
        help="Skip the destructive git reset/git clean preflight and only git pull.",
    )
    parser.add_argument("--python", default=sys.executable, help="Python executable for subprocess phases.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without executing them.")
    return parser


def merge_dicts(base: Dict[str, Any], extra: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict(base)
    for key, value in extra.items():
        if isinstance(merged.get(key), dict) and isinstance(value, dict):
            merged[key] = merge_dicts(merged[key], value)
        else:
            merged[key] = value
    return merged


def parse_json_object(raw: str | None, label: str) -> Dict[str, Any]:
    if not raw:
        return {}
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise ValueError(f"{label} must decode to a JSON object.")
    return parsed


def load_runtime_config(args: argparse.Namespace) -> Dict[str, Any]:
    config: Dict[str, Any] = {}
    if args.config_file:
        with open(args.config_file, "r", encoding="utf-8") as handler:
            file_config = json.load(handler)
        if not isinstance(file_config, dict):
            raise ValueError("config-file must contain a JSON object.")
        config = merge_dicts(config, file_config)
    config = merge_dicts(config, parse_json_object(args.config_json, "config-json"))

    if args.payload_json:
        config["added_to_payload"] = merge_dicts(
            config.get("added_to_payload", {}),
            parse_json_object(args.payload_json, "payload-json"),
        )
    if args.tools_json:
        config["tools"] = json.loads(args.tools_json)

    config.setdefault("provider", args.provider)
    config.setdefault("alias", args.alias or args.model_name)
    config.setdefault("base_model", args.base_model or args.model_name)
    config.setdefault("api_url", args.api_url or PROVIDER_API_URLS.get(config["provider"]))
    config.setdefault("api_key_env", args.api_key_env or PROVIDER_API_KEY_ENVS.get(config["provider"]))
    if args.api_key_file:
        config["api_key_file"] = args.api_key_file
    if args.reasoning_effort is not None:
        config["reasoning_effort"] = args.reasoning_effort
    if args.thinking_tokens is not None:
        config["thinking_tokens"] = args.thinking_tokens
    if args.temperature is not None:
        config["temperature"] = args.temperature
    if args.max_tokens is not None:
        config["max_tokens"] = args.max_tokens
    if args.system_prompt is not None:
        config["system_prompt"] = args.system_prompt
    if args.add_prompt is not None:
        config["added_to_prompt"] = args.add_prompt

    return config


def read_api_key(config: Dict[str, Any]) -> str | None:
    api_key_file = config.get("api_key_file")
    if api_key_file:
        with open(api_key_file, "r", encoding="utf-8") as handler:
            return handler.read().strip()

    api_key_env = config.get("api_key_env")
    if api_key_env and api_key_env in os.environ:
        return os.environ[api_key_env]

    fallback_path = PROVIDER_API_KEY_FILES.get(config["provider"])
    if fallback_path:
        candidate = (REPO_ROOT / fallback_path).resolve()
        if candidate.exists():
            with open(candidate, "r", encoding="utf-8") as handler:
                return handler.read().strip()

    return None


def needs_manual_entry(config: Dict[str, Any]) -> bool:
    simple_alias = config["alias"] == config["base_model"] == config["model_name"]
    managed_fields = {
        "model_name",
        "provider",
        "alias",
        "base_model",
        "api_url",
        "api_key_env",
        "api_key_file",
    }
    extra_fields = [key for key in config if key not in managed_fields]
    return (not simple_alias) or bool(extra_fields)


def ensure_model_registered(config: Dict[str, Any], dry_run: bool) -> None:
    with open(MODELS_CONFIG_PATH, "r", encoding="utf-8") as handler:
        models_config = json.load(handler)

    provider = config["provider"]
    alias = config["alias"]

    if provider not in models_config:
        raise ValueError(f"Provider {provider!r} is not present in {MODELS_CONFIG_PATH}.")

    provider_models = models_config[provider].setdefault("models", [])
    manual_models = models_config.setdefault("manual", {}).setdefault("models", {})

    clean = lambda model_name: model_name.replace("/", "").replace(":", "")
    already_present = clean(alias) in {clean(item) for item in provider_models}
    already_present = already_present or clean(alias) in {clean(key) for key in manual_models}
    if already_present:
        return

    if needs_manual_entry(config):
        manual_entry: Dict[str, Any] = {
            "provider": provider,
            "base_model": config["base_model"],
        }
        for key in (
            "system_prompt",
            "thinking_tokens",
            "reasoning_effort",
            "temperature",
            "max_tokens",
            "added_to_prompt",
            "tools",
            "added_to_payload",
        ):
            if key in config:
                manual_entry[key] = config[key]
        manual_models[alias] = manual_entry
    else:
        provider_models.append(config["model_name"])

    if dry_run:
        return

    with open(MODELS_CONFIG_PATH, "w", encoding="utf-8") as handler:
        json.dump(models_config, handler, indent=2)
        handler.write("\n")


def run_subprocess(command: list[str], cwd: Path, dry_run: bool) -> None:
    print("+", " ".join(command))
    if dry_run:
        return
    subprocess.run(command, cwd=str(cwd), check=True)


def sync_repository(dry_run: bool, skip_git_reset_clean: bool) -> None:
    git_commands = []
    if not skip_git_reset_clean:
        git_commands.extend(
            [
                ["git", "reset", "--hard", "HEAD"],
                ["git", "clean", "-x", "-f"],
            ]
        )
    git_commands.append(["git", "pull"])
    for command in git_commands:
        run_subprocess(command, cwd=REPO_ROOT, dry_run=dry_run)


def apply_shared_settings(common_module: Any, config: Dict[str, Any]) -> None:
    common_module.Shared.SYSTEM_PROMPT = config.get("system_prompt")
    common_module.Shared.ANTHROPIC_THINKING_TOKENS = config.get("thinking_tokens")
    common_module.Shared.PAYLOAD_REASONING_EFFORT = config.get("reasoning_effort")
    common_module.Shared.CUSTOM_TEMPERATURE = config.get("temperature")
    common_module.Shared.MAX_REQUESTED_TOKENS = config.get("max_tokens", 32000)
    common_module.Shared.ADDED_TO_PROMPT = config.get("added_to_prompt")
    common_module.Shared.TOOLS_PAYLOAD = config.get("tools")
    common_module.Shared.ADDED_TO_PAYLOAD = config.get("added_to_payload")


def reset_shared_settings(common_module: Any) -> None:
    common_module.Shared.SYSTEM_PROMPT = None
    common_module.Shared.ANTHROPIC_THINKING_TOKENS = None
    common_module.Shared.PAYLOAD_REASONING_EFFORT = None
    common_module.Shared.CUSTOM_TEMPERATURE = None
    common_module.Shared.MAX_REQUESTED_TOKENS = 32000
    common_module.Shared.ADDED_TO_PROMPT = None
    common_module.Shared.TOOLS_PAYLOAD = None
    common_module.Shared.ADDED_TO_PAYLOAD = None


def import_benchmark_modules() -> tuple[Any, Any]:
    original_argv = sys.argv[:]
    try:
        # pm-llm-benchmark/common.py reads ANSWERING_MODEL_NAME and
        # EVALUATING_MODEL_NAME directly from sys.argv positional entries.
        # This wrapper should not feed its own flags into that path.
        sys.argv = [original_argv[0]]
        common_module = importlib.import_module("common")
        answer_module = importlib.import_module("answer")
        return common_module, answer_module
    finally:
        sys.argv = original_argv


def execute_pipeline(config: Dict[str, Any], python_executable: str, dry_run: bool) -> None:
    if dry_run:
        print(f"Would execute pm-llm-benchmark for alias={config['alias']} base_model={config['base_model']}")
        return

    common_module, answer_module = import_benchmark_modules()

    common_module.insert_api_keys()
    answer_module.configure_rate_limiter(
        requests_per_minute=50,
        requests_per_hour=1000,
        tokens_per_minute=90000,
        tokens_per_hour=2000000,
        max_concurrent=50,
    )

    api_key = read_api_key(config)
    api_url = config.get("api_url") or common_module.MODELS_DICT[config["provider"]]["api_url"]

    try:
        apply_shared_settings(common_module, config)
        answer_module.answer_question(
            config["base_model"],
            api_url=api_url,
            api_key=api_key,
            alias_model_name=config["alias"],
            use_multithreading=answer_module.USE_MULTITHREADING,
        )
    finally:
        reset_shared_settings(common_module)

    run_subprocess(
        [python_executable, "utils/perform_mass_eval.py", "--exit-on-no-changes"],
        cwd=REPO_ROOT,
        dry_run=False,
    )

    target_prefix = common_module.clean_model_name(config["alias"]) + "_"
    base_evaluation_path = REPO_ROOT / common_module.get_base_evaluation_path(
        common_module.clean_model_name(common_module.EVALUATING_MODEL_NAME)
    )

    with tempfile.TemporaryDirectory(prefix="pm_hallucinations_", dir=str(REPO_ROOT / "hallucinations")) as tmp_dir:
        temp_input_dir = Path(tmp_dir)
        for source_file in base_evaluation_path.iterdir():
            if source_file.is_file() and source_file.name.startswith(target_prefix):
                shutil.copy2(source_file, temp_input_dir / source_file.name)

        run_subprocess(
            [
                python_executable,
                "detect.py",
                "--input_dir",
                str(temp_input_dir),
                "--output_dir",
                str(REPO_ROOT / "hallucinations" / "output"),
            ],
            cwd=REPO_ROOT / "hallucinations",
            dry_run=False,
        )

    for script_name in ("aggregate.py", "CORRELATION.py", "validate_models.py"):
        run_subprocess([python_executable, script_name], cwd=REPO_ROOT / "hallucinations", dry_run=False)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    config = load_runtime_config(args)
    config["model_name"] = args.model_name

    sync_repository(args.dry_run, args.skip_git_reset_clean)
    ensure_model_registered(config, args.dry_run)
    execute_pipeline(config, python_executable=args.python, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
