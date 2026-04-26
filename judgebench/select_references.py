import argparse
import csv
import logging
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from benchlib import average, load_score_csv, population_stdev


DEFAULT_CATEGORIES = ("cat01", "cat02", "cat03", "cat04", "cat05", "cat06")
DEFAULT_QUANTILES = (0.25, 0.50, 0.75, 1.00)


def _question_stats(scores_by_model: Dict[str, Dict[str, float]], question: str) -> Tuple[int, float, float, float]:
    values = [scores[question] for scores in scores_by_model.values() if question in scores]
    avg = average(values)
    stdev = population_stdev(values)
    return len(values), avg, stdev, avg - stdev


def _select_representative_question(
    category: str,
    questions: Sequence[str],
    scores_by_model: Dict[str, Dict[str, float]],
    logger: logging.Logger,
) -> Optional[Dict[str, object]]:
    candidates = [question for question in questions if question.startswith(f"{category}_")]
    best: Optional[Dict[str, object]] = None

    logger.info("Scanning %s with %d candidate questions.", category, len(candidates))
    for question in candidates:
        count, avg, stdev, avg_minus_stdev = _question_stats(scores_by_model, question)
        if count == 0:
            logger.debug("%s: no scores available.", question)
            continue

        logger.debug(
            "%s: n=%d average=%.4f stdev=%.4f average_minus_stdev=%.4f",
            question,
            count,
            avg,
            stdev,
            avg_minus_stdev,
        )
        candidate = {
            "category": category,
            "question": question,
            "count": count,
            "average": avg,
            "stdev": stdev,
            "average_minus_stdev": avg_minus_stdev,
        }
        if best is None or (
            float(candidate["average_minus_stdev"]),
            str(candidate["question"]),
        ) < (
            float(best["average_minus_stdev"]),
            str(best["question"]),
        ):
            best = candidate

    if best is None:
        logger.warning("No scored question found for %s.", category)
    else:
        logger.info(
            "Selected %s for %s: n=%d average=%.4f stdev=%.4f average_minus_stdev=%.4f",
            best["question"],
            category,
            best["count"],
            best["average"],
            best["stdev"],
            best["average_minus_stdev"],
        )
    return best


def _quantile_target(sorted_values: Sequence[float], quantile: float) -> float:
    if not sorted_values:
        raise ValueError("Cannot compute a quantile over no values.")
    if quantile <= 0.0:
        return sorted_values[0]
    if quantile >= 1.0:
        return sorted_values[-1]

    position = (len(sorted_values) - 1) * quantile
    lower_index = int(position)
    upper_index = min(lower_index + 1, len(sorted_values) - 1)
    fraction = position - lower_index
    return sorted_values[lower_index] * (1.0 - fraction) + sorted_values[upper_index] * fraction


def _find_nearest_quantile_answer(
    question: str,
    quantile: float,
    scores_by_model: Dict[str, Dict[str, float]],
) -> Tuple[str, float, float]:
    scored_models = sorted(
        (model, scores[question])
        for model, scores in scores_by_model.items()
        if question in scores
    )
    if not scored_models:
        raise ValueError(f"No scored models available for {question}.")

    sorted_values = sorted(score for _, score in scored_models)
    target = _quantile_target(sorted_values, quantile)
    model, score = min(scored_models, key=lambda item: (abs(item[1] - target), item[1], item[0]))
    return model, score, target


def _format_quantile(quantile: float) -> str:
    return f"q{int(round(quantile * 100)):03d}"


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    parser = argparse.ArgumentParser(
        description=(
            "Select one representative PM-LLM-Benchmark question per category and copy "
            "the answers closest to the requested score quantiles into judgebench/answers."
        )
    )
    parser.add_argument(
        "--scores-csv",
        type=Path,
        default=script_dir / "scores.csv",
        help="CSV produced by extract_scores.py. Defaults to judgebench/scores.csv.",
    )
    parser.add_argument(
        "--answers-dir",
        type=Path,
        default=project_root / "answers",
        help="Main benchmark answers directory. Defaults to ../answers.",
    )
    parser.add_argument(
        "--questions-dir",
        type=Path,
        default=project_root / "questions",
        help="Main benchmark questions directory. Defaults to ../questions.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=script_dir,
        help="Destination root. Defaults to judgebench.",
    )
    parser.add_argument(
        "--categories",
        nargs="+",
        default=list(DEFAULT_CATEGORIES),
        help="Categories to include. Defaults to cat01 through cat06.",
    )
    parser.add_argument(
        "--quantiles",
        nargs="+",
        type=float,
        default=list(DEFAULT_QUANTILES),
        help="Score quantiles to copy. Defaults to 0.25 0.5 0.75 1.0.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(name)s - %(message)s")
    logger = logging.getLogger("judgebench.select_references")

    questions, scores_by_model = load_score_csv(args.scores_csv)
    answers_out = args.output_root / "answers"
    questions_out = args.output_root / "questions"
    answers_out.mkdir(parents=True, exist_ok=True)
    questions_out.mkdir(parents=True, exist_ok=True)

    metadata_rows: List[Dict[str, object]] = []
    for category in args.categories:
        representative = _select_representative_question(category, questions, scores_by_model, logger)
        if representative is None:
            continue

        question = str(representative["question"])
        source_question = args.questions_dir / f"{question}.txt"
        destination_question = questions_out / source_question.name
        if not source_question.is_file():
            logger.warning("Question file missing, cannot copy: %s", source_question)
            continue

        shutil.copy2(source_question, destination_question)
        logger.info("Copied representative question %s -> %s", source_question, destination_question)

        for quantile in args.quantiles:
            answer_model, reference_score, target_score = _find_nearest_quantile_answer(
                question,
                quantile,
                scores_by_model,
            )
            source_answer = args.answers_dir / f"{answer_model}_{question}.txt"
            if not source_answer.is_file():
                logger.warning("Answer file missing, cannot copy: %s", source_answer)
                continue

            copied_answer_name = f"{category}_{_format_quantile(quantile)}_{source_answer.name}"
            copied_answer = answers_out / copied_answer_name
            shutil.copy2(source_answer, copied_answer)
            logger.info(
                "Copied %s quantile %.2f answer: model=%s score=%.4f target=%.4f -> %s",
                category,
                quantile,
                answer_model,
                reference_score,
                target_score,
                copied_answer,
            )

            metadata_rows.append(
                {
                    "category": category,
                    "question": question,
                    "representative_average": f"{float(representative['average']):.6g}",
                    "representative_stdev": f"{float(representative['stdev']):.6g}",
                    "representative_average_minus_stdev": f"{float(representative['average_minus_stdev']):.6g}",
                    "quantile": f"{quantile:.2f}",
                    "target_score": f"{target_score:.6g}",
                    "reference_score": f"{reference_score:.6g}",
                    "answer_model": answer_model,
                    "source_answer_file": source_answer.name,
                    "copied_answer_file": copied_answer.name,
                    "copied_question_file": destination_question.name,
                }
            )

    metadata_path = args.output_root / "selected_answers.csv"
    with metadata_path.open("w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "category",
            "question",
            "representative_average",
            "representative_stdev",
            "representative_average_minus_stdev",
            "quantile",
            "target_score",
            "reference_score",
            "answer_model",
            "source_answer_file",
            "copied_answer_file",
            "copied_question_file",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metadata_rows)

    logger.info("Wrote %d selected reference rows to %s", len(metadata_rows), metadata_path)


if __name__ == "__main__":
    main()
