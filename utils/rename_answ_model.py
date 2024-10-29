import os

original_name = "o1-mini"
novel_name = "o1-mini-2024-09-12"

files = [x for x in os.listdir("../answers") if x.startswith(original_name)]

for f in files:
    original_path = os.path.join("../answers", f)
    new_path = original_path.replace(original_name, novel_name)

    print(original_path, new_path, os.path.exists(original_path), os.path.exists(new_path))
    os.rename(original_path, new_path)
