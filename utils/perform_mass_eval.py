import os
import sys
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
import evalscript
from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path, get_ordered_references_llms, \
    RATE_LIMITER, configure_rate_limiter
from utils import overall_table


# Global lock for preventing duplicate model processing
MODEL_PROCESSING_LOCK = threading.Lock()
PROCESSING_MODELS = set()


def evaluate_model_threaded(m):
    """Evaluate a single model in a thread."""
    try:
        # Check and mark model as being processed
        with MODEL_PROCESSING_LOCK:
            if m in PROCESSING_MODELS:
                print(f"Model {m} already being processed, skipping")
                return False
            PROCESSING_MODELS.add(m)
        
        try:
            if "__init" not in m.lower():
                print(f"Processing model: {m}")
                evalscript.perform_evaluation(m)
                overall_table.write_evaluation(".", extra=True)
                return True
            return False
        finally:
            # Remove model from processing set
            with MODEL_PROCESSING_LOCK:
                PROCESSING_MODELS.discard(m)
    except Exception as e:
        print(f"Error processing model {m}: {e}")
        with MODEL_PROCESSING_LOCK:
            PROCESSING_MODELS.discard(m)
        return False


def perform_mass_eval(use_multithreading=True, max_workers=3):
    answers = os.listdir("answers")
    answers_models = Counter([x.split("_cat")[0] for x in answers])
    # answers_models = {x: y for x, y in answers_models.items() if y >= 44}

    e_m_name = clean_model_name(EVALUATING_MODEL_NAME)
    base_evaluation_path = get_base_evaluation_path(e_m_name)
    evaluations = os.listdir(base_evaluation_path)
    evaluations_models = Counter([x.split("_cat")[0] for x in evaluations])

    answer_models_keys = list(answers_models.keys())

    ordered, referenced = get_ordered_references_llms(".")
    ordered = ordered + referenced
    ordered = [clean_model_name(x) for x in ordered]
    answer_models_keys.sort(key=lambda x: (ordered.index(x) if x in ordered else sys.maxsize, x))

    answer_models_keys = [x for x in answer_models_keys if evaluations_models[x] != answers_models[x]]
    answer_models_keys.sort(key=lambda x: (0 if answers_models[x] - evaluations_models[x] < 10 else 1,
                                           0 if x.lower().startswith("gpt") else 1 if "gpt" in x.lower() else 2 if x.lower().startswith("o") else 3 if x.lower().startswith("claude") else 4,
                                           answers_models[x] - evaluations_models[x],
                                           x.lower()))
    print(answer_models_keys)

    overall_table.write_evaluation(".", extra=True)

    changed = False
    
    if use_multithreading:
        # Process models in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for m in answer_models_keys:
                # Check if model is already being processed before submitting
                with MODEL_PROCESSING_LOCK:
                    if m not in PROCESSING_MODELS:
                        future = executor.submit(evaluate_model_threaded, m)
                        futures.append((m, future))
                    else:
                        print(f"Model {m} already in processing queue, skipping")
            
            # Wait for all evaluations to complete
            for m, future in futures:
                try:
                    result = future.result(timeout=1800)  # 30 minute timeout per model
                    if result:
                        changed = True
                except Exception as e:
                    print(f"Failed to evaluate model {m}: {e}")
    else:
        # Single-threaded processing (original behavior)
        for m in answer_models_keys:
            if "__init" not in m.lower():
                print(m)
                evalscript.perform_evaluation(m)
                overall_table.write_evaluation(".", extra=True)
                changed = True

    if changed:
        overall_table.write_evaluation(".", extra=True)

    return changed


if __name__ == "__main__":
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)
    
    # Configure rate limiter
    configure_rate_limiter(
        requests_per_minute=60,
        requests_per_hour=1000,
        tokens_per_minute=90000,
        tokens_per_hour=2000000,
        max_concurrent=10
    )
    
    # Enable multi-threading in evalscript
    evalscript.Shared.USE_MULTITHREADING = True
    evalscript.Shared.MAX_WORKERS = 5

    iterations = sys.maxsize
    # iterations = 1
    
    use_multithreading = True  # Set to False to use original single-threaded behavior
    max_model_workers = 3  # Number of models to process in parallel

    for i in range(iterations):
        print(f"\n=== Iteration {i+1} ===")
        print(f"Multi-threading enabled: {use_multithreading}")
        print(f"Rate limiter stats: {RATE_LIMITER.get_stats()}")
        
        changed = perform_mass_eval(use_multithreading=use_multithreading, 
                                   max_workers=max_model_workers)
        
        if not changed:
            print("No changes detected, waiting before next iteration...")
            time.sleep(60)  # Wait 1 minute before checking again
