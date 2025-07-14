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


def aggregate_reports(output_dir):
    summary = {}
    for fname in os.listdir(output_dir):
        path = os.path.join(output_dir, fname)
        if not os.path.isfile(path):
            continue
        model_name = fname.split('_', 1)[0]
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
        for cat, details in data.get('categories', {}).items():
            if cat in summary[model_name]['by_category']:
                summary[model_name]['by_category'][cat] += details.get('count', 0)
    return summary


def write_reports(summary, output_dir, report_name_md='hallucination_report.md', report_name_csv='hallucination_report.csv'):
    # Sort models by total hallucinations ascending
    sorted_models = sorted(summary.items(), key=lambda x: x[1]['total_hallucinations'])

    # Prepare headers
    headers = ['Model', 'Total'] + CATEGORY_KEYS

    # Write Markdown report
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

    # Write CSV report
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


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate hallucination counts per model and write reports"
    )
    parser.add_argument(
        '--output_dir', type=str, default='output',
        help='Directory containing JSON report files and where to save reports'
    )
    parser.add_argument(
        '--report_name_md', type=str, default='hallucination_report.md',
        help='Filename for the generated markdown report'
    )
    parser.add_argument(
        '--report_name_csv', type=str, default='hallucination_report.csv',
        help='Filename for the generated CSV report'
    )
    args = parser.parse_args()
    summary = aggregate_reports(args.output_dir)
    write_reports(summary, args.output_dir, args.report_name_md, args.report_name_csv)


if __name__ == '__main__':
    main()
