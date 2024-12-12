import os
import common
from utils import forge_eval_prompt
import pyperclip
import subprocess

def read_contents(file_path):
    try:
        content = open(file_path, "r").read()
    except:
        content = open(file_path, "r", encoding="utf-8").read()

    return content


ANSWERING_MODEL_NAME = "gpt-4o-mini-2024-07-18"
EVALUATING_MODEL_NAME = "o1-2024-12-05"

m_name = common.clean_model_name(ANSWERING_MODEL_NAME)
e_m_name = common.clean_model_name(EVALUATING_MODEL_NAME)

questions_path = "../questions"
answers_path = "../answers"
base_evaluation_path = common.get_base_evaluation_path(e_m_name)
evaluation_path = os.path.join("..", base_evaluation_path)

if not os.path.exists(evaluation_path):
    os.mkdir(evaluation_path)

answers = [x for x in os.listdir(answers_path) if x.startswith(m_name)]

for answ in answers:
    answer_path = os.path.join(answers_path, answ)
    answer = read_contents(answer_path)

    question = "cat" + answ.split("_cat")[1].split(".")[0]

    ev_path = os.path.join(evaluation_path, m_name + "_" + question + ".txt")
    q_path = os.path.join(questions_path, question)

    cont = False
    if not os.path.exists(ev_path):
        cont = True
    elif os.path.getsize(ev_path) == 0:
        cont = True

    if cont:
        if os.path.exists(q_path+".txt"):
            q_path = q_path + ".txt"
        elif os.path.exists(q_path+".png"):
            q_path = q_path + ".png"
        else:
            raise Exception("not existing!")

        inquiry, base64_image = forge_eval_prompt.forge(q_path, answer)
        pyperclip.copy(inquiry)

        F = open(ev_path, "w")
        F.close()
        subprocess.run(["notepad.exe", ev_path])
