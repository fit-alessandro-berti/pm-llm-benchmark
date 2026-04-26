import argparse
import csv
import logging
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from benchlib import (
    average,
    pairwise_order_accuracy,
    parse_pm_score,
    read_text,
)


def _load_reference_rows(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"category", "question", "quantile", "reference_score", "copied_answer_file"}
        if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
            raise ValueError(f"Selected answers CSV must contain {sorted(required)}: {path}")
        return [row for row in reader if row.get("copied_answer_file")]


def _match_reference(eval_name: str, references: Sequence[Dict[str, str]]) -> Optional[Dict[str, str]]:
    for row in sorted(references, key=lambda item: len(item["copied_answer_file"]), reverse=True):
        if eval_name.endswith(f"_{row['copied_answer_file']}"):
            return row
    return None


def _extract_judge_name(eval_name: str, copied_answer_file: str) -> str:
    suffix = f"_{copied_answer_file}"
    if eval_name.endswith(suffix):
        return eval_name[: -len(suffix)]
    return eval_name


def _format_optional(value: Optional[float], digits: int = 4) -> str:
    if value is None:
        return ""
    return f"{value:.{digits}f}"


def _quality_score(mae: float, order_accuracy: Optional[float]) -> float:
    calibration_component = max(0.0, 1.0 - min(mae, 10.0) / 10.0)
    order_component = order_accuracy if order_accuracy is not None else calibration_component
    return 100.0 * (0.75 * calibration_component + 0.25 * order_component)


def _category_columns(categories: Sequence[str]) -> List[str]:
    columns: List[str] = []
    for category in categories:
        columns.extend([f"{category}_mae", f"{category}_order_accuracy"])
    return columns


def _render_markdown(judge_rows: List[Dict[str, object]], categories: Sequence[str]) -> str:
    lines = [
        "# JudgeBench Results",
        "",
        "The reference score is the original PM-LLM-Benchmark judge score for each copied answer. "
        "Quality is a 0-100 synthetic score combining closeness to the reference scores and pairwise ordering.",
        "",
    ]

    if not judge_rows:
        lines.append("No valid JudgeBench evaluations found.")
        return "\n".join(lines) + "\n"

    headers = ["Judge", "Quality", *_category_columns(categories)]
    alignments = ["---", "---:", *(["---:"] * len(_category_columns(categories)))]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(alignments) + " |")
    for row in judge_rows:
        cells = [str(row["judge"]), f"{float(row['quality_score']):.3f}"]
        for category in categories:
            cells.append(_format_optional(row.get(f"{category}_mae"), digits=3))  # type: ignore[arg-type]
            cells.append(_format_optional(row.get(f"{category}_order_accuracy"), digits=3))  # type: ignore[arg-type]
        lines.append(
            "| " + " | ".join(cells) + " |"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description="Parse JudgeBench evaluations and report judge quality against reference PM scores."
    )
    parser.add_argument(
        "--evaluations-dir",
        type=Path,
        default=script_dir / "evaluations",
        help="Directory containing JudgeBench evaluation TXT files.",
    )
    parser.add_argument(
        "--selected-csv",
        type=Path,
        default=script_dir / "selected_answers.csv",
        help="CSV produced by select_references.py.",
    )
    parser.add_argument(
        "--csv-output",
        type=Path,
        default=script_dir / "judge_quality.csv",
        help="CSV output for per-judge metrics.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=script_dir / "results.md",
        help="Markdown report output. Defaults to judgebench/results.md.",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Parse raw grades instead of applying the benchmark pre-normalization.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s - %(message)s")
    logger = logging.getLogger("judgebench.results")

    references = _load_reference_rows(args.selected_csv)
    observations_by_judge: Dict[str, List[Dict[str, object]]] = defaultdict(list)

    for eval_path in sorted(path for path in args.evaluations_dir.glob("*.txt") if path.is_file()):
        reference = _match_reference(eval_path.name, references)
        if reference is None:
            logger.warning("Skipping evaluation that does not match selected answers: %s", eval_path.name)
            continue

        judge_score = parse_pm_score(read_text(eval_path), normalize=not args.raw)
        if judge_score is None:
            logger.warning("No parseable judge score in %s", eval_path)
            continue

        copied_answer_file = reference["copied_answer_file"]
        judge_name = _extract_judge_name(eval_path.name, copied_answer_file)
        reference_score = float(reference["reference_score"])
        observations_by_judge[judge_name].append(
            {
                "category": reference["category"],
                "question": reference["question"],
                "quantile": reference["quantile"],
                "answer_file": copied_answer_file,
                "reference_score": reference_score,
                "judge_score": judge_score,
                "error": judge_score - reference_score,
            }
        )

    categories = sorted({row["category"] for row in references if row.get("category")})
    judge_rows: List[Dict[str, object]] = []
    for judge_name, observations in observations_by_judge.items():
        reference_scores = [float(row["reference_score"]) for row in observations]
        judge_scores = [float(row["judge_score"]) for row in observations]
        errors = [float(row["error"]) for row in observations]
        abs_errors = [abs(error) for error in errors]
        mae = average(abs_errors)
        order_accuracy = pairwise_order_accuracy(reference_scores, judge_scores)

        judge_row: Dict[str, object] = {
            "judge": judge_name,
            "quality_score": _quality_score(mae, order_accuracy),
        }

        for category in categories:
            category_observations = [row for row in observations if row["category"] == category]
            if not category_observations:
                judge_row[f"{category}_mae"] = None
                judge_row[f"{category}_order_accuracy"] = None
                continue

            category_errors = [float(row["error"]) for row in category_observations]
            category_reference = [float(row["reference_score"]) for row in category_observations]
            category_judge = [float(row["judge_score"]) for row in category_observations]
            judge_row[f"{category}_mae"] = average(abs(error) for error in category_errors)
            judge_row[f"{category}_order_accuracy"] = pairwise_order_accuracy(
                category_reference,
                category_judge,
            )

        judge_rows.append(judge_row)

    judge_rows.sort(key=lambda row: (-float(row["quality_score"]), str(row["judge"]).lower()))

    args.csv_output.parent.mkdir(parents=True, exist_ok=True)
    with args.csv_output.open("w", newline="", encoding="utf-8") as file:
        fieldnames = ["judge", "quality_score", *_category_columns(categories)]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in judge_rows:
            writer.writerow(
                {
                    key: _format_optional(row[key]) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in fieldnames
                }
            )

    markdown = _render_markdown(judge_rows, categories)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")
    print(markdown, end="")
    logger.info("Wrote JudgeBench reports to %s and %s", args.output, args.csv_output)


if __name__ == "__main__":
    main()
