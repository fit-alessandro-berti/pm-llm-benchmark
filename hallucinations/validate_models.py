#!/usr/bin/env python3
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from file_utils import read_file_with_fallback

def resolve_script_path(filepath):
    path = Path(filepath)
    if path.is_absolute():
        return path
    return SCRIPT_DIR / path

def validate_model_info(json_file='model_info.json'):
    models = json.loads(read_file_with_fallback(resolve_script_path(json_file)))
    
    models_without_info = []
    models_with_info = []
    
    for model_name, sizes in models.items():
        if not sizes:
            models_without_info.append(model_name)
        else:
            total_size = sizes[0] if isinstance(sizes, list) else sizes
            models_with_info.append((model_name, total_size))
    
    print("Models without size information:")
    for model in models_without_info:
        print(f"  {model}")
    
    print("\nModels with size information (sorted by size, smallest to largest):")
    models_with_info.sort(key=lambda x: x[1])
    for model, size in models_with_info:
        print(f"  {model}: {size}B")

if __name__ == "__main__":
    validate_model_info()
