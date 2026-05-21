# Correlation Analysis Report

================================================================================
## VARIABLE EXPLANATIONS
================================================================================

### HALLUCINATION CATEGORIES:
----------------------------------------
**Category 1 - Input Misalignment:**
- 1a_instruction_override: Model ignores explicit instructions
- 1b_context_omission: Model omits provided context
- 1c_prompt_contradiction: Model contradicts the prompt

**Category 2 - Factual Errors:**
- 2a_concept_fabrication: Model invents concepts/facts
- 2b_spurious_numeric: Model generates incorrect numbers
- 2c_false_citation: Model creates false references

**Category 3 - Logical Errors:**
- 3a_unsupported_leap: Model makes unsupported logical jumps
- 3b_self_contradiction: Model contradicts itself
- 3c_circular_reasoning: Model uses circular logic

**Category 4 - Technical Errors:**
- 4a_syntax_error: Model produces syntactically incorrect output
- 4b_model_semantics_breach: Model violates semantic rules
- 4c_visual_descr_mismatch: Model misinterprets visual descriptions

### MODEL FEATURES:
----------------------------------------
- **model_size**: Total model parameters in billions (B)
- **is_opensource**: Binary (1=open source, 0=proprietary)
- **is_reasoning**: Binary (1=reasoning model, 0=standard model)
- **benchmark_score**: Performance score from PM-LLM benchmark
- **days_since_2024**: Days since Jan 1, 2024 (model age indicator)

================================================================================
## CORRELATION ANALYSIS: Hallucinations vs Model Features
================================================================================

================================================================================
## CATEGORY-LEVEL CORRELATIONS (Summed Categories)
================================================================================

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.607 ***
- Linear fit: y = -0.087x + 132.1
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.518 ***
- Linear fit: y = -2.923x + 160.6
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.407 ***
- Linear fit: y = -21.612x + 86.1
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.144 
- Linear fit: y = -7.718x + 76.7
- P-value: 0.1223
- N samples: 117

**Model Size (B):**
- Correlation: 0.101 
- Linear fit: y = 0.002x + 73.1
- P-value: 0.2908
- N samples: 112

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.302 ***
- Linear fit: y = -1.654x + 97.5
- P-value: 0.0009
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.197 *
- Linear fit: y = -10.140x + 54.1
- P-value: 0.0333
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.051 
- Linear fit: y = 0.007x + 43.5
- P-value: 0.5825
- N samples: 117

**Model Size (B):**
- Correlation: -0.047 
- Linear fit: y = -0.001x + 48.5
- P-value: 0.6232
- N samples: 112

**Is Open Source:**
- Correlation: -0.031 
- Linear fit: y = -1.597x + 48.9
- P-value: 0.7430
- N samples: 117

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.475 ***
- Linear fit: y = -19.996x + 115.3
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.371 ***
- Linear fit: y = -1.657x + 153.1
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.247 **
- Linear fit: y = -10.501x + 108.0
- P-value: 0.0074
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.091 
- Linear fit: y = -0.010x + 110.8
- P-value: 0.3274
- N samples: 117

**Model Size (B):**
- Correlation: 0.081 
- Linear fit: y = 0.001x + 102.7
- P-value: 0.3953
- N samples: 112

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.447 ***
- Linear fit: y = -1.119x + 64.0
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.277 **
- Linear fit: y = -6.535x + 34.5
- P-value: 0.0025
- N samples: 117

**Model Size (B):**
- Correlation: -0.205 *
- Linear fit: y = -0.002x + 32.2
- P-value: 0.0304
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.078 
- Linear fit: y = -0.005x + 34.1
- P-value: 0.4006
- N samples: 117

**Is Open Source:**
- Correlation: -0.059 
- Linear fit: y = -1.398x + 31.3
- P-value: 0.5305
- N samples: 117

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.614 ***
- Linear fit: y = -7.929x + 500.5
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.514 ***
- Linear fit: y = -62.524x + 300.4
- P-value: 0.0000
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.301 ***
- Linear fit: y = -0.099x + 330.9
- P-value: 0.0010
- N samples: 117

**Is Open Source:**
- Correlation: -0.170 
- Linear fit: y = -20.869x + 272.8
- P-value: 0.0676
- N samples: 117

