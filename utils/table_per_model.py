import os
import re
import sys
import pandas as pd

evaluation_folder = "../evaluation" if len(sys.argv) < 3 else sys.argv[2]
pattern = r'[-+]?\d*\.\d+'
reg_expr = re.compile(pattern)


if __name__ == "__main__":
    model_name = "" if len(sys.argv) < 2 else sys.argv[1]

    while not model_name:
        model_name = input("Please insert the name of the model -> ")

    model_name = model_name.replace("/", "").replace(":", "")
    responses = [x for x in os.listdir(evaluation_folder) if x.startswith(model_name)]

    evaluations = []
    total_score = 0.0
    score_textual = 0.0

    for resp in responses:
        question = resp.split(model_name+"_")[1].split(".")[0]
        target_path = os.path.join(evaluation_folder, resp)

        is_textual = True if int(question.split("_")[0].split("cat")[1]) <= 6 else False

        contents = open(target_path, "r").read()

        numbers = reg_expr.findall(contents)

        if numbers:
            numb = float(numbers[0])
            total_score += numb

            if is_textual:
                score_textual += numb
        else:
            numb = 1.0

        evaluations.append({"Question": question, "Score": numb})

    evaluations = sorted(evaluations, key=lambda x: x["Question"])
    evaluations = pd.DataFrame(evaluations)
    evaluations = evaluations.to_markdown(index=False)

    print(evaluations)

    total_score /= 10
    score_textual /= 10

    print("\n==OVERALL SCORES==", "\t", score_textual, "\t", total_score)

