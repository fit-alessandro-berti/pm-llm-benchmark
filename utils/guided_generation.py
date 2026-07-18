import os
import shlex
import shutil
import subprocess
import sys

try:
    from utils.script_bootstrap import chdir_repo_root
except ModuleNotFoundError:
    from script_bootstrap import chdir_repo_root

from common import clean_model_name
from file_utils import read_file_with_fallback


chdir_repo_root()


def read_contents(file_path):
    return read_file_with_fallback(file_path)


def copy_to_clipboard(text):
    try:
        import pyperclip
    except ModuleNotFoundError as exc:
        raise RuntimeError("pyperclip is required for clipboard operations.") from exc
    pyperclip.copy(text)


def open_text_editor(file_path):
    configured_editor = os.environ.get("VISUAL") or os.environ.get("EDITOR")
    if configured_editor:
        subprocess.run(shlex.split(configured_editor) + [file_path])
        return

    if sys.platform.startswith("linux"):
        editor_candidates = ["mousepad", "xdg-open"]
    elif os.name == "nt":
        editor_candidates = ["notepad++.exe", "notepad.exe"]
    else:
        editor_candidates = ["open"]

    for editor in editor_candidates:
        if shutil.which(editor):
            subprocess.run([editor, file_path])
            return

    raise RuntimeError(
        "No supported text editor found. Install mousepad on Linux, "
        "Notepad++/Notepad on Windows, or set VISUAL/EDITOR."
    )


questions_folder = "questions"
answers_folder = "answers"

questions = [x for x in os.listdir(questions_folder) if x.endswith("txt")]
graphical_questions = [x for x in os.listdir(questions_folder) if x.endswith("png")]

print("!!!=== GUIDED GENERATION SCRIPT !!!===")
response = input("Do you want to generate a serie of TXT scripts? (y/n) ->")
if response.lower() != "y":
    sys.exit(0)

model_name = input("Give me the name of the model that you are testing -> ")

for q in questions:
    question_path = os.path.join(questions_folder, q)

    question = read_contents(question_path).strip()

    answer_path = os.path.join(answers_folder, clean_model_name(model_name) + "_" + q).replace(".png", ".txt")

    proceed = False

    if not os.path.exists(answer_path):
        proceed = True
    else:
        contents = read_contents(answer_path).strip()
        if not contents:
            proceed = True

    if proceed:
        copy_to_clipboard(question)

        F = open(answer_path, "w")
        F.close()

        open_text_editor(answer_path)

also_graphical = input("Does the model support multi-modality (pictures) ? (y/n)")

if also_graphical == "y":
    for q in graphical_questions:
        print(q)
        answer_path = os.path.join(answers_folder, clean_model_name(model_name) + "_" + q).replace(".png", ".txt")

        proceed = False

        if not os.path.exists(answer_path):
            proceed = True
        else:
            contents = read_file_with_fallback(answer_path).strip()
            if not contents:
                proceed = True

        if proceed:
            copy_to_clipboard("Can you explain the provided visualization?")

            F = open(answer_path, "w")
            F.close()

            open_text_editor(answer_path)
