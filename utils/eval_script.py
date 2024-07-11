import os
import numpy as np


contents = open("../README.md", "r").readlines()

open = False
debug = False

all_results = {}
results_per_category = {}

model_category = None
model_name = None
question_category = None

for row in contents:
    row = row.strip()

    if "Preliminary Scores" in row:
        open = True

    if open:
        if row.startswith("####"):
            model_name = row.split("####")[-1].split("(")[0].split("=>")[0].strip()
            question_category = None
            if debug:
                print("\t"+model_name)
            all_results[model_category][model_name] = []
            results_per_category[model_category][model_name] = {}
        elif row.startswith("###"):
            model_category = row.split("###")[-1].strip()
            model_name = None
            question_category = None
            if debug:
                print(model_category)
            all_results[model_category] = {}
            results_per_category[model_category] = {}
        elif row.startswith("|") and "cat" in row:
            question = row.split("|")[1].strip()
            question_category = question.split("_")[0]
            score = row.split("|")[2].strip()
            if score:
                score = float(score)
                if question_category not in results_per_category[model_category][model_name]:
                    results_per_category[model_category][model_name][question_category] = []
                if debug:
                    print("\t\t"+question_category+"\t"+question+"\t"+str(score))
                all_results[model_category][model_name].append(score)
                results_per_category[model_category][model_name][question_category].append(score)

for model_category in results_per_category:
    for model_name in results_per_category[model_category]:
        all_results[model_category][model_name] = round(float(sum(all_results[model_category][model_name]))/10.0, 1)
    all_results[model_category] = [(k, v) for k, v in all_results[model_category].items()]
    all_results[model_category] = sorted(all_results[model_category], key=lambda x: (x[1], x[0]), reverse=True)
    print(model_category, all_results[model_category])
