import os
import json
import pandas as pd
from collections import Counter
from utils.table_per_model import execute_script
from common import EVALUATING_MODEL_NAME


def format_numb_in_table(score, max_score, good_diff=0.3):
    if score == max_score:
        return ":mage_woman: **%.1f**" % (score)
    elif score >= max_score - good_diff:
        return "**%.1f**" % (score)
    return "%.1f" % (score)


def execute(evaluation_folder):
    e_m_name = EVALUATING_MODEL_NAME.replace("/", "").replace(":", "")

    files = os.listdir(evaluation_folder)
    models = Counter([f.split("_cat")[0] for f in files if not "__init__" in f])
    models = {x: y for x, y in models.items() if y >= 44}

    temp = {}
    results = []
    all_jsons = {}

    max_c1 = 0.0
    max_c2 = 0.0
    max_c3 = 0.0
    max_c4 = 0.0
    max_c5 = 0.0
    max_c6 = 0.0
    max_c7 = 0.0

    for m in models:
        res, this_json = execute_script(evaluation_folder, m)
        temp[m] = res

        this_json["score_c1"] = round(this_json["score_c1"], 1)
        this_json["score_c2"] = round(this_json["score_c2"], 1)
        this_json["score_c3"] = round(this_json["score_c3"], 1)
        this_json["score_c4"] = round(this_json["score_c4"], 1)
        this_json["score_c5"] = round(this_json["score_c5"], 1)
        this_json["score_c6"] = round(this_json["score_c6"], 1)
        this_json["score_c7"] = round(this_json["score_c7"], 1)

        max_c1 = max(max_c1, this_json["score_c1"])
        max_c2 = max(max_c2, this_json["score_c2"])
        max_c3 = max(max_c3, this_json["score_c3"])
        max_c4 = max(max_c4, this_json["score_c4"])
        max_c5 = max(max_c5, this_json["score_c5"])
        max_c6 = max(max_c6, this_json["score_c6"])
        max_c7 = max(max_c7, this_json["score_c7"])

        all_jsons[m] = this_json

    for m in models:
        res = temp[m]
        this_json = all_jsons[m]
        table = res.split("==OVERALL SCORES==")[0]

        score_c1 = format_numb_in_table(this_json["score_c1"], max_c1)
        score_c2 = format_numb_in_table(this_json["score_c2"], max_c2)
        score_c3 = format_numb_in_table(this_json["score_c3"], max_c3)
        score_c4 = format_numb_in_table(this_json["score_c4"], max_c4)
        score_c5 = format_numb_in_table(this_json["score_c5"], max_c5)
        score_c6 = format_numb_in_table(this_json["score_c6"], max_c6)
        score_c7 = format_numb_in_table(this_json["score_c7"], max_c7)

        results.append((m, this_json["score_textual"], this_json["total_score"], table, score_c1, score_c2, score_c3, score_c4, score_c5, score_c6, score_c7))

    results.sort(key=lambda x: (x[1], x[2], x[0]), reverse=True)

    overall_table = []

    for m in results:
        if m[1] == m[2]:
            entry = {"Model": m[0], "Overall Score": "**%.1f**" % (m[1]), "C1": m[4], "C2": m[5], "C3": m[6], "C4": m[7], "C5": m[8], "C6": m[9], "C7": m[10]}
        else:
            entry = {"Model": m[0], "Overall Score": "**%.1f** (C1-6: **%.1f**)" % (m[2], m[1]), "C1": m[4], "C2": m[5], "C3": m[6], "C4": m[7], "C5": m[8], "C6": m[9], "C7": m[10]}
        overall_table.append(entry)

    overall_table = pd.DataFrame(overall_table)
    overall_table.columns = ["Model", "Total Score", "PMI", "DK", "PMO", "PQ", "HG", "FA", "VI"]
    overall_table = overall_table.to_markdown(index=False)

    output = []
    output.append("A score in the range **27-33** is considered **sufficient**; a score in the range **33-45** is considered **good**; a score **>45** is considered **excellent**.")
    output.append("## Leaderboard (1-shot; %s used as a judge)" % (EVALUATING_MODEL_NAME))
    output.append(overall_table)

    for m in results:
        output.append("### %s   => %.1f (/52) points" % (m[0], m[2]))
        output.append(m[3])

    output = "\n\n".join(output)

    F = open("../leaderboard_"+e_m_name+".md", "w")
    F.write(output)
    F.close()

    #print(json.dumps(all_jsons, indent=2))

    return output, all_jsons


if __name__ == "__main__":
    e_m_name = EVALUATING_MODEL_NAME.replace("/", "").replace(":", "")
    evaluation_folder = "../evaluation" if "gpt-4o" in EVALUATING_MODEL_NAME else "../evaluation-" + e_m_name
    execute(evaluation_folder)
