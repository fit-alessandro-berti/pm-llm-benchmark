import os
import json
from utils.table_per_model import execute_script, index_evaluation_files, render_markdown_table
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


def round_model_scores(this_json):
    for score_key in ("score_c1", "score_c2", "score_c3", "score_c4", "score_c5",
                      "score_c6", "score_c7", "score_c8", "score_c9", "score_c10"):
        this_json[score_key] = round(this_json[score_key], 1)
    return this_json


def model_is_allowed(model_name, allowed_models):
    if allowed_models is None:
        return True
    if model_name in allowed_models:
        return True
    return any(model_name in candidate or candidate in model_name for candidate in allowed_models)


def build_model_results(evaluation_folder):
    responses_by_model = index_evaluation_files(evaluation_folder)
    model_results = {}

    for model_name, responses in responses_by_model.items():
        if len(responses) < 44 or is_excluded_from_table(model_name):
            continue
        rendered_table, this_json = execute_script(evaluation_folder, model_name, responses=responses)
        model_results[model_name] = {
            "response_count": len(responses),
            "table": rendered_table.split("==OVERALL SCORES==")[0].rstrip(),
            "scores": round_model_scores(this_json),
        }

    return model_results


def execute(evaluation_folder, target_file, include_closed_source=True, require_vision=False,
            require_reasoning=False, require_reasoning_custom=False, require_not_reasoning=False,
            leaderboard_title="Overall Leaderboard", reg_expr=None, json_file=None, allowed_models=None,
            model_results=None):
    if model_results is None:
        model_results = build_model_results(evaluation_folder)

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

    for m, model_data in model_results.items():
        if not model_is_allowed(m, allowed_models):
            continue
        if (include_closed_source or is_open_source(m)) and \
                (not require_reasoning or (is_large_reasoning_model(m) and
                                           (not require_reasoning_custom or force_custom_evaluation_lrm(m)))) and \
                (not require_not_reasoning or not is_large_reasoning_model(m)):
            if reg_expr is None or reg_expr.lower() in m.lower():
                this_json = model_data["scores"]

                if this_json["score_c7"] > 0 or not require_vision:
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

    for m, model_data in model_results.items():
        if m not in all_jsons:
            continue
        this_json = all_jsons[m]
        table = model_data["table"]

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

        results.append({
            "model": m,
            "score_textual": this_json["score_textual"],
            "total_score": this_json["total_score"],
            "table": table,
            "raw_scores": (
                this_json["score_c1"], this_json["score_c2"], this_json["score_c3"], this_json["score_c4"],
                this_json["score_c5"], this_json["score_c6"], this_json["score_c7"], this_json["score_c8"],
                this_json["score_c9"], this_json["score_c10"]
            ),
            "formatted_scores": (score_c1, score_c2, score_c3, score_c4, score_c5, score_c6, score_c7, score_c8, score_c9, score_c10),
        })

    results.sort(
        key=lambda x: (
            x["score_textual"], x["total_score"], x["raw_scores"][0], x["raw_scores"][1], x["raw_scores"][2],
            x["raw_scores"][3], x["raw_scores"][4], x["model"]
        ),
        reverse=True,
    )

    overall_table = []
    leaderboard_stats = []

    target_len = 33
    for result in results:
        display_model_name = manage_file_name(result["model"])
        if len(display_model_name) > target_len:
            spli = display_model_name.split("-")
            news = ""
            i = 0
            while i < len(spli):
                if i == 0 or len(news) + len(spli[i]) + 1 <= target_len:
                    if i > 0:
                        news += "-"
                    news += spli[i]
                else:
                    break
                i = i + 1
            display_model_name = news[0:min(target_len+1, len(news))]

        formatted_scores = result["formatted_scores"]
        entry = {"Model": display_model_name, "Score": "**%.1f**" % (result["score_textual"]),
                 "OS": format_is_open_source(result["model"]), "LRM": format_is_lrm(result["model"]),
                 "C1": formatted_scores[0], "C2": formatted_scores[1], "C3": formatted_scores[2],
                 "C4": formatted_scores[3], "C5": formatted_scores[4], "C6": formatted_scores[5],
                 "C8": formatted_scores[7], "C7": formatted_scores[6]}
        overall_table.append(entry)
        leaderboard_stats.append({**entry, "Model": result["model"]})

    if json_file is not None:
        with open(json_file, "w") as handler:
            json.dump(leaderboard_stats, handler)

    headers = ["Model", "Score", "OS", "LRM", "PCo", "CC", "PMo", "PQ", "HG", "FA", "OPT", ":nerd_face: VI"]
    rows = [
        [entry["Model"], entry["Score"], entry["OS"], entry["LRM"], entry["C1"], entry["C2"], entry["C3"],
         entry["C4"], entry["C5"], entry["C6"], entry["C8"], entry["C7"]]
        for entry in overall_table
    ]
    overall_table_markdown = render_markdown_table(headers, rows)

    output = []
    output.append(
        "A score in the range **20-25** is considered **sufficient**; a score in the range **25-30** is considered **fair**; a score in the range **30-37** is considered **good**; and a score **>37** is considered **excellent**.")

    output.append("## %s (1-shot; %s used as a judge)" % (leaderboard_title, EVALUATING_MODEL_NAME))
    output.append(overall_table_markdown)

    for result in results:
        output.append("### %s   => %.1f points" % (result["model"], result["score_textual"]))
        output.append(result["table"])

    output = "\n\n".join(output)

    if target_file is not None:
        with open(target_file, "w") as handler:
            handler.write(output)
        print("wrote", target_file)

    return output, all_jsons, [result["model"] for result in results]


