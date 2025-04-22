import os
import sys
from collections import Counter
import evalscript
from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path, get_ordered_references_llms
from utils import overall_table


def perform_mass_eval():
    answers = os.listdir("answers")
    answers_models = Counter([x.split("_cat")[0] for x in answers])
    #answers_models = {x: y for x, y in answers_models.items() if y >= 44}

    e_m_name = clean_model_name(EVALUATING_MODEL_NAME)
    base_evaluation_path = get_base_evaluation_path(e_m_name)
    evaluations = os.listdir(base_evaluation_path)
    evaluations_models = Counter([x.split("_cat")[0] for x in evaluations])

    answer_models_keys = list(answers_models.keys())

    ordered, referenced = get_ordered_references_llms(".")
    ordered = ordered + referenced
    ordered = [clean_model_name(x) for x in ordered]
    answer_models_keys.sort(key=lambda x: (ordered.index(x) if x in ordered else sys.maxsize, x))

    answer_models_keys = [x for x in answer_models_keys if evaluations_models[x] != answers_models[x]]
    print(answer_models_keys)

    overall_table.write_evaluation(".", extra=True)

    changed = False
    for m in answer_models_keys:
        if "__init" not in m.lower():
            print(m)
            evalscript.perform_evaluation(m)
            overall_table.write_evaluation(".", extra=True)
            changed = True

    if changed:
        overall_table.write_evaluation(".", extra=True)

    return changed


if __name__ == "__main__":
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)

    iterations = sys.maxsize
    #iterations = 1

    for i in range(iterations):
        changed = perform_mass_eval()
