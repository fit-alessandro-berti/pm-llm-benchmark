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
- Correlation: -0.487 ***
- Linear fit: y = -2.277x + 139.4
- P-value: 0.0000
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.465 ***
- Linear fit: y = -24.030x + 89.0
- P-value: 0.0000
- N samples: 102

**Model Size (B):**
- Correlation: 0.131 
- Linear fit: y = 0.003x + 74.4
- P-value: 0.2034
- N samples: 96

**Is Open Source:**
- Correlation: -0.077 
- Linear fit: y = -3.949x + 77.4
- P-value: 0.4429
- N samples: 102

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.287 **
- Linear fit: y = -1.410x + 93.3
- P-value: 0.0035
- N samples: 102

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
- Correlation: 0.057 
- Linear fit: y = 3.106x + 52.4
- P-value: 0.5660
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -2.560x + 55.2
- P-value: 0.6381
- N samples: 102

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.413 ***
- Linear fit: y = -17.078x + 116.3
- P-value: 0.0000
- N samples: 102

**Is Open Source:**
- Correlation: -0.279 **
- Linear fit: y = -11.481x + 112.1
- P-value: 0.0045
- N samples: 102

**Benchmark Score:**
- Correlation: -0.226 *
- Linear fit: y = -0.845x + 130.4
- P-value: 0.0223
- N samples: 102

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
- Correlation: -0.529 ***
- Linear fit: y = -1.201x + 66.6
- P-value: 0.0000
- N samples: 102

**Model Size (B):**
- Correlation: -0.249 *
- Linear fit: y = -0.002x + 34.4
- P-value: 0.0143
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.223 *
- Linear fit: y = -5.601x + 36.0
- P-value: 0.0241
- N samples: 102

**Is Open Source:**
- Correlation: 0.055 
- Linear fit: y = 1.384x + 32.2
- P-value: 0.5798
- N samples: 102

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
- Correlation: -0.579 ***
- Linear fit: y = -6.218x + 452.5
- P-value: 0.0000
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.447 ***
- Linear fit: y = -53.007x + 307.9
- P-value: 0.0000
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: -0.135 
- Linear fit: y = -0.049x + 308.6
- P-value: 0.1819
- N samples: 99

**Is Open Source:**
- Correlation: -0.086 
- Linear fit: y = -10.104x + 283.0
- P-value: 0.3925
- N samples: 102

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
- Correlation: -0.487 ***
- Linear fit: y = -2.277x + 139.4
- P-value: 0.0000
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.465 ***
- Linear fit: y = -24.030x + 89.0
- P-value: 0.0000
- N samples: 102

**Model Size (B):**
- Correlation: 0.131 
- Linear fit: y = 0.003x + 74.4
- P-value: 0.2034
- N samples: 96

**Is Open Source:**
- Correlation: -0.077 
- Linear fit: y = -3.949x + 77.4
- P-value: 0.4429
- N samples: 102

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.287 **
- Linear fit: y = -1.410x + 93.3
- P-value: 0.0035
- N samples: 102

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
- Correlation: 0.057 
- Linear fit: y = 3.106x + 52.4
- P-value: 0.5660
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -2.560x + 55.2
- P-value: 0.6381
- N samples: 102

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.413 ***
- Linear fit: y = -17.078x + 116.3
- P-value: 0.0000
- N samples: 102

**Is Open Source:**
- Correlation: -0.279 **
- Linear fit: y = -11.481x + 112.1
- P-value: 0.0045
- N samples: 102

**Benchmark Score:**
- Correlation: -0.226 *
- Linear fit: y = -0.845x + 130.4
- P-value: 0.0223
- N samples: 102

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
- Correlation: -0.529 ***
- Linear fit: y = -1.201x + 66.6
- P-value: 0.0000
- N samples: 102

**Model Size (B):**
- Correlation: -0.249 *
- Linear fit: y = -0.002x + 34.4
- P-value: 0.0143
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.223 *
- Linear fit: y = -5.601x + 36.0
- P-value: 0.0241
- N samples: 102

**Is Open Source:**
- Correlation: 0.055 
- Linear fit: y = 1.384x + 32.2
- P-value: 0.5798
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: -0.011 
- Linear fit: y = -0.001x + 33.4
- P-value: 0.9127
- N samples: 99

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.633 ***
- Linear fit: y = -0.514x + 25.9
- P-value: 0.0000
- N samples: 102

**Is Open Source:**
- Correlation: 0.271 **
- Linear fit: y = 2.417x + 10.3
- P-value: 0.0059
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.247 *
- Linear fit: y = -2.220x + 12.7
- P-value: 0.0122
- N samples: 102

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
- Linear fit: y = -18.847x + 69.4
- P-value: 0.0000
- N samples: 102

