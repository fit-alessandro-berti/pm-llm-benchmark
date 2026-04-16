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
- Correlation: -0.545 ***
- Linear fit: y = -0.083x + 128.8
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.486 ***
- Linear fit: y = -2.427x + 144.6
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.444 ***
- Linear fit: y = -23.726x + 88.9
- P-value: 0.0000
- N samples: 118

**Model Size (B):**
- Correlation: 0.124 
- Linear fit: y = 0.003x + 74.8
- P-value: 0.1880
- N samples: 114

**Is Open Source:**
- Correlation: -0.089 
- Linear fit: y = -4.747x + 77.8
- P-value: 0.3382
- N samples: 118

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.302 ***
- Linear fit: y = -1.493x + 94.1
- P-value: 0.0009
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.140 
- Linear fit: y = -7.407x + 55.8
- P-value: 0.1309
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.091 
- Linear fit: y = 0.014x + 43.0
- P-value: 0.3297
- N samples: 118

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 3.039x + 50.3
- P-value: 0.5363
- N samples: 118

**Model Size (B):**
- Correlation: -0.055 
- Linear fit: y = -0.001x + 52.0
- P-value: 0.5645
- N samples: 114

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.467 ***
- Linear fit: y = -19.161x + 116.1
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.249 **
- Linear fit: y = -0.952x + 132.4
- P-value: 0.0067
- N samples: 118

**Is Open Source:**
- Correlation: -0.227 *
- Linear fit: y = -9.286x + 109.6
- P-value: 0.0135
- N samples: 118

**Model Size (B):**
- Correlation: 0.106 
- Linear fit: y = 0.002x + 104.3
- P-value: 0.2631
- N samples: 114

**Days Since 2024-01-01:**
- Correlation: -0.003 
- Linear fit: y = -0.000x + 105.6
- P-value: 0.9715
- N samples: 118

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.515 ***
- Linear fit: y = -1.188x + 66.2
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.244 **
- Linear fit: y = -6.020x + 35.8
- P-value: 0.0078
- N samples: 118

**Model Size (B):**
- Correlation: -0.235 *
- Linear fit: y = -0.002x + 34.0
- P-value: 0.0120
- N samples: 114

**Is Open Source:**
- Correlation: 0.061 
- Linear fit: y = 1.495x + 31.8
- P-value: 0.5141
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.035 
- Linear fit: y = -0.002x + 34.0
- P-value: 0.7060
- N samples: 118

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.589 ***
- Linear fit: y = -6.548x + 460.3
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.507 ***
- Linear fit: y = -60.322x + 308.0
- P-value: 0.0000
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.217 *
- Linear fit: y = -0.073x + 321.3
- P-value: 0.0184
- N samples: 118

**Is Open Source:**
- Correlation: -0.071 
- Linear fit: y = -8.386x + 278.0
- P-value: 0.4475
- N samples: 118

**Model Size (B):**
- Correlation: 0.010 
- Linear fit: y = 0.000x + 274.5
- P-value: 0.9174
- N samples: 114

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.545 ***
- Linear fit: y = -0.083x + 128.8
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.486 ***
- Linear fit: y = -2.427x + 144.6
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.444 ***
- Linear fit: y = -23.726x + 88.9
- P-value: 0.0000
- N samples: 118

**Model Size (B):**
- Correlation: 0.124 
- Linear fit: y = 0.003x + 74.8
- P-value: 0.1880
- N samples: 114

**Is Open Source:**
- Correlation: -0.089 
- Linear fit: y = -4.747x + 77.8
- P-value: 0.3382
- N samples: 118

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.302 ***
- Linear fit: y = -1.493x + 94.1
- P-value: 0.0009
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.140 
- Linear fit: y = -7.407x + 55.8
- P-value: 0.1309
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.091 
- Linear fit: y = 0.014x + 43.0
- P-value: 0.3297
- N samples: 118

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 3.039x + 50.3
- P-value: 0.5363
- N samples: 118

