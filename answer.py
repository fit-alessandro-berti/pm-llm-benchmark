import os
import traceback
import time
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from common import query_text_simple, query_image_simple, callback_write, set_api_key, is_visual_model, MODELS_DICT, \
    query_text_simple_with_rate_limit, query_image_simple_with_rate_limit, RATE_LIMITER, configure_rate_limiter
import common

WAITING_TIME_RETRY = 15
USE_MULTITHREADING = True
MAX_WORKERS = 1
TIME_BETWEEN_ANSWERS = 0


def process_single_question(q, model_name, alias_model_name, use_rate_limit=False):
    """Process a single question."""
    question_path = os.path.join("questions", q)
    answer_path = os.path.join("answers", common.clean_model_name(alias_model_name) + "_" + q).replace(
        ".png", ".txt")
    
    if not os.path.exists(answer_path):
        # Check if file is already being processed
        if use_rate_limit and RATE_LIMITER.is_file_processing(answer_path):
            print(f"File {answer_path} already being processed, skipping")
            return False
        
        try:
            if question_path.endswith(".txt"):
                print("Executing", question_path)
                if use_rate_limit:
                    query_text_simple_with_rate_limit(question_path, answer_path, callback_write, 
                                                     use_rate_limit=True)
                    time.sleep(TIME_BETWEEN_ANSWERS)
                else:
                    query_text_simple(question_path, answer_path, callback_write)
                    time.sleep(TIME_BETWEEN_ANSWERS)
                return True
            elif is_visual_model(model_name):
                try:
                    print("Executing", question_path)
                    if use_rate_limit:
                        query_image_simple_with_rate_limit(question_path, answer_path, callback_write,
                                                          use_rate_limit=True)
                    else:
                        query_image_simple(question_path, answer_path, callback_write)
                except:
                    traceback.print_exc()
                return True
        except SystemExit as e:
            sys.exit(0)
        except Exception as e:
            if "context length" in str(e):
                return False
            
            traceback.print_exc()
            
            if not use_rate_limit:
                # If not using rate limit, sleep and retry (original behavior)
                print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))
                time.sleep(WAITING_TIME_RETRY)
                return None  # Indicates retry needed
            else:
                # With rate limiting, the retry is handled by the rate limiter
                return False
    return False


def answer_question(model_name, api_url=None, api_key=None, alias_model_name=None, use_multithreading=None):
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

    if use_multithreading is None:
        use_multithreading = USE_MULTITHREADING
    
    questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]
    
    if use_multithreading:
        # Multi-threaded processing
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = []
            for q in questions:
                answer_path = os.path.join("answers", common.clean_model_name(alias_model_name) + "_" + q).replace(
                    ".png", ".txt")
                
                if not os.path.exists(answer_path):
                    # Submit task to thread pool
                    future = executor.submit(process_single_question, q, model_name, alias_model_name, 
                                           use_rate_limit=True)
                    futures.append((q, future))
            
            # Wait for all tasks to complete
            for q, future in futures:
                try:
                    result = future.result(timeout=1200)  # 20 minute timeout per question
                    if result:
                        print(f"Successfully processed {q}")
                except Exception as e:
                    print(f"Failed to process {q}: {e}")
                    traceback.print_exc()
    else:
        # Single-threaded processing (original behavior)
        for q in questions:
            answer_path = os.path.join("answers", common.clean_model_name(alias_model_name) + "_" + q).replace(
                ".png", ".txt")

            if not os.path.exists(answer_path):
                while not os.path.exists(answer_path):
                    result = process_single_question(q, model_name, alias_model_name, use_rate_limit=False)
                    if result is None:
                        # Retry needed
                        continue
                    else:
                        # Success or permanent failure
                        break


if __name__ == "__main__":
    # Configure rate limiter
    configure_rate_limiter(
        requests_per_minute=50,
        requests_per_hour=1000,
        tokens_per_minute=90000,
        tokens_per_hour=2000000,
        max_concurrent=50
    )
    
    if True:
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
                            common.Shared.MAX_REQUESTED_TOKENS = ref["max_tokens"] if "max_tokens" in ref else 32000
                            common.Shared.ADDED_TO_PROMPT = ref["added_to_prompt"] if "added_to_prompt" in ref else None
                            common.Shared.TOOLS_PAYLOAD = ref["tools"] if "tools" in ref else None
                            common.Shared.ADDED_TO_PAYLOAD = ref["added_to_payload"] if "added_to_payload" in ref else None

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
                            answer_question(model_name, api_url=api_url, api_key=api_key, 
                                         alias_model_name=alias_model_name, use_multithreading=USE_MULTITHREADING)
                        else:
                            print(model_name, provider, "excluded")

                    common.Shared.SYSTEM_PROMPT = None
                    common.Shared.ANTHROPIC_THINKING_TOKENS = None
                    common.Shared.PAYLOAD_REASONING_EFFORT = None
                    common.Shared.CUSTOM_TEMPERATURE = None
                    common.Shared.MAX_REQUESTED_TOKENS = 32000
                    common.Shared.ADDED_TO_PROMPT = None
                    common.Shared.TOOLS_PAYLOAD = None
                    common.Shared.ADDED_TO_PAYLOAD = None

                    found = True
                    break
            if not found:
                print("problem with "+str(llm)+" not found!")
    else:
        models = [common.ANSWERING_MODEL_NAME]
        for model in models:
            answer_question(model, use_multithreading=USE_MULTITHREADING)