**Model Size (B):**
- Correlation: 0.004 
- Linear fit: y = 0.000x + 264.9
- P-value: 0.9634
- N samples: 112

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.607 ***
- Linear fit: y = -0.087x + 132.1
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.518 ***
- Linear fit: y = -2.923x + 160.6
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.407 ***
- Linear fit: y = -21.612x + 86.1
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.144 
- Linear fit: y = -7.718x + 76.7
- P-value: 0.1223
- N samples: 117

**Model Size (B):**
- Correlation: 0.101 
- Linear fit: y = 0.002x + 73.1
- P-value: 0.2908
- N samples: 112

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.302 ***
- Linear fit: y = -1.654x + 97.5
- P-value: 0.0009
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.197 *
- Linear fit: y = -10.140x + 54.1
- P-value: 0.0333
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.051 
- Linear fit: y = 0.007x + 43.5
- P-value: 0.5825
- N samples: 117

**Model Size (B):**
- Correlation: -0.047 
- Linear fit: y = -0.001x + 48.5
- P-value: 0.6232
- N samples: 112

**Is Open Source:**
- Correlation: -0.031 
- Linear fit: y = -1.597x + 48.9
- P-value: 0.7430
- N samples: 117

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.475 ***
- Linear fit: y = -19.996x + 115.3
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.371 ***
- Linear fit: y = -1.657x + 153.1
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.247 **
- Linear fit: y = -10.501x + 108.0
- P-value: 0.0074
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.091 
- Linear fit: y = -0.010x + 110.8
- P-value: 0.3274
- N samples: 117

**Model Size (B):**
- Correlation: 0.081 
- Linear fit: y = 0.001x + 102.7
- P-value: 0.3953
- N samples: 112

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.447 ***
- Linear fit: y = -1.119x + 64.0
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.277 **
- Linear fit: y = -6.535x + 34.5
- P-value: 0.0025
- N samples: 117

**Model Size (B):**
- Correlation: -0.205 *
- Linear fit: y = -0.002x + 32.2
- P-value: 0.0304
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.078 
- Linear fit: y = -0.005x + 34.1
- P-value: 0.4006
- N samples: 117

**Is Open Source:**
- Correlation: -0.059 
- Linear fit: y = -1.398x + 31.3
- P-value: 0.5305
- N samples: 117

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.601 ***
- Linear fit: y = -0.580x + 28.2
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.357 ***
- Linear fit: y = -3.243x + 12.8
- P-value: 0.0001
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.198 *
- Linear fit: y = -0.005x + 14.2
- P-value: 0.0328
- N samples: 117

**Is Open Source:**
- Correlation: 0.131 
- Linear fit: y = 1.201x + 10.5
- P-value: 0.1604
- N samples: 117

**Model Size (B):**
- Correlation: 0.083 
- Linear fit: y = 0.000x + 10.7
- P-value: 0.3819
- N samples: 112

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.622 ***
- Linear fit: y = -0.078x + 110.1
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.384 ***
- Linear fit: y = -1.883x + 114.1
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.344 ***
- Linear fit: y = -15.881x + 67.2
- P-value: 0.0001
- N samples: 117

**Is Open Source:**
- Correlation: -0.203 *
- Linear fit: y = -9.491x + 61.8
- P-value: 0.0281
- N samples: 117

**Model Size (B):**
- Correlation: 0.115 
- Linear fit: y = 0.002x + 57.5
- P-value: 0.2275
- N samples: 112

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.676 ***
- Linear fit: y = -0.459x + 18.3
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.389 ***
- Linear fit: y = -2.488x + 6.1
- P-value: 0.0000
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.263 **
- Linear fit: y = -0.005x + 7.7
- P-value: 0.0041
- N samples: 117

**Model Size (B):**
- Correlation: -0.109 
- Linear fit: y = -0.000x + 4.9
- P-value: 0.2548
- N samples: 112

**Is Open Source:**
- Correlation: 0.088 
- Linear fit: y = 0.571x + 4.5
- P-value: 0.3442
- N samples: 117

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.244 **
- Linear fit: y = -0.662x + 40.5
- P-value: 0.0079
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.141 
- Linear fit: y = 0.010x + 14.4
- P-value: 0.1303
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.114 
- Linear fit: y = -2.893x + 22.5
- P-value: 0.2226
- N samples: 117

**Model Size (B):**
- Correlation: 0.019 
- Linear fit: y = 0.000x + 20.4
- P-value: 0.8421
- N samples: 112

