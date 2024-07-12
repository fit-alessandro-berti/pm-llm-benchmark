import os

answers_path = "../answers"

answers = os.listdir(answers_path)

models = set()

for file in answers:
    if file.endswith(".txt"):
        model = file.split("_cat")[0]

        models.add(model)

models = sorted(list(models))

for model in models:
    print(model)