def get_suffix_name(e_m_name):
    return e_m_name.split("-exp")[0].split("-preview")[0]


def write_evaluation(base_path, extra=True):
    e_m_name = clean_model_name(EVALUATING_MODEL_NAME)
    base_evaluation_path = get_base_evaluation_path(EVALUATING_MODEL_NAME)
    evaluation_folder = os.path.join(base_path, base_evaluation_path)
    model_results = build_model_results(evaluation_folder)

    # Main overall leaderboard
    execute(
        evaluation_folder,
        os.path.join(base_path, "leaderboard_" + get_suffix_name(e_m_name) + ".md"),
        include_closed_source=True,
        require_vision=False,
        leaderboard_title="Overall Leaderboard",
        json_file=os.path.join(base_path, "hallucinations/leaderboard_stats.md"),
        model_results=model_results,
    )

    # --- New: small models leaderboard based on hallucinations/model_info.json ---
    model_info_path = os.path.join(base_path, "hallucinations", "model_info.json")
    small_models = set()
    try:
        with open(model_info_path, "r") as f:
            model_info = json.load(f)
        for k, v in model_info.items():
            if isinstance(v, list) and len(v) > 0:
                first_val = v[0]
                # Accept numeric values that are strictly lower than 5
                try:
                    first_val_num = float(first_val)
                    if first_val_num < 5:
                        small_models.add(k)
                except (TypeError, ValueError):
                    # Non-numeric first value, ignore
                    continue
    except FileNotFoundError:
        model_info = {}
        small_models = set()

    if True and (extra and "gpt-5.4" in e_m_name):
        if len(small_models) > 0:
            execute(
                evaluation_folder,
                os.path.join(base_path, "leaderboard_small_" + get_suffix_name(e_m_name) + ".md"),
                include_closed_source=True,
                require_vision=False,
                leaderboard_title="Small Models (<5B) Leaderboard",
                allowed_models=small_models,
                model_results=model_results,
            )

        execute(evaluation_folder, os.path.join(base_path, "leaderboard_lrms_cot_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=True,
                require_vision=False, require_reasoning=True, require_reasoning_custom=True, leaderboard_title="Large Reasoning Models Leaderboard (Models with CoT)", model_results=model_results)
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_nolrms_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=True,
                require_vision=False, require_not_reasoning=True, leaderboard_title="Base LLMs Leaderboard", model_results=model_results)
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_os_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=False,
                require_vision=False, leaderboard_title="Open-Source Leaderboard", model_results=model_results)
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_os_nolrms_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=False,
                require_vision=False, require_not_reasoning=True, leaderboard_title="Base Open-Source LLMs Leaderboard", model_results=model_results)
        execute(evaluation_folder, os.path.join(base_path, "leaderboard_QWEN_" + get_suffix_name(e_m_name) + ".md"), include_closed_source=True, require_vision=False,
                leaderboard_title="QWEN Leaderboard", reg_expr="qwen", model_results=model_results)


if __name__ == "__main__":
    write_evaluation("..", extra=True)
