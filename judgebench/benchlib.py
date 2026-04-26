import math
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


PM_SCORE_RE = re.compile(
    r"(?P<sign>[-+]?)(?:(?P<float>\d+\.\d+)|(?P<int>\d+)|(?P<numerator>\d+)/(?P<denominator>\d+))(?!\.)"
)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def extract_raw_pm_score(text: str) -> Optional[float]:
    float_scores: List[float] = []
    int_scores: List[float] = []

    for match in PM_SCORE_RE.finditer(text):
        match_text = match.group(0)
        try:
            value = float(match_text)
        except ValueError:
            continue

        if 1.0 <= value <= 10.0:
            if "." in match_text:
                float_scores.append(value)
            else:
                int_scores.append(value)

    if float_scores:
        if 10.0 in float_scores:
            ten_index = float_scores.index(10.0)
            if ten_index > 0:
                return float_scores[ten_index - 1]
        return float_scores[0]

    if int_scores:
        return int_scores[0]

    return None


def normalize_pm_score(score: float) -> float:
    return min(7.0, score) + 0.5 * max(min(score, 9.0) - 7.0, 0.0) + 2.0 * max(score - 9.0, 0.0)


def parse_pm_score(text: str, normalize: bool = True) -> Optional[float]:
    raw_score = extract_raw_pm_score(text)
    if raw_score is None:
        return None
    return normalize_pm_score(raw_score) if normalize else raw_score


def question_stems_from_dir(questions_dir: Path) -> List[str]:
    return sorted((path.stem for path in questions_dir.glob("*.txt") if path.is_file()), key=len, reverse=True)


def question_stem_from_filename(filename: str, question_stems: Sequence[str]) -> Optional[str]:
    for stem in question_stems:
        if filename.endswith(f"_{stem}.txt") or filename == f"{stem}.txt":
            return stem
    return None


def model_key_from_filename(filename: str, question_stem: str) -> Optional[str]:
    suffix = f"_{question_stem}.txt"
    if filename.endswith(suffix):
        return filename[: -len(suffix)]
    if filename == f"{question_stem}.txt":
        return ""
    return None


def sanitize_name(name: str) -> str:
    sanitized = name.replace("/", "").replace(":", "")
    return "".join(char if char.isalnum() or char in {"-", "_", "."} else "_" for char in sanitized)


def average(values: Iterable[float]) -> float:
    materialized = [float(value) for value in values]
    if not materialized:
        return 0.0
    return sum(materialized) / len(materialized)


def population_stdev(values: Iterable[float]) -> float:
    materialized = [float(value) for value in values]
    if len(materialized) < 2:
        return 0.0
    mean = average(materialized)
    return math.sqrt(sum((value - mean) ** 2 for value in materialized) / len(materialized))


def pearson(xs: Sequence[float], ys: Sequence[float]) -> Optional[float]:
    if len(xs) != len(ys) or len(xs) < 2:
        return None

    mean_x = average(xs)
    mean_y = average(ys)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    denominator_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    denominator = denominator_x * denominator_y
    if denominator == 0.0:
        return None
    return numerator / denominator


def ranks(values: Sequence[float]) -> List[float]:
    ordered = sorted(enumerate(values), key=lambda item: item[1])
    result = [0.0] * len(values)
    index = 0
    while index < len(ordered):
        end = index + 1
        while end < len(ordered) and ordered[end][1] == ordered[index][1]:
            end += 1
        rank = (index + 1 + end) / 2.0
        for original_index, _ in ordered[index:end]:
            result[original_index] = rank
        index = end
    return result


def spearman(xs: Sequence[float], ys: Sequence[float]) -> Optional[float]:
    if len(xs) != len(ys) or len(xs) < 2:
        return None
    return pearson(ranks(xs), ranks(ys))


def pairwise_order_accuracy(reference_scores: Sequence[float], judge_scores: Sequence[float]) -> Optional[float]:
    if len(reference_scores) != len(judge_scores) or len(reference_scores) < 2:
        return None

    correct = 0
    total = 0
    for left in range(len(reference_scores)):
        for right in range(left + 1, len(reference_scores)):
            reference_diff = reference_scores[left] - reference_scores[right]
            judge_diff = judge_scores[left] - judge_scores[right]
            if reference_diff == 0.0:
                continue
            total += 1
            if judge_diff == 0.0:
                correct += 0.5
            elif (reference_diff > 0.0 and judge_diff > 0.0) or (reference_diff < 0.0 and judge_diff < 0.0):
                correct += 1

    if total == 0:
        return None
    return correct / total


def load_score_csv(path: Path) -> Tuple[List[str], Dict[str, Dict[str, float]]]:
    import csv

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None or "model" not in reader.fieldnames:
            raise ValueError(f"Score CSV must contain a 'model' column: {path}")
        question_columns = [field for field in reader.fieldnames if field != "model"]
        scores_by_model: Dict[str, Dict[str, float]] = {}
        for row in reader:
            model = row.get("model", "").strip()
            if not model:
                continue
            scores_by_model[model] = {}
            for question in question_columns:
                raw_value = row.get(question, "")
                if raw_value is None or raw_value == "":
                    continue
                scores_by_model[model][question] = float(raw_value)
    return question_columns, scores_by_model
