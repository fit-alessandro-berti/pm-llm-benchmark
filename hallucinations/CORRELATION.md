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
- Correlation: -0.535 ***
- Linear fit: y = -0.079x + 123.3
- P-value: 0.0000
- N samples: 78

**Benchmark Score:**
- Correlation: -0.454 ***
- Linear fit: y = -1.896x + 127.8
- P-value: 0.0000
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.453 ***
- Linear fit: y = -21.742x + 86.4
- P-value: 0.0000
- N samples: 78

**Model Size (B):**
- Correlation: 0.171 
- Linear fit: y = 0.003x + 73.2
- P-value: 0.1386
- N samples: 76

**Is Open Source:**
- Correlation: -0.072 
- Linear fit: y = -3.558x + 76.3
- P-value: 0.5298
- N samples: 78

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.296 **
- Linear fit: y = -1.427x + 93.8
- P-value: 0.0086
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.195 
- Linear fit: y = 0.033x + 33.6
- P-value: 0.0865
- N samples: 78

**Is Open Source:**
- Correlation: 0.102 
- Linear fit: y = 5.800x + 51.8
- P-value: 0.3753
- N samples: 78

**Model Size (B):**
- Correlation: -0.071 
- Linear fit: y = -0.001x + 54.6
- P-value: 0.5409
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.028 
- Linear fit: y = -1.575x + 54.9
- P-value: 0.8053
- N samples: 78

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.417 ***
- Linear fit: y = -17.101x + 117.8
- P-value: 0.0001
- N samples: 78

**Is Open Source:**
- Correlation: -0.194 
- Linear fit: y = -8.171x + 111.9
- P-value: 0.0884
- N samples: 78

**Benchmark Score:**
- Correlation: -0.177 
- Linear fit: y = -0.630x + 126.4
- P-value: 0.1214
- N samples: 78

**Model Size (B):**
- Correlation: 0.100 
- Linear fit: y = 0.001x + 107.6
- P-value: 0.3921
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.090 
- Linear fit: y = 0.011x + 101.8
- P-value: 0.4331
- N samples: 78

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.495 ***
- Linear fit: y = -1.096x + 64.9
- P-value: 0.0000
- N samples: 78

**Model Size (B):**
- Correlation: -0.307 **
- Linear fit: y = -0.003x + 36.5
- P-value: 0.0069
- N samples: 76

**Is Open Source:**
- Correlation: 0.184 
- Linear fit: y = 4.800x + 32.5
- P-value: 0.1073
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.150 
- Linear fit: y = -3.815x + 36.4
- P-value: 0.1903
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.052 
- Linear fit: y = 0.004x + 31.8
- P-value: 0.6486
- N samples: 78

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.544 ***
- Linear fit: y = -5.469x + 433.9
- P-value: 0.0000
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.410 ***
- Linear fit: y = -47.397x + 306.3
- P-value: 0.0002
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.079 
- Linear fit: y = -0.028x + 298.5
- P-value: 0.4934
- N samples: 78

**Model Size (B):**
- Correlation: -0.004 
- Linear fit: y = -0.000x + 281.4
- P-value: 0.9745
- N samples: 76

**Is Open Source:**
- Correlation: 0.003 
- Linear fit: y = 0.308x + 281.3
- P-value: 0.9820
- N samples: 78

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.535 ***
- Linear fit: y = -0.079x + 123.3
- P-value: 0.0000
- N samples: 78

**Benchmark Score:**
- Correlation: -0.454 ***
- Linear fit: y = -1.896x + 127.8
- P-value: 0.0000
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.453 ***
- Linear fit: y = -21.742x + 86.4
- P-value: 0.0000
- N samples: 78

**Model Size (B):**
- Correlation: 0.171 
- Linear fit: y = 0.003x + 73.2
- P-value: 0.1386
- N samples: 76

**Is Open Source:**
- Correlation: -0.072 
- Linear fit: y = -3.558x + 76.3
- P-value: 0.5298
- N samples: 78

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.296 **
- Linear fit: y = -1.427x + 93.8
- P-value: 0.0086
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.195 
- Linear fit: y = 0.033x + 33.6
- P-value: 0.0865
- N samples: 78

