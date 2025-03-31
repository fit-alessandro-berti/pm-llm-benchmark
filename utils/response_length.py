import os
import pandas as pd


models_counter = {}
answers_folder = "../answers"
target_file = "../response_length.md"

for file_name in os.listdir(answers_folder):
    if file_name.endswith(".txt"):
        file_path = os.path.join(answers_folder, file_name)
        model = file_name.split("_")[0]
        if model not in models_counter:
            models_counter[model] = []

        lenn = os.stat(file_path).st_size
        models_counter[model].append(lenn)

mck = list(models_counter)
mck.sort()

df = []

for model in mck:
    models_counter[model].sort()
    lst = models_counter[model]
    el_min = lst[0]
    el_max = lst[-1]
    el_fquart = lst[int(len(lst)*0.25)]
    el_median = lst[int(len(lst)*0.5)]
    el_tquart = lst[int(len(lst)*0.75)]

    df.append({"Model": model, "Min": el_min, "1stQuart": el_fquart, "Median": el_median, "3rdQuart": el_tquart, "Max": el_max})


df = pd.DataFrame(df)
df.sort_values(["Median", "3rdQuart", "Model"], ascending=False, inplace=True)
df.to_markdown(target_file, index=False)