**Is Open Source:**
- Correlation: -0.015 
- Linear fit: y = -0.384x + 21.0
- P-value: 0.8735
- N samples: 117

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.311 ***
- Linear fit: y = -0.953x + 54.9
- P-value: 0.0007
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.253 **
- Linear fit: y = -7.297x + 30.8
- P-value: 0.0059
- N samples: 117

**Model Size (B):**
- Correlation: -0.095 
- Linear fit: y = -0.001x + 27.3
- P-value: 0.3180
- N samples: 112

**Is Open Source:**
- Correlation: -0.043 
- Linear fit: y = -1.244x + 27.1
- P-value: 0.6484
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.041 
- Linear fit: y = -0.003x + 28.7
- P-value: 0.6631
- N samples: 117

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.146 
- Linear fit: y = -0.040x + 2.0
- P-value: 0.1154
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.092 
- Linear fit: y = 0.001x + 0.4
- P-value: 0.3264
- N samples: 117

**Model Size (B):**
- Correlation: -0.044 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.6459
- N samples: 112

**Is Reasoning Model:**
- Correlation: 0.020 
- Linear fit: y = 0.051x + 0.8
- P-value: 0.8315
- N samples: 117

**Is Open Source:**
- Correlation: 0.012 
- Linear fit: y = 0.031x + 0.8
- P-value: 0.8981
- N samples: 117

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.428 ***
- Linear fit: y = -15.410x + 103.4
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.331 ***
- Linear fit: y = -12.092x + 99.3
- P-value: 0.0003
- N samples: 117

**Benchmark Score:**
- Correlation: -0.277 **
- Linear fit: y = -1.063x + 126.2
- P-value: 0.0025
- N samples: 117

**Model Size (B):**
- Correlation: 0.153 
- Linear fit: y = 0.002x + 92.7
- P-value: 0.1078
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.097 
- Linear fit: y = -0.010x + 100.9
- P-value: 0.2968
- N samples: 117

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.611 ***
- Linear fit: y = -0.596x + 26.9
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.495 ***
- Linear fit: y = -4.541x + 11.8
- P-value: 0.0000
- N samples: 117

**Model Size (B):**
- Correlation: -0.240 *
- Linear fit: y = -0.001x + 9.9
- P-value: 0.0108
- N samples: 112

**Is Open Source:**
- Correlation: 0.176 
- Linear fit: y = 1.639x + 8.5
- P-value: 0.0570
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.039 
- Linear fit: y = -0.001x + 9.8
- P-value: 0.6800
- N samples: 117

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.131 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.1682
- N samples: 112

**Is Open Source:**
- Correlation: -0.079 
- Linear fit: y = -0.047x + 0.1
- P-value: 0.3946
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.077 
- Linear fit: y = -0.045x + 0.1
- P-value: 0.4098
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.030 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.7508
- N samples: 117

**Benchmark Score:**
- Correlation: 0.019 
- Linear fit: y = 0.001x + 0.1
- P-value: 0.8400
- N samples: 117

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.279 **
- Linear fit: y = -0.307x + 16.0
- P-value: 0.0023
- N samples: 117

**Model Size (B):**
- Correlation: -0.192 *
- Linear fit: y = -0.001x + 7.5
- P-value: 0.0429
- N samples: 112

**Is Open Source:**
- Correlation: 0.125 
- Linear fit: y = 1.306x + 6.3
- P-value: 0.1806
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.065 
- Linear fit: y = -0.668x + 7.2
- P-value: 0.4896
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.060 
- Linear fit: y = 0.002x + 5.7
- P-value: 0.5234
- N samples: 117

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.545 ***
- Linear fit: y = -0.688x + 37.4
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.373 ***
- Linear fit: y = -4.425x + 19.4
- P-value: 0.0000
- N samples: 117

**Model Size (B):**
- Correlation: -0.276 **
- Linear fit: y = -0.001x + 17.9
- P-value: 0.0032
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.098 
- Linear fit: y = -0.003x + 19.0
- P-value: 0.2949
- N samples: 117

**Is Open Source:**
- Correlation: 0.084 
- Linear fit: y = 1.015x + 16.5
- P-value: 0.3658
- N samples: 117

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.333 ***
- Linear fit: y = -3.719x + 8.4
- P-value: 0.0002
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.131 
- Linear fit: y = -1.442x + 7.8
- P-value: 0.1602
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.118 
- Linear fit: y = -0.004x + 9.3
- P-value: 0.2038
- N samples: 117

