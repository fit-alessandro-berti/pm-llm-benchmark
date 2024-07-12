import os
import re

pattern = r'\d+'
reg_expr = re.compile(pattern)

evaluation_folder = "../evaluation"

eval_files = os.listdir(evaluation_folder)

for file in eval_files:
    if ".txt" in file:
        full_path = os.path.join(evaluation_folder, file)

        contents = open(full_path, "r").read()

        numbers = reg_expr.findall(contents)

        if numbers:
            numbers = [float(x) for x in numbers]
