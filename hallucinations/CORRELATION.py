#!/usr/bin/env python3
import json
import re
from datetime import datetime
import numpy as np
from scipy import stats
import pandas as pd

def parse_hallucination_report(filepath='hallucination_report.md'):
    """Parse the markdown table from hallucination report"""
    data = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Find the table (skip header lines)
    in_table = False
    for line in lines:
        if '| Model |' in line:
            in_table = True
            continue
        if '| --- |' in line:
            continue
        if in_table and line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 2 and parts[0] and parts[1].isdigit():
                model_name = parts[0]
                scores = [int(p) if p.isdigit() else 0 for p in parts[1:]]
                data.append({
                    'model': model_name,
                    'total_hallucinations': scores[0],
                    '1a_instruction_override': scores[1] if len(scores) > 1 else 0,
                    '1b_context_omission': scores[2] if len(scores) > 2 else 0,
                    '1c_prompt_contradiction': scores[3] if len(scores) > 3 else 0,
                    '2a_concept_fabrication': scores[4] if len(scores) > 4 else 0,
                    '2b_spurious_numeric': scores[5] if len(scores) > 5 else 0,
                    '2c_false_citation': scores[6] if len(scores) > 6 else 0,
                    '3a_unsupported_leap': scores[7] if len(scores) > 7 else 0,
                    '3b_self_contradiction': scores[8] if len(scores) > 8 else 0,
                    '3c_circular_reasoning': scores[9] if len(scores) > 9 else 0,
                    '4a_syntax_error': scores[10] if len(scores) > 10 else 0,
                    '4b_model_semantics_breach': scores[11] if len(scores) > 11 else 0,
                    '4c_visual_descr_mismatch': scores[12] if len(scores) > 12 else 0
                })
    
    return pd.DataFrame(data)

