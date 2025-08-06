# LLM Hallucination Detection Benchmark

## Overview

This benchmark provides a systematic framework for detecting, categorizing, and analyzing hallucinations in Large Language Model (LLM) outputs, specifically focused on Process Mining (PM) domain tasks. The system uses a multi-stage pipeline to evaluate model responses across 12 distinct hallucination types organized into 4 main categories.

## Hallucination Taxonomy

### Category 1: Input Misalignment
- **1a_instruction_override**: Model ignores explicit constraints in the prompt
- **1b_context_omission**: Model silently drops prompt context needed for the answer
- **1c_prompt_contradiction**: Model states the opposite of what the prompt requests

### Category 2: Factual Errors
- **2a_concept_fabrication**: Model invents PM concepts, methods, or KPI definitions
- **2b_spurious_numeric**: Model uses numbers not supported by prompt or sources
- **2c_false_citation**: Model attributes statements to non-existent or wrong sources

### Category 3: Logical Errors
- **3a_unsupported_leap**: Conclusions not justified by preceding facts
- **3b_self_contradiction**: Claims that conflict within the same answer
- **3c_circular_reasoning**: Model uses claim as its own proof

### Category 4: Technical Errors
- **4a_syntax_error**: Invalid JSON, code, or other structured output
- **4b_model_semantics_breach**: Violations of modeling notation rules
- **4c_visual_descr_mismatch**: Describes elements not present in images/diagrams

## Severity Scale

Each detected hallucination is classified by severity:
- **low**: Minor inconsistency; does not alter main usefulness
- **medium**: Noticeable error; could mislead non-experts or require repair
- **high**: Substantially wrong; invalidates key parts of the answer
- **critical**: Fatal error; answer cannot be used as-is

## Pipeline Architecture

### 1. Detection Phase (`detect.py`)

Processes model outputs to identify hallucinations:
- **Input**: Judge evaluation reports of LLM answers
- **Processing**: Uses GPT-4 to analyze text against the hallucination taxonomy
- **Output**: JSON reports with categorized hallucinations, snippets, explanations, and severity levels
- **Validation**: Ensures all JSON outputs conform to the required schema
- **Parallelization**: Supports concurrent processing with configurable thread limits

**Usage:**
```bash
python detect.py --input_dir answers/ --output_dir output/ --max_threads 10 --model gpt-4o-mini
```

### 2. Aggregation Phase (`aggregate.py`)

Compiles individual detection reports into comprehensive summaries:
- **Input**: JSON detection reports from the output directory
- **Processing**: Aggregates hallucination counts by model and category
- **Outputs**:
  - `hallucination_report.md`: Markdown table sorted by total hallucinations
  - `hallucination_report.csv`: Complete CSV with all categories
  - `hallucination_report_category[1-4].csv`: Separate CSV files per category

**Usage:**
```bash
python aggregate.py --output_dir output/ --report_name_md hallucination_report.md
```

### 3. Correlation Analysis (`CORRELATION.py`)

Analyzes relationships between hallucinations and model characteristics:
- **Data Sources**:
  - `hallucination_report.md`: Hallucination counts per model
  - `model_info.json`: Model parameter sizes (in billions)
  - `model_is_os.json`: Open-source status (binary)
  - `model_is_reasoning.json`: Reasoning model classification (binary)
  - `model_scores.json`: PM-LLM benchmark performance scores
  - `model_date.json`: Model publication dates

- **Analysis Features**:
  - Pearson correlation coefficients between hallucinations and model features
  - Linear regression equations (y = ax + b) for trend analysis
  - Statistical significance testing (p-values)
  - Category-level aggregation analysis
  - Top 40 strongest correlations highlighted

**Usage:**
```bash
python CORRELATION.py
```

### 4. Model Validation (`validate_models.py`)

Utility script for checking model information completeness:
- Lists models without size information
- Displays models with sizes sorted from smallest to largest
- Helps identify data gaps in model metadata

**Usage:**
```bash
python validate_models.py
```

## Data Files

### Input Data
- `answers/`: Directory containing LLM responses to evaluate
- Model metadata JSON files (see above)

### Generated Reports
- `hallucination_report.md`: Main summary in Markdown format
- `hallucination_report.csv`: Full data in CSV format
- `hallucination_report_category[1-4].csv`: Category-specific reports
- `output/`: Individual JSON detection reports per model/task

## Key Insights from Analysis

The correlation analysis reveals trends between model characteristics and hallucination patterns:
- **Model Size**: Relationship with different hallucination types
- **Open Source vs Proprietary**: Impact on reliability
- **Reasoning Models**: Performance differences in logical consistency
- **Model Age**: Evolution of hallucination patterns over time
- **Benchmark Scores**: Correlation with hallucination rates

## Requirements

- Python 3.7+
- Required packages:
  - `requests`: API communication
  - `numpy`: Numerical computations
  - `scipy`: Statistical analysis
  - `pandas`: Data manipulation
  - OpenAI API key (set as environment variable `OPENAI_API_KEY`)

## Installation

```bash
# Clone the repository
git clone [repository-url]
cd hallucinations/

# Install dependencies
pip install requests numpy scipy pandas

# Set API key
export OPENAI_API_KEY="your-api-key"
```

## Running the Complete Pipeline

```bash
# 1. Detect hallucinations in model outputs
python detect.py --input_dir answers/ --output_dir output/

# 2. Aggregate results into reports
python aggregate.py --output_dir output/

# 3. Analyze correlations with model features
python CORRELATION.py

# 4. (Optional) Validate model information
python validate_models.py
```

## Interpreting Results

### Hallucination Reports
- Lower total counts indicate better model performance
- Category breakdowns reveal specific model weaknesses
- Severity distributions help prioritize improvements

### Correlation Analysis
- **Positive correlations**: Feature increases associated with more hallucinations
- **Negative correlations**: Feature increases associated with fewer hallucinations
- **Significance levels**: * p<0.05, ** p<0.01, *** p<0.001
- **Linear equations**: Quantify the relationship strength and direction

## Contributing

To add new models or update existing data:
1. Add model outputs to the `answers/` directory
2. Update model metadata JSON files with appropriate information
3. Run the detection and analysis pipeline
4. Review generated reports for insights

## License

[Specify your license here]

## Contact

[Specify contact information for questions or contributions]