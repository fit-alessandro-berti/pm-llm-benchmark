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
- Correlation: -0.507 ***
- Linear fit: y = -0.081x + 126.3
- P-value: 0.0000
- N samples: 99

**Benchmark Score:**
- Correlation: -0.483 ***
- Linear fit: y = -2.275x + 139.6
- P-value: 0.0000
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.463 ***
- Linear fit: y = -24.145x + 89.2
- P-value: 0.0000
- N samples: 99

**Model Size (B):**
- Correlation: 0.131 
- Linear fit: y = 0.003x + 74.4
- P-value: 0.2034
- N samples: 96

**Is Open Source:**
- Correlation: -0.069 
- Linear fit: y = -3.607x + 77.4
- P-value: 0.4956
- N samples: 99

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.270 **
- Linear fit: y = -1.328x + 90.9
- P-value: 0.0069
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: 0.173 
- Linear fit: y = 0.029x + 35.6
- P-value: 0.0867
- N samples: 99

**Model Size (B):**
- Correlation: -0.072 
- Linear fit: y = -0.001x + 54.2
- P-value: 0.4867
- N samples: 96

**Is Open Source:**
- Correlation: 0.052 
- Linear fit: y = 2.804x + 52.4
- P-value: 0.6122
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.033 
- Linear fit: y = -1.777x + 54.6
- P-value: 0.7485
- N samples: 99

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.408 ***
- Linear fit: y = -16.927x + 116.1
- P-value: 0.0000
- N samples: 99

**Is Open Source:**
- Correlation: -0.291 **
- Linear fit: y = -12.015x + 112.1
- P-value: 0.0035
- N samples: 99

**Benchmark Score:**
- Correlation: -0.207 *
- Linear fit: y = -0.776x + 128.4
- P-value: 0.0395
- N samples: 99

**Model Size (B):**
- Correlation: 0.118 
- Linear fit: y = 0.002x + 105.1
- P-value: 0.2527
- N samples: 96

**Days Since 2024-01-01:**
- Correlation: 0.038 
- Linear fit: y = 0.005x + 103.7
- P-value: 0.7073
- N samples: 99

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.514 ***
- Linear fit: y = -1.154x + 65.2
- P-value: 0.0000
- N samples: 99

**Model Size (B):**
- Correlation: -0.249 *
- Linear fit: y = -0.002x + 34.4
- P-value: 0.0143
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.205 *
- Linear fit: y = -5.109x + 35.7
- P-value: 0.0413
- N samples: 99

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 1.426x + 32.2
- P-value: 0.5720
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: -0.011 
- Linear fit: y = -0.001x + 33.4
- P-value: 0.9127
- N samples: 99

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.565 ***
- Linear fit: y = -6.008x + 446.7
- P-value: 0.0000
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.437 ***
- Linear fit: y = -51.386x + 306.8
- P-value: 0.0000
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: -0.135 
- Linear fit: y = -0.049x + 308.6
- P-value: 0.1819
- N samples: 99

**Is Open Source:**
- Correlation: -0.090 
- Linear fit: y = -10.556x + 283.0
- P-value: 0.3762
- N samples: 99

**Model Size (B):**
- Correlation: 0.006 
- Linear fit: y = 0.000x + 277.7
- P-value: 0.9572
- N samples: 96

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.507 ***
- Linear fit: y = -0.081x + 126.3
- P-value: 0.0000
- N samples: 99

**Benchmark Score:**
- Correlation: -0.483 ***
- Linear fit: y = -2.275x + 139.6
- P-value: 0.0000
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.463 ***
- Linear fit: y = -24.145x + 89.2
- P-value: 0.0000
- N samples: 99

**Model Size (B):**
- Correlation: 0.131 
- Linear fit: y = 0.003x + 74.4
- P-value: 0.2034
- N samples: 96

**Is Open Source:**
- Correlation: -0.069 
- Linear fit: y = -3.607x + 77.4
- P-value: 0.4956
- N samples: 99

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.270 **
- Linear fit: y = -1.328x + 90.9
- P-value: 0.0069
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: 0.173 
- Linear fit: y = 0.029x + 35.6
- P-value: 0.0867
- N samples: 99

**Model Size (B):**
- Correlation: -0.072 
- Linear fit: y = -0.001x + 54.2
- P-value: 0.4867
- N samples: 96