**Benchmark Score:**
- Correlation: -0.312 **
- Linear fit: y = -1.257x + 94.1
- P-value: 0.0014
- N samples: 102

**Is Open Source:**
- Correlation: -0.180 
- Linear fit: y = -7.970x + 62.6
- P-value: 0.0705
- N samples: 102

**Model Size (B):**
- Correlation: 0.151 
- Linear fit: y = 0.003x + 57.8
- P-value: 0.1432
- N samples: 96

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.713 ***
- Linear fit: y = -0.506x + 19.4
- P-value: 0.0000
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.377 ***
- Linear fit: y = -2.964x + 6.9
- P-value: 0.0001
- N samples: 102

**Is Open Source:**
- Correlation: 0.205 *
- Linear fit: y = 1.604x + 4.5
- P-value: 0.0384
- N samples: 102

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
- Correlation: -0.254 **
- Linear fit: y = -0.631x + 41.2
- P-value: 0.0099
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: 0.237 *
- Linear fit: y = 0.020x + 10.8
- P-value: 0.0180
- N samples: 99

**Is Open Source:**
- Correlation: 0.047 
- Linear fit: y = 1.296x + 22.9
- P-value: 0.6357
- N samples: 102

**Model Size (B):**
- Correlation: 0.002 
- Linear fit: y = 0.000x + 23.0
- P-value: 0.9820
- N samples: 96

**Is Reasoning Model:**
- Correlation: 0.001 
- Linear fit: y = 0.025x + 23.5
- P-value: 0.9929
- N samples: 102

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.281 **
- Linear fit: y = -0.758x + 50.5
- P-value: 0.0042
- N samples: 102

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.001x + 30.1
- P-value: 0.2302
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.094 
- Linear fit: y = -2.796x + 30.9
- P-value: 0.3479
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: 0.084 
- Linear fit: y = 0.008x + 24.5
- P-value: 0.4098
- N samples: 99

**Is Open Source:**
- Correlation: 0.050 
- Linear fit: y = 1.472x + 28.6
- P-value: 0.6199
- N samples: 102

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.123 
- Linear fit: y = 0.001x + 0.3
- P-value: 0.2235
- N samples: 99

**Is Open Source:**
- Correlation: 0.110 
- Linear fit: y = 0.338x + 0.9
- P-value: 0.2701
- N samples: 102

**Model Size (B):**
- Correlation: -0.080 
- Linear fit: y = -0.000x + 1.1
- P-value: 0.4380
- N samples: 96

**Benchmark Score:**
- Correlation: -0.074 
- Linear fit: y = -0.021x + 1.6
- P-value: 0.4606
- N samples: 102

**Is Reasoning Model:**
- Correlation: 0.069 
- Linear fit: y = 0.212x + 0.9
- P-value: 0.4928
- N samples: 102

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.408 ***
- Linear fit: y = -14.509x + 102.9
- P-value: 0.0000
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.363 ***
- Linear fit: y = -12.987x + 103.4
- P-value: 0.0002
- N samples: 102

**Model Size (B):**
- Correlation: 0.208 *
- Linear fit: y = 0.003x + 93.9
- P-value: 0.0425
- N samples: 96

**Benchmark Score:**
- Correlation: -0.072 
- Linear fit: y = -0.233x + 102.6
- P-value: 0.4712
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: 0.032 
- Linear fit: y = 0.004x + 93.8
- P-value: 0.7505
- N samples: 99

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.648 ***
- Linear fit: y = -0.599x + 27.3
- P-value: 0.0000
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.396 ***
- Linear fit: y = -4.046x + 12.8
- P-value: 0.0000
- N samples: 102

**Is Open Source:**
- Correlation: 0.295 **
- Linear fit: y = 2.995x + 9.1
- P-value: 0.0026
- N samples: 102

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
- Correlation: -0.224 *
- Linear fit: y = -0.013x + 0.5
- P-value: 0.0238
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: -0.077 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.4485
- N samples: 99

**Is Reasoning Model:**
- Correlation: -0.073 
- Linear fit: y = -0.046x + 0.1
- P-value: 0.4658
- N samples: 102

**Model Size (B):**
- Correlation: 0.070 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.4981
- N samples: 96

**Is Open Source:**
- Correlation: 0.052 
- Linear fit: y = 0.032x + 0.1
- P-value: 0.6027
- N samples: 102

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.443 ***
- Linear fit: y = -0.432x + 19.8
- P-value: 0.0000
- N samples: 102

**Model Size (B):**
- Correlation: -0.266 **
- Linear fit: y = -0.001x + 8.4
- P-value: 0.0087
- N samples: 96