**Model Size (B):**
- Correlation: -0.055 
- Linear fit: y = -0.001x + 52.0
- P-value: 0.5645
- N samples: 114

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.467 ***
- Linear fit: y = -19.161x + 116.1
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.249 **
- Linear fit: y = -0.952x + 132.4
- P-value: 0.0067
- N samples: 118

**Is Open Source:**
- Correlation: -0.227 *
- Linear fit: y = -9.286x + 109.6
- P-value: 0.0135
- N samples: 118

**Model Size (B):**
- Correlation: 0.106 
- Linear fit: y = 0.002x + 104.3
- P-value: 0.2631
- N samples: 114

**Days Since 2024-01-01:**
- Correlation: -0.003 
- Linear fit: y = -0.000x + 105.6
- P-value: 0.9715
- N samples: 118

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.515 ***
- Linear fit: y = -1.188x + 66.2
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.244 **
- Linear fit: y = -6.020x + 35.8
- P-value: 0.0078
- N samples: 118

**Model Size (B):**
- Correlation: -0.235 *
- Linear fit: y = -0.002x + 34.0
- P-value: 0.0120
- N samples: 114

**Is Open Source:**
- Correlation: 0.061 
- Linear fit: y = 1.495x + 31.8
- P-value: 0.5141
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.035 
- Linear fit: y = -0.002x + 34.0
- P-value: 0.7060
- N samples: 118

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.607 ***
- Linear fit: y = -0.512x + 26.1
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.293 **
- Linear fit: y = -2.645x + 13.0
- P-value: 0.0013
- N samples: 118

**Is Open Source:**
- Correlation: 0.226 *
- Linear fit: y = 2.033x + 10.6
- P-value: 0.0140
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.153 
- Linear fit: y = -0.004x + 14.1
- P-value: 0.0976
- N samples: 118

**Model Size (B):**
- Correlation: 0.080 
- Linear fit: y = 0.000x + 11.4
- P-value: 0.3997
- N samples: 114

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.576 ***
- Linear fit: y = -0.076x + 107.3
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.396 ***
- Linear fit: y = -18.269x + 69.0
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.329 ***
- Linear fit: y = -1.418x + 99.0
- P-value: 0.0003
- N samples: 118

**Is Open Source:**
- Correlation: -0.181 *
- Linear fit: y = -8.338x + 62.5
- P-value: 0.0499
- N samples: 118

**Model Size (B):**
- Correlation: 0.148 
- Linear fit: y = 0.003x + 57.8
- P-value: 0.1162
- N samples: 114

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.706 ***
- Linear fit: y = -0.497x + 19.5
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.373 ***
- Linear fit: y = -2.813x + 6.9
- P-value: 0.0000
- N samples: 118

**Is Open Source:**
- Correlation: 0.207 *
- Linear fit: y = 1.558x + 4.6
- P-value: 0.0244
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.155 
- Linear fit: y = -0.003x + 7.5
- P-value: 0.0932
- N samples: 118

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.000x + 5.6
- P-value: 0.2161
- N samples: 114

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.250 **
- Linear fit: y = -0.625x + 40.4
- P-value: 0.0063
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.189 *
- Linear fit: y = 0.014x + 13.5
- P-value: 0.0407
- N samples: 118

**Is Open Source:**
- Correlation: 0.069 
- Linear fit: y = 1.837x + 21.9
- P-value: 0.4593
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.051 
- Linear fit: y = -1.351x + 23.4
- P-value: 0.5870
- N samples: 118

**Model Size (B):**
- Correlation: 0.004 
- Linear fit: y = 0.000x + 22.3
- P-value: 0.9653
- N samples: 114

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.307 ***
- Linear fit: y = -0.842x + 52.0
- P-value: 0.0007
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.210 *
- Linear fit: y = -6.160x + 31.5
- P-value: 0.0226
- N samples: 118

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.001x + 28.7
- P-value: 0.3181
- N samples: 114