def load_json_data(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def calculate_model_size(model_info):
    """Calculate total model size from model_info.json"""
    model_sizes = {}
    for model, sizes in model_info.items():
        if sizes and isinstance(sizes, list):
            model_sizes[model] = sum(sizes)
        elif sizes:
            model_sizes[model] = sizes
        else:
            model_sizes[model] = None
    return model_sizes

def date_to_days_since_epoch(date_str):
    """Convert date string to days since a reference date"""
    if not date_str or date_str == 'null':
        return None
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        reference = datetime(2024, 1, 1)
        return (date_obj - reference).days
    except:
        return None

def calculate_correlation(x, y, name_x, name_y):
    """Calculate correlation between two variables, handling NaN values"""
    # Remove pairs where either value is None/NaN
    valid_pairs = [(xi, yi) for xi, yi in zip(x, y) if xi is not None and yi is not None and not np.isnan(xi) and not np.isnan(yi)]
    
    if len(valid_pairs) < 3:
        return None, None, None, None, 0
    
    x_valid = [p[0] for p in valid_pairs]
    y_valid = [p[1] for p in valid_pairs]
    
    # Calculate Pearson correlation
    corr, p_value = stats.pearsonr(x_valid, y_valid)
    
    # Calculate linear regression (y = ax + b)
    slope, intercept, r_value, p_val, std_err = stats.linregress(x_valid, y_valid)
    
    return corr, p_value, slope, intercept, len(valid_pairs)

def main():
    # Load all data
    print("Loading data and generating correlation analysis...")
    hallucination_df = parse_hallucination_report()
    model_info = load_json_data('model_info.json')
    model_is_os = load_json_data('model_is_os.json')
    model_is_reasoning = load_json_data('model_is_reasoning.json')
    model_scores = load_json_data('model_scores.json')
    model_dates = load_json_data('model_date.json')
    
    # Open output file
    output_file = open('CORRELATION.md', 'w')
    
    # Helper function to write to file
    def write(text=""):
        output_file.write(text + "\n")
    
    # Write variable explanations
    write("# Correlation Analysis Report")
    write("")
    write("=" * 80)
    write("## VARIABLE EXPLANATIONS")
    write("=" * 80)
    write("")
    write("### HALLUCINATION CATEGORIES:")
    write("-" * 40)
    write("**Category 1 - Input Misalignment:**")
    write("- 1a_instruction_override: Model ignores explicit instructions")
    write("- 1b_context_omission: Model omits provided context")
    write("- 1c_prompt_contradiction: Model contradicts the prompt")
    write("")
    write("**Category 2 - Factual Errors:**")
    write("- 2a_concept_fabrication: Model invents concepts/facts")
    write("- 2b_spurious_numeric: Model generates incorrect numbers")
    write("- 2c_false_citation: Model creates false references")
    write("")
    write("**Category 3 - Logical Errors:**")
    write("- 3a_unsupported_leap: Model makes unsupported logical jumps")
    write("- 3b_self_contradiction: Model contradicts itself")
    write("- 3c_circular_reasoning: Model uses circular logic")
    write("")
    write("**Category 4 - Technical Errors:**")
    write("- 4a_syntax_error: Model produces syntactically incorrect output")
    write("- 4b_model_semantics_breach: Model violates semantic rules")
    write("- 4c_visual_descr_mismatch: Model misinterprets visual descriptions")
    write("")
    write("### MODEL FEATURES:")
    write("-" * 40)
    write("- **model_size**: Total model parameters in billions (B)")
    write("- **is_opensource**: Binary (1=open source, 0=proprietary)")
    write("- **is_reasoning**: Binary (1=reasoning model, 0=standard model)")
    write("- **benchmark_score**: Performance score from PM-LLM benchmark")
    write("- **days_since_2024**: Days since Jan 1, 2024 (model age indicator)")
    
    # Calculate model sizes
    model_sizes = calculate_model_size(model_info)
    
    # Create combined dataframe
    combined_data = []
    for _, row in hallucination_df.iterrows():
        model = row['model']
        
        # Calculate category sums
        category1_sum = (row['1a_instruction_override'] + 
                        row['1b_context_omission'] + 
                        row['1c_prompt_contradiction'])
        category2_sum = (row['2a_concept_fabrication'] + 
                        row['2b_spurious_numeric'] + 
                        row['2c_false_citation'])
        category3_sum = (row['3a_unsupported_leap'] + 
                        row['3b_self_contradiction'] + 
                        row['3c_circular_reasoning'])
        category4_sum = (row['4a_syntax_error'] + 
                        row['4b_model_semantics_breach'] + 
                        row['4c_visual_descr_mismatch'])
        
        combined_data.append({
            'model': model,
            'total_hallucinations': row['total_hallucinations'],
            '1a_instruction_override': row['1a_instruction_override'],
            '1b_context_omission': row['1b_context_omission'],
            '1c_prompt_contradiction': row['1c_prompt_contradiction'],
            '2a_concept_fabrication': row['2a_concept_fabrication'],
            '2b_spurious_numeric': row['2b_spurious_numeric'],
            '2c_false_citation': row['2c_false_citation'],
            '3a_unsupported_leap': row['3a_unsupported_leap'],
            '3b_self_contradiction': row['3b_self_contradiction'],
            '3c_circular_reasoning': row['3c_circular_reasoning'],
            '4a_syntax_error': row['4a_syntax_error'],
            '4b_model_semantics_breach': row['4b_model_semantics_breach'],
            '4c_visual_descr_mismatch': row['4c_visual_descr_mismatch'],
            'category1_input_misalignment': category1_sum,
            'category2_factual_errors': category2_sum,
            'category3_logical_errors': category3_sum,
            'category4_technical_errors': category4_sum,
            'model_size': model_sizes.get(model),
            'is_opensource': 1 if model_is_os.get(model) else 0 if model in model_is_os else None,
            'is_reasoning': 1 if model_is_reasoning.get(model) else 0 if model in model_is_reasoning else None,
            'benchmark_score': model_scores.get(model),
            'days_since_2024': date_to_days_since_epoch(model_dates.get(model))
        })
    
    combined_df = pd.DataFrame(combined_data)
    
    # Define hallucination columns
    hallucination_cols = [
        'total_hallucinations',
        'category1_input_misalignment',
        'category2_factual_errors',
        'category3_logical_errors',
        'category4_technical_errors',
        '1a_instruction_override',
        '1b_context_omission', 
        '1c_prompt_contradiction',
        '2a_concept_fabrication',
        '2b_spurious_numeric',
        '2c_false_citation',
        '3a_unsupported_leap',
        '3b_self_contradiction',
        '3c_circular_reasoning',
        '4a_syntax_error',
        '4b_model_semantics_breach',
        '4c_visual_descr_mismatch'
    ]
    
    # Define feature columns
    feature_cols = [
        ('model_size', 'Model Size (B)'),
        ('is_opensource', 'Is Open Source'),
        ('is_reasoning', 'Is Reasoning Model'),
        ('benchmark_score', 'Benchmark Score'),
        ('days_since_2024', 'Days Since 2024-01-01')
    ]
    
    # Write header
    write("")
    write("=" * 80)
    write("## CORRELATION ANALYSIS: Hallucinations vs Model Features")
    write("=" * 80)
    
    # First, analyze category sums specifically
    write("")
    write("=" * 80)
    write("## CATEGORY-LEVEL CORRELATIONS (Summed Categories)")
    write("=" * 80)
    
    category_cols = [
        'category1_input_misalignment',
        'category2_factual_errors',
        'category3_logical_errors',
        'category4_technical_errors'
    ]
    
    for cat_col in category_cols:
        write("")
        write("-" * 60)
        write(f"### Correlations with: {cat_col}")
        write("-" * 60)
        
        correlations = []
        
        for feat_col, feat_name in feature_cols:
            y = combined_df[cat_col].values
            x = combined_df[feat_col].values
            
            corr, p_val, slope, intercept, n_valid = calculate_correlation(x, y, feat_name, cat_col)
            
            if corr is not None:
                correlations.append({
                    'feature': feat_name,
                    'correlation': corr,
                    'p_value': p_val,
                    'slope': slope,
                    'intercept': intercept,
                    'n_samples': n_valid
                })
        
        # Sort by absolute correlation
        correlations.sort(key=lambda x: abs(x['correlation']), reverse=True)
        
        # Write results
        for c in correlations:
            significance = ""
            if c['p_value'] < 0.001:
                significance = "***"
            elif c['p_value'] < 0.01:
                significance = "**"
            elif c['p_value'] < 0.05:
                significance = "*"
            
            write("")
            write(f"**{c['feature']}:**")
            write(f"- Correlation: {c['correlation']:.3f} {significance}")
            write(f"- Linear fit: y = {c['slope']:.3f}x + {c['intercept']:.1f}")
            write(f"- P-value: {c['p_value']:.4f}")
            write(f"- N samples: {c['n_samples']}")
    
    write("")
    write("=" * 80)
    write("## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS")
    write("=" * 80)
    
    # For each hallucination type
    for hall_col in hallucination_cols:
        write("")
        write("-" * 60)
        write(f"### Correlations with: {hall_col}")
        write("-" * 60)
        
        correlations = []
        
        for feat_col, feat_name in feature_cols:
            y = combined_df[hall_col].values
            x = combined_df[feat_col].values
            
            corr, p_val, slope, intercept, n_valid = calculate_correlation(x, y, feat_name, hall_col)
            
            if corr is not None:
                correlations.append({
                    'feature': feat_name,
                    'correlation': corr,
                    'p_value': p_val,
                    'slope': slope,
                    'intercept': intercept,
                    'n_samples': n_valid
                })
        
        # Sort by absolute correlation
        correlations.sort(key=lambda x: abs(x['correlation']), reverse=True)
        
        # Write results
        for c in correlations:
            significance = ""
            if c['p_value'] < 0.001:
                significance = "***"
            elif c['p_value'] < 0.01:
                significance = "**"
            elif c['p_value'] < 0.05:
                significance = "*"
            
            write("")
            write(f"**{c['feature']}:**")
            write(f"- Correlation: {c['correlation']:.3f} {significance}")
            write(f"- Linear fit: y = {c['slope']:.3f}x + {c['intercept']:.1f}")
            write(f"- P-value: {c['p_value']:.4f}")
            write(f"- N samples: {c['n_samples']}")
    
    # Summary statistics
    write("")
    write("=" * 80)
    write("## SUMMARY STATISTICS")
    write("=" * 80)
    
    write("")
    write("### Strongest Correlations (|r| > 0.3):")
    write("-" * 40)
    
    strong_correlations = []
    for hall_col in hallucination_cols:
        for feat_col, feat_name in feature_cols:
            y = combined_df[hall_col].values
            x = combined_df[feat_col].values
            corr, p_val, slope, intercept, n_valid = calculate_correlation(x, y, feat_name, hall_col)
            
            if corr is not None and abs(corr) > 0.3 and p_val < 0.05:
                strong_correlations.append({
                    'hallucination': hall_col,
                    'feature': feat_name,
                    'correlation': corr,
                    'equation': f"y = {slope:.3f}x + {intercept:.1f}"
                })
    
    strong_correlations.sort(key=lambda x: abs(x['correlation']), reverse=True)
    
    for sc in strong_correlations[:40]:  # Top 40 strongest
        write(f"**{sc['hallucination']} vs {sc['feature']}:**")
        write(f"  r = {sc['correlation']:.3f}, {sc['equation']}")
        write("")
    
    write("")
    write("=" * 80)
    write("## Legend:")
    write("- \\* p < 0.05")
    write("- \\*\\* p < 0.01")
    write("- \\*\\*\\* p < 0.001")
    write("=" * 80)
    
    # Inter-category correlations
    write("")
    write("=" * 80)
    write("## INTER-CATEGORY CORRELATIONS")
    write("=" * 80)
    write("")
    write("How different hallucination categories correlate with each other:")
    write("(Shows if models prone to one type also tend to have others)")
    write("-" * 60)
    
    # Define all hallucination columns for inter-correlation
    inter_corr_cols = [
        ('total_hallucinations', 'Total Hallucinations'),
        ('category1_input_misalignment', 'Category 1: Input Misalignment'),
        ('category2_factual_errors', 'Category 2: Factual Errors'),
        ('category3_logical_errors', 'Category 3: Logical Errors'),
        ('category4_technical_errors', 'Category 4: Technical Errors'),
        ('1a_instruction_override', '1a: Instruction Override'),
        ('1b_context_omission', '1b: Context Omission'),
        ('1c_prompt_contradiction', '1c: Prompt Contradiction'),
        ('2a_concept_fabrication', '2a: Concept Fabrication'),
        ('2b_spurious_numeric', '2b: Spurious Numeric'),
        ('2c_false_citation', '2c: False Citation'),
        ('3a_unsupported_leap', '3a: Unsupported Leap'),
        ('3b_self_contradiction', '3b: Self Contradiction'),
        ('3c_circular_reasoning', '3c: Circular Reasoning'),
        ('4a_syntax_error', '4a: Syntax Error'),
        ('4b_model_semantics_breach', '4b: Model Semantics Breach'),
        ('4c_visual_descr_mismatch', '4c: Visual Descr Mismatch')
    ]
    
    # Calculate all inter-correlations
    inter_correlations = []
    for i, (col1, name1) in enumerate(inter_corr_cols):
        for j, (col2, name2) in enumerate(inter_corr_cols):
            if i >= j:  # Skip diagonal and duplicate pairs
                continue
            
            x = combined_df[col1].values
            y = combined_df[col2].values
            
            corr, p_val, slope, intercept, n_valid = calculate_correlation(x, y, name1, name2)
            
            if corr is not None:
                inter_correlations.append({
                    'pair': f"{name1} vs {name2}",
                    'col1': name1,
                    'col2': name2,
                    'correlation': corr,
                    'p_value': p_val,
                    'equation': f"y = {slope:.3f}x + {intercept:.1f}"
                })
    
    # Sort by absolute correlation
    inter_correlations.sort(key=lambda x: abs(x['correlation']), reverse=True)
    
    # Write category-level correlations first
    write("")
    write("### CATEGORY-LEVEL CORRELATIONS")
    write("-" * 40)
    category_pairs = [
        ('Category 1: Input Misalignment', 'Category 2: Factual Errors'),
        ('Category 1: Input Misalignment', 'Category 3: Logical Errors'),
        ('Category 1: Input Misalignment', 'Category 4: Technical Errors'),
        ('Category 2: Factual Errors', 'Category 3: Logical Errors'),
        ('Category 2: Factual Errors', 'Category 4: Technical Errors'),
        ('Category 3: Logical Errors', 'Category 4: Technical Errors'),
    ]
    
    for cat1, cat2 in category_pairs:
        for ic in inter_correlations:
            if (ic['col1'] == cat1 and ic['col2'] == cat2) or (ic['col1'] == cat2 and ic['col2'] == cat1):
                significance = ""
                if ic['p_value'] < 0.001:
                    significance = "***"
                elif ic['p_value'] < 0.01:
                    significance = "**"
                elif ic['p_value'] < 0.05:
                    significance = "*"
                
                write("")
                write(f"**{cat1}**")
                write(f"  vs **{cat2}:**")
                write(f"- Correlation: {ic['correlation']:.3f} {significance}")
                write(f"- Linear fit: {ic['equation']}")
                break
    
    # Write strongest inter-hallucination correlations
    write("")
    write("### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS")
    write("-" * 40)
    
    count = 0
    for ic in inter_correlations:
        # Skip if it involves total_hallucinations (too obvious)
        if 'Total Hallucinations' in ic['col1'] or 'Total Hallucinations' in ic['col2']:
            continue
        
        if abs(ic['correlation']) > 0.3 and ic['p_value'] < 0.05:
            significance = ""
            if ic['p_value'] < 0.001:
                significance = "***"
            elif ic['p_value'] < 0.01:
                significance = "**"
            elif ic['p_value'] < 0.05:
                significance = "*"
            
            write("")
            write(f"**{ic['pair']}:**")
            write(f"  r = {ic['correlation']:.3f} {significance}, {ic['equation']}")
            
            count += 1
            if count >= 20:
                break
    
    # Write interesting negative correlations if any
    write("")
    write("### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)")
    write("-" * 40)
    negative_found = False
    for ic in inter_correlations:
        if 'Total Hallucinations' in ic['col1'] or 'Total Hallucinations' in ic['col2']:
            continue
        
        if ic['correlation'] < -0.2 and ic['p_value'] < 0.05:
            significance = ""
            if ic['p_value'] < 0.001:
                significance = "***"
            elif ic['p_value'] < 0.01:
                significance = "**"
            elif ic['p_value'] < 0.05:
                significance = "*"
            
            write("")
            write(f"**{ic['pair']}:**")
            write(f"  r = {ic['correlation']:.3f} {significance}, {ic['equation']}")
            write(f"  (Models good at one tend to be worse at the other)")
            negative_found = True
    
    if not negative_found:
        write("")
        write("No significant negative correlations found between hallucination types.")
    
    write("")
    write("=" * 80)
    write("## END OF ANALYSIS")
    write("=" * 80)
    
    # Close the file
    output_file.close()
    print("Correlation analysis complete. Results saved to CORRELATION.md")

if __name__ == "__main__":
    main()