import os
import pandas as pd
import json
from collections import Counter
from utils.table_per_model import execute_script
from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path, is_open_source, is_large_reasoning_model, force_custom_evaluation_lrm, is_excluded_from_table


def format_numb_in_table(score, max_score, good_diff=0.3):
    if score == max_score:
        return ":mage_woman: **%.1f**" % (score)
    elif score >= max_score - good_diff:
        return "**%.1f**" % (score)
    return "%.1f" % (score)


def format_is_open_source(m_name):
    if is_open_source(m_name):
        return ":white_check_mark:"
    else:
        return ":x:"


def format_is_lrm(m_name):
    if is_large_reasoning_model(m_name):
        return ":white_check_mark:"
    else:
        return ":x:"


def manage_file_name(file_name, rec_depth=0):
    if rec_depth > 1:
        return file_name

    if "deepseek-ai" in file_name:
        return manage_file_name(file_name.split("deepseek-ai")[-1], rec_depth+1)

    if "nvidia" in file_name:
        return manage_file_name(file_name.split("nvidia")[-1], rec_depth+1)

    if file_name.lower().startswith("qwenqw"):
        file_name = file_name[4:]
        return manage_file_name(file_name, rec_depth+1)

    if file_name.startswith("microsoft"):
        file_name = file_name[9:]
        return manage_file_name(file_name, rec_depth+1)

    if file_name.startswith("meta-llama"):
        file_name = file_name[10:]
        return manage_file_name(file_name, rec_depth+1)

    if file_name.startswith("deepseekdeep"):
        file_name = file_name[8:]
        return manage_file_name(file_name, rec_depth+1)

    if file_name.lower().startswith("meta-"):
        file_name = file_name[5:]
        return manage_file_name(file_name, rec_depth+1)

    if file_name.lower().endswith("free"):
        file_name = file_name.split("free")[0]
        return manage_file_name(file_name, rec_depth+1)

    if "nemotron" in file_name.lower():
        file_name = "nemotron" + file_name.lower().split("nemotron")[-1]
        return manage_file_name(file_name, rec_depth+1)

    return file_name


def execute(evaluation_folder, target_file, include_closed_source=True, require_vision=False,
            require_reasoning=False, require_reasoning_custom=False, require_not_reasoning=False,
            leaderboard_title="Overall Leaderboard", reg_expr=None, json_file=None):
    files = os.listdir(evaluation_folder)
    models = Counter([f.split("_cat")[0] for f in files if not "__init__" in f])
    models = {x: y for x, y in models.items() if y >= 44 and not is_excluded_from_table(x)}

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
        if (include_closed_source or is_open_source(m)) and \
                (not require_reasoning or (is_large_reasoning_model(m) and \
                                           (not require_reasoning_custom or force_custom_evaluation_lrm(m)))) and \
                (not require_not_reasoning or not is_large_reasoning_model(m)):
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

    target_len = 33
    for m in results:
        m_n = manage_file_name(m[0])
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

        average = float(m[1]) / 4.6

        if m[1] == m[2]:
            entry = {"Model": m_n, "Score": "**%.1f**" % (m[1]),
                     "OS": format_is_open_source(m[0]), "LRM": format_is_lrm(m[0]),
                     "C1": m[4], "C2": m[5], "C3": m[6], "C4": m[7], "C5": m[8], "C6": m[9], "C8": m[11], "C7": m[10]}
        else:
            entry = {"Model": m_n, "Score": "**%.1f**" % (m[1]),
                     "OS": format_is_open_source(m[0]), "LRM": format_is_lrm(m[0]),
                     "C1": m[4], "C2": m[5], "C3": m[6], "C4": m[7], "C5": m[8], "C6": m[9], "C8": m[11], "C7": m[10]}
        overall_table.append(entry)

    if json_file is not None:
        F = open(json_file, "w")
        json.dump(overall_table, F)
        F.close()

    overall_table = pd.DataFrame(overall_table)
    overall_table.columns = ["Model", "Score", "OS", "LRM", "PCo", "CC", "PMo", "PQ", "HG", "FA", "OPT", ":nerd_face: VI"]
    overall_table = overall_table.to_markdown(index=False)

    output = []
    output.append(
        "A score in the range **24-29** is considered **sufficient**; a score in the range **29-34** is considered **fair**; a score in the range **34-40** is considered **good**; and a score **>40** is considered **excellent**.")

    output.append("## %s (1-shot; %s used as a judge)" % (leaderboard_title, EVALUATING_MODEL_NAME))
    output.append(overall_table)

    for m in results:
        output.append("### %s   => %.1f points" % (m[0], m[1]))
        output.append(m[3])

    output = "\n\n".join(output)

    if target_file is not None:
        F = open(target_file, "w")
        F.write(output)
        F.close()
        print("wrote", target_file)

    return output, all_jsons, [m[0] for m in results]


def get_suffix_name(e_m_name):
    return e_m_name.split("-exp")[0].split("-preview")[0]


def write_evaluation(base_path, extra=True):
    e_m_name = clean_model_name(EVALUATING_MODEL_NAME)
    base_evaluation_path = get_base_evaluation_path(EVALUATING_MODEL_NAME)
    evaluation_folder = os.path.join(base_path, base_evaluation_path)

    execute(evaluation_folder, os.path.join(base_path, "leaderboard_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=True, require_vision=False,
            leaderboard_title="Overall Leaderboard", json_file=os.path.join(base_path, "hallucinations/leaderboard_stats.md"))

    if extra and e_m_name.startswith("gemini-2.5-pro"):
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_lrms_cot_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=True,
                require_vision=False, require_reasoning=True, require_reasoning_custom=True, leaderboard_title="Large Reasoning Models Leaderboard (Models with CoT)")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_nolrms_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=True,
                require_vision=False, require_not_reasoning=True, leaderboard_title="Base LLMs Leaderboard")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_os_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=False,
                require_vision=False, leaderboard_title="Open-Source Leaderboard")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_os_nolrms_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=False,
                require_vision=False, require_not_reasoning=True, leaderboard_title="Base Open-Source LLMs Leaderboard")
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_QWEN_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=True, require_vision=False,
                leaderboard_title="QWEN Leaderboard", reg_expr="qwen")


if __name__ == "__main__":
    write_evaluation("..", extra=True)
