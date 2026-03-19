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
- Correlation: -0.496 ***
- Linear fit: y = -0.077x + 124.3
- P-value: 0.0000
- N samples: 107

**Benchmark Score:**
- Correlation: -0.474 ***
- Linear fit: y = -2.217x + 137.8
- P-value: 0.0000
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.473 ***
- Linear fit: y = -24.323x + 89.4
- P-value: 0.0000
- N samples: 107

**Model Size (B):**
- Correlation: 0.128 
- Linear fit: y = 0.003x + 74.0
- P-value: 0.1922
- N samples: 105

**Is Open Source:**
- Correlation: -0.079 
- Linear fit: y = -4.033x + 77.0
- P-value: 0.4199
- N samples: 107

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.313 **
- Linear fit: y = -1.562x + 96.3
- P-value: 0.0010
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: 0.102 
- Linear fit: y = 0.017x + 41.4
- P-value: 0.2974
- N samples: 107

**Is Open Source:**
- Correlation: 0.101 
- Linear fit: y = 5.543x + 49.7
- P-value: 0.2990
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.062 
- Linear fit: y = -3.391x + 54.1
- P-value: 0.5280
- N samples: 107

**Model Size (B):**
- Correlation: -0.062 
- Linear fit: y = -0.001x + 52.8
- P-value: 0.5331
- N samples: 105

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.429 ***
- Linear fit: y = -17.948x + 116.0
- P-value: 0.0000
- N samples: 107

**Benchmark Score:**
- Correlation: -0.245 *
- Linear fit: y = -0.932x + 132.0
- P-value: 0.0109
- N samples: 107

**Is Open Source:**
- Correlation: -0.239 *
- Linear fit: y = -9.953x + 110.0
- P-value: 0.0132
- N samples: 107

**Model Size (B):**
- Correlation: 0.113 
- Linear fit: y = 0.002x + 104.4
- P-value: 0.2516
- N samples: 105

**Days Since 2024-01-01:**
- Correlation: -0.018 
- Linear fit: y = -0.002x + 107.1
- P-value: 0.8521
- N samples: 107

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.531 ***
- Linear fit: y = -1.215x + 66.9
- P-value: 0.0000
- N samples: 107

**Model Size (B):**
- Correlation: -0.248 *
- Linear fit: y = -0.002x + 34.2
- P-value: 0.0107
- N samples: 105

**Is Reasoning Model:**
- Correlation: -0.230 *
- Linear fit: y = -5.788x + 35.9
- P-value: 0.0173
- N samples: 107

**Is Open Source:**
- Correlation: 0.081 
- Linear fit: y = 2.040x + 31.7
- P-value: 0.4047
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: -0.037 
- Linear fit: y = -0.003x + 34.3
- P-value: 0.7086
- N samples: 107

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.584 ***
- Linear fit: y = -6.422x + 455.9
- P-value: 0.0000
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.456 ***
- Linear fit: y = -55.263x + 306.7
- P-value: 0.0000
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: -0.184 
- Linear fit: y = -0.068x + 317.5
- P-value: 0.0575
- N samples: 107

**Is Open Source:**
- Correlation: -0.044 
- Linear fit: y = -5.248x + 276.9
- P-value: 0.6559
- N samples: 107

**Model Size (B):**
- Correlation: 0.006 
- Linear fit: y = 0.000x + 274.7
- P-value: 0.9509
- N samples: 105

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.496 ***
- Linear fit: y = -0.077x + 124.3
- P-value: 0.0000
- N samples: 107

**Benchmark Score:**
- Correlation: -0.474 ***
- Linear fit: y = -2.217x + 137.8
- P-value: 0.0000
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.473 ***
- Linear fit: y = -24.323x + 89.4
- P-value: 0.0000
- N samples: 107

**Model Size (B):**
- Correlation: 0.128 
- Linear fit: y = 0.003x + 74.0
- P-value: 0.1922
- N samples: 105

**Is Open Source:**
- Correlation: -0.079 
- Linear fit: y = -4.033x + 77.0
- P-value: 0.4199
- N samples: 107

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.313 **
- Linear fit: y = -1.562x + 96.3
- P-value: 0.0010
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: 0.102 
- Linear fit: y = 0.017x + 41.4
- P-value: 0.2974
- N samples: 107

