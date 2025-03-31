import os
from collections import Counter
import evalscript
from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path, is_open_source
from utils import overall_table
import sys
import random

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
os.chdir(parent_directory)

answers = os.listdir("answers")
answers_models = Counter([x.split("_cat")[0] for x in answers])
#answers_models = {x: y for x, y in answers_models.items() if y >= 44}

e_m_name = clean_model_name(EVALUATING_MODEL_NAME)
base_evaluation_path = get_base_evaluation_path(e_m_name)
evaluations = os.listdir(base_evaluation_path)
evaluations_models = Counter([x.split("_cat")[0] for x in evaluations])

models_list = []

answer_models_keys = list(answers_models.keys())
diff = set(models_list).difference(answer_models_keys)

if diff:
    print(answer_models_keys)
    print(diff)
    input()

answer_models_keys.sort(key=lambda x: (models_list.index(x) if x in models_list else sys.maxsize, -evaluations_models[x], not is_open_source(x), len(x[0]), x[0]))
answer_models_keys = [x for x in answer_models_keys if evaluations_models[x] != answers_models[x]]

print(answer_models_keys)
#input()

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