**Is Open Source:**
- Correlation: 0.030 
- Linear fit: y = 0.893x + 27.7
- P-value: 0.7433
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.018 
- Linear fit: y = -0.001x + 29.0
- P-value: 0.8479
- N samples: 118

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.105 
- Linear fit: y = 0.310x + 0.8
- P-value: 0.2562
- N samples: 118

**Benchmark Score:**
- Correlation: -0.094 
- Linear fit: y = -0.026x + 1.7
- P-value: 0.3100
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.091 
- Linear fit: y = 0.001x + 0.4
- P-value: 0.3293
- N samples: 118

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.4674
- N samples: 114

**Is Reasoning Model:**
- Correlation: 0.035 
- Linear fit: y = 0.104x + 0.9
- P-value: 0.7034
- N samples: 118

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.415 ***
- Linear fit: y = -14.626x + 103.3
- P-value: 0.0000
- N samples: 118

**Is Open Source:**
- Correlation: -0.346 ***
- Linear fit: y = -12.185x + 100.6
- P-value: 0.0001
- N samples: 118

**Model Size (B):**
- Correlation: 0.193 *
- Linear fit: y = 0.003x + 93.3
- P-value: 0.0394
- N samples: 114

**Benchmark Score:**
- Correlation: -0.102 
- Linear fit: y = -0.338x + 104.7
- P-value: 0.2695
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.008 
- Linear fit: y = -0.001x + 95.7
- P-value: 0.9289
- N samples: 118

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.637 ***
- Linear fit: y = -0.603x + 27.3
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.443 ***
- Linear fit: y = -4.491x + 12.7
- P-value: 0.0000
- N samples: 118

**Is Open Source:**
- Correlation: 0.283 **
- Linear fit: y = 2.859x + 8.9
- P-value: 0.0019
- N samples: 118

**Model Size (B):**
- Correlation: -0.248 **
- Linear fit: y = -0.001x + 10.9
- P-value: 0.0077
- N samples: 114

**Days Since 2024-01-01:**
- Correlation: 0.018 
- Linear fit: y = 0.001x + 9.8
- P-value: 0.8467
- N samples: 118

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.190 *
- Linear fit: y = -0.011x + 0.4
- P-value: 0.0397
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.069 
- Linear fit: y = -0.044x + 0.1
- P-value: 0.4558
- N samples: 118

**Is Open Source:**
- Correlation: 0.063 
- Linear fit: y = 0.040x + 0.1
- P-value: 0.4967
- N samples: 118

**Model Size (B):**
- Correlation: 0.050 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.5978
- N samples: 114

**Days Since 2024-01-01:**
- Correlation: -0.041 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.6593
- N samples: 118

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.402 ***
- Linear fit: y = -0.409x + 19.2
- P-value: 0.0000
- N samples: 118

**Model Size (B):**
- Correlation: -0.243 **
- Linear fit: y = -0.001x + 8.3
- P-value: 0.0092
- N samples: 114

**Is Open Source:**
- Correlation: 0.226 *
- Linear fit: y = 2.448x + 6.5
- P-value: 0.0141
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.076 
- Linear fit: y = -0.826x + 8.0
- P-value: 0.4134
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.066 
- Linear fit: y = 0.002x + 6.3
- P-value: 0.4802
- N samples: 118

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.645 ***
- Linear fit: y = -0.786x + 40.2
- P-value: 0.0000
- N samples: 118

**Model Size (B):**
- Correlation: -0.300 **
- Linear fit: y = -0.002x + 18.9
- P-value: 0.0012
- N samples: 114

**Is Reasoning Model:**
- Correlation: -0.285 **
- Linear fit: y = -3.723x + 20.0
- P-value: 0.0017
- N samples: 118

**Is Open Source:**
- Correlation: 0.230 *
- Linear fit: y = 2.993x + 16.6
- P-value: 0.0123
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.069 
- Linear fit: y = -0.003x + 19.5
- P-value: 0.4556
- N samples: 118

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.357 ***
- Linear fit: y = -3.946x + 8.7
- P-value: 0.0001
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.133 
- Linear fit: y = -1.470x + 7.8
- P-value: 0.1516
- N samples: 118

