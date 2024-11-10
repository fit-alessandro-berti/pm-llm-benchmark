import os
import traceback
import time
import datetime
from common import ANSWERING_MODEL_NAME, EVALUATING_MODEL_NAME, query_text_simple, query_image_simple, callback_write, \
    encode_image, set_api_key, is_visual_model


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

    while True:
        missing = False
        for q in questions:
            m_name = answering_model_name.replace("/", "").replace(":", "")
            e_m_name = EVALUATING_MODEL_NAME.replace("/", "").replace(":", "")

            question_path = os.path.join("questions", q)

            answer_path = m_name + "_" + q
            answer_path = os.path.join("answers", answer_path)
            answer_path = answer_path.replace(".png", ".txt")

            if INCLUDE_EVALUATING_MNAME_IN_EVALUATION:
                evaluation_path = m_name + "__" + e_m_name + "__" + q
            else:
                evaluation_path = m_name + "_" + q

            if "gpt-4o" in e_m_name:
                base_evaluation_path = "evaluation"
            else:
                base_evaluation_path = "evaluation-" + e_m_name

            if not os.path.exists(base_evaluation_path):
                os.mkdir(base_evaluation_path)

            evaluation_path = os.path.join(base_evaluation_path, evaluation_path)
            evaluation_path = evaluation_path.replace(".png", ".txt")

            if os.path.exists(answer_path) and not os.path.exists(evaluation_path):
                print("Evaluating:", answer_path)

                answer = open(answer_path, "r").read()

                if answer is not None and answer:
                    missing = True
                    try:
                        if question_path.endswith(".txt"):
                            question = open(question_path, "r", encoding="utf-8").read()

                            inquiry = ["Given the following question:\n\n"]
                            inquiry.append(question)
                            inquiry.append(
                                "\n\nHow would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? Please put the grade at the beginning of the response.\n\n")
                            inquiry.append(answer)
                            inquiry = ",".join(inquiry)

                            query_text_simple(None, evaluation_path, callback_write, question=inquiry)
                        elif is_visual_model(EVALUATING_MODEL_NAME):
                            base64_image = encode_image(question_path)
                            inquiry = [
                                "Given the attached image, how would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)?\n\n"]
                            inquiry.append(answer)
                            inquiry = "".join(inquiry)
                            query_image_simple(None, evaluation_path, callback_write, base64_image=base64_image,
                                               text=inquiry)
                    except:
                        traceback.print_exc()

        last_hour_answers = files_modified_last_hour("answers", m_name)
        last_hour_evaluations = files_modified_last_hour(base_evaluation_path, m_name)

        if Shared.MASS_EVAL:
            break_condition = (not missing) or (not last_hour_answers and not last_hour_evaluations)
        else:
            break_condition = (not missing) and (not last_hour_answers and not last_hour_evaluations)

        if break_condition:
            break

        time.sleep(15)


set_api_key("evaluation")
if __name__ == "__main__":
    Shared.MASS_EVAL = False

    perform_evaluation()