**Is Open Source:**
- Correlation: 0.102 
- Linear fit: y = 5.800x + 51.8
- P-value: 0.3753
- N samples: 78

**Model Size (B):**
- Correlation: -0.071 
- Linear fit: y = -0.001x + 54.6
- P-value: 0.5409
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.028 
- Linear fit: y = -1.575x + 54.9
- P-value: 0.8053
- N samples: 78

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.417 ***
- Linear fit: y = -17.101x + 117.8
- P-value: 0.0001
- N samples: 78

**Is Open Source:**
- Correlation: -0.194 
- Linear fit: y = -8.171x + 111.9
- P-value: 0.0884
- N samples: 78

**Benchmark Score:**
- Correlation: -0.177 
- Linear fit: y = -0.630x + 126.4
- P-value: 0.1214
- N samples: 78

**Model Size (B):**
- Correlation: 0.100 
- Linear fit: y = 0.001x + 107.6
- P-value: 0.3921
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.090 
- Linear fit: y = 0.011x + 101.8
- P-value: 0.4331
- N samples: 78

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.495 ***
- Linear fit: y = -1.096x + 64.9
- P-value: 0.0000
- N samples: 78

**Model Size (B):**
- Correlation: -0.307 **
- Linear fit: y = -0.003x + 36.5
- P-value: 0.0069
- N samples: 76

**Is Open Source:**
- Correlation: 0.184 
- Linear fit: y = 4.800x + 32.5
- P-value: 0.1073
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.150 
- Linear fit: y = -3.815x + 36.4
- P-value: 0.1903
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.052 
- Linear fit: y = 0.004x + 31.8
- P-value: 0.6486
- N samples: 78

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.631 ***
- Linear fit: y = -0.479x + 24.3
- P-value: 0.0000
- N samples: 78

**Is Open Source:**
- Correlation: 0.286 *
- Linear fit: y = 2.567x + 10.0
- P-value: 0.0111
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.209 
- Linear fit: y = -1.824x + 11.9
- P-value: 0.0666
- N samples: 78

**Model Size (B):**
- Correlation: 0.155 
- Linear fit: y = 0.000x + 10.6
- P-value: 0.1821
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.078 
- Linear fit: y = -0.002x + 12.3
- P-value: 0.4949
- N samples: 78

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.572 ***
- Linear fit: y = -0.073x + 103.4
- P-value: 0.0000
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.414 ***
- Linear fit: y = -17.166x + 67.7
- P-value: 0.0002
- N samples: 78

**Benchmark Score:**
- Correlation: -0.258 *
- Linear fit: y = -0.931x + 84.6
- P-value: 0.0226
- N samples: 78

**Is Open Source:**
- Correlation: -0.194 
- Linear fit: y = -8.254x + 61.9
- P-value: 0.0892
- N samples: 78

**Model Size (B):**
- Correlation: 0.185 
- Linear fit: y = 0.003x + 57.1
- P-value: 0.1100
- N samples: 76

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.697 ***
- Linear fit: y = -0.486x + 18.8
- P-value: 0.0000
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.343 **
- Linear fit: y = -2.751x + 6.7
- P-value: 0.0021
- N samples: 78

**Is Open Source:**
- Correlation: 0.259 *
- Linear fit: y = 2.129x + 4.4
- P-value: 0.0222
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.155 
- Linear fit: y = -0.004x + 7.6
- P-value: 0.1760
- N samples: 78

**Model Size (B):**
- Correlation: -0.097 
- Linear fit: y = -0.000x + 5.5
- P-value: 0.4059
- N samples: 76

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.258 *
- Linear fit: y = -0.626x + 41.0
- P-value: 0.0226
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.240 *
- Linear fit: y = 0.021x + 10.9
- P-value: 0.0339
- N samples: 78

**Is Open Source:**
- Correlation: 0.078 
- Linear fit: y = 2.233x + 22.7
- P-value: 0.4971
- N samples: 78

**Is Reasoning Model:**
- Correlation: 0.049 
- Linear fit: y = 1.360x + 22.8
- P-value: 0.6716
- N samples: 78

**Model Size (B):**
- Correlation: 0.009 
- Linear fit: y = 0.000x + 23.1
- P-value: 0.9360
- N samples: 76

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.293 **
- Linear fit: y = -0.784x + 51.4
- P-value: 0.0093
- N samples: 78