**Model Size (B):**
- Correlation: 0.069 
- Linear fit: y = 0.000x + 6.8
- P-value: 0.4668
- N samples: 114

**Days Since 2024-01-01:**
- Correlation: -0.061 
- Linear fit: y = -0.002x + 8.2
- P-value: 0.5119
- N samples: 118

**Benchmark Score:**
- Correlation: 0.006 
- Linear fit: y = 0.006x + 6.8
- P-value: 0.9487
- N samples: 118

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.706, y = -0.497x + 19.5

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.645, y = -0.786x + 40.2

**3b_self_contradiction vs Benchmark Score:**
  r = -0.637, y = -0.603x + 27.3

**1a_instruction_override vs Benchmark Score:**
  r = -0.607, y = -0.512x + 26.1

**total_hallucinations vs Benchmark Score:**
  r = -0.589, y = -6.548x + 460.3

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.576, y = -0.076x + 107.3

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.545, y = -0.083x + 128.8

**category4_technical_errors vs Benchmark Score:**
  r = -0.515, y = -1.188x + 66.2

**total_hallucinations vs Is Reasoning Model:**
  r = -0.507, y = -60.322x + 308.0

**category1_input_misalignment vs Benchmark Score:**
  r = -0.486, y = -2.427x + 144.6

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.467, y = -19.161x + 116.1

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.444, y = -23.726x + 88.9

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.443, y = -4.491x + 12.7

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.415, y = -14.626x + 103.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.402, y = -0.409x + 19.2

**1b_context_omission vs Is Reasoning Model:**
  r = -0.396, y = -18.269x + 69.0

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.373, y = -2.813x + 6.9

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.357, y = -3.946x + 8.7

**3a_unsupported_leap vs Is Open Source:**
  r = -0.346, y = -12.185x + 100.6

**1b_context_omission vs Benchmark Score:**
  r = -0.329, y = -1.418x + 99.0

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.307, y = -0.842x + 52.0

**category2_factual_errors vs Benchmark Score:**
  r = -0.302, y = -1.493x + 94.1


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
- Correlation: -0.227 *
- Linear fit: y = -0.223x + 69.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.046 
- Linear fit: y = 0.035x + 102.9

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.058 
- Linear fit: y = 0.026x + 30.4

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.631 ***
- Linear fit: y = 0.481x + 80.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.533 ***
- Linear fit: y = 0.242x + 19.8

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.468 ***
- Linear fit: y = 0.278x + 3.0

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.835x + 6.8

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.967 ***, y = 0.825x + -3.9

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.925 ***, y = 0.509x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.912 ***, y = 0.457x + -1.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.819 ***, y = 0.435x + 3.9

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.709 ***, y = 0.313x + -2.5

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.691 ***, y = 0.758x + 11.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.633 ***, y = 0.163x + -6.7

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.631 ***, y = 0.481x + 80.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.607 ***, y = 0.119x + 4.3

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.602 ***, y = 0.215x + 4.4

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.601 ***, y = 0.434x + -17.4

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.590 ***, y = 0.487x + -0.2

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.580 ***, y = 0.099x + 4.2

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.579 ***, y = 0.788x + 6.1

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.565 ***, y = 0.693x + 10.7

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.561 ***, y = 0.034x + -0.8

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.558 ***, y = 0.367x + -16.0

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.558 ***, y = 0.252x + -1.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.555 ***, y = 0.240x + 2.7

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.378 ***, y = -0.026x + 2.6
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.362 ***, y = -0.209x + 35.2
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.356 ***, y = -0.310x + 75.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.300 ***, y = -0.018x + 2.4
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.276 **, y = -0.175x + 38.8
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.241 **, y = -0.118x + 31.9
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.227 *, y = -0.223x + 69.3
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
