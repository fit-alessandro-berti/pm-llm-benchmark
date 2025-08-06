#!/usr/bin/env python3
import json

def validate_model_info(json_file='model_info.json'):
    with open(json_file, 'r') as f:
        models = json.load(f)
    
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