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
- Linear fit: y = -0.088x + 132.1
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.518 ***
- Linear fit: y = -2.923x + 160.6
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.408 ***
- Linear fit: y = -21.642x + 86.1
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.143 
- Linear fit: y = -7.690x + 76.7
- P-value: 0.1238
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
- Linear fit: y = -10.170x + 54.1
- P-value: 0.0328
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.051 
- Linear fit: y = 0.007x + 43.5
- P-value: 0.5865
- N samples: 117

**Model Size (B):**
- Correlation: -0.047 
- Linear fit: y = -0.001x + 48.5
- P-value: 0.6232
- N samples: 112

**Is Open Source:**
- Correlation: -0.030 
- Linear fit: y = -1.569x + 48.9
- P-value: 0.7475
- N samples: 117

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.479 ***
- Linear fit: y = -20.235x + 115.3
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.369 ***
- Linear fit: y = -1.657x + 153.0
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.240 **
- Linear fit: y = -10.276x + 107.7
- P-value: 0.0091
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.096 
- Linear fit: y = -0.011x + 111.0
- P-value: 0.3037
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
- Correlation: -0.446 ***
- Linear fit: y = -1.119x + 63.9
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.283 **
- Linear fit: y = -6.669x + 34.5
- P-value: 0.0020
- N samples: 117

**Model Size (B):**
- Correlation: -0.205 *
- Linear fit: y = -0.002x + 32.2
- P-value: 0.0304
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.083 
- Linear fit: y = -0.005x + 34.2
- P-value: 0.3709
- N samples: 117

**Is Open Source:**
- Correlation: -0.053 
- Linear fit: y = -1.271x + 31.1
- P-value: 0.5685
- N samples: 117

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.611 ***
- Linear fit: y = -7.928x + 500.2
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.516 ***
- Linear fit: y = -62.972x + 300.4
- P-value: 0.0000
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.303 ***
- Linear fit: y = -0.100x + 331.4
- P-value: 0.0009
- N samples: 117

**Is Open Source:**
- Correlation: -0.165 
- Linear fit: y = -20.447x + 272.3
- P-value: 0.0746
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
- Linear fit: y = -0.088x + 132.1
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.518 ***
- Linear fit: y = -2.923x + 160.6
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.408 ***
- Linear fit: y = -21.642x + 86.1
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.143 
- Linear fit: y = -7.690x + 76.7
- P-value: 0.1238
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
- Linear fit: y = -10.170x + 54.1
- P-value: 0.0328
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.051 
- Linear fit: y = 0.007x + 43.5
- P-value: 0.5865
- N samples: 117

**Model Size (B):**
- Correlation: -0.047 
- Linear fit: y = -0.001x + 48.5
- P-value: 0.6232
- N samples: 112

**Is Open Source:**
- Correlation: -0.030 
- Linear fit: y = -1.569x + 48.9
- P-value: 0.7475
- N samples: 117

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.479 ***
- Linear fit: y = -20.235x + 115.3
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.369 ***
- Linear fit: y = -1.657x + 153.0
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.240 **
- Linear fit: y = -10.276x + 107.7
- P-value: 0.0091
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.096 
- Linear fit: y = -0.011x + 111.0
- P-value: 0.3037
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
- Correlation: -0.446 ***
- Linear fit: y = -1.119x + 63.9
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.283 **
- Linear fit: y = -6.669x + 34.5
- P-value: 0.0020
- N samples: 117

**Model Size (B):**
- Correlation: -0.205 *
- Linear fit: y = -0.002x + 32.2
- P-value: 0.0304
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.083 
- Linear fit: y = -0.005x + 34.2
- P-value: 0.3709
- N samples: 117

**Is Open Source:**
- Correlation: -0.053 
- Linear fit: y = -1.271x + 31.1
- P-value: 0.5685
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
- Linear fit: y = -0.078x + 110.2
- P-value: 0.0000
- N samples: 117

**Benchmark Score:**
- Correlation: -0.384 ***
- Linear fit: y = -1.883x + 114.1
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.345 ***
- Linear fit: y = -15.911x + 67.2
- P-value: 0.0001
- N samples: 117

**Is Open Source:**
- Correlation: -0.202 *
- Linear fit: y = -9.463x + 61.8
- P-value: 0.0286
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
- P-value: 0.0080
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: 0.140 
- Linear fit: y = 0.010x + 14.4
- P-value: 0.1335
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.115 
- Linear fit: y = -2.923x + 22.5
- P-value: 0.2182
- N samples: 117

**Model Size (B):**
- Correlation: 0.019 
- Linear fit: y = 0.000x + 20.4
- P-value: 0.8421
- N samples: 112

**Is Open Source:**
- Correlation: -0.014 
- Linear fit: y = -0.355x + 21.0
- P-value: 0.8828
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
- Correlation: -0.431 ***
- Linear fit: y = -15.634x + 103.4
- P-value: 0.0000
- N samples: 117

**Is Open Source:**
- Correlation: -0.324 ***
- Linear fit: y = -11.881x + 99.1
- P-value: 0.0004
- N samples: 117

**Benchmark Score:**
- Correlation: -0.276 **
- Linear fit: y = -1.063x + 126.0
- P-value: 0.0026
- N samples: 117

