import os
import re
import numpy as np


pattern = r'\d+'
reg_expr = re.compile(pattern)

evaluation_folder = "../evaluation"

eval_files = os.listdir(evaluation_folder)

questions_eval = {}

for file in eval_files:
    if ".txt" in file:
        full_path = os.path.join(evaluation_folder, file)

        contents = open(full_path, "r").read()

        numbers = reg_expr.findall(contents)

        if numbers:
            numbers = [float(x) for x in numbers]

            if numbers[0] >= 1 and numbers[0] <= 10:
                if "__" in file:
                    answering_llm = file.split("__")[0]
                    evaluating_llm = file.split("__")[1]
                    tup = (answering_llm, evaluating_llm)
                    question = file.split("__")[-1].split(".")[0]

                    #print(question, answering_llm, evaluating_llm, numbers[0])

                    if tup not in questions_eval:
                        questions_eval[tup] = []

                    questions_eval[tup].append(numbers[0])

for tup in questions_eval:
    questions_eval[tup] = (round(float(np.mean(questions_eval[tup])) , 1), round(float(np.std(questions_eval[tup])), 1))

    print(tup, questions_eval[tup])
