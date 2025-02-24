import os
import pandas as pd
from collections import Counter
from utils.table_per_model import execute_script
from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path


def format_numb_in_table(score, max_score, good_diff=0.3):
    if score == max_score:
        return ":mage_woman: **%.1f**" % (score)
    elif score >= max_score - good_diff:
        return "**%.1f**" % (score)
    return "%.1f" % (score)


def is_open_source(m_name):
    m_name = m_name.lower()
    patterns = ["gpt-4", "gpt-3.5", "claude", "gemini", "o1-", "o3-", "ministral-3b", "grok", "sonus", "2.5-plus", "2.5-turbo", "2.5-max", "qwen-plus", "qwen-turbo", "qwen-max", "sonar-pro"]

    for p in patterns:
        if p in m_name:
            return False

    return True


def is_large_reasoning_model(m_name):
    m_name = m_name.lower()
    patterns = ["o1-", "o3-", "-thinking-", "qwq", "marco", "deepseek-r1", "reason", "r1-1776"]

    for p in patterns:
        if p in m_name:
            return True

    return False



def format_is_open_source(m_name):
    if is_open_source(m_name):
        return ":white_check_mark:"
    else:
        return ":x:"


def execute(evaluation_folder, target_file, include_closed_source=True, require_vision=False,
            require_reasoning=False, leaderboard_title="Overall Leaderboard", reg_expr=None):
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
    max_c8 = 0.0
    max_c9 = 0.0
    max_c10 = 0.0

    for m in models:
        if "DeepSeek-R1-671B-HB" in m:
            continue

        if (include_closed_source or is_open_source(m)) and (not require_reasoning or is_large_reasoning_model(m)):
            if reg_expr is None or reg_expr.lower() in m.lower():
                res, this_json = execute_script(evaluation_folder, m)

                this_json["score_c1"] = round(this_json["score_c1"], 1)
                this_json["score_c2"] = round(this_json["score_c2"], 1)
                this_json["score_c3"] = round(this_json["score_c3"], 1)
                this_json["score_c4"] = round(this_json["score_c4"], 1)
                this_json["score_c5"] = round(this_json["score_c5"], 1)
                this_json["score_c6"] = round(this_json["score_c6"], 1)
                this_json["score_c7"] = round(this_json["score_c7"], 1)
                this_json["score_c8"] = round(this_json["score_c8"], 1)
                this_json["score_c9"] = round(this_json["score_c9"], 1)
                this_json["score_c10"] = round(this_json["score_c10"], 1)

                if this_json["score_c7"] > 0 or not require_vision:
                    temp[m] = res
                    max_c1 = max(max_c1, this_json["score_c1"])
                    max_c2 = max(max_c2, this_json["score_c2"])
                    max_c3 = max(max_c3, this_json["score_c3"])
                    max_c4 = max(max_c4, this_json["score_c4"])
                    max_c5 = max(max_c5, this_json["score_c5"])
                    max_c6 = max(max_c6, this_json["score_c6"])
                    max_c7 = max(max_c7, this_json["score_c7"])
                    max_c8 = max(max_c8, this_json["score_c8"])
                    max_c9 = max(max_c9, this_json["score_c9"])
                    max_c10 = max(max_c10, this_json["score_c10"])

                    all_jsons[m] = this_json

    for m in temp:
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
        score_c8 = format_numb_in_table(this_json["score_c8"], max_c8)
        score_c9 = format_numb_in_table(this_json["score_c9"], max_c9)
        score_c10 = format_numb_in_table(this_json["score_c10"], max_c10)

        results.append((m, this_json["score_textual"], this_json["total_score"], table, score_c1, score_c2, score_c3,
                        score_c4, score_c5, score_c6, score_c7, score_c8, score_c9, score_c10))

    results.sort(key=lambda x: (
    x[1], x[2], this_json["score_c1"], this_json["score_c2"], this_json["score_c3"], this_json["score_c4"],
    this_json["score_c5"], x[0]), reverse=True)

    overall_table = []

    target_len = 29
    for m in results:
        m_n = m[0]
        if len(m_n) > target_len:
            spli = m_n.split("-")
            news = ""
            i = 0
            while i < len(spli):
                if i == 0 or len(news)+len(spli[i])+1 <= target_len:
                    if i > 0:
                        news += "-"
                    news += spli[i]
                else:
                    break
                i = i + 1
            m_n = news[0:min(target_len+1, len(news))]
        #m_n = m_n.capitalize()

        average = float(m[1]) / 4.6

        if m[1] == m[2]:
            entry = {"Model": m_n, "Avg": "**%.1f**" % (average), "Score": "**%.1f**" % (m[1]), "OS": format_is_open_source(m[0]), "C1": m[4],
                     "C2": m[5], "C3": m[6], "C4": m[7], "C5": m[8], "C6": m[9], "C7": m[10]}
        else:
            entry = {"Model": m_n, "Avg": "**%.1f**" % (average), "Score": "**%.1f**" % (m[1]), "OS": format_is_open_source(m[0]), "C1": m[4],
                     "C2": m[5], "C3": m[6], "C4": m[7], "C5": m[8], "C6": m[9], "C7": m[10]}
        overall_table.append(entry)

    overall_table = pd.DataFrame(overall_table)
    overall_table.columns = ["Model", "Avg", "Score", "OS", "PCo", "CC", "PMo", "PQ", "HG", "FA", ":nerd_face: VI"]
    overall_table = overall_table.to_markdown(index=False)

    output = []
    output.append(
        "A score in the range **25-30** is considered **sufficient**; a score in the range **30-35** is considered **good**; and a score **>35** is considered **excellent**.")
    output.append(
        "\n**As of 2025-01-26, the chain of thought of Large Reasoning Models, if provided, is considered in the assessment of answers.**")

    output.append("## %s (1-shot; %s used as a judge)" % (leaderboard_title, EVALUATING_MODEL_NAME))
    output.append(overall_table)

    for m in results:
        output.append("### %s   => %.1f points" % (m[0], m[1]))
        output.append(m[3])

    output = "\n\n".join(output)

    F = open(target_file, "w")
    F.write(output)
    F.close()

    print("wrote", target_file)

    return output, all_jsons, [m[0] for m in results]


