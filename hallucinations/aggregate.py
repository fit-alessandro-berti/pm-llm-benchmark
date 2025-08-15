#!/usr/bin/env python3
import os
import json
import argparse
import csv

# Define the fixed category ordering
CATEGORY_KEYS = [
    "1a_instruction_override",
    "1b_context_omission",
    "1c_prompt_contradiction",
    "2a_concept_fabrication",
    "2b_spurious_numeric",
    "2c_false_citation",
    "3a_unsupported_leap",
    "3b_self_contradiction",
    "3c_circular_reasoning",
    "4a_syntax_error",
    "4b_model_semantics_breach",
    "4c_visual_descr_mismatch"
]

# Group the keys by their top‑level category (1, 2, 3, 4)
CATEGORY_GROUPS = {
    "1": [k for k in CATEGORY_KEYS if k.startswith("1")],
    "2": [k for k in CATEGORY_KEYS if k.startswith("2")],
    "3": [k for k in CATEGORY_KEYS if k.startswith("3")],
    "4": [k for k in CATEGORY_KEYS if k.startswith("4")],
}


def aggregate_reports(output_dir):
    summary = {}
    # Also collect data for PM-LLM categories
    pm_llm_data = {}  # Structure: {hallucination_cat: {pm_cat: count}}
    
    for fname in os.listdir(output_dir):
        path = os.path.join(output_dir, fname)
        if not os.path.isfile(path):
            continue
        model_name = fname.split('_', 1)[0]
        
        # Extract PM-LLM category from filename (e.g., cat01, cat02, etc.)
        parts = fname.split('_')
        pm_cat = None
        for part in parts:
            if part.startswith('cat'):
                pm_cat = part
                break
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            continue
        if model_name not in summary:
            summary[model_name] = {
                'total_hallucinations': 0,
                'by_category': {k: 0 for k in CATEGORY_KEYS}
            }
        total = data.get('totals', {}).get('hallucinations_overall', 0)
        summary[model_name]['total_hallucinations'] += total
        
        # Aggregate hallucination data
        for cat, details in data.get('categories', {}).items():
            count = details.get('count', 0)
            if cat in summary[model_name]['by_category']:
                summary[model_name]['by_category'][cat] += count
            
            # Aggregate for PM-LLM category table
            if pm_cat and count > 0:
                if cat not in pm_llm_data:
                    pm_llm_data[cat] = {}
                if pm_cat not in pm_llm_data[cat]:
                    pm_llm_data[cat][pm_cat] = 0
                pm_llm_data[cat][pm_cat] += count
    
    return summary, pm_llm_data


