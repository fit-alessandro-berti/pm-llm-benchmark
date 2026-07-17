import os

try:
    from utils.script_bootstrap import chdir_repo_root
except ModuleNotFoundError:
    from script_bootstrap import chdir_repo_root

chdir_repo_root()

from file_utils import read_file_with_fallback


def starts_with_think(file_path):
    return read_file_with_fallback(file_path)[:1024].lstrip().startswith("<think>")


llms = set()
for filename in os.listdir("answers"):
    if "_cat" not in filename:
        continue

    file_path = os.path.join("answers", filename)
    if starts_with_think(file_path):
        llms.add(filename.split("_cat", 1)[0])

with open(os.path.join("utils", "lrms_list.txt"), "w", encoding="utf-8") as handler:
    handler.write("\n".join(sorted(llms)))
