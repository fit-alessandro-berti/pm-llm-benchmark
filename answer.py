import os
import traceback
import time
import sys
from concurrent.futures import ThreadPoolExecutor
from common import query_text_simple, query_image_simple, callback_write, set_api_key, is_visual_model, MODELS_DICT, \
    query_text_simple_with_rate_limit, query_image_simple_with_rate_limit, RATE_LIMITER, configure_rate_limiter
import common

WAITING_TIME_RETRY = 15
USE_MULTITHREADING = True
MAX_WORKERS = 100
TIME_BETWEEN_ANSWERS = 0
MAX_VISUAL_FAILURES = 5
VISUAL_FAILURE_ANSWER = "."


def get_answer_path(q, alias_model_name):
    return os.path.join("answers", common.clean_model_name(alias_model_name) + "_" + q).replace(
        ".png", ".txt")


def is_retry_limited_visual_question(q, model_name):
    return q.endswith(".png") and is_visual_model(model_name)


def write_visual_failure_answer(answer_path):
    callback_write(VISUAL_FAILURE_ANSWER, answer_path)


def should_stop_visual_retries(q, model_name, failed_attempts):
    return is_retry_limited_visual_question(q, model_name) and failed_attempts >= MAX_VISUAL_FAILURES


def process_single_question(q, model_name, alias_model_name, use_rate_limit=False, failed_attempts=0):
    """Process a single question."""
    question_path = os.path.join("questions", q)
    answer_path = get_answer_path(q, alias_model_name)
    
    if not common.is_completed_output(answer_path):
        # Check if file is already being processed
        if use_rate_limit and RATE_LIMITER.is_file_processing(answer_path):
            print(f"File {answer_path} already being processed, skipping")
            return None
        
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
            elif is_visual_model(model_name):
                print("Executing", question_path)
                if use_rate_limit:
                    query_image_simple_with_rate_limit(question_path, answer_path, callback_write,
                                                      use_rate_limit=True)
                else:
                    query_image_simple(question_path, answer_path, callback_write)
            else:
                return False

            if common.is_completed_output(answer_path):
                return True

            failed_attempts += 1
            if should_stop_visual_retries(q, model_name, failed_attempts):
                print(f"Visual question {question_path} failed {failed_attempts} time(s); writing fallback answer")
                write_visual_failure_answer(answer_path)
                return True

            print(f"No completed answer was written for {question_path}; retrying")
            time.sleep(WAITING_TIME_RETRY)
            return None
        except SystemExit as e:
            sys.exit(0)
        except Exception as e:
            if "context length" in str(e):
                return False
            
            traceback.print_exc()

            failed_attempts += 1
            if should_stop_visual_retries(q, model_name, failed_attempts):
                print(f"Visual question {question_path} failed {failed_attempts} time(s); writing fallback answer")
                write_visual_failure_answer(answer_path)
                return True

            print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))
            time.sleep(WAITING_TIME_RETRY)
            return None  # Indicates retry needed
    return False


def mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
    failed_attempts = failure_counts.get(q, 0) + 1
    failure_counts[q] = failed_attempts

    if should_stop_visual_retries(q, model_name, failed_attempts):
        question_path = os.path.join("questions", q)
        answer_path = get_answer_path(q, alias_model_name)
        print(f"Visual question {question_path} failed {failed_attempts} time(s); writing fallback answer")
        write_visual_failure_answer(answer_path)
        return False

    return True


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
    failure_counts = {}
    
    if use_multithreading:
        # Multi-threaded processing
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = []
            for q in questions:
                answer_path = get_answer_path(q, alias_model_name)
                
                if not common.is_completed_output(answer_path):
                    # Submit task to thread pool
                    future = executor.submit(process_single_question, q, model_name, alias_model_name, 
                                             use_rate_limit=True, failed_attempts=failure_counts.get(q, 0))
                    futures.append((q, future))
            
            # Wait for all tasks to complete
            retry_questions = []
            for q, future in futures:
                try:
                    result = future.result(timeout=1200)  # 20 minute timeout per question
                    if result:
                        print(f"Successfully processed {q}")
                    elif result is None:
                        if mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
                            retry_questions.append(q)
                except Exception as e:
                    print(f"Failed to process {q}: {e}")
                    traceback.print_exc()
                    if mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
                        retry_questions.append(q)

            while retry_questions:
                retry_questions = [
                    q for q in retry_questions
                    if not common.is_completed_output(
                        get_answer_path(q, alias_model_name)
                    )
                ]
                if not retry_questions:
                    break

                print(f"Retrying {len(retry_questions)} question(s) after transient failures")
                time.sleep(WAITING_TIME_RETRY)

                with ThreadPoolExecutor(max_workers=MAX_WORKERS) as retry_executor:
                    retry_futures = [
                        (q, retry_executor.submit(process_single_question, q, model_name, alias_model_name,
                                                  use_rate_limit=True, failed_attempts=failure_counts.get(q, 0)))
                        for q in retry_questions
                    ]

                    next_retry_questions = []
                    for q, future in retry_futures:
                        try:
                            result = future.result(timeout=1200)
                            if result:
                                print(f"Successfully processed {q}")
                            elif result is None:
                                if mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
                                    next_retry_questions.append(q)
                        except Exception as e:
                            print(f"Failed to process {q}: {e}")
                            traceback.print_exc()
                            if mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
                                next_retry_questions.append(q)

                    retry_questions = next_retry_questions
    else:
        # Single-threaded processing (original behavior)
        for q in questions:
            answer_path = get_answer_path(q, alias_model_name)

            if not common.is_completed_output(answer_path):
                while not common.is_completed_output(answer_path):
                    result = process_single_question(q, model_name, alias_model_name, use_rate_limit=False,
                                                     failed_attempts=failure_counts.get(q, 0))
                    if result is None:
                        # Retry needed
                        if mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
                            continue
                        break
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