**Is Open Source:**
- Correlation: 0.052 
- Linear fit: y = 2.804x + 52.4
- P-value: 0.6122
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.033 
- Linear fit: y = -1.777x + 54.6
- P-value: 0.7485
- N samples: 99

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.408 ***
- Linear fit: y = -16.927x + 116.1
- P-value: 0.0000
- N samples: 99

**Is Open Source:**
- Correlation: -0.291 **
- Linear fit: y = -12.015x + 112.1
- P-value: 0.0035
- N samples: 99

**Benchmark Score:**
- Correlation: -0.207 *
- Linear fit: y = -0.776x + 128.4
- P-value: 0.0395
- N samples: 99

**Model Size (B):**
- Correlation: 0.118 
- Linear fit: y = 0.002x + 105.1
- P-value: 0.2527
- N samples: 96

**Days Since 2024-01-01:**
- Correlation: 0.038 
- Linear fit: y = 0.005x + 103.7
- P-value: 0.7073
- N samples: 99

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.514 ***
- Linear fit: y = -1.154x + 65.2
- P-value: 0.0000
- N samples: 99

**Model Size (B):**
- Correlation: -0.249 *
- Linear fit: y = -0.002x + 34.4
- P-value: 0.0143
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.205 *
- Linear fit: y = -5.109x + 35.7
- P-value: 0.0413
- N samples: 99

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 1.426x + 32.2
- P-value: 0.5720
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: -0.011 
- Linear fit: y = -0.001x + 33.4
- P-value: 0.9127
- N samples: 99

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.632 ***
- Linear fit: y = -0.513x + 25.8
- P-value: 0.0000
- N samples: 99

**Is Open Source:**
- Correlation: 0.263 **
- Linear fit: y = 2.356x + 10.3
- P-value: 0.0086
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.256 *
- Linear fit: y = -2.300x + 12.7
- P-value: 0.0105
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: -0.115 
- Linear fit: y = -0.003x + 13.4
- P-value: 0.2576
- N samples: 99

**Model Size (B):**
- Correlation: 0.096 
- Linear fit: y = 0.000x + 11.1
- P-value: 0.3544
- N samples: 96

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.532 ***
- Linear fit: y = -0.074x + 104.8
- P-value: 0.0000
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.423 ***
- Linear fit: y = -19.014x + 69.7
- P-value: 0.0000
- N samples: 99

**Benchmark Score:**
- Correlation: -0.311 **
- Linear fit: y = -1.265x + 94.6
- P-value: 0.0017
- N samples: 99

**Is Open Source:**
- Correlation: -0.168 
- Linear fit: y = -7.552x + 62.6
- P-value: 0.0961
- N samples: 99

**Model Size (B):**
- Correlation: 0.151 
- Linear fit: y = 0.003x + 57.8
- P-value: 0.1432
- N samples: 96

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.706 ***
- Linear fit: y = -0.497x + 19.2
- P-value: 0.0000
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.363 ***
- Linear fit: y = -2.832x + 6.8
- P-value: 0.0002
- N samples: 99

**Is Open Source:**
- Correlation: 0.204 *
- Linear fit: y = 1.589x + 4.5
- P-value: 0.0427
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: -0.191 
- Linear fit: y = -0.005x + 8.1
- P-value: 0.0579
- N samples: 99

**Model Size (B):**
- Correlation: -0.101 
- Linear fit: y = -0.000x + 5.5
- P-value: 0.3286
- N samples: 96

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.241 *
- Linear fit: y = -0.599x + 40.1
- P-value: 0.0165
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: 0.237 *
- Linear fit: y = 0.020x + 10.8
- P-value: 0.0180
- N samples: 99

**Is Open Source:**
- Correlation: 0.037 
- Linear fit: y = 1.019x + 22.9
- P-value: 0.7161
- N samples: 99

**Is Reasoning Model:**
- Correlation: 0.017 
- Linear fit: y = 0.477x + 23.1
- P-value: 0.8650
- N samples: 99

**Model Size (B):**
- Correlation: 0.002 
- Linear fit: y = 0.000x + 23.0
- P-value: 0.9820
- N samples: 96

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.263 **
- Linear fit: y = -0.708x + 49.2
- P-value: 0.0085
- N samples: 99

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.001x + 30.1
- P-value: 0.2302
- N samples: 96

