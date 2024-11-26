import os
import traceback
import time
import sys
from common import query_text_simple, query_image_simple, callback_write, set_api_key, is_visual_model
import common

WAITING_TIME_RETRY = 60


def answer_question(model_name):
    common.ANSWERING_MODEL_NAME = model_name
    set_api_key("answer")

    print("=====", common.ANSWERING_MODEL_NAME)

    questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]

    for q in questions:
        question_path = os.path.join("questions", q)
        answer_path = os.path.join("answers", model_name.replace("/", "").replace(":", "") + "_" + q).replace(
            ".png", ".txt")

        if not os.path.exists(answer_path):
            while not os.path.exists(answer_path):
                try:
                    if question_path.endswith(".txt"):
                        print("Executing", question_path)
                        query_text_simple(question_path, answer_path, callback_write)
                        break
                    elif is_visual_model(model_name):
                        try:
                            print("Executing", question_path)
                            query_image_simple(question_path, answer_path, callback_write)
                        except:
                            traceback.print_exc()
                        break
                    else:
                        break
                except SystemExit as e:
                    sys.exit(0)
                except Exception as e:
                    if "context length" in str(e):
                        break

                    traceback.print_exc()

                    print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                    time.sleep(WAITING_TIME_RETRY)


if __name__ == "__main__":
    models_openai = ["o1-preview-2024-09-12", "o1-mini-2024-09-12", "gpt-4o-2024-11-20", "gpt-4o-2024-08-06",
                     "gpt-4o-2024-05-13", "gpt-4o-mini-2024-07-18", "gpt-4-turbo-2024-04-09", "gpt-4-0613",
                     "gpt-3.5-turbo"]
    models_google = ["gemini-1.5-pro-002", "gemini-1.5-flash-002", "gemini-1.5-flash-8b", "gemini-exp-1114",
                     "gemini-exp-1121"]
    models_claude = ["claude-3-5-sonnet-20241022", "claude-3-5-sonnet-20240620"]

    models = [common.ANSWERING_MODEL_NAME]
    #models = models_openai + models_google + models_claude + models_deepinfra

    for model in models:
        answer_question(model)
