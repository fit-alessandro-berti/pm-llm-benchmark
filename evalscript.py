import os
import traceback
import time
import datetime
from utils import forge_eval_prompt
from common import ANSWERING_MODEL_NAME, EVALUATING_MODEL_NAME, query_text_simple, query_image_simple, callback_write, \
    set_api_key, is_visual_model, get_base_evaluation_path
import common


class Shared:
    MASS_EVAL = True


def files_modified_last_hour(folder_path, m_name):
    # Get the current time
    now = datetime.datetime.now()
    # Calculate the time one hour ago
    one_hour_ago = now - datetime.timedelta(hours=1)

    # List to store files modified in the last hour
    modified_files = []

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.startswith(m_name):
            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                # Get the last modified time of the file
                file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                # Check if the file was modified within the last hour
                if file_mod_time > one_hour_ago:
                    modified_files.append(filename)

    return modified_files


def perform_evaluation(answering_model_name=None):
    if answering_model_name is None:
        answering_model_name = ANSWERING_MODEL_NAME

    questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]
    INCLUDE_EVALUATING_MNAME_IN_EVALUATION = False

    something_ever_changed = False

    while True:
        missing = False
        for q in questions:
            m_name = common.clean_model_name(answering_model_name)
            e_m_name = common.clean_model_name(EVALUATING_MODEL_NAME)

            question_path = os.path.join("questions", q)

            answer_path = m_name + "_" + q
            answer_path = os.path.join("answers", answer_path)
            answer_path = answer_path.replace(".png", ".txt")

            if INCLUDE_EVALUATING_MNAME_IN_EVALUATION:
                evaluation_path = m_name + "__" + e_m_name + "__" + q
            else:
                evaluation_path = m_name + "_" + q

            base_evaluation_path = get_base_evaluation_path(e_m_name)

            if not os.path.exists(base_evaluation_path):
                os.mkdir(base_evaluation_path)

            evaluation_path = os.path.join(base_evaluation_path, evaluation_path)
            evaluation_path = evaluation_path.replace(".png", ".txt")

            if os.path.exists(answer_path) and not os.path.exists(evaluation_path):
                print("Evaluating:", answer_path)

                try:
                    answer = open(answer_path, "r").read()
                except:
                    answer = open(answer_path, "r", encoding="utf-8").read()

                if answer is not None and answer:
                    try:
                        if question_path.endswith(".txt"):
                            #answer = answer.split("</think>")[-1].strip()

                            #print(answer)

                            inquiry, base64_image = forge_eval_prompt.forge(question_path, answer, answering_model_name=answering_model_name)

                            query_text_simple(None, evaluation_path, callback_write, question=inquiry)

                            missing = True
                            something_ever_changed = True
                        elif is_visual_model(EVALUATING_MODEL_NAME):
                            inquiry, base64_image = forge_eval_prompt.forge(question_path, answer, answering_model_name=answering_model_name)

                            query_image_simple(None, evaluation_path, callback_write, base64_image=base64_image,
                                               text=inquiry)

                            missing = True
                            something_ever_changed = True
                    except:
                        traceback.print_exc()

        last_hour_answers = files_modified_last_hour("answers", m_name)
        last_hour_evaluations = files_modified_last_hour(base_evaluation_path, m_name)

        if not something_ever_changed:
            break

        if Shared.MASS_EVAL:
            break_condition = (not missing)
        else:
            break_condition = (not missing) and (not last_hour_answers and not last_hour_evaluations)

        if break_condition:
            break

        time.sleep(15)


set_api_key("evaluation")
if __name__ == "__main__":
    Shared.MASS_EVAL = False

    print(EVALUATING_MODEL_NAME)

    perform_evaluation()