**Is Open Source:**
- Correlation: 0.101 
- Linear fit: y = 5.543x + 49.7
- P-value: 0.2990
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.062 
- Linear fit: y = -3.391x + 54.1
- P-value: 0.5280
- N samples: 107

**Model Size (B):**
- Correlation: -0.062 
- Linear fit: y = -0.001x + 52.8
- P-value: 0.5331
- N samples: 105

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.429 ***
- Linear fit: y = -17.948x + 116.0
- P-value: 0.0000
- N samples: 107

**Benchmark Score:**
- Correlation: -0.245 *
- Linear fit: y = -0.932x + 132.0
- P-value: 0.0109
- N samples: 107

**Is Open Source:**
- Correlation: -0.239 *
- Linear fit: y = -9.953x + 110.0
- P-value: 0.0132
- N samples: 107

**Model Size (B):**
- Correlation: 0.113 
- Linear fit: y = 0.002x + 104.4
- P-value: 0.2516
- N samples: 105

**Days Since 2024-01-01:**
- Correlation: -0.018 
- Linear fit: y = -0.002x + 107.1
- P-value: 0.8521
- N samples: 107

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.531 ***
- Linear fit: y = -1.215x + 66.9
- P-value: 0.0000
- N samples: 107

**Model Size (B):**
- Correlation: -0.248 *
- Linear fit: y = -0.002x + 34.2
- P-value: 0.0107
- N samples: 105

**Is Reasoning Model:**
- Correlation: -0.230 *
- Linear fit: y = -5.788x + 35.9
- P-value: 0.0173
- N samples: 107

**Is Open Source:**
- Correlation: 0.081 
- Linear fit: y = 2.040x + 31.7
- P-value: 0.4047
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: -0.037 
- Linear fit: y = -0.003x + 34.3
- P-value: 0.7086
- N samples: 107

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.632 ***
- Linear fit: y = -0.513x + 25.8
- P-value: 0.0000
- N samples: 107

**Is Open Source:**
- Correlation: 0.254 **
- Linear fit: y = 2.262x + 10.3
- P-value: 0.0082
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.254 **
- Linear fit: y = -2.273x + 12.6
- P-value: 0.0082
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: -0.125 
- Linear fit: y = -0.003x + 13.5
- P-value: 0.2002
- N samples: 107

**Model Size (B):**
- Correlation: 0.089 
- Linear fit: y = 0.000x + 11.1
- P-value: 0.3664
- N samples: 105

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.521 ***
- Linear fit: y = -0.070x + 103.2
- P-value: 0.0000
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.427 ***
- Linear fit: y = -19.022x + 69.7
- P-value: 0.0000
- N samples: 107

**Benchmark Score:**
- Correlation: -0.298 **
- Linear fit: y = -1.206x + 92.7
- P-value: 0.0018
- N samples: 107

**Is Open Source:**
- Correlation: -0.181 
- Linear fit: y = -8.018x + 62.2
- P-value: 0.0619
- N samples: 107

**Model Size (B):**
- Correlation: 0.149 
- Linear fit: y = 0.003x + 57.3
- P-value: 0.1285
- N samples: 105

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.712 ***
- Linear fit: y = -0.498x + 19.4
- P-value: 0.0000
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.393 ***
- Linear fit: y = -3.028x + 7.0
- P-value: 0.0000
- N samples: 107

**Is Open Source:**
- Correlation: 0.225 *
- Linear fit: y = 1.722x + 4.5
- P-value: 0.0200
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: -0.161 
- Linear fit: y = -0.004x + 7.7
- P-value: 0.0977
- N samples: 107

**Model Size (B):**
- Correlation: -0.107 
- Linear fit: y = -0.000x + 5.5
- P-value: 0.2787
- N samples: 105

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.281 **
- Linear fit: y = -0.708x + 42.7
- P-value: 0.0034
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: 0.170 
- Linear fit: y = 0.014x + 13.7
- P-value: 0.0804
- N samples: 107

**Is Open Source:**
- Correlation: 0.083 
- Linear fit: y = 2.300x + 21.7
- P-value: 0.3935
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.029 
- Linear fit: y = -0.807x + 23.2
- P-value: 0.7663
- N samples: 107

**Model Size (B):**
- Correlation: 0.008 
- Linear fit: y = 0.000x + 22.4
- P-value: 0.9345
- N samples: 105

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.303 **
- Linear fit: y = -0.827x + 51.8
- P-value: 0.0015
- N samples: 107

