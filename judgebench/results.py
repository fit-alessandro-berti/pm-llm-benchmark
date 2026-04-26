import argparse
import csv
import logging
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from benchlib import (
    average,
    parse_pm_score,
    population_stdev,
    read_text,
)


MAX_SCORE_STDEV = 4.5


def _load_selected_rows(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"category", "copied_answer_file"}
        if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
            raise ValueError(f"Selected answers CSV must contain {sorted(required)}: {path}")
        return [row for row in reader if row.get("copied_answer_file")]


def _match_selected_row(eval_name: str, selected_rows: Sequence[Dict[str, str]]) -> Optional[Dict[str, str]]:
    for row in sorted(selected_rows, key=lambda item: len(item["copied_answer_file"]), reverse=True):
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


def _quality_score(score_average: float, score_stdev: float) -> float:
    lower_average_component = max(0.0, min(1.0, (10.0 - score_average) / 9.0))
    high_stdev_component = max(0.0, min(1.0, score_stdev / MAX_SCORE_STDEV))
    return 100.0 * (0.5 * lower_average_component + 0.5 * high_stdev_component)


def _category_columns(categories: Sequence[str]) -> List[str]:
    columns: List[str] = []
    for category in categories:
        columns.extend([f"{category}_average", f"{category}_stdev"])
    return columns


def _render_markdown(judge_rows: List[Dict[str, object]], categories: Sequence[str]) -> str:
    lines = [
        "# JudgeBench Results",
        "",
        "Quality is a 0-100 synthetic score using only the judge's assigned scores. "
        "It rewards lower average scores and higher score standard deviation.",
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
            cells.append(_format_optional(row.get(f"{category}_average"), digits=3))  # type: ignore[arg-type]
            cells.append(_format_optional(row.get(f"{category}_stdev"), digits=3))  # type: ignore[arg-type]
        lines.append(
            "| " + " | ".join(cells) + " |"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description="Parse JudgeBench evaluations and report judge quality from score average and spread."
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
        "-o",
        "--output",
        type=Path,
        default=script_dir / "judge_quality.md",
        help="Markdown report output. Defaults to judgebench/judge_quality.md.",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Parse raw grades instead of applying the benchmark pre-normalization.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s - %(message)s")
    logger = logging.getLogger("judgebench.results")

    selected_rows = _load_selected_rows(args.selected_csv)
    observations_by_judge: Dict[str, List[Dict[str, object]]] = defaultdict(list)

    for eval_path in sorted(path for path in args.evaluations_dir.glob("*.txt") if path.is_file()):
        selected_row = _match_selected_row(eval_path.name, selected_rows)
        if selected_row is None:
            logger.warning("Skipping evaluation that does not match selected answers: %s", eval_path.name)
            continue

        judge_score = parse_pm_score(read_text(eval_path), normalize=not args.raw)
        if judge_score is None:
            logger.warning("No parseable judge score in %s", eval_path)
            continue

        copied_answer_file = selected_row["copied_answer_file"]
        judge_name = _extract_judge_name(eval_path.name, copied_answer_file)
        observations_by_judge[judge_name].append(
            {
                "category": selected_row["category"],
                "answer_file": copied_answer_file,
                "judge_score": judge_score,
            }
        )

    categories = sorted({row["category"] for row in selected_rows if row.get("category")})
    judge_rows: List[Dict[str, object]] = []
    for judge_name, observations in observations_by_judge.items():
        judge_scores = [float(row["judge_score"]) for row in observations]
        score_average = average(judge_scores)
        score_stdev = population_stdev(judge_scores)

        judge_row: Dict[str, object] = {
            "judge": judge_name,
            "quality_score": _quality_score(score_average, score_stdev),
        }

        for category in categories:
            category_observations = [row for row in observations if row["category"] == category]
            if not category_observations:
                judge_row[f"{category}_average"] = None
                judge_row[f"{category}_stdev"] = None
                continue

            category_judge = [float(row["judge_score"]) for row in category_observations]
            judge_row[f"{category}_average"] = average(category_judge)
            judge_row[f"{category}_stdev"] = population_stdev(category_judge)

        judge_rows.append(judge_row)

    judge_rows.sort(key=lambda row: (-float(row["quality_score"]), str(row["judge"]).lower()))

    markdown = _render_markdown(judge_rows, categories)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")
    print(markdown, end="")
    logger.info("Wrote JudgeBench report to %s", args.output)


if __name__ == "__main__":
    main()
