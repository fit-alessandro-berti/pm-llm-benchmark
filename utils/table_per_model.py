import os
import re
import sys
from common import ANSWERING_MODEL_NAME, EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path, force_custom_evaluation_lrm


pattern = r'(?P<sign>[-+]?)(?:(?P<float>\d+\.\d+)|(?P<int>\d+)|(?P<numerator>\d+)/(?P<denominator>\d+))(?!\.)'
reg_expr = re.compile(pattern)


def render_markdown_table(headers, rows):
    headers = [str(header) for header in headers]
    rows = [[str(cell) for cell in row] for row in rows]
    widths = [len(header) for header in headers]

    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))

    def format_row(row):
        return "| " + " | ".join(cell.ljust(widths[index]) for index, cell in enumerate(row)) + " |"

    separator = "| " + " | ".join("-" * width for width in widths) + " |"
    output = [format_row(headers), separator]
    output.extend(format_row(row) for row in rows)
    return "\n".join(output)


def index_evaluation_files(evaluation_folder, files=None):
    if files is None:
        files = os.listdir(evaluation_folder)

    responses_by_model = {}
    for filename in files:
        if "__init__" in filename:
            continue
        model_name = filename.split("_cat")[0]
        responses_by_model.setdefault(model_name, []).append(filename)

    return responses_by_model


def match_regex(text):
    matches = list(reg_expr.finditer(text))
    matches_numbers_floats = []
    matches_numbers_ints = []
    for match in matches:
        match_stri = str(match.group(0))
        number = float(match_stri)
        if number >= 1 and number <= 10:
            if "." in match_stri:
                matches_numbers_floats.append(number)
            else:
                matches_numbers_ints.append(number)

    if matches_numbers_floats:
        if 10.0 in matches_numbers_floats:
            idx = matches_numbers_floats.index(10.0)
            if idx > 0:
                return matches_numbers_floats[idx-1]
        return matches_numbers_floats[0]
    elif matches_numbers_ints:
        return matches_numbers_ints[0]


def execute_script(evaluation_folder, model_name, responses=None):
    if responses is None:
        responses = [x for x in os.listdir(evaluation_folder) if x.startswith(model_name+"_")]

    evaluations = []
    total_score = 0.0
    score_textual = 0.0
    score_c1 = 0.0
    score_c2 = 0.0
    score_c3 = 0.0
    score_c4 = 0.0
    score_c5 = 0.0
    score_c6 = 0.0
    score_c7 = 0.0
    score_c8 = 0.0
    score_c9 = 0.0
    score_c10 = 0.0

    this_json = {"score_questions": []}
    needs_custom_evaluation = force_custom_evaluation_lrm(model_name)

    for resp in responses:
        question = resp.split(model_name + "_")[1].split(".")[0]
        target_path = os.path.join(evaluation_folder, resp)

        catnum = int(question.split("_")[0].split("cat")[1])
        is_textual = True if catnum != 7 else False

        try:
            with open(target_path, "r", encoding="utf-8") as handler:
                contents = handler.read()
        except UnicodeDecodeError:
            with open(target_path, "r", encoding="latin-1") as handler:
                contents = handler.read()

        numbers = match_regex(contents)
        numb = float(numbers) if numbers is not None else 1.0

        # pre-normalization step
        numb = min(7.0, numb) + 0.5 * max(min(numb, 9.0) - 7.0, 0) + 2.0 * max(numb - 9.0, 0)

        if needs_custom_evaluation:
            numb0 = numb
            diff = 10.0 - numb0
            factor = 1.15
            diff = round(diff * factor, 1)
            numb = max(1.0, 10.0 - diff)

        total_score += numb

        if is_textual:
            score_textual += numb

        if catnum == 1:
            score_c1 += numb
        elif catnum == 2:
            score_c2 += numb
        elif catnum == 3:
            score_c3 += numb
        elif catnum == 4:
            score_c4 += numb
        elif catnum == 5:
            score_c5 += numb
        elif catnum == 6:
            score_c6 += numb
        elif catnum == 7:
            score_c7 += numb
        elif catnum == 8:
            score_c8 += numb
        elif catnum == 9:
            score_c9 += numb
        elif catnum == 10:
            score_c10 += numb

        evaluations.append({"Question": question, "Score": numb})
        this_json["score_questions"].append([question, numb])

    evaluations = sorted(evaluations, key=lambda x: x["Question"])
    evaluations_markdown = render_markdown_table(
        ["Question", "Score"],
        [[entry["Question"], f"{entry['Score']:.1f}"] for entry in evaluations],
    )

    result = [evaluations_markdown]

    total_score /= 10
    score_textual /= 10
    score_c1 /= 10
    score_c2 /= 10
    score_c3 /= 10
    score_c4 /= 10
    score_c5 /= 10
    score_c6 /= 10
    score_c7 /= 10
    score_c8 /= 10
    score_c9 /= 10
    score_c10 /= 10

    this_json["score_questions"].sort(key=lambda x: x[0])
    this_json["total_score"] = total_score
    this_json["score_textual"] = score_textual
    this_json["score_c1"] = score_c1
    this_json["score_c2"] = score_c2
    this_json["score_c3"] = score_c3
    this_json["score_c4"] = score_c4
    this_json["score_c5"] = score_c5
    this_json["score_c6"] = score_c6
    this_json["score_c7"] = score_c7
    this_json["score_c8"] = score_c8
    this_json["score_c9"] = score_c9
    this_json["score_c10"] = score_c10

    result.append("==OVERALL SCORES==\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f" % (score_textual, total_score, score_c1, score_c2, score_c3, score_c4, score_c5, score_c6, score_c7, score_c8, score_c9, score_c10))

    return "\n\n".join(result), this_json


if __name__ == "__main__":
    evaluation_folder = os.path.join("..", get_base_evaluation_path(EVALUATING_MODEL_NAME)) if len(sys.argv) < 3 else sys.argv[2]

    model_name = ANSWERING_MODEL_NAME
    #model_name = "gpt-4o-2024-11-20"

    model_name = clean_model_name(model_name)
    result, this_json = execute_script(evaluation_folder, model_name)

    print(result)
