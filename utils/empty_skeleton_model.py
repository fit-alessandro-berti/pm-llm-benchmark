import os

questions = [x for x in os.listdir("../questions") if x.endswith(".txt") or x.endswith(".png")]

MODEL_NAME = "claude-3-sonnet"

for q in questions:
    question_path = os.path.join("../questions", q)
    answer_path = (MODEL_NAME.replace("/", "").replace(":", "") + "_" + q).replace(".png", ".txt")

    if not os.path.exists(answer_path):
        F = open(answer_path, "w")
        F.close()
