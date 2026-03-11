import os
import sys
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from common import EVALUATING_MODEL_NAME, clean_model_name, get_base_evaluation_path, \
    get_ordered_references_llms_with_scores, RATE_LIMITER, configure_rate_limiter


# Global lock for preventing duplicate model processing
MODEL_PROCESSING_LOCK = threading.Lock()
PROCESSING_MODELS = set()
EVALSCRIPT_MODULE = None


def get_evalscript_module():
    global EVALSCRIPT_MODULE
    if EVALSCRIPT_MODULE is None:
        import evalscript
        EVALSCRIPT_MODULE = evalscript
    return EVALSCRIPT_MODULE


def write_leaderboard_if_enabled(create_leaderboard):
    if create_leaderboard:
        from utils import overall_table
        overall_table.write_evaluation(".", extra=True)


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
                get_evalscript_module().perform_evaluation(m)
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


def get_models_to_evaluate_with_scores(base_path=".", min_leaderboard_score=None, only_pending=True):
    answers = [
        filename
        for filename in os.listdir(os.path.join(base_path, "answers"))
        if "__init__" not in filename.lower()
    ]
    answers_models = Counter([x.split("_cat")[0] for x in answers])
    # answers_models = {x: y for x, y in answers_models.items() if y >= 44}

    e_m_name = clean_model_name(EVALUATING_MODEL_NAME)
    base_evaluation_path = os.path.join(base_path, get_base_evaluation_path(e_m_name))
    evaluations = [
        filename
        for filename in os.listdir(base_evaluation_path)
        if "__init__" not in filename.lower()
    ]
    evaluations_models = Counter([x.split("_cat")[0] for x in evaluations])

    answer_models_keys = list(answers_models.keys())

    ordered_with_scores, referenced_with_scores = get_ordered_references_llms_with_scores(base_path)
    all_models_with_scores = [
        (clean_model_name(model_name), score)
        for model_name, score in ordered_with_scores + referenced_with_scores
    ]
    order_index = {model: index for index, (model, _) in enumerate(all_models_with_scores)}
    leaderboard_scores = {model: score for model, score in all_models_with_scores}

    if only_pending:
        answer_models_keys = [x for x in answer_models_keys if evaluations_models[x] != answers_models[x]]

    answer_models_with_scores = [
        (model_name, leaderboard_scores.get(model_name, 0.0))
        for model_name in answer_models_keys
    ]

    if min_leaderboard_score is not None:
        answer_models_with_scores = [
            (model_name, score)
            for model_name, score in answer_models_with_scores
            if score >= min_leaderboard_score
        ]

    answer_models_with_scores.sort(
        key=lambda item: (
            order_index.get(item[0], sys.maxsize),
            -item[1],
            item[0].lower()
        )
    )

    answer_models_with_scores.sort(
        key=lambda item: (
            0 if answers_models[item[0]] - evaluations_models[item[0]] < 10 else 1,
            0 if item[0].lower().startswith("gpt") else 1 if "gpt" in item[0].lower() else 2 if item[0].lower().startswith("o") else 3 if item[0].lower().startswith("claude") else 4,
            -item[1],
            answers_models[item[0]] - evaluations_models[item[0]],
            item[0].lower()
        )
    )

    return answer_models_with_scores


def perform_mass_eval(use_multithreading=True, max_workers=3, create_leaderboard=True, min_leaderboard_score=None):
    models_to_evaluate = get_models_to_evaluate_with_scores(
        base_path=".",
        min_leaderboard_score=min_leaderboard_score,
        only_pending=True
    )
    answer_models_keys = [model_name for model_name, _ in models_to_evaluate]
    print(models_to_evaluate)

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
            print(m)
            get_evalscript_module().perform_evaluation(m)
            changed = True

    if changed:
        write_leaderboard_if_enabled(create_leaderboard)

    return changed


if __name__ == "__main__":
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)
    
    # Configure rate limiter
    configure_rate_limiter(
        requests_per_minute=100,
        requests_per_hour=20000,
        tokens_per_minute=900000,
        tokens_per_hour=2000000,
        max_concurrent=50
    )
    
    evalscript = get_evalscript_module()
    # Enable multi-threading in evalscript
    evalscript.Shared.USE_MULTITHREADING = True
    evalscript.Shared.MAX_WORKERS = 50

    iterations = sys.maxsize
    # iterations = 1

    use_multithreading = True  # Set to False to use original single-threaded behavior
    max_model_workers = 15  # Number of models to process in parallel
    create_leaderboard = True  # Set to False to skip leaderboard generation

    for i in range(iterations):
        print(f"\n=== Iteration {i+1} ===")
        print(f"Multi-threading enabled: {use_multithreading}")
        print(f"Rate limiter stats: {RATE_LIMITER.get_stats()}")
        print(f"Leaderboard creation enabled: {create_leaderboard}")
        
        changed = perform_mass_eval(use_multithreading=use_multithreading, 
                                   max_workers=max_model_workers,
                                   create_leaderboard=create_leaderboard, min_leaderboard_score=38.95)
        
        if not changed:
            print("No changes detected, waiting before next iteration...")
            time.sleep(60)  # Wait 1 minute before checking again
