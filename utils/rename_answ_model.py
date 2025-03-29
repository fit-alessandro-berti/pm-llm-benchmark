import os
from overall_table import write_evaluation


def do_renaming(base_path, original_name, novel_name):
    if not os.path.exists(base_path):
        raise Exception("base_path %s does not exists!" % (base_path))

    files = [x for x in os.listdir(base_path) if x.startswith(original_name)]

    for f in files:
        original_path = os.path.join(base_path, f)
        new_path = original_path.replace(original_name, novel_name)

        print(original_path, new_path, os.path.exists(original_path), os.path.exists(new_path))
        os.rename(original_path, new_path)


if __name__ == "__main__":
    original_name = "chatgpt-4o-latest_"
    novel_name = "chatgpt-4o-latest-2025-03-26_"

    if not original_name.endswith("_"):
        raise Exception("original_name must terminate with _")

    if not novel_name.endswith("_"):
        raise Exception("novel_name must terminate with _")

    do_renaming("../answers", original_name, novel_name)
    do_renaming("../evaluation-gemini-2.5-pro", original_name, novel_name)

    write_evaluation("..", extra=True)
