import os
import pyperclip
import subprocess

questions_folder = "../questions"
answers_folder = "../answers"

questions = [x for x in os.listdir(questions_folder) if x.endswith("txt")]

model_name = input("Give me the name of the model that you are testing -> ")

for q in questions:
    question_path = os.path.join(questions_folder, q)

    question = open(question_path, "r").read().strip()

    answer_path = os.path.join(answers_folder, model_name.replace("/", "").replace(":", "") + "_" + q).replace(".png", ".txt")

    pyperclip.copy(question)

    if os.path.exists(answer_path):
        continue
    else:
        F = open(answer_path, "w")
        F.close()

    subprocess.run(["notepad.exe", answer_path])