def write_pm_llm_category_table(pm_llm_data, output_file='pm_llm_category_table.md'):
    """Write a Markdown table with PM-LLM categories as columns and hallucination types as rows."""
    # Get all PM-LLM categories present in the data
    all_pm_cats = set()
    for hall_cat in pm_llm_data.values():
        all_pm_cats.update(hall_cat.keys())
    
    # Sort PM-LLM categories
    pm_cats_sorted = sorted(all_pm_cats)
    
    # Define readable names for hallucination categories
    hallucination_names = {
        "1a_instruction_override": "1a. Instruction Override",
        "1b_context_omission": "1b. Context Omission",
        "1c_prompt_contradiction": "1c. Prompt Contradiction",
        "2a_concept_fabrication": "2a. Concept Fabrication",
        "2b_spurious_numeric": "2b. Spurious Numeric",
        "2c_false_citation": "2c. False Citation",
        "3a_unsupported_leap": "3a. Unsupported Leap",
        "3b_self_contradiction": "3b. Self Contradiction",
        "3c_circular_reasoning": "3c. Circular Reasoning",
        "4a_syntax_error": "4a. Syntax Error",
        "4b_model_semantics_breach": "4b. Model Semantics Breach",
        "4c_visual_descr_mismatch": "4c. Visual Description Mismatch"
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# PM-LLM Benchmark Hallucination Analysis\n\n')
        f.write('Aggregated hallucination counts across all LLMs, organized by PM-LLM benchmark categories.\n\n')
        
        # Write table header
        header = ['Hallucination Type'] + [cat.upper() for cat in pm_cats_sorted] + ['Total']
        f.write('| ' + ' | '.join(header) + ' |\n')
        f.write('| ' + ' | '.join(['---'] * len(header)) + ' |\n')
        
        # Write data rows
        for hall_cat in CATEGORY_KEYS:
            row = [hallucination_names.get(hall_cat, hall_cat)]
            row_total = 0
            
            for pm_cat in pm_cats_sorted:
                count = pm_llm_data.get(hall_cat, {}).get(pm_cat, 0)
                row.append(str(count))
                row_total += count
            
            row.append(str(row_total))
            f.write('| ' + ' | '.join(row) + ' |\n')
        
        # Write totals row
        f.write('| **Total** |')
        grand_total = 0
        for pm_cat in pm_cats_sorted:
            col_total = sum(pm_llm_data.get(hall_cat, {}).get(pm_cat, 0) 
                          for hall_cat in CATEGORY_KEYS)
            f.write(f' **{col_total}** |')
            grand_total += col_total
        f.write(f' **{grand_total}** |\n')
    
    print(f"PM-LLM category table written to {output_file}")

def write_reports(summary,
                  pm_llm_data,
                  output_dir,
                  report_name_md='hallucination_report.md',
                  report_name_csv='hallucination_report.csv'):
    # Sort models by raw total hallucinations ascending
    sorted_models = sorted(summary.items(),
                           key=lambda x: x[1]['total_hallucinations'])

    # Prepare headers for the overall reports
    headers = ['Model', 'Total'] + CATEGORY_KEYS

    # === Write Markdown report (absolute counts) ===
    md_path = report_name_md
    with open(md_path, 'w', encoding='utf-8') as md:
        md.write('# Hallucination Summary Report\n\n')
        md.write('| ' + ' | '.join(headers) + ' |\n')
        md.write('| ' + ' | '.join(['---'] * len(headers)) + ' |\n')
        for model, data in sorted_models:
            row = [model, str(data['total_hallucinations'])]
            for cat in CATEGORY_KEYS:
                row.append(str(data['by_category'].get(cat, 0)))
            md.write('| ' + ' | '.join(row) + ' |\n')
    print(f"Markdown report written to {md_path}")

    # === Write CSV report (absolute counts) ===
    csv_path = report_name_csv
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for model, data in sorted_models:
            row = [model, data['total_hallucinations']]
            for cat in CATEGORY_KEYS:
                row.append(data['by_category'].get(cat, 0))
            writer.writerow(row)
    print(f"CSV report written to {csv_path}")

    # === Write separate CSVs for each top‑level category group ===
    base, _ = os.path.splitext(report_name_csv)
    for group, keys in CATEGORY_GROUPS.items():
        # Now put the group total right after the model
        grp_headers = ['Model', f'Category_{group}_Total'] + keys
        csv_grp_path = f"{base}_category{group}.csv"

        # Sort by this group's total
        sorted_by_group = sorted(
            summary.items(),
            key=lambda x: sum(x[1]['by_category'].get(k, 0) for k in keys)
        )

        with open(csv_grp_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(grp_headers)
            for model, data in sorted_by_group:
                counts = [data['by_category'].get(k, 0) for k in keys]
                total_grp = sum(counts)
                # Write: Model, Total_for_this_group, sub-category counts...
                writer.writerow([model, total_grp, *counts])
        print(f"Category {group} CSV report written to {csv_grp_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate hallucination counts per model and write reports"
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        default='output',
        help='Directory containing JSON report files and where to save reports'
    )
    parser.add_argument(
        '--report_name_md',
        type=str,
        default='hallucination_report.md',
        help='Filename for the generated markdown report'
    )
    parser.add_argument(
        '--report_name_csv',
        type=str,
        default='hallucination_report.csv',
        help='Filename for the generated CSV report'
    )
    parser.add_argument(
        '--pm_llm_table',
        type=str,
        default='pm_llm_category_table.md',
        help='Filename for the PM-LLM category table'
    )
    args = parser.parse_args()
    summary, pm_llm_data = aggregate_reports(args.output_dir)
    write_reports(summary,
                  pm_llm_data,
                  args.output_dir,
                  args.report_name_md,
                  args.report_name_csv)
    write_pm_llm_category_table(pm_llm_data, args.pm_llm_table)


if __name__ == '__main__':
    main()
