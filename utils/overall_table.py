import os
import pandas as pd
from collections import Counter
from utils.table_per_model import execute_script
from common import EVALUATING_MODEL_NAME


def execute(evaluation_folder):
    e_m_name = EVALUATING_MODEL_NAME.replace("/", "").replace(":", "")

    files = os.listdir(evaluation_folder)
    models = Counter([f.split("_cat")[0] for f in files if not "__init__" in f])
    models = {x: y for x, y in models.items() if y >= 44}

    results = []

    for m in models:
        res = execute_script(evaluation_folder, m)
        table = res.split("==OVERALL SCORES==")[0]
        scores = res.split("==OVERALL SCORES==")[1].split("\t")

        results.append((m, float(scores[1]), float(scores[2]), table, float(scores[3]), float(scores[4]), float(scores[5]), float(scores[6]), float(scores[7]), float(scores[8]), float(scores[9])))

    results.sort(key=lambda x: (x[1], x[2], x[0]), reverse=True)

    overall_table = []

    for m in results:
        if m[1] == m[2]:
            entry = {"Model": m[0], "Overall Score": "%.1f" % (m[1]), "C1": m[4], "C2": m[5], "C3": m[6], "C4": m[7], "C5": m[8], "C6": m[9], "C7": m[10]}
        else:
            entry = {"Model": m[0], "Overall Score": "%.1f (%.1f on C1-C6)" % (m[2], m[1]), "C1": m[4], "C2": m[5], "C3": m[6], "C4": m[7], "C5": m[8], "C6": m[9], "C7": m[10]}
        overall_table.append(entry)

    overall_table = pd.DataFrame(overall_table)
    overall_table.columns = ["Model", "Overall Score", "C1", "C2", "C3", "C4", "C5", "C6", "C7"]
    overall_table = overall_table.to_markdown(index=False)

    output = ["## Leaderboard (1-shot; %s used as a judge)" % (EVALUATING_MODEL_NAME)]
    output.append("Overall leaderboard (a score in the range **27-33** is considered **sufficient**; a score in the range **33-45** is considered **good**; a score **>45** is considered **excellent**):")
    output.append(overall_table)

    for m in results:
        output.append("### %s   => %.1f (/52) points" % (m[0], m[2]))
        output.append(m[3])

    output = "\n\n".join(output)

    F = open("../leaderboard_"+e_m_name+".md", "w")
    F.write(output)
    F.close()

    return output


if __name__ == "__main__":
    e_m_name = EVALUATING_MODEL_NAME.replace("/", "").replace(":", "")
    evaluation_folder = "../evaluation" if "gpt-4o" in EVALUATING_MODEL_NAME else "../evaluation-" + e_m_name
    execute(evaluation_folder)
