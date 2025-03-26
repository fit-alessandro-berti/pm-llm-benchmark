import os
from collections import Counter
import evalscript
from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path
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

models_list = ["mistral-small-2503", "gemini-2.0-flash", "gpt-4o-2024-11-20", "DeepSeek-R1-Distill-Llama-70B", "DeepSeek-R1-Distill-Qwen-32B", "o3-mini-20250131-HIGH", "o3-mini-20250131-LOW", "DeepSeek-R1-671B-DS", "gemini-2.5-pro-exp-03-25", "gpt-4.5-preview", "deepseek-aiDeepSeek-V3-0324", "qwen-max-2025-01-25", "qwen-plus-2025-01-25", "claude-3-7-sonnet-20250219", "nvidiallama-3.3-nemotron-super-49b-v1", "Grok-3-beta-20250220", "gemini-2.0-flash-thinking-exp-01-21", "Grok-3-beta-thinking-20250221", "grok-2-1212", "qwen2.5-72b-instruct"]
answer_models_keys = list(answers_models.keys())
diff = set(models_list).difference(answer_models_keys)
if diff:
    print(answer_models_keys)
    print(diff)
    input()
answer_models_keys.sort(key=lambda x: (models_list.index(x) if x in models_list else sys.maxsize, random.random(), x[0]))

print(answer_models_keys)
#input()

for m in answer_models_keys:
    if evaluations_models[m] != answers_models[m]:
        if "o1-pro" not in m:
            print(m)
            evalscript.perform_evaluation(m)
            overall_table.write_evaluation(".", extra=False)

overall_table.write_evaluation(".", extra=True)