**Model Size (B):**
- Correlation: -0.111 
- Linear fit: y = -0.001x + 29.3
- P-value: 0.2582
- N samples: 105

**Is Open Source:**
- Correlation: 0.095 
- Linear fit: y = 2.830x + 27.2
- P-value: 0.3320
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.091 
- Linear fit: y = -2.744x + 30.1
- P-value: 0.3496
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: 0.019 
- Linear fit: y = 0.002x + 27.4
- P-value: 0.8475
- N samples: 107

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.136 
- Linear fit: y = 0.413x + 0.8
- P-value: 0.1635
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: 0.102 
- Linear fit: y = 0.001x + 0.4
- P-value: 0.2939
- N samples: 107

**Benchmark Score:**
- Correlation: -0.094 
- Linear fit: y = -0.026x + 1.7
- P-value: 0.3368
- N samples: 107

**Model Size (B):**
- Correlation: -0.071 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.4721
- N samples: 105

**Is Reasoning Model:**
- Correlation: 0.052 
- Linear fit: y = 0.159x + 0.9
- P-value: 0.5938
- N samples: 107

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.383 ***
- Linear fit: y = -13.827x + 103.3
- P-value: 0.0000
- N samples: 107

**Is Open Source:**
- Correlation: -0.364 ***
- Linear fit: y = -13.055x + 101.0
- P-value: 0.0001
- N samples: 107

**Model Size (B):**
- Correlation: 0.201 *
- Linear fit: y = 0.003x + 93.4
- P-value: 0.0394
- N samples: 105

**Benchmark Score:**
- Correlation: -0.095 
- Linear fit: y = -0.311x + 104.1
- P-value: 0.3314
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: -0.015 
- Linear fit: y = -0.002x + 96.4
- P-value: 0.8748
- N samples: 107

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.656 ***
- Linear fit: y = -0.610x + 27.5
- P-value: 0.0000
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.399 ***
- Linear fit: y = -4.084x + 12.6
- P-value: 0.0000
- N samples: 107

**Is Open Source:**
- Correlation: 0.302 **
- Linear fit: y = 3.074x + 8.9
- P-value: 0.0016
- N samples: 107

**Model Size (B):**
- Correlation: -0.251 **
- Linear fit: y = -0.001x + 10.9
- P-value: 0.0099
- N samples: 105

**Days Since 2024-01-01:**
- Correlation: -0.016 
- Linear fit: y = -0.000x + 10.6
- P-value: 0.8694
- N samples: 107

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.201 *
- Linear fit: y = -0.012x + 0.4
- P-value: 0.0380
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: -0.067 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.4918
- N samples: 107

**Model Size (B):**
- Correlation: 0.061 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.5383
- N samples: 105

**Is Reasoning Model:**
- Correlation: -0.057 
- Linear fit: y = -0.037x + 0.1
- P-value: 0.5585
- N samples: 107

**Is Open Source:**
- Correlation: 0.044 
- Linear fit: y = 0.028x + 0.1
- P-value: 0.6564
- N samples: 107

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.433 ***
- Linear fit: y = -0.432x + 20.0
- P-value: 0.0000
- N samples: 107

**Is Open Source:**
- Correlation: 0.288 **
- Linear fit: y = 3.149x + 6.4
- P-value: 0.0027
- N samples: 107

**Model Size (B):**
- Correlation: -0.270 **
- Linear fit: y = -0.001x + 8.5
- P-value: 0.0054
- N samples: 105

**Is Reasoning Model:**
- Correlation: -0.078 
- Linear fit: y = -0.863x + 8.3
- P-value: 0.4219
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: 0.056 
- Linear fit: y = 0.002x + 6.6
- P-value: 0.5685
- N samples: 107

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.648 ***
- Linear fit: y = -0.796x + 40.4
- P-value: 0.0000
- N samples: 107

**Model Size (B):**
- Correlation: -0.311 **
- Linear fit: y = -0.002x + 19.0
- P-value: 0.0012
- N samples: 105

**Is Reasoning Model:**
- Correlation: -0.291 **
- Linear fit: y = -3.938x + 20.2
- P-value: 0.0023
- N samples: 107

**Is Open Source:**
- Correlation: 0.259 **
- Linear fit: y = 3.482x + 16.4
- P-value: 0.0071
- N samples: 107

