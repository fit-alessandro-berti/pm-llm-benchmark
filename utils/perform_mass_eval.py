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

models_list = ["mistral-small-2503", "gemini-2.0-flash", "gpt-4o-2024-11-20", "DeepSeek-R1-Distill-Llama-70B", "DeepSeek-R1-Distill-Qwen-32B", "o3-mini-20250131-HIGH", "o3-mini-20250131-LOW", "gemini-2.5-pro-exp-03-25", "gpt-4.5-preview", "deepseek-aiDeepSeek-V3-0324", "gemini-2.0-flash-lite", "gemini-1.5-pro-002", "qwen-max-2025-01-25", "qwen-plus-2025-01-25", "Grok-3-beta-20250220", "gemini-2.0-flash-thinking-exp-01-21", "Grok-3-beta-thinking-20250221", "grok-2-1212", "qwen2.5-72b-instruct"]
models_list = models_list + ['claude-3-7-sonnet-nothink-20250219']
models_list = models_list + ['claude-3-7-sonnet-thinkhigh-20250219']
models_list = models_list + ['DeepSeek-R1-671B-HB', 'Perplexity-R1-1776', 'o1-2024-12-17', 'exaone-deep32b-fp16', 'QwenQwQ-32B', 'o1-preview-2024-09-12']
models_list = models_list + ['meta-llamaLlama-3.3-70B-Instruct']
models_list = models_list + ['qwen2.5-32b-instruct', 'qwen2.5-14b-instruct', 'DeepSeek-R1-Distill-Qwen-14B']
models_list = models_list + ['qwen2.5-7b-instruct', 'DeepSeek-R1-Distill-Qwen-7B']
models_list = models_list + ['meta-llamaMeta-Llama-3.1-8B-Instruct', 'DeepSeek-R1-Distill-Llama-8B']
models_list = models_list + ['exaone-deep7.8b-fp16', 'exaone-deep2.4b-fp16']
models_list = models_list + ['qwen-turbo-2024-11-01', 'qwen2.5-72b-instruct', 'qwen2.5-14b-instruct-1m', 'qwen2.5-7b-instruct-1m']

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

for m in answer_models_keys:
    print(m)
    evalscript.perform_evaluation(m)
    overall_table.write_evaluation(".", extra=True)

overall_table.write_evaluation(".", extra=True)
