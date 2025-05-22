import os
import traceback
import time
import sys
from common import query_text_simple, query_image_simple, callback_write, set_api_key, is_visual_model, MODELS_DICT
import common

WAITING_TIME_RETRY = 15


def answer_question(model_name, api_url=None, api_key=None, alias_model_name=None):
    if api_url is not None:
        common.Shared.API_URL = api_url

    if alias_model_name is None:
        alias_model_name = model_name

    if api_key is not None:
        common.Shared.API_KEY = api_key
        common.Shared.MODEL_NAME = model_name
        common.Shared.ALIAS_MODEL_NAME = alias_model_name
    else:
        set_api_key("answer")

    common.ANSWERING_MODEL_NAME = model_name

    print("=====", common.Shared.ALIAS_MODEL_NAME)

    questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]

    for q in questions:
        question_path = os.path.join("questions", q)
        answer_path = os.path.join("answers", common.clean_model_name(alias_model_name) + "_" + q).replace(
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
        e_m_name = common.clean_model_name(common.EVALUATING_MODEL_NAME)
        common.insert_api_keys()

        ordered_llms, referenced_llms = common.get_ordered_references_llms(".")
        ordered_llms = ordered_llms + referenced_llms

        #ordered_llms = ordered_llms[::-1]

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
                            model_name = ref["base_model"]
                            alias_model_name = cleaned_models[llm]

                            common.Shared.SYSTEM_PROMPT = ref["system_prompt"] if "system_prompt" in ref else None
                            common.Shared.ANTHROPIC_THINKING_TOKENS = ref["thinking_tokens"] if "thinking_tokens" in ref else None
                            common.Shared.PAYLOAD_REASONING_EFFORT = ref["reasoning_effort"] if "reasoning_effort" in ref else None
                            common.Shared.CUSTOM_TEMPERATURE = ref["temperature"] if "temperature" in ref else None
                            common.Shared.MAX_REQUESTED_TOKENS = ref["max_tokens"] if "max_tokens" in ref else None
                            common.Shared.ADDED_TO_PROMPT = ref["added_to_prompt"] if "added_to_prompt" in ref else None
                            this_provider = ref["provider"]
                        else:
                            api_key = None
                    else:
                        api_url = info["api_url"]
                        api_key = info["api_key"]
                        model_name = cleaned_models[llm]
                        alias_model_name = cleaned_models[llm]
                        this_provider = provider

                    """
                    print(model_name, alias_model_name, this_provider, common.Shared.ANTHROPIC_THINKING_TOKENS, \
                          common.Shared.PAYLOAD_REASONING_EFFORT, common.Shared.CUSTOM_TEMPERATURE, \
                          common.Shared.SYSTEM_PROMPT)
                    """

                    if api_key is not None:
                        excluded_providers = {}

                        if provider not in excluded_providers and this_provider not in excluded_providers:
                            answer_question(model_name, api_url=api_url, api_key=api_key, alias_model_name=alias_model_name)
                        else:
                            print(model_name, provider, "excluded")

                    common.Shared.SYSTEM_PROMPT = None
                    common.Shared.ANTHROPIC_THINKING_TOKENS = None
                    common.Shared.PAYLOAD_REASONING_EFFORT = None
                    common.Shared.CUSTOM_TEMPERATURE = None
                    common.Shared.MAX_REQUESTED_TOKENS = 32000
                    common.Shared.ADDED_TO_PROMPT = None

                    found = True
                    break
            if not found:
                print("problem with "+str(llm)+" not found!")
    else:
        models = [common.ANSWERING_MODEL_NAME]
        for model in models:
            answer_question(model)
