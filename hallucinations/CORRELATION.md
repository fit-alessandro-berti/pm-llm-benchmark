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
- Correlation: -0.533 ***
- Linear fit: y = -0.079x + 123.4
- P-value: 0.0000
- N samples: 77

**Benchmark Score:**
- Correlation: -0.451 ***
- Linear fit: y = -1.895x + 127.8
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.450 ***
- Linear fit: y = -21.701x + 86.4
- P-value: 0.0000
- N samples: 77

**Model Size (B):**
- Correlation: 0.171 
- Linear fit: y = 0.003x + 73.2
- P-value: 0.1386
- N samples: 76

**Is Open Source:**
- Correlation: -0.078 
- Linear fit: y = -3.841x + 76.6
- P-value: 0.5015
- N samples: 77

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.294 **
- Linear fit: y = -1.429x + 93.9
- P-value: 0.0095
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.201 
- Linear fit: y = 0.034x + 33.1
- P-value: 0.0794
- N samples: 77

**Is Open Source:**
- Correlation: 0.099 
- Linear fit: y = 5.676x + 52.0
- P-value: 0.3905
- N samples: 77

**Model Size (B):**
- Correlation: -0.071 
- Linear fit: y = -0.001x + 54.6
- P-value: 0.5409
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.025 
- Linear fit: y = -1.392x + 54.9
- P-value: 0.8296
- N samples: 77

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.412 ***
- Linear fit: y = -16.934x + 117.8
- P-value: 0.0002
- N samples: 77

**Is Open Source:**
- Correlation: -0.203 
- Linear fit: y = -8.552x + 112.3
- P-value: 0.0763
- N samples: 77

**Benchmark Score:**
- Correlation: -0.169 
- Linear fit: y = -0.603x + 125.8
- P-value: 0.1425
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.101 
- Linear fit: y = 0.013x + 101.2
- P-value: 0.3802
- N samples: 77

**Model Size (B):**
- Correlation: 0.100 
- Linear fit: y = 0.001x + 107.6
- P-value: 0.3921
- N samples: 76

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.490 ***
- Linear fit: y = -1.087x + 64.7
- P-value: 0.0000
- N samples: 77

**Model Size (B):**
- Correlation: -0.307 **
- Linear fit: y = -0.003x + 36.5
- P-value: 0.0069
- N samples: 76

**Is Open Source:**
- Correlation: 0.177 
- Linear fit: y = 4.619x + 32.7
- P-value: 0.1238
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.141 
- Linear fit: y = -3.601x + 36.4
- P-value: 0.2203
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.065 
- Linear fit: y = 0.005x + 31.4
- P-value: 0.5760
- N samples: 77

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.540 ***
- Linear fit: y = -5.442x + 433.3
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.404 ***
- Linear fit: y = -46.849x + 306.3
- P-value: 0.0003
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.069 
- Linear fit: y = -0.024x + 296.9
- P-value: 0.5533
- N samples: 77

**Is Open Source:**
- Correlation: -0.005 
- Linear fit: y = -0.634x + 282.2
- P-value: 0.9632
- N samples: 77

**Model Size (B):**
- Correlation: -0.004 
- Linear fit: y = -0.000x + 281.4
- P-value: 0.9745
- N samples: 76

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.533 ***
- Linear fit: y = -0.079x + 123.4
- P-value: 0.0000
- N samples: 77

**Benchmark Score:**
- Correlation: -0.451 ***
- Linear fit: y = -1.895x + 127.8
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.450 ***
- Linear fit: y = -21.701x + 86.4
- P-value: 0.0000
- N samples: 77

**Model Size (B):**
- Correlation: 0.171 
- Linear fit: y = 0.003x + 73.2
- P-value: 0.1386
- N samples: 76

**Is Open Source:**
- Correlation: -0.078 
- Linear fit: y = -3.841x + 76.6
- P-value: 0.5015
- N samples: 77

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.294 **
- Linear fit: y = -1.429x + 93.9
- P-value: 0.0095
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.201 
- Linear fit: y = 0.034x + 33.1
- P-value: 0.0794
- N samples: 77