def write_evaluation(base_path, extra=True):
    e_m_name = clean_model_name(EVALUATING_MODEL_NAME)
    base_evaluation_path = get_base_evaluation_path(EVALUATING_MODEL_NAME)
    evaluation_folder = os.path.join(base_path, base_evaluation_path)

    execute(evaluation_folder, os.path.join(base_path, "leaderboard_" + e_m_name + ".md"), include_closed_source=True, require_vision=False,
            leaderboard_title="Overall Leaderboard")

    if extra and e_m_name == "gpt-4o-2024-11-20":
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_lrms_" + e_m_name + ".md"), include_closed_source=True,
                require_vision=False, require_reasoning=True, leaderboard_title="Large Reasoning Models Leaderboard")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_os_" + e_m_name + ".md"), include_closed_source=False,
                require_vision=False, leaderboard_title="Open-Source Leaderboard")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_vis_" + e_m_name + ".md"), include_closed_source=True,
                require_vision=True, leaderboard_title="Vision Leaderboard")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_os_vis_" + e_m_name + ".md"), include_closed_source=False,
                require_vision=True, leaderboard_title="Open-Source Vision Leaderboard")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_qwen_" + e_m_name + ".md"),
                include_closed_source=True, require_vision=False,
                leaderboard_title="QWEN Leaderboard", reg_expr="qwen")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_deepseek_" + e_m_name + ".md"),
                include_closed_source=True, require_vision=False,
                leaderboard_title="DEEPSEEK Leaderboard", reg_expr="deepseek")


if __name__ == "__main__":
    write_evaluation("..", extra=True)
