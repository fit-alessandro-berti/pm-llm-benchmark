"""List models that have fewer than 56 answers or evaluations.

Prints a Markdown table sorted by (answers + evaluations) ascending.
"""

import os
from collections import Counter

try:
    from utils.script_bootstrap import chdir_repo_root
except ModuleNotFoundError:
    from script_bootstrap import chdir_repo_root

chdir_repo_root()

from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path

TARGET_COUNT = 51


def count_by_model(folder):
    """Return Counter of model_name -> file count for ``*_cat*`` files in *folder*."""
    if not os.path.isdir(folder):
        return Counter()

    names = []
    for filename in os.listdir(folder):
        if "__init__" in filename.lower():
            continue
        if "_cat" not in filename:
            continue
        names.append(filename.split("_cat", 1)[0])
    return Counter(names)


def main():
    answers_folder = "answers"
    evaluation_folder = get_base_evaluation_path(clean_model_name(EVALUATING_MODEL_NAME))

    answers_by_model = count_by_model(answers_folder)
    evaluations_by_model = count_by_model(evaluation_folder)

    all_models = set(answers_by_model) | set(evaluations_by_model)

    incomplete = []
    for model in all_models:
        n_answers = answers_by_model.get(model, 0)
        n_evals = evaluations_by_model.get(model, 0)
        if n_answers < TARGET_COUNT or n_evals < TARGET_COUNT:
            incomplete.append((n_answers + n_evals, n_answers, n_evals, model))

    incomplete.sort(key=lambda row: (row[0], row[1], row[2], row[3]))

    print(f"# Models below {TARGET_COUNT} answers or evaluations")
    print()
    print(f"Evaluation folder: `{evaluation_folder}`")
    print()
    print("| Model | Answers | Evaluations | Sum |")
    print("| --- | ---: | ---: | ---: |")
    for total, n_answers, n_evals, model in incomplete:
        print(f"| {model} | {n_answers} | {n_evals} | {total} |")

    if not incomplete:
        print()
        print("_None — every model has at least "
              f"{TARGET_COUNT} answers and evaluations._")
    else:
        print()
        print(f"_{len(incomplete)} model(s) incomplete._")


if __name__ == "__main__":
    main()