**Benchmark Score:**
- Correlation: -0.106 
- Linear fit: y = -0.124x + 10.7
- P-value: 0.2573
- N samples: 117

**Model Size (B):**
- Correlation: 0.040 
- Linear fit: y = 0.000x + 6.9
- P-value: 0.6763
- N samples: 112

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.676, y = -0.459x + 18.3

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.622, y = -0.078x + 110.1

**total_hallucinations vs Benchmark Score:**
  r = -0.614, y = -7.929x + 500.5

**3b_self_contradiction vs Benchmark Score:**
  r = -0.611, y = -0.596x + 26.9

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.607, y = -0.087x + 132.1

**1a_instruction_override vs Benchmark Score:**
  r = -0.601, y = -0.580x + 28.2

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.545, y = -0.688x + 37.4

**category1_input_misalignment vs Benchmark Score:**
  r = -0.518, y = -2.923x + 160.6

**total_hallucinations vs Is Reasoning Model:**
  r = -0.514, y = -62.524x + 300.4

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.495, y = -4.541x + 11.8

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.475, y = -19.996x + 115.3

**category4_technical_errors vs Benchmark Score:**
  r = -0.447, y = -1.119x + 64.0

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.428, y = -15.410x + 103.4

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.407, y = -21.612x + 86.1

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.389, y = -2.488x + 6.1

**1b_context_omission vs Benchmark Score:**
  r = -0.384, y = -1.883x + 114.1

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.373, y = -4.425x + 19.4

**category3_logical_errors vs Benchmark Score:**
  r = -0.371, y = -1.657x + 153.1

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.357, y = -3.243x + 12.8

**1b_context_omission vs Is Reasoning Model:**
  r = -0.344, y = -15.881x + 67.2

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.333, y = -3.719x + 8.4

**3a_unsupported_leap vs Is Open Source:**
  r = -0.331, y = -12.092x + 99.3

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.311, y = -0.953x + 54.9

**category2_factual_errors vs Benchmark Score:**
  r = -0.302, y = -1.654x + 97.5

**total_hallucinations vs Days Since 2024-01-01:**
  r = -0.301, y = -0.099x + 330.9


================================================================================
## Legend:
- \* p < 0.05
- \*\* p < 0.01
- \*\*\* p < 0.001
================================================================================

================================================================================
## INTER-CATEGORY CORRELATIONS
================================================================================

How different hallucination categories correlate with each other:
(Shows if models prone to one type also tend to have others)
------------------------------------------------------------

### CATEGORY-LEVEL CORRELATIONS
----------------------------------------

**Category 1: Input Misalignment**
  vs **Category 2: Factual Errors:**
- Correlation: -0.177 *
- Linear fit: y = -0.178x + 63.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.114 
- Linear fit: y = 0.089x + 98.2

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.102 
- Linear fit: y = 0.048x + 28.1

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.681 ***
- Linear fit: y = 0.529x + 78.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.562 ***
- Linear fit: y = 0.260x + 18.4

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.518 ***
- Linear fit: y = 0.309x + -0.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.978 ***, y = 0.837x + 7.5

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.966 ***, y = 0.835x + -4.3

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.935 ***, y = 0.522x + 1.5

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.915 ***, y = 0.453x + -1.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.816 ***, y = 0.414x + 4.2

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.714 ***, y = 0.805x + 10.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.688 ***, y = 0.312x + -2.6

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.681 ***, y = 0.529x + 78.0

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.677 ***, y = 0.162x + -7.4

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.653 ***, y = 0.470x + -21.4

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.643 ***, y = 0.214x + 3.6

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.627 ***, y = 0.116x + 3.7

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.622 ***, y = 0.413x + 74.3

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.600 ***, y = 0.383x + -18.3

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.592 ***, y = 0.273x + -1.6

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.584 ***, y = 0.694x + 75.8

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.562 ***, y = 0.260x + 18.4

**2a: Concept Fabrication vs 3a: Unsupported Leap:**
  r = 0.560 ***, y = 0.751x + 78.7

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.559 ***, y = 0.225x + 2.5

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.558 ***, y = 0.705x + 10.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.360 ***, y = -0.020x + 2.0
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.311 ***, y = -0.267x + 70.0
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.301 ***, y = -0.174x + 31.5
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.288 ***, y = -0.014x + 1.9
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.260 **, y = -0.169x + 37.3
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