**Days Since 2024-01-01:**
- Correlation: 0.084 
- Linear fit: y = 0.008x + 24.5
- P-value: 0.4098
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.082 
- Linear fit: y = -2.459x + 30.7
- P-value: 0.4170
- N samples: 99

**Is Open Source:**
- Correlation: 0.050 
- Linear fit: y = 1.500x + 28.6
- P-value: 0.6202
- N samples: 99

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.123 
- Linear fit: y = 0.001x + 0.3
- P-value: 0.2235
- N samples: 99

**Is Open Source:**
- Correlation: 0.092 
- Linear fit: y = 0.285x + 0.9
- P-value: 0.3652
- N samples: 99

**Model Size (B):**
- Correlation: -0.080 
- Linear fit: y = -0.000x + 1.1
- P-value: 0.4380
- N samples: 96

**Benchmark Score:**
- Correlation: -0.074 
- Linear fit: y = -0.021x + 1.6
- P-value: 0.4653
- N samples: 99

**Is Reasoning Model:**
- Correlation: 0.066 
- Linear fit: y = 0.205x + 0.9
- P-value: 0.5174
- N samples: 99

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.420 ***
- Linear fit: y = -15.104x + 102.9
- P-value: 0.0000
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.358 ***
- Linear fit: y = -12.900x + 103.2
- P-value: 0.0003
- N samples: 99

**Model Size (B):**
- Correlation: 0.208 *
- Linear fit: y = 0.003x + 93.9
- P-value: 0.0425
- N samples: 96

**Benchmark Score:**
- Correlation: -0.055 
- Linear fit: y = -0.178x + 101.1
- P-value: 0.5904
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: 0.032 
- Linear fit: y = 0.004x + 93.8
- P-value: 0.7505
- N samples: 99

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.638 ***
- Linear fit: y = -0.585x + 26.9
- P-value: 0.0000
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.392 ***
- Linear fit: y = -3.982x + 12.7
- P-value: 0.0001
- N samples: 99

**Is Open Source:**
- Correlation: 0.301 **
- Linear fit: y = 3.048x + 9.1
- P-value: 0.0025
- N samples: 99

**Model Size (B):**
- Correlation: -0.262 **
- Linear fit: y = -0.001x + 11.1
- P-value: 0.0100
- N samples: 96

**Days Since 2024-01-01:**
- Correlation: 0.046 
- Linear fit: y = 0.001x + 9.6
- P-value: 0.6514
- N samples: 99

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.228 *
- Linear fit: y = -0.013x + 0.5
- P-value: 0.0235
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: -0.077 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.4485
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.072 
- Linear fit: y = -0.045x + 0.1
- P-value: 0.4796
- N samples: 99

**Model Size (B):**
- Correlation: 0.070 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.4981
- N samples: 96

**Is Open Source:**
- Correlation: 0.065 
- Linear fit: y = 0.041x + 0.1
- P-value: 0.5256
- N samples: 99

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.436 ***
- Linear fit: y = -0.427x + 19.6
- P-value: 0.0000
- N samples: 99

**Is Open Source:**
- Correlation: 0.267 **
- Linear fit: y = 2.893x + 6.4
- P-value: 0.0075
- N samples: 99

**Model Size (B):**
- Correlation: -0.266 **
- Linear fit: y = -0.001x + 8.4
- P-value: 0.0087
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.055 
- Linear fit: y = -0.600x + 8.0
- P-value: 0.5863
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: 0.041 
- Linear fit: y = 0.001x + 6.8
- P-value: 0.6893
- N samples: 99

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.638 ***
- Linear fit: y = -0.783x + 40.3
- P-value: 0.0000
- N samples: 99

**Model Size (B):**
- Correlation: -0.330 **
- Linear fit: y = -0.002x + 19.4
- P-value: 0.0010
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.298 **
- Linear fit: y = -4.041x + 20.6
- P-value: 0.0028
- N samples: 99

**Is Open Source:**
- Correlation: 0.266 **
- Linear fit: y = 3.604x + 16.7
- P-value: 0.0078
- N samples: 99