**Is Open Source:**
- Correlation: 0.099 
- Linear fit: y = 5.676x + 52.0
- P-value: 0.3905
- N samples: 77

**Model Size (B):**
- Correlation: -0.071 
- Linear fit: y = -0.001x + 54.6
- P-value: 0.5409
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.025 
- Linear fit: y = -1.392x + 54.9
- P-value: 0.8296
- N samples: 77

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.412 ***
- Linear fit: y = -16.934x + 117.8
- P-value: 0.0002
- N samples: 77

**Is Open Source:**
- Correlation: -0.203 
- Linear fit: y = -8.552x + 112.3
- P-value: 0.0763
- N samples: 77

**Benchmark Score:**
- Correlation: -0.169 
- Linear fit: y = -0.603x + 125.8
- P-value: 0.1425
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.101 
- Linear fit: y = 0.013x + 101.2
- P-value: 0.3802
- N samples: 77

**Model Size (B):**
- Correlation: 0.100 
- Linear fit: y = 0.001x + 107.6
- P-value: 0.3921
- N samples: 76

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.490 ***
- Linear fit: y = -1.087x + 64.7
- P-value: 0.0000
- N samples: 77

**Model Size (B):**
- Correlation: -0.307 **
- Linear fit: y = -0.003x + 36.5
- P-value: 0.0069
- N samples: 76

**Is Open Source:**
- Correlation: 0.177 
- Linear fit: y = 4.619x + 32.7
- P-value: 0.1238
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.141 
- Linear fit: y = -3.601x + 36.4
- P-value: 0.2203
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.065 
- Linear fit: y = 0.005x + 31.4
- P-value: 0.5760
- N samples: 77

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.630 ***
- Linear fit: y = -0.482x + 24.4
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.283 *
- Linear fit: y = 2.545x + 10.0
- P-value: 0.0126
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.205 
- Linear fit: y = -1.796x + 11.9
- P-value: 0.0743
- N samples: 77

**Model Size (B):**
- Correlation: 0.155 
- Linear fit: y = 0.000x + 10.6
- P-value: 0.1821
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.002x + 12.2
- P-value: 0.5301
- N samples: 77

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.571 ***
- Linear fit: y = -0.073x + 103.6
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.411 ***
- Linear fit: y = -17.153x + 67.7
- P-value: 0.0002
- N samples: 77

**Benchmark Score:**
- Correlation: -0.254 *
- Linear fit: y = -0.924x + 84.5
- P-value: 0.0256
- N samples: 77

**Is Open Source:**
- Correlation: -0.199 
- Linear fit: y = -8.506x + 62.1
- P-value: 0.0826
- N samples: 77

**Model Size (B):**
- Correlation: 0.185 
- Linear fit: y = 0.003x + 57.1
- P-value: 0.1100
- N samples: 76

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.698 ***
- Linear fit: y = -0.490x + 18.9
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.341 **
- Linear fit: y = -2.753x + 6.7
- P-value: 0.0024
- N samples: 77

**Is Open Source:**
- Correlation: 0.257 *
- Linear fit: y = 2.120x + 4.4
- P-value: 0.0242
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.152 
- Linear fit: y = -0.004x + 7.6
- P-value: 0.1880
- N samples: 77

**Model Size (B):**
- Correlation: -0.097 
- Linear fit: y = -0.000x + 5.5
- P-value: 0.4059
- N samples: 76

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.256 *
- Linear fit: y = -0.624x + 40.9
- P-value: 0.0249
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.247 *
- Linear fit: y = 0.021x + 10.6
- P-value: 0.0302
- N samples: 77

**Is Open Source:**
- Correlation: 0.075 
- Linear fit: y = 2.155x + 22.7
- P-value: 0.5166
- N samples: 77

**Is Reasoning Model:**
- Correlation: 0.053 
- Linear fit: y = 1.489x + 22.8
- P-value: 0.6463
- N samples: 77

**Model Size (B):**
- Correlation: 0.009 
- Linear fit: y = 0.000x + 23.1
- P-value: 0.9360
- N samples: 76

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.292 **
- Linear fit: y = -0.789x + 51.6
- P-value: 0.0099
- N samples: 77

