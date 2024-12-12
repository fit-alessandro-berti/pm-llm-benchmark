import os
import re
import sys
import pandas as pd
from common import ANSWERING_MODEL_NAME, clean_model_name


pattern = r'(?P<sign>[-+]?)(?:\d*\.\d+|(?P<numerator>\d+)/(?P<denominator>\d+))'
reg_expr = re.compile(pattern)

def match_regex(text):
    for match in reg_expr.finditer(text):
        if match.group('numerator'):
            numerator = int(match.group('numerator'))
            return numerator
        else:
            number = float(match.group(0))
            return number


def execute_script(evaluation_folder, model_name):
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

    for resp in responses:
        question = resp.split(model_name + "_")[1].split(".")[0]
        target_path = os.path.join(evaluation_folder, resp)

        catnum = int(question.split("_")[0].split("cat")[1])
        is_textual = True if catnum != 7 else False

        contents = open(target_path, "r").read()

        numbers = match_regex(contents)
        numb = float(numbers) if numbers is not None else 1.0

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
    evaluations = pd.DataFrame(evaluations)
    evaluations.columns = ["Question", "Score"]
    evaluations = evaluations.to_markdown(index=False)

    result = [evaluations]

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
    evaluation_folder = "../evaluation" if len(sys.argv) < 3 else sys.argv[2]

    model_name = ANSWERING_MODEL_NAME
    #model_name = "gpt-4o-2024-11-20"

    model_name = clean_model_name(model_name)
    result, this_json = execute_script(evaluation_folder, model_name)

    print(result)
