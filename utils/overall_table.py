import os
import pandas as pd
from collections import Counter
from utils.table_per_model import execute_script


EVALUATING_MODEL_NAME = "gpt-4o"

e_m_name = EVALUATING_MODEL_NAME.replace("/", "").replace(":", "")
evaluation_folder = "../evaluation" if EVALUATING_MODEL_NAME.startswith(
    "gpt-4o") else "../evaluation-" + e_m_name

files = os.listdir(evaluation_folder)
models = Counter([f.split("_cat")[0] for f in files])
models = {x: y for x, y in models.items() if y == 52 or y == 46}

results = []

for m in models:
    res = execute_script(evaluation_folder, m)
    table = res.split("==OVERALL SCORES==")[0]
    scores = res.split("==OVERALL SCORES==")[1].split("\t")

    results.append((m, float(scores[1]), float(scores[2]), table))

results.sort(key=lambda x: (x[1], x[2], x[0]), reverse=True)

overall_table = []

for m in results:
    if m[1] == m[2]:
        overall_table.append({"Model": m[0], "Overall Score": "%.1f" % (m[1])})
    else:
        overall_table.append({"Model": m[0], "Overall Score": "%.1f (%.1f on C1-C6)" % (m[2], m[1])})

overall_table = pd.DataFrame(overall_table)
overall_table = overall_table.to_markdown(index=False)

output = ["## Leaderboard (1-shot)"]
output.append(overall_table)

for m in results:
    output.append("### %s   => %.1f (/52) points" % (m[0], m[2]))
    output.append(m[3])

output = "\n\n".join(output)
#print(output)

F = open("../leaderboard_"+e_m_name+".md", "w")
F.write(output)
F.close()
