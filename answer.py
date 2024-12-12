import os
import traceback
import time
import sys
from common import query_text_simple, query_image_simple, callback_write, set_api_key, is_visual_model, check_missing_models, check_all_models, MODELS_DICT
import common

WAITING_TIME_RETRY = 60


def answer_question(model_name, api_url=None, api_key=None):
    if api_url is not None:
        common.API_URL = api_url
    if api_key is not None:
        common.Shared.API_KEY = api_key

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
    if True:
        check_missing_models()
        check_all_models()
        for provider in MODELS_DICT:
            info = MODELS_DICT[provider]
            for model in info["models"]:
                answer_question(model, api_url=info["api_url"], api_key=info["api_key"])
    else:
        models = [common.ANSWERING_MODEL_NAME]
        for model in models:
            answer_question(model)