**Model Size (B):**
- Correlation: -0.129 
- Linear fit: y = -0.001x + 30.5
- P-value: 0.2673
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.122 
- Linear fit: y = 0.012x + 22.5
- P-value: 0.2904
- N samples: 77

**Is Open Source:**
- Correlation: 0.105 
- Linear fit: y = 3.348x + 28.3
- P-value: 0.3613
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.102 
- Linear fit: y = -3.170x + 31.3
- P-value: 0.3758
- N samples: 77

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.188 
- Linear fit: y = 0.002x + -0.0
- P-value: 0.1016
- N samples: 77

**Is Reasoning Model:**
- Correlation: 0.105 
- Linear fit: y = 0.289x + 0.8
- P-value: 0.3652
- N samples: 77

**Model Size (B):**
- Correlation: -0.067 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.5635
- N samples: 76

**Benchmark Score:**
- Correlation: -0.066 
- Linear fit: y = -0.016x + 1.4
- P-value: 0.5661
- N samples: 77

**Is Open Source:**
- Correlation: 0.061 
- Linear fit: y = 0.173x + 0.9
- P-value: 0.5976
- N samples: 77

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.372 ***
- Linear fit: y = -13.385x + 105.1
- P-value: 0.0009
- N samples: 77

**Is Open Source:**
- Correlation: -0.347 **
- Linear fit: y = -12.804x + 103.2
- P-value: 0.0020
- N samples: 77

**Model Size (B):**
- Correlation: 0.197 
- Linear fit: y = 0.002x + 96.0
- P-value: 0.0873
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.095 
- Linear fit: y = 0.010x + 91.8
- P-value: 0.4131
- N samples: 77

**Benchmark Score:**
- Correlation: 0.001 
- Linear fit: y = 0.003x + 98.1
- P-value: 0.9932
- N samples: 77

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.660 ***
- Linear fit: y = -0.592x + 27.1
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.394 ***
- Linear fit: y = 4.157x + 9.0
- P-value: 0.0004
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.341 **
- Linear fit: y = -3.511x + 12.5
- P-value: 0.0024
- N samples: 77

**Model Size (B):**
- Correlation: -0.297 **
- Linear fit: y = -0.001x + 11.5
- P-value: 0.0093
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.078 
- Linear fit: y = 0.002x + 9.1
- P-value: 0.4994
- N samples: 77

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.234 *
- Linear fit: y = -0.014x + 0.5
- P-value: 0.0401
- N samples: 77

**Is Open Source:**
- Correlation: 0.130 
- Linear fit: y = 0.094x + 0.1
- P-value: 0.2581
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.068 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.5595
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.053 
- Linear fit: y = -0.037x + 0.2
- P-value: 0.6467
- N samples: 77

**Model Size (B):**
- Correlation: 0.044 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.7063
- N samples: 76

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.396 ***
- Linear fit: y = -0.397x + 19.3
- P-value: 0.0004
- N samples: 77

**Is Open Source:**
- Correlation: 0.351 **
- Linear fit: y = 4.138x + 6.6
- P-value: 0.0018
- N samples: 77

**Model Size (B):**
- Correlation: -0.302 **
- Linear fit: y = -0.001x + 9.1
- P-value: 0.0081
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.118 
- Linear fit: y = 0.004x + 5.7
- P-value: 0.3061
- N samples: 77

**Is Reasoning Model:**
- Correlation: 0.021 
- Linear fit: y = 0.244x + 8.1
- P-value: 0.8549
- N samples: 77

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.645 ***
- Linear fit: y = -0.784x + 40.8
- P-value: 0.0000
- N samples: 77

**Model Size (B):**
- Correlation: -0.379 ***
- Linear fit: y = -0.002x + 20.4
- P-value: 0.0007
- N samples: 76

**Is Open Source:**
- Correlation: 0.364 **
- Linear fit: y = 5.209x + 17.0
- P-value: 0.0011
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.263 *
- Linear fit: y = -3.667x + 20.9
- P-value: 0.0210
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.033 
- Linear fit: y = 0.001x + 18.1
- P-value: 0.7743
- N samples: 77

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.412 ***
- Linear fit: y = -4.728x + 9.1
- P-value: 0.0002
- N samples: 77

