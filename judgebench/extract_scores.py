import argparse
import csv
import logging
from pathlib import Path
from typing import Dict

from benchlib import (
    model_key_from_filename,
    parse_pm_score,
    question_stem_from_filename,
    question_stems_from_dir,
    read_text,
)


def _default_evaluation_dir(script_dir: Path) -> Path:
    return script_dir.parent / "evaluation-gpt-5.4"


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    parser = argparse.ArgumentParser(
        description=(
            "Parse PM-LLM-Benchmark text evaluations into a wide CSV with one row per model "
            "and one column per question."
        )
    )
    parser.add_argument(
        "--evaluation-dir",
        type=Path,
        default=_default_evaluation_dir(script_dir),
        help="Directory containing main benchmark evaluation TXT files. Defaults to ../evaluation-gpt-5.4.",
    )
    parser.add_argument(
        "--questions-dir",
        type=Path,
        default=project_root / "questions",
        help="Directory containing benchmark questions. Defaults to ../questions.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=script_dir / "scores.csv",
        help="Output CSV path. Defaults to judgebench/scores.csv.",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Store raw extracted grades instead of applying the benchmark pre-normalization.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s - %(message)s")
    logger = logging.getLogger("judgebench.extract_scores")

    if not args.evaluation_dir.is_dir():
        raise FileNotFoundError(f"Evaluation directory does not exist: {args.evaluation_dir}")
    if not args.questions_dir.is_dir():
        raise FileNotFoundError(f"Questions directory does not exist: {args.questions_dir}")

    question_stems = question_stems_from_dir(args.questions_dir)
    question_columns = sorted(question_stems)
    scores_by_model: Dict[str, Dict[str, float]] = {}
    skipped = 0

    for eval_path in sorted(path for path in args.evaluation_dir.glob("*.txt") if path.is_file()):
        question_stem = question_stem_from_filename(eval_path.name, question_stems)
        if question_stem is None:
            logger.debug("Skipping file without known question suffix: %s", eval_path.name)
            skipped += 1
            continue

        model_key = model_key_from_filename(eval_path.name, question_stem)
        if model_key is None or not model_key:
            logger.debug("Skipping file with invalid model/question naming: %s", eval_path.name)
            skipped += 1
            continue

        score = parse_pm_score(read_text(eval_path), normalize=not args.raw)
        if score is None:
            logger.warning("No parseable score in %s", eval_path)
            skipped += 1
            continue

        scores_by_model.setdefault(model_key, {})[question_stem] = score

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["model", *question_columns])
        writer.writeheader()
        for model_key in sorted(scores_by_model):
            row = {"model": model_key}
            row.update(
                {
                    question: f"{scores_by_model[model_key][question]:.6g}"
                    for question in question_columns
                    if question in scores_by_model[model_key]
                }
            )
            writer.writerow(row)

    logger.info(
        "Wrote %d models and %d question columns to %s; skipped %d files.",
        len(scores_by_model),
        len(question_columns),
        args.output,
        skipped,
    )


if __name__ == "__main__":
    main()
