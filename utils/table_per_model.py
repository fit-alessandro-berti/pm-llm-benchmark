import os
import re
import sys
import pandas as pd

pattern = r'[-+]?\d*\.\d+'
reg_expr = re.compile(pattern)


def execute_script(evaluation_folder, model_name):
    responses = [x for x in os.listdir(evaluation_folder) if x.startswith(model_name)]

    evaluations = []
    total_score = 0.0
    score_textual = 0.0

    for resp in responses:
        question = resp.split(model_name + "_")[1].split(".")[0]
        target_path = os.path.join(evaluation_folder, resp)

        is_textual = True if int(question.split("_")[0].split("cat")[1]) <= 6 else False

        contents = open(target_path, "r").read()

        numbers = reg_expr.findall(contents)
        numb = 1.0

        if numbers:
            numb = float(numbers[0])
            if numb < 1.0 or numb > 10.0:
                numb = 1.0


        total_score += numb

        if is_textual:
            score_textual += numb

        evaluations.append({"Question": question, "Score": numb})

    evaluations = sorted(evaluations, key=lambda x: x["Question"])
    evaluations = pd.DataFrame(evaluations)
    evaluations = evaluations.to_markdown(index=False)

    result = [evaluations]

    total_score /= 10
    score_textual /= 10

    result.append("==OVERALL SCORES==\t%.1f\t%.1f" % (score_textual, total_score))

    return "\n\n".join(result)


if __name__ == "__main__":
    evaluation_folder = "../evaluation" if len(sys.argv) < 3 else sys.argv[2]

    model_name = "" if len(sys.argv) < 2 else sys.argv[1]

    while not model_name:
        model_name = input("Please insert the name of the model -> ")

    model_name = model_name.replace("/", "").replace(":", "")
    result = execute_script(evaluation_folder, model_name)

    print(result)