**Days Since 2024-01-01:**
- Correlation: -0.059 
- Linear fit: y = -0.002x + 19.5
- P-value: 0.5442
- N samples: 107

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.424 ***
- Linear fit: y = -4.590x + 8.9
- P-value: 0.0000
- N samples: 107

**Is Reasoning Model:**
- Correlation: -0.091 
- Linear fit: y = -0.987x + 7.4
- P-value: 0.3534
- N samples: 107

**Model Size (B):**
- Correlation: 0.085 
- Linear fit: y = 0.000x + 6.6
- P-value: 0.3872
- N samples: 105

**Days Since 2024-01-01:**
- Correlation: -0.067 
- Linear fit: y = -0.002x + 8.3
- P-value: 0.4907
- N samples: 107

**Benchmark Score:**
- Correlation: 0.013 
- Linear fit: y = 0.013x + 6.5
- P-value: 0.8962
- N samples: 107

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.712, y = -0.498x + 19.4

**3b_self_contradiction vs Benchmark Score:**
  r = -0.656, y = -0.610x + 27.5

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.648, y = -0.796x + 40.4

**1a_instruction_override vs Benchmark Score:**
  r = -0.632, y = -0.513x + 25.8

**total_hallucinations vs Benchmark Score:**
  r = -0.584, y = -6.422x + 455.9

**category4_technical_errors vs Benchmark Score:**
  r = -0.531, y = -1.215x + 66.9

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.521, y = -0.070x + 103.2

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.496, y = -0.077x + 124.3

**category1_input_misalignment vs Benchmark Score:**
  r = -0.474, y = -2.217x + 137.8

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.473, y = -24.323x + 89.4

**total_hallucinations vs Is Reasoning Model:**
  r = -0.456, y = -55.263x + 306.7

**4a_syntax_error vs Benchmark Score:**
  r = -0.433, y = -0.432x + 20.0

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.429, y = -17.948x + 116.0

**1b_context_omission vs Is Reasoning Model:**
  r = -0.427, y = -19.022x + 69.7

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.424, y = -4.590x + 8.9

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.399, y = -4.084x + 12.6

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.393, y = -3.028x + 7.0

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.383, y = -13.827x + 103.3

**3a_unsupported_leap vs Is Open Source:**
  r = -0.364, y = -13.055x + 101.0

**category2_factual_errors vs Benchmark Score:**
  r = -0.313, y = -1.562x + 96.3

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.311, y = -0.002x + 19.0

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.303, y = -0.827x + 51.8

**3b_self_contradiction vs Is Open Source:**
  r = 0.302, y = 3.074x + 8.9


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
- Correlation: -0.235 *
- Linear fit: y = -0.247x + 71.6

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.040 
- Linear fit: y = 0.032x + 103.3

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.051 
- Linear fit: y = 0.024x + 30.7

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.642 ***
- Linear fit: y = 0.482x + 80.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.542 ***
- Linear fit: y = 0.241x + 19.8

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.457 ***
- Linear fit: y = 0.271x + 3.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.837x + 6.5

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.963 ***, y = 0.820x + -3.4

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.930 ***, y = 0.505x + 2.2

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.920 ***, y = 0.461x + -1.5

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.817 ***, y = 0.441x + 3.7

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.732 ***, y = 0.320x + -2.6

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.717 ***, y = 0.777x + 11.1

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.642 ***, y = 0.482x + 80.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.630 ***, y = 0.121x + 4.2

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.629 ***, y = 0.161x + -6.4

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.614 ***, y = 0.217x + 4.3

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.601 ***, y = 0.435x + -17.2

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.589 ***, y = 0.394x + -18.8

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.588 ***, y = 0.497x + -0.3

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.582 ***, y = 0.783x + 6.3

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.579 ***, y = 0.249x + 2.5

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.575 ***, y = 0.721x + 10.4

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.562 ***, y = 0.034x + -0.7

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.559 ***, y = 0.099x + 4.1

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.557 ***, y = 0.360x + 76.1

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.394 ***, y = -0.029x + 2.8
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.376 ***, y = -0.305x + 75.4
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.353 ***, y = -0.218x + 35.8
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.322 ***, y = -0.215x + 41.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.304 **, y = -0.019x + 2.5
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.235 *, y = -0.247x + 71.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.221 *, y = -0.116x + 31.7
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
