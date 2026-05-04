#!/usr/bin/env python3
import argparse
import csv
import json
import os
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

SCRIPT_DIR = Path(__file__).resolve().parent

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

CATEGORY_TEMPLATE = {k: 0 for k in CATEGORY_KEYS}
GROUP_KEYS = tuple(CATEGORY_GROUPS.keys())
HALLUCINATION_NAMES = {
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
    "4c_visual_descr_mismatch": "4c. Visual Description Mismatch",
}


def extract_pm_category(filename_parts):
    for part in filename_parts[1:]:
        if part.startswith("cat"):
            return part
    return None


def load_report(report_entry):
    filename, path = report_entry
    filename_parts = filename.split("_")
    model_name = filename_parts[0]
    pm_cat = extract_pm_category(filename_parts)

    try:
        with open(path, "r", encoding="utf-8") as handler:
            data = json.load(handler)
    except Exception:
        return None

    return (
        model_name,
        pm_cat,
        data.get("totals", {}).get("hallucinations_overall", 0),
        data.get("categories", {}),
    )


def aggregate_reports(output_dir):
    summary = {}
    pm_llm_data = defaultdict(lambda: defaultdict(int))
    report_entries = [(entry.name, entry.path) for entry in os.scandir(output_dir) if entry.is_file()]
    max_workers = min(32, max(1, (os.cpu_count() or 1) * 2))

    if len(report_entries) < 200:
        report_iter = map(load_report, report_entries)
    else:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            report_iter = executor.map(load_report, report_entries, chunksize=64)
            report_iter = list(report_iter)

    for report in report_iter:
        if report is None:
            continue

        model_name, pm_cat, total, categories = report

        if model_name not in summary:
            summary[model_name] = {
                "total_hallucinations": 0,
                "by_category": CATEGORY_TEMPLATE.copy(),
                "group_totals": {group: 0 for group in GROUP_KEYS},
            }

        model_summary = summary[model_name]
        model_summary["total_hallucinations"] += total
        by_category = model_summary["by_category"]
        group_totals = model_summary["group_totals"]

        for cat, details in categories.items():
            if cat not in by_category:
                continue

            count = details.get("count", 0)
            if count <= 0:
                continue

            by_category[cat] += count
            group_totals[cat[0]] += count

            if pm_cat:
                pm_llm_data[cat][pm_cat] += count

    return summary, pm_llm_data


def write_pm_llm_category_table(pm_llm_data, output_file='pm_llm_category_table.md'):
    """Write a Markdown table with PM-LLM categories as columns and hallucination types as rows."""
    all_pm_cats = set()
    for hall_cat in pm_llm_data.values():
        all_pm_cats.update(hall_cat.keys())

    pm_cats_sorted = sorted(all_pm_cats)

    lines = [
        '# PM-LLM Benchmark Hallucination Analysis',
        '',
        'Aggregated hallucination counts across all LLMs, organized by PM-LLM benchmark categories.',
        '',
    ]

    header = ['Hallucination Type'] + [cat.upper() for cat in pm_cats_sorted] + ['Total']
    lines.append('| ' + ' | '.join(header) + ' |')
    lines.append('| ' + ' | '.join(['---'] * len(header)) + ' |')

    pm_cat_totals = {pm_cat: 0 for pm_cat in pm_cats_sorted}
    grand_total = 0

    for hall_cat in CATEGORY_KEYS:
        row = [HALLUCINATION_NAMES.get(hall_cat, hall_cat)]
        row_total = 0
        counts_for_category = pm_llm_data.get(hall_cat, {})

        for pm_cat in pm_cats_sorted:
            count = counts_for_category.get(pm_cat, 0)
            row.append(str(count))
            row_total += count
            pm_cat_totals[pm_cat] += count

        row.append(str(row_total))
        grand_total += row_total
        lines.append('| ' + ' | '.join(row) + ' |')

    total_row = ['**Total**'] + [f'**{pm_cat_totals[pm_cat]}**' for pm_cat in pm_cats_sorted] + [f'**{grand_total}**']
    lines.append('| ' + ' | '.join(total_row) + ' |')

    with open(output_file, 'w', encoding='utf-8') as handler:
        handler.write('\n'.join(lines) + '\n')
    
    print(f"PM-LLM category table written to {output_file}")

def write_reports(summary,
                  report_name_md='hallucination_report.md',
                  report_name_csv='hallucination_report.csv'):
    sorted_models = sorted(summary.items(), key=lambda item: item[1]['total_hallucinations'])

    headers = ['Model', 'Total'] + CATEGORY_KEYS
    markdown_lines = [
        '# Hallucination Summary Report',
        '',
        '| ' + ' | '.join(headers) + ' |',
        '| ' + ' | '.join(['---'] * len(headers)) + ' |',
    ]
    csv_rows = []

    for model, data in sorted_models:
        category_counts = [data['by_category'].get(cat, 0) for cat in CATEGORY_KEYS]
        markdown_lines.append('| ' + ' | '.join([model, str(data['total_hallucinations']), *map(str, category_counts)]) + ' |')
        csv_rows.append([model, data['total_hallucinations'], *category_counts])

    md_path = report_name_md
    with open(md_path, 'w', encoding='utf-8') as md:
        md.write('\n'.join(markdown_lines) + '\n')
    print(f"Markdown report written to {md_path}")

    csv_path = report_name_csv
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(csv_rows)
    print(f"CSV report written to {csv_path}")

    base, _ = os.path.splitext(report_name_csv)
    for group, keys in CATEGORY_GROUPS.items():
        grp_headers = ['Model', f'Category_{group}_Total'] + keys
        csv_grp_path = f"{base}_category{group}.csv"

        sorted_by_group = sorted(summary.items(), key=lambda item: item[1]['group_totals'][group])

        with open(csv_grp_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(grp_headers)
            for model, data in sorted_by_group:
                counts = [data['by_category'].get(k, 0) for k in keys]
                writer.writerow([model, data['group_totals'][group], *counts])
        print(f"Category {group} CSV report written to {csv_grp_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate hallucination counts per model and write reports"
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        default=str(SCRIPT_DIR / 'output'),
        help='Directory containing JSON report files and where to save reports'
    )
    parser.add_argument(
        '--report_name_md',
        type=str,
        default=str(SCRIPT_DIR / 'hallucination_report.md'),
        help='Filename for the generated markdown report'
    )
    parser.add_argument(
        '--report_name_csv',
        type=str,
        default=str(SCRIPT_DIR / 'hallucination_report.csv'),
        help='Filename for the generated CSV report'
    )
    parser.add_argument(
        '--pm_llm_table',
        type=str,
        default=str(SCRIPT_DIR / 'pm_llm_category_table.md'),
        help='Filename for the PM-LLM category table'
    )
    args = parser.parse_args()
    summary, pm_llm_data = aggregate_reports(args.output_dir)
    write_reports(summary,
                  args.report_name_md,
                  args.report_name_csv)
    write_pm_llm_category_table(pm_llm_data, args.pm_llm_table)


if __name__ == '__main__':
    main()
