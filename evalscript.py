import os
import traceback
import time
import datetime
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import forge_eval_prompt
from common import ANSWERING_MODEL_NAME, EVALUATING_MODEL_NAME, query_text_simple, query_image_simple, callback_write, \
    set_api_key, is_visual_model, get_base_evaluation_path, query_text_simple_with_rate_limit, \
    query_image_simple_with_rate_limit, RATE_LIMITER, configure_rate_limiter
import common


class Shared:
    MASS_EVAL = True
    USE_MULTITHREADING = True
    MAX_WORKERS = 5


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


def evaluate_single_question(q, answering_model_name, INCLUDE_EVALUATING_MNAME_IN_EVALUATION=False):
    """Process a single question evaluation."""
    try:
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
            # Check if already being processed
            if RATE_LIMITER.is_file_processing(evaluation_path):
                return False
            
            print(f"Evaluating: {answer_path}")
            
            try:
                answer = open(answer_path, "r").read()
            except:
                answer = open(answer_path, "r", encoding="utf-8").read()
            
            if answer is not None and answer:
                try:
                    if question_path.endswith(".txt"):
                        inquiry, base64_image = forge_eval_prompt.forge(question_path, answer, answering_model_name=answering_model_name)
                        
                        if Shared.USE_MULTITHREADING:
                            query_text_simple_with_rate_limit(None, evaluation_path, callback_write, 
                                                             question=inquiry, use_rate_limit=True)
                        else:
                            query_text_simple(None, evaluation_path, callback_write, question=inquiry)
                        
                        return True
                    elif is_visual_model(EVALUATING_MODEL_NAME):
                        inquiry, base64_image = forge_eval_prompt.forge(question_path, answer, answering_model_name=answering_model_name)
                        
                        if Shared.USE_MULTITHREADING:
                            query_image_simple_with_rate_limit(None, evaluation_path, callback_write, 
                                                              base64_image=base64_image, text=inquiry, 
                                                              use_rate_limit=True)
                        else:
                            query_image_simple(None, evaluation_path, callback_write, 
                                             base64_image=base64_image, text=inquiry)
                        
                        return True
                except:
                    traceback.print_exc()
                    return False
        return False
    except Exception as e:
        print(f"Error processing {q}: {e}")
        traceback.print_exc()
        return False


def perform_evaluation(answering_model_name=None):
    if answering_model_name is None:
        answering_model_name = ANSWERING_MODEL_NAME

    questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]
    INCLUDE_EVALUATING_MNAME_IN_EVALUATION = False

    something_ever_changed = False

    while True:
        missing = False
        
        if Shared.USE_MULTITHREADING:
            # Multi-threaded processing
            with ThreadPoolExecutor(max_workers=Shared.MAX_WORKERS) as executor:
                futures = []
                for q in questions:
                    # Submit task to thread pool
                    future = executor.submit(evaluate_single_question, q, answering_model_name, 
                                           INCLUDE_EVALUATING_MNAME_IN_EVALUATION)
                    futures.append(future)
                
                # Wait for all tasks to complete
                for future in as_completed(futures):
                    try:
                        result = future.result()
                        if result:
                            missing = True
                            something_ever_changed = True
                    except Exception as e:
                        print(f"Task failed: {e}")
                        traceback.print_exc()
        else:
            # Single-threaded processing (original behavior)
            for q in questions:
                result = evaluate_single_question(q, answering_model_name, INCLUDE_EVALUATING_MNAME_IN_EVALUATION)
                if result:
                    missing = True
                    something_ever_changed = True

        m_name = common.clean_model_name(answering_model_name)
        e_m_name = common.clean_model_name(EVALUATING_MODEL_NAME)
        base_evaluation_path = get_base_evaluation_path(e_m_name)
        
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
    
    # Configure rate limiter based on model/provider
    # You can adjust these values based on your API limits
    configure_rate_limiter(
        requests_per_minute=60,
        requests_per_hour=1000,
        tokens_per_minute=90000,
        tokens_per_hour=2000000,
        max_concurrent=5
    )

    print(EVALUATING_MODEL_NAME)
    print(f"Multi-threading: {Shared.USE_MULTITHREADING}, Max workers: {Shared.MAX_WORKERS}")

    perform_evaluation()
