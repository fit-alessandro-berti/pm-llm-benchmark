import os
import traceback
import time
import sys
from common import query_text_simple, query_image_simple, callback_write, set_api_key, is_visual_model, MODELS_DICT, Shared
import common

WAITING_TIME_RETRY = 15


def answer_question(model_name, api_url=None, api_key=None):
    if api_url is not None:
        common.Shared.API_URL = api_url

    if api_key is not None:
        common.Shared.API_KEY = api_key
        common.Shared.MODEL_NAME = model_name
    else:
        set_api_key("answer")

    common.ANSWERING_MODEL_NAME = model_name

    print("=====", common.ANSWERING_MODEL_NAME)

    questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]

    for q in questions:
        question_path = os.path.join("questions", q)
        answer_path = os.path.join("answers", common.clean_model_name(model_name) + "_" + q).replace(
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
    if False:
        from utils import overall_table
        e_m_name = common.clean_model_name(common.EVALUATING_MODEL_NAME)
        common.insert_api_keys()
        try:
            output, all_jsons, ordered_llms = overall_table.execute("evaluation-gemini-2.5-pro", None, include_closed_source=True, require_vision=False,
                leaderboard_title="Overall Leaderboard")
        except:
            traceback.print_exc()
            ordered_llms = []
        referenced_llms = set()
        for provider in MODELS_DICT:
            info = MODELS_DICT[provider]
            referenced_llms = referenced_llms.union(info["models"])
        referenced_llms = [common.clean_model_name(x) for x in referenced_llms if common.clean_model_name(x) not in ordered_llms]
        ordered_llms = ordered_llms + referenced_llms
        for llm in ordered_llms:
            found = False
            for provider in MODELS_DICT:
                info = MODELS_DICT[provider]
                cleaned_models = {common.clean_model_name(x): x for x in info["models"]}
                if llm in cleaned_models:
                    if provider == "manual":
                        ref = MODELS_DICT[provider]["models"][cleaned_models[llm]]
                        if "provider" in ref and ref["provider"] in MODELS_DICT:
                            api_url = MODELS_DICT[ref["provider"]]["api_url"]
                            api_key = MODELS_DICT[ref["provider"]]["api_key"]
                            base_model = ref["base_model"]
                    else:
                        api_url = info["api_url"]
                        api_key = info["api_key"]
                    answer_question(cleaned_models[llm], api_url=api_url, api_key=api_key)
                    Shared.SYSTEM_PROMPT = None
                    Shared.ANTHROPIC_THINKING_TOKENS = None
                    Shared.PAYLOAD_REASONING_EFFORT = None
                    found = True
                    break
            if not found:
                print("problem with "+str(llm)+" not found!")
    else:
        models = [common.ANSWERING_MODEL_NAME]
        for model in models:
            answer_question(model)
