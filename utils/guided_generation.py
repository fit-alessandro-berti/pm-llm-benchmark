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

    proceed = False

    if not os.path.exists(answer_path):
        proceed = True
    else:
        contents = open(answer_path, "r").read().strip()
        if not contents:
            proceed = True

    if proceed:
        pyperclip.copy(question)

        F = open(answer_path, "w")
        F.close()

        subprocess.run(["notepad.exe", answer_path])
