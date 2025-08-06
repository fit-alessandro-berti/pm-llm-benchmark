#!/usr/bin/env python3
import json
from datetime import datetime
import sys

# Load model_date.json
try:
    with open('model_date.json', 'r') as f:
        model_dates = json.load(f)
except FileNotFoundError:
    print("Error: model_date.json not found. Please run create_model_json_files.py first.")
    sys.exit(1)

# Get current date and set boundaries
current_date = datetime.now()
min_date = datetime(2024, 1, 1)

# Validate and parse dates
parsed_dates = {}
invalid_entries = []
empty_entries = []
out_of_range_entries = []

for model, date_str in model_dates.items():
    # Check for empty dates
    if not date_str or date_str.strip() == "":
        empty_entries.append(model)
        continue
    
    # Try to parse the date
    # Try multiple date formats
    date_formats = [
        "%Y-%m-%d",      # 2024-03-15
        "%Y/%m/%d",      # 2024/03/15
        "%d-%m-%Y",      # 15-03-2024
        "%d/%m/%Y",      # 15/03/2024
        "%B %d, %Y",     # March 15, 2024
        "%b %d, %Y",     # Mar 15, 2024
        "%Y-%m",         # 2024-03
        "%Y",            # 2024
    ]
    
    parsed = False
    for fmt in date_formats:
        try:
            parsed_date = datetime.strptime(date_str.strip(), fmt)
            
            # Check if date is in valid range
            if parsed_date < min_date:
                out_of_range_entries.append((model, date_str, "before 2024"))
            elif parsed_date > current_date:
                out_of_range_entries.append((model, date_str, "future date"))
            else:
                parsed_dates[model] = (parsed_date, date_str)
            
            parsed = True
            break
        except ValueError:
            continue
    
    if not parsed:
        invalid_entries.append((model, date_str))

# Report any issues
if empty_entries or invalid_entries or out_of_range_entries:
    print("ERROR: Found invalid, empty, or out-of-range date entries!\n")
    
    if empty_entries:
        print(f"Empty dates ({len(empty_entries)} models):")
        for model in sorted(empty_entries):
            print(f"  - {model}")
        print()
    
    if invalid_entries:
        print(f"Invalid dates ({len(invalid_entries)} models):")
        for model, date_str in sorted(invalid_entries):
            print(f"  - {model}: '{date_str}'")
        print()
    
    if out_of_range_entries:
        print(f"Out-of-range dates ({len(out_of_range_entries)} models):")
        for model, date_str, reason in sorted(out_of_range_entries):
            print(f"  - {model}: '{date_str}' ({reason})")
        print()
    
    raise ValueError(f"Found {len(empty_entries)} empty, {len(invalid_entries)} invalid, and {len(out_of_range_entries)} out-of-range date entries")

# Sort models by date
sorted_models = sorted(parsed_dates.items(), key=lambda x: x[1][0])

# Print models sorted by date
print(f"Models sorted by publication date ({len(sorted_models)} models):\n")
print(f"{'Date':<12} {'Model':<50}")
print("-" * 65)

for model, (parsed_date, original_date) in sorted_models:
    print(f"{original_date:<12} {model:<50}")

# Print some statistics
if sorted_models:
    oldest_model, (oldest_date, _) = sorted_models[0]
    newest_model, (newest_date, _) = sorted_models[-1]
    
    print(f"\nStatistics:")
    print(f"  Oldest model: {oldest_model} ({oldest_date.strftime('%Y-%m-%d')})")
    print(f"  Newest model: {newest_model} ({newest_date.strftime('%Y-%m-%d')})")
    print(f"  Total models with valid dates: {len(sorted_models)}")