**Model Size (B):**
- Correlation: 0.153 
- Linear fit: y = 0.002x + 92.7
- P-value: 0.1078
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.102 
- Linear fit: y = -0.010x + 101.1
- P-value: 0.2729
- N samples: 117

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.610 ***
- Linear fit: y = -0.595x + 26.9
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.497 ***
- Linear fit: y = -4.556x + 11.8
- P-value: 0.0000
- N samples: 117

**Model Size (B):**
- Correlation: -0.240 *
- Linear fit: y = -0.001x + 9.9
- P-value: 0.0108
- N samples: 112

**Is Open Source:**
- Correlation: 0.178 
- Linear fit: y = 1.653x + 8.5
- P-value: 0.0550
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.040 
- Linear fit: y = -0.001x + 9.8
- P-value: 0.6690
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
- Correlation: -0.546 ***
- Linear fit: y = -0.688x + 37.3
- P-value: 0.0000
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.377 ***
- Linear fit: y = -4.470x + 19.4
- P-value: 0.0000
- N samples: 117

**Model Size (B):**
- Correlation: -0.276 **
- Linear fit: y = -0.001x + 17.9
- P-value: 0.0032
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.101 
- Linear fit: y = -0.003x + 19.1
- P-value: 0.2773
- N samples: 117

**Is Open Source:**
- Correlation: 0.088 
- Linear fit: y = 1.057x + 16.5
- P-value: 0.3448
- N samples: 117

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.324 ***
- Linear fit: y = -3.635x + 8.4
- P-value: 0.0004
- N samples: 117

**Is Reasoning Model:**
- Correlation: -0.138 
- Linear fit: y = -1.531x + 7.8
- P-value: 0.1376
- N samples: 117

**Days Since 2024-01-01:**
- Correlation: -0.125 
- Linear fit: y = -0.004x + 9.4
- P-value: 0.1796
- N samples: 117

**Benchmark Score:**
- Correlation: -0.105 
- Linear fit: y = -0.124x + 10.6
- P-value: 0.2602
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
  r = -0.622, y = -0.078x + 110.2

**total_hallucinations vs Benchmark Score:**
  r = -0.611, y = -7.928x + 500.2

**3b_self_contradiction vs Benchmark Score:**
  r = -0.610, y = -0.595x + 26.9

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.607, y = -0.088x + 132.1

**1a_instruction_override vs Benchmark Score:**
  r = -0.601, y = -0.580x + 28.2

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.546, y = -0.688x + 37.3

**category1_input_misalignment vs Benchmark Score:**
  r = -0.518, y = -2.923x + 160.6

**total_hallucinations vs Is Reasoning Model:**
  r = -0.516, y = -62.972x + 300.4

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.497, y = -4.556x + 11.8

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.479, y = -20.235x + 115.3

**category4_technical_errors vs Benchmark Score:**
  r = -0.446, y = -1.119x + 63.9

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.431, y = -15.634x + 103.4

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.408, y = -21.642x + 86.1

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.389, y = -2.488x + 6.1

**1b_context_omission vs Benchmark Score:**
  r = -0.384, y = -1.883x + 114.1

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.377, y = -4.470x + 19.4

**category3_logical_errors vs Benchmark Score:**
  r = -0.369, y = -1.657x + 153.0

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.357, y = -3.243x + 12.8

**1b_context_omission vs Is Reasoning Model:**
  r = -0.345, y = -15.911x + 67.2

**3a_unsupported_leap vs Is Open Source:**
  r = -0.324, y = -11.881x + 99.1

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.324, y = -3.635x + 8.4

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.311, y = -0.953x + 54.9

**total_hallucinations vs Days Since 2024-01-01:**
  r = -0.303, y = -0.100x + 331.4

**category2_factual_errors vs Benchmark Score:**
  r = -0.302, y = -1.654x + 97.5


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
- Correlation: -0.174 
- Linear fit: y = -0.166x + 61.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.131 
- Linear fit: y = 0.102x + 96.2

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.056 
- Linear fit: y = 0.025x + 29.3

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.660 ***
- Linear fit: y = 0.537x + 77.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.598 ***
- Linear fit: y = 0.282x + 17.3

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.526 ***
- Linear fit: y = 0.305x + -0.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.982 ***, y = 0.844x + 6.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.969 ***, y = 0.842x + -4.4

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.929 ***, y = 0.525x + 1.4

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.906 ***, y = 0.450x + -1.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.811 ***, y = 0.413x + 4.3

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.690 ***, y = 0.155x + -6.8

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.689 ***, y = 0.784x + 10.7

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.676 ***, y = 0.303x + -2.3

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.660 ***, y = 0.537x + 77.4

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.648 ***, y = 0.209x + 3.5

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.634 ***, y = 0.116x + 3.6

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.629 ***, y = 0.436x + -18.1

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.612 ***, y = 0.285x + -2.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.602 ***, y = 0.422x + 73.8

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.598 ***, y = 0.282x + 17.3

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.573 ***, y = 0.349x + -15.2

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.567 ***, y = 0.219x + 2.4

**Category 4: Technical Errors vs 2a: Concept Fabrication:**
  r = 0.564 ***, y = 0.593x + 2.6

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.562 ***, y = 0.696x + 75.5

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.542 ***, y = 0.141x + -4.1

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.350 ***, y = -0.019x + 1.9
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.297 ***, y = -0.269x + 70.3
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.290 ***, y = -0.159x + 30.1
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.286 **, y = -0.014x + 1.8
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.239 **, y = -0.149x + 35.7
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 4a: Syntax Error:**
  r = -0.201 *, y = -0.047x + 9.8
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
