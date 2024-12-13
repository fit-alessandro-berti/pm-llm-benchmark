import os
from collections import Counter
import evalscript
from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path
from utils import overall_table


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

for m in answers_models:
    if evaluations_models[m] != answers_models[m]:
        if "o1-pro" not in m:
            print(m)
            evalscript.perform_evaluation(m)
            overall_table.write_evaluation(".", extra=False)

overall_table.write_evaluation(".", extra=True)