**Model Size (B):**
- Correlation: -0.129 
- Linear fit: y = -0.001x + 30.5
- P-value: 0.2673
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.119 
- Linear fit: y = 0.011x + 22.7
- P-value: 0.3007
- N samples: 78

**Is Open Source:**
- Correlation: 0.107 
- Linear fit: y = 3.375x + 28.3
- P-value: 0.3523
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.104 
- Linear fit: y = -3.197x + 31.3
- P-value: 0.3658
- N samples: 78

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.176 
- Linear fit: y = 0.001x + 0.0
- P-value: 0.1228
- N samples: 78

**Is Reasoning Model:**
- Correlation: 0.095 
- Linear fit: y = 0.262x + 0.8
- P-value: 0.4072
- N samples: 78

**Benchmark Score:**
- Correlation: -0.075 
- Linear fit: y = -0.018x + 1.5
- P-value: 0.5126
- N samples: 78

**Is Open Source:**
- Correlation: 0.068 
- Linear fit: y = 0.192x + 0.9
- P-value: 0.5557
- N samples: 78

**Model Size (B):**
- Correlation: -0.067 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.5635
- N samples: 76

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.375 ***
- Linear fit: y = -13.452x + 105.1
- P-value: 0.0007
- N samples: 78

**Is Open Source:**
- Correlation: -0.340 **
- Linear fit: y = -12.508x + 102.9
- P-value: 0.0023
- N samples: 78

**Model Size (B):**
- Correlation: 0.197 
- Linear fit: y = 0.002x + 96.0
- P-value: 0.0873
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.087 
- Linear fit: y = 0.010x + 92.2
- P-value: 0.4511
- N samples: 78

**Benchmark Score:**
- Correlation: -0.006 
- Linear fit: y = -0.019x + 98.6
- P-value: 0.9582
- N samples: 78

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.665 ***
- Linear fit: y = -0.597x + 27.2
- P-value: 0.0000
- N samples: 78

**Is Open Source:**
- Correlation: 0.400 ***
- Linear fit: y = 4.242x + 9.0
- P-value: 0.0003
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.349 **
- Linear fit: y = -3.608x + 12.5
- P-value: 0.0017
- N samples: 78

**Model Size (B):**
- Correlation: -0.297 **
- Linear fit: y = -0.001x + 11.5
- P-value: 0.0093
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.062 
- Linear fit: y = 0.002x + 9.4
- P-value: 0.5922
- N samples: 78

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.238 *
- Linear fit: y = -0.014x + 0.5
- P-value: 0.0358
- N samples: 78

**Is Open Source:**
- Correlation: 0.134 
- Linear fit: y = 0.096x + 0.1
- P-value: 0.2423
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.5271
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.058 
- Linear fit: y = -0.040x + 0.2
- P-value: 0.6159
- N samples: 78

**Model Size (B):**
- Correlation: 0.044 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.7063
- N samples: 76

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.405 ***
- Linear fit: y = -0.406x + 19.5
- P-value: 0.0002
- N samples: 78

**Is Open Source:**
- Correlation: 0.358 **
- Linear fit: y = 4.233x + 6.5
- P-value: 0.0013
- N samples: 78

**Model Size (B):**
- Correlation: -0.302 **
- Linear fit: y = -0.001x + 9.1
- P-value: 0.0081
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.101 
- Linear fit: y = 0.004x + 5.9
- P-value: 0.3775
- N samples: 78

**Is Reasoning Model:**
- Correlation: 0.008 
- Linear fit: y = 0.090x + 8.1
- P-value: 0.9461
- N samples: 78

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.649 ***
- Linear fit: y = -0.789x + 40.9
- P-value: 0.0000
- N samples: 78

**Model Size (B):**
- Correlation: -0.379 ***
- Linear fit: y = -0.002x + 20.4
- P-value: 0.0007
- N samples: 76

**Is Open Source:**
- Correlation: 0.371 ***
- Linear fit: y = 5.313x + 16.9
- P-value: 0.0008
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.272 *
- Linear fit: y = -3.794x + 20.9
- P-value: 0.0161
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.019 
- Linear fit: y = 0.001x + 18.4
- P-value: 0.8706
- N samples: 78

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.414 ***
- Linear fit: y = -4.746x + 9.1
- P-value: 0.0002
- N samples: 78

