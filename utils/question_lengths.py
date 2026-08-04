import os

try:
    from utils.script_bootstrap import chdir_repo_root
except ModuleNotFoundError:
    from script_bootstrap import chdir_repo_root


chdir_repo_root()

questions_folder = "questions"
lengths = []

for file_name in os.listdir(questions_folder):
    if not file_name.endswith(".txt"):
        continue
    file_path = os.path.join(questions_folder, file_name)
    lengths.append((os.stat(file_path).st_size, file_name))

for size, _ in sorted(lengths):
    print(size)