**Is Open Source:**
- Correlation: 0.264 **
- Linear fit: y = 2.836x + 6.4
- P-value: 0.0073
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.056 
- Linear fit: y = -0.601x + 8.0
- P-value: 0.5778
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: 0.041 
- Linear fit: y = 0.001x + 6.8
- P-value: 0.6893
- N samples: 99

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.642 ***
- Linear fit: y = -0.789x + 40.3
- P-value: 0.0000
- N samples: 102

**Model Size (B):**
- Correlation: -0.330 **
- Linear fit: y = -0.002x + 19.4
- P-value: 0.0010
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.314 **
- Linear fit: y = -4.267x + 20.6
- P-value: 0.0013
- N samples: 102

**Is Open Source:**
- Correlation: 0.241 *
- Linear fit: y = 3.252x + 16.7
- P-value: 0.0149
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: -0.003 
- Linear fit: y = -0.000x + 18.4
- P-value: 0.9769
- N samples: 99

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.433 ***
- Linear fit: y = -4.704x + 9.2
- P-value: 0.0000
- N samples: 102

**Model Size (B):**
- Correlation: 0.108 
- Linear fit: y = 0.000x + 6.6
- P-value: 0.2957
- N samples: 96

**Is Reasoning Model:**
- Correlation: -0.067 
- Linear fit: y = -0.733x + 7.4
- P-value: 0.5022
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: -0.063 
- Linear fit: y = -0.002x + 8.2
- P-value: 0.5346
- N samples: 99

**Benchmark Score:**
- Correlation: 0.020 
- Linear fit: y = 0.020x + 6.4
- P-value: 0.8394
- N samples: 102

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.713, y = -0.506x + 19.4

**3b_self_contradiction vs Benchmark Score:**
  r = -0.648, y = -0.599x + 27.3

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.642, y = -0.789x + 40.3

**1a_instruction_override vs Benchmark Score:**
  r = -0.633, y = -0.514x + 25.9

**total_hallucinations vs Benchmark Score:**
  r = -0.579, y = -6.218x + 452.5

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.532, y = -0.074x + 104.8

**category4_technical_errors vs Benchmark Score:**
  r = -0.529, y = -1.201x + 66.6

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.507, y = -0.081x + 126.3

**category1_input_misalignment vs Benchmark Score:**
  r = -0.487, y = -2.277x + 139.4

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.465, y = -24.030x + 89.0

**total_hallucinations vs Is Reasoning Model:**
  r = -0.447, y = -53.007x + 307.9

**4a_syntax_error vs Benchmark Score:**
  r = -0.443, y = -0.432x + 19.8

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.433, y = -4.704x + 9.2

**1b_context_omission vs Is Reasoning Model:**
  r = -0.423, y = -18.847x + 69.4

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.413, y = -17.078x + 116.3

**3a_unsupported_leap vs Is Open Source:**
  r = -0.408, y = -14.509x + 102.9

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.396, y = -4.046x + 12.8

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.377, y = -2.964x + 6.9

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.363, y = -12.987x + 103.4

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.330, y = -0.002x + 19.4

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.314, y = -4.267x + 20.6

**1b_context_omission vs Benchmark Score:**
  r = -0.312, y = -1.257x + 94.1


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
- Correlation: -0.257 **
- Linear fit: y = -0.265x + 74.6

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.014 
- Linear fit: y = 0.011x + 106.0

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.046 
- Linear fit: y = 0.021x + 31.2

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.635 ***
- Linear fit: y = 0.476x + 81.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.539 ***
- Linear fit: y = 0.242x + 19.7

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.449 ***
- Linear fit: y = 0.269x + 4.1

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.971 ***, y = 0.840x + 6.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.963 ***, y = 0.818x + -3.2

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.929 ***, y = 0.506x + 2.2

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.918 ***, y = 0.461x + -1.4

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.824 ***, y = 0.449x + 3.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.721 ***, y = 0.311x + -2.5

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.710 ***, y = 0.770x + 11.4

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.635 ***, y = 0.476x + 81.0

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.618 ***, y = 0.119x + 4.4

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.612 ***, y = 0.158x + -6.0

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.606 ***, y = 0.215x + 4.5

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.598 ***, y = 0.434x + -16.8

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.586 ***, y = 0.502x + -0.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.582 ***, y = 0.250x + 2.7

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.580 ***, y = 0.734x + 10.3

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.576 ***, y = 0.385x + -17.6

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.570 ***, y = 0.750x + 6.8

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.556 ***, y = 0.098x + 4.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.555 ***, y = 0.084x + -1.0

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.552 ***, y = 0.034x + -0.7

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.411 ***, y = -0.031x + 2.9
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.399 ***, y = -0.328x + 77.4
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.377 ***, y = -0.230x + 37.3
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.339 ***, y = -0.224x + 43.0
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.320 ***, y = -0.020x + 2.7
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.257 **, y = -0.265x + 74.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.245 *, y = -0.127x + 33.3
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = -0.210 *, y = -0.118x + 38.7
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