**Benchmark Score:**
- Correlation: 0.102 
- Linear fit: y = 0.099x + 4.6
- P-value: 0.3735
- N samples: 78

**Model Size (B):**
- Correlation: 0.083 
- Linear fit: y = 0.000x + 7.0
- P-value: 0.4733
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.010 
- Linear fit: y = -0.110x + 7.4
- P-value: 0.9317
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.009 
- Linear fit: y = -0.000x + 7.5
- P-value: 0.9403
- N samples: 78

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.697, y = -0.486x + 18.8

**3b_self_contradiction vs Benchmark Score:**
  r = -0.665, y = -0.597x + 27.2

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.649, y = -0.789x + 40.9

**1a_instruction_override vs Benchmark Score:**
  r = -0.631, y = -0.479x + 24.3

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.572, y = -0.073x + 103.4

**total_hallucinations vs Benchmark Score:**
  r = -0.544, y = -5.469x + 433.9

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.535, y = -0.079x + 123.3

**category4_technical_errors vs Benchmark Score:**
  r = -0.495, y = -1.096x + 64.9

**category1_input_misalignment vs Benchmark Score:**
  r = -0.454, y = -1.896x + 127.8

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.453, y = -21.742x + 86.4

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.417, y = -17.101x + 117.8

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.414, y = -4.746x + 9.1

**1b_context_omission vs Is Reasoning Model:**
  r = -0.414, y = -17.166x + 67.7

**total_hallucinations vs Is Reasoning Model:**
  r = -0.410, y = -47.397x + 306.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.405, y = -0.406x + 19.5

**3b_self_contradiction vs Is Open Source:**
  r = 0.400, y = 4.242x + 9.0

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.379, y = -0.002x + 20.4

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.375, y = -13.452x + 105.1

**4b_model_semantics_breach vs Is Open Source:**
  r = 0.371, y = 5.313x + 16.9

**4a_syntax_error vs Is Open Source:**
  r = 0.358, y = 4.233x + 6.5

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.349, y = -3.608x + 12.5

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.343, y = -2.751x + 6.7

**3a_unsupported_leap vs Is Open Source:**
  r = -0.340, y = -12.508x + 102.9

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
- Correlation: -0.272 **
- Linear fit: y = -0.279x + 75.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.002 
- Linear fit: y = 0.002x + 106.6

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.030 
- Linear fit: y = 0.013x + 31.7

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.630 ***
- Linear fit: y = 0.473x + 81.2

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.529 ***
- Linear fit: y = 0.234x + 20.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.430 ***
- Linear fit: y = 0.254x + 5.7

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.971 ***, y = 0.845x + 5.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.965 ***, y = 0.819x + -3.1

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.931 ***, y = 0.507x + 2.2

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.919 ***, y = 0.459x + -1.5

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.825 ***, y = 0.452x + 3.5

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.733 ***, y = 0.318x + -2.7

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.717 ***, y = 0.783x + 11.4

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.630 ***, y = 0.473x + 81.2

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.615 ***, y = 0.117x + 4.4

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.603 ***, y = 0.153x + -5.6

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.602 ***, y = 0.211x + 4.5

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.595 ***, y = 0.509x + -0.4

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.592 ***, y = 0.430x + -16.3

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.577 ***, y = 0.760x + 6.6

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.575 ***, y = 0.731x + 10.5

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.574 ***, y = 0.382x + -17.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.569 ***, y = 0.099x + 4.0

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.566 ***, y = 0.244x + 2.8

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.556 ***, y = 0.083x + -0.9

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.553 ***, y = 0.034x + -0.8

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.410 ***, y = -0.030x + 2.9
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.407 ***, y = -0.337x + 78.4
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.382 ***, y = -0.230x + 37.1
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.351 ***, y = -0.231x + 43.5
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.324 ***, y = -0.020x + 2.7
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.272 **, y = -0.279x + 75.5
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.258 **, y = -0.132x + 33.5
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = -0.227 *, y = -0.126x + 39.4
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