**Days Since 2024-01-01:**
- Correlation: -0.003 
- Linear fit: y = -0.000x + 18.4
- P-value: 0.9769
- N samples: 99

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.473 ***
- Linear fit: y = -5.070x + 9.2
- P-value: 0.0000
- N samples: 99

**Model Size (B):**
- Correlation: 0.108 
- Linear fit: y = 0.000x + 6.6
- P-value: 0.2957
- N samples: 96

**Days Since 2024-01-01:**
- Correlation: -0.063 
- Linear fit: y = -0.002x + 8.2
- P-value: 0.5346
- N samples: 99

**Benchmark Score:**
- Correlation: 0.058 
- Linear fit: y = 0.057x + 5.3
- P-value: 0.5653
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.044 
- Linear fit: y = -0.468x + 7.2
- P-value: 0.6684
- N samples: 99

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.706, y = -0.497x + 19.2

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.638, y = -0.783x + 40.3

**3b_self_contradiction vs Benchmark Score:**
  r = -0.638, y = -0.585x + 26.9

**1a_instruction_override vs Benchmark Score:**
  r = -0.632, y = -0.513x + 25.8

**total_hallucinations vs Benchmark Score:**
  r = -0.565, y = -6.008x + 446.7

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.532, y = -0.074x + 104.8

**category4_technical_errors vs Benchmark Score:**
  r = -0.514, y = -1.154x + 65.2

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.507, y = -0.081x + 126.3

**category1_input_misalignment vs Benchmark Score:**
  r = -0.483, y = -2.275x + 139.6

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.473, y = -5.070x + 9.2

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.463, y = -24.145x + 89.2

**total_hallucinations vs Is Reasoning Model:**
  r = -0.437, y = -51.386x + 306.8

**4a_syntax_error vs Benchmark Score:**
  r = -0.436, y = -0.427x + 19.6

**1b_context_omission vs Is Reasoning Model:**
  r = -0.423, y = -19.014x + 69.7

**3a_unsupported_leap vs Is Open Source:**
  r = -0.420, y = -15.104x + 102.9

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.408, y = -16.927x + 116.1

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.392, y = -3.982x + 12.7

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.363, y = -2.832x + 6.8

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.358, y = -12.900x + 103.2

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.330, y = -0.002x + 19.4

**1b_context_omission vs Benchmark Score:**
  r = -0.311, y = -1.265x + 94.6

**3b_self_contradiction vs Is Open Source:**
  r = 0.301, y = 3.048x + 9.1


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
- Correlation: -0.270 **
- Linear fit: y = -0.277x + 75.4

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.003 
- Linear fit: y = 0.002x + 106.6

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.031 
- Linear fit: y = 0.014x + 31.7

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.627 ***
- Linear fit: y = 0.470x + 81.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.526 ***
- Linear fit: y = 0.233x + 20.2

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.433 ***
- Linear fit: y = 0.256x + 5.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.971 ***, y = 0.844x + 5.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.964 ***, y = 0.818x + -3.2

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.928 ***, y = 0.504x + 2.3

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.918 ***, y = 0.461x + -1.5

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.826 ***, y = 0.453x + 3.5

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.722 ***, y = 0.316x + -2.7

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.710 ***, y = 0.767x + 11.6

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.627 ***, y = 0.470x + 81.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.609 ***, y = 0.117x + 4.6

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.602 ***, y = 0.154x + -5.6

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.595 ***, y = 0.210x + 4.7

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.589 ***, y = 0.427x + -16.0

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.588 ***, y = 0.500x + -0.4

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.577 ***, y = 0.732x + 10.4

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.570 ***, y = 0.382x + -17.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.566 ***, y = 0.245x + 2.8

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.560 ***, y = 0.098x + 4.1

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.559 ***, y = 0.736x + 6.8

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.557 ***, y = 0.034x + -0.8

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.556 ***, y = 0.083x + -1.0

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.407 ***, y = -0.337x + 78.2
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2c: False Citation:**
  r = -0.407 ***, y = -0.030x + 2.9
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.381 ***, y = -0.232x + 37.3
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.351 ***, y = -0.230x + 43.4
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.318 **, y = -0.020x + 2.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.270 **, y = -0.277x + 75.4
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.253 **, y = -0.131x + 33.5
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = -0.226 *, y = -0.126x + 39.3
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
