#!/usr/bin/env python3
import json
import os
import glob
import ast
from difflib import SequenceMatcher

# Read leaderboard stats
with open('leaderboard_stats.md', 'r') as f:
    content = f.read()

# Parse the JSON from markdown file
leaderboard_data = ast.literal_eval(content)

# Get unique model names from output directory
output_files = glob.glob('output/*.txt')
real_model_names = set()
for file in output_files:
    model_name = os.path.basename(file).split('_')[0]
    real_model_names.add(model_name)

print(f"Found {len(real_model_names)} unique real model names in output directory")
print(f"Found {len(leaderboard_data)} models in leaderboard")

# Create mapping from beautified to real names using approximate string matching
beautified_to_real = {}

def normalize_string(s):
    """Normalize string for comparison"""
    return s.lower().replace('-', '').replace('_', '').replace(' ', '').replace('.', '')

def get_similarity(s1, s2):
    """Get similarity score between two strings"""
    return SequenceMatcher(None, normalize_string(s1), normalize_string(s2)).ratio()

for entry in leaderboard_data:
    beautified = entry['Model']
    
    best_match = None
    best_score = 0
    
    for real in real_model_names:
        score = get_similarity(beautified, real)
        
        if score > best_score:
            best_score = score
            best_match = real
    
    # Use a threshold to ensure reasonable matches
    if best_score > 0.6:
        beautified_to_real[beautified] = best_match
        print(f"Matched: {beautified} -> {best_match} (score: {best_score:.3f})")
    else:
        print(f"No match found for: {beautified} (best score: {best_score:.3f})")

print(f"\nMatched {len(beautified_to_real)} out of {len(leaderboard_data)} models")

# Create dictionaries for each output
model_scores = {}
model_is_reasoning = {}
model_is_os = {}

for entry in leaderboard_data:
    beautified = entry['Model']
    if beautified in beautified_to_real:
        real_name = beautified_to_real[beautified]
        
        # Extract score (remove ** markdown formatting)
        score = float(entry['Score'].replace('**', ''))
        model_scores[real_name] = score
        
        # Check if reasoning model (LRM column)
        is_reasoning = entry['LRM'] == ':white_check_mark:'
        model_is_reasoning[real_name] = is_reasoning
        
        # Check if open source (OS column)
        is_os = entry['OS'] == ':white_check_mark:'
        model_is_os[real_name] = is_os

# Handle model_date.json (publication dates)
model_date = {}
if os.path.exists('model_date.json'):
    with open('model_date.json', 'r') as f:
        model_date = json.load(f)
    print(f"\nLoaded existing model_date.json with {len(model_date)} entries")

# Add new models with empty dates
for real_name in model_scores.keys():
    if real_name not in model_date:
        model_date[real_name] = ""

# Handle model_info.json (model information like parameters)
model_info = {}
if os.path.exists('model_info.json'):
    with open('model_info.json', 'r') as f:
        model_info = json.load(f)
    print(f"Loaded existing model_info.json with {len(model_info)} entries")

# Add new models with empty lists
for real_name in model_scores.keys():
    if real_name not in model_info:
        model_info[real_name] = []

# Write JSON files
with open('model_scores.json', 'w') as f:
    json.dump(model_scores, f, indent=2)
    print(f"\nCreated model_scores.json with {len(model_scores)} entries")

with open('model_is_reasoning.json', 'w') as f:
    json.dump(model_is_reasoning, f, indent=2)
    print(f"Created model_is_reasoning.json with {len(model_is_reasoning)} entries")

with open('model_is_os.json', 'w') as f:
    json.dump(model_is_os, f, indent=2)
    print(f"Created model_is_os.json with {len(model_is_os)} entries")

with open('model_date.json', 'w') as f:
    json.dump(model_date, f, indent=2, sort_keys=True)
    print(f"Created/Updated model_date.json with {len(model_date)} entries")

with open('model_info.json', 'w') as f:
    json.dump(model_info, f, indent=2, sort_keys=True)
    print(f"Created/Updated model_info.json with {len(model_info)} entries")

# Print unmatched models for debugging
unmatched = [entry['Model'] for entry in leaderboard_data if entry['Model'] not in beautified_to_real]
if unmatched:
    print(f"\nUnmatched models ({len(unmatched)}):")
    for model in unmatched:
        print(f"  - {model}")

# Print which models need manual updates
new_models_date = [model for model in model_date.keys() if model_date[model] == ""]
new_models_info = [model for model in model_info.keys() if model_info[model] == []]

if new_models_date:
    print(f"\nModels needing publication dates ({len(new_models_date)} models):")
    for model in sorted(new_models_date):
        print(f"  - {model}")

if new_models_info:
    print(f"\nModels needing info ({len(new_models_info)} models):")
    for model in sorted(new_models_info):
        print(f"  - {model}")