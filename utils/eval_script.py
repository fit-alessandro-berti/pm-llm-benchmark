import os
import numpy as np


contents = open("../leaderboard_gpt-4o_2024_05_13.md", "r").readlines()

open = False
debug = False

all_results = {}
results_per_category = {}
results_per_question = {}

model_category = None
model_name = None
question_category = None
question = None

for row in contents:
    row = row.strip()

    if "Leaderboard" in row:
        open = True

    if open:
        if row.startswith("####"):
            model_name = row.split("####")[-1].split("=>")[0].strip()
            question_category = None
            question = None
            if debug:
                print("\t"+model_name)
            all_results[model_category][model_name] = []
        elif row.startswith("###"):
            model_category = row.split("###")[-1].strip()
            model_name = None
            question_category = None
            question = None
            if debug:
                print(model_category)
            all_results[model_category] = {}
            results_per_category[model_category] = {}
            results_per_question[model_category] = {}
        elif row.startswith("|") and "cat" in row:
            question = row.split("|")[1].strip()
            question_category = question.split("_")[0]
            score = row.split("|")[2].strip()
            if score:
                score = float(score)
                if question_category not in results_per_category[model_category]:
                    results_per_category[model_category][question_category] = []

                if question not in results_per_question[model_category]:
                    results_per_question[model_category][question] = []

                if debug:
                    print("\t\t"+question_category+"\t"+question+"\t"+str(score))

                all_results[model_category][model_name].append(score)
                results_per_category[model_category][question_category].append(score)
                results_per_question[model_category][question].append(score)

max_len_all_results = 0
max_len_results_per_category = 0
max_len_results_per_question = 0

for model_category in all_results:
    for model_name in all_results[model_category]:
        all_results[model_category][model_name] = (round(float(np.mean(all_results[model_category][model_name])), 1), round(float(np.std(all_results[model_category][model_name])), 1))

    for question_category in results_per_category[model_category]:
        results_per_category[model_category][question_category] = (round(float(np.mean(results_per_category[model_category][question_category])), 1), round(float(np.std(results_per_category[model_category][question_category])), 1))

    for question in results_per_question[model_category]:
        results_per_question[model_category][question] = (round(float(np.mean(results_per_question[model_category][question])), 1), round(float(np.std(results_per_question[model_category][question])), 1))

    all_results[model_category] = [(k, v) for k, v in all_results[model_category].items()]
    all_results[model_category] = sorted(all_results[model_category], key=lambda x: (x[1][0], x[1][1], x[0]), reverse=True)
    max_len_all_results = max(max_len_all_results, len(all_results[model_category]))

    results_per_category[model_category] = [(k, v) for k, v in results_per_category[model_category].items()]
    results_per_category[model_category] = sorted(results_per_category[model_category], key=lambda x: x[0])
    max_len_results_per_category = max(max_len_results_per_category, len(results_per_category[model_category]))

    results_per_question[model_category] = [(k, v) for k, v in results_per_question[model_category].items()]
    results_per_question[model_category] = sorted(results_per_question[model_category], key=lambda x: x[0])
    max_len_results_per_question = max(max_len_results_per_question, len(results_per_question[model_category]))

for model_category in all_results:
     print(model_category, all_results[model_category])

print("\n\n")

for model_category in results_per_category:
    print(model_category, results_per_category[model_category])

print("\n\n")

for model_category in results_per_question:
    print(model_category, results_per_question[model_category])