**Benchmark Score:**
- Correlation: 0.096 
- Linear fit: y = 0.094x + 4.7
- P-value: 0.4045
- N samples: 77

**Model Size (B):**
- Correlation: 0.083 
- Linear fit: y = 0.000x + 7.0
- P-value: 0.4733
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.016 
- Linear fit: y = -0.178x + 7.4
- P-value: 0.8908
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.016 
- Linear fit: y = -0.001x + 7.6
- P-value: 0.8931
- N samples: 77

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.698, y = -0.490x + 18.9

**3b_self_contradiction vs Benchmark Score:**
  r = -0.660, y = -0.592x + 27.1

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.645, y = -0.784x + 40.8

**1a_instruction_override vs Benchmark Score:**
  r = -0.630, y = -0.482x + 24.4

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.571, y = -0.073x + 103.6

**total_hallucinations vs Benchmark Score:**
  r = -0.540, y = -5.442x + 433.3

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.533, y = -0.079x + 123.4

**category4_technical_errors vs Benchmark Score:**
  r = -0.490, y = -1.087x + 64.7

**category1_input_misalignment vs Benchmark Score:**
  r = -0.451, y = -1.895x + 127.8

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.450, y = -21.701x + 86.4

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.412, y = -16.934x + 117.8

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.412, y = -4.728x + 9.1

**1b_context_omission vs Is Reasoning Model:**
  r = -0.411, y = -17.153x + 67.7

**total_hallucinations vs Is Reasoning Model:**
  r = -0.404, y = -46.849x + 306.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.396, y = -0.397x + 19.3

**3b_self_contradiction vs Is Open Source:**
  r = 0.394, y = 4.157x + 9.0

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.379, y = -0.002x + 20.4

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.372, y = -13.385x + 105.1

**4b_model_semantics_breach vs Is Open Source:**
  r = 0.364, y = 5.209x + 17.0

**4a_syntax_error vs Is Open Source:**
  r = 0.351, y = 4.138x + 6.6

**3a_unsupported_leap vs Is Open Source:**
  r = -0.347, y = -12.804x + 103.2

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.341, y = -2.753x + 6.7

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.341, y = -3.511x + 12.5

**category4_technical_errors vs Model Size (B):**
  r = -0.307, y = -0.003x + 36.5

**4a_syntax_error vs Model Size (B):**
  r = -0.302, y = -0.001x + 9.1


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
- Correlation: -0.274 **
- Linear fit: y = -0.281x + 75.8

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: -0.001 
- Linear fit: y = -0.001x + 106.9

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.026 
- Linear fit: y = 0.012x + 32.0

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.630 ***
- Linear fit: y = 0.472x + 81.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.528 ***
- Linear fit: y = 0.233x + 20.3

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.427 ***
- Linear fit: y = 0.252x + 5.9

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.971 ***, y = 0.846x + 5.5

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.965 ***, y = 0.819x + -3.1

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.931 ***, y = 0.508x + 2.2

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.919 ***, y = 0.459x + -1.5

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.824 ***, y = 0.451x + 3.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.732 ***, y = 0.316x + -2.6

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.717 ***, y = 0.783x + 11.4

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.630 ***, y = 0.472x + 81.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.616 ***, y = 0.117x + 4.5

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.604 ***, y = 0.210x + 4.6

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.601 ***, y = 0.152x + -5.4

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.594 ***, y = 0.509x + -0.4

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.593 ***, y = 0.431x + -16.5

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.577 ***, y = 0.756x + 6.7

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.574 ***, y = 0.382x + -17.6

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.571 ***, y = 0.727x + 10.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.568 ***, y = 0.099x + 4.0

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.563 ***, y = 0.242x + 2.9

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.555 ***, y = 0.082x + -0.9

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.553 ***, y = 0.034x + -0.7

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.414 ***, y = -0.031x + 2.9
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.409 ***, y = -0.339x + 78.6
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.384 ***, y = -0.231x + 37.2
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.353 ***, y = -0.232x + 43.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.328 ***, y = -0.021x + 2.7
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.274 **, y = -0.281x + 75.8
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.260 **, y = -0.133x + 33.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = -0.228 *, y = -0.127x + 39.5
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
