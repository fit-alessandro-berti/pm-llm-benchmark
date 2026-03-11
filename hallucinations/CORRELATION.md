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

**Benchmark Score:**
- Correlation: -0.794 ***
- Linear fit: y = -2.477x + 129.7
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.550 ***
- Linear fit: y = -22.092x + 48.9
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.273 *
- Linear fit: y = 11.224x + 33.0
- P-value: 0.0165
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.230 *
- Linear fit: y = -0.028x + 54.8
- P-value: 0.0440
- N samples: 77

**Model Size (B):**
- Correlation: -0.127 
- Linear fit: y = -0.002x + 39.0
- P-value: 0.2727
- N samples: 76

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.544 ***
- Linear fit: y = -1.624x + 88.7
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.325 **
- Linear fit: y = 12.809x + 23.2
- P-value: 0.0039
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.317 **
- Linear fit: y = -12.189x + 34.5
- P-value: 0.0050
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.293 **
- Linear fit: y = 0.035x + 7.0
- P-value: 0.0097
- N samples: 77

**Model Size (B):**
- Correlation: -0.157 
- Linear fit: y = -0.002x + 29.5
- P-value: 0.1745
- N samples: 76

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.761 ***
- Linear fit: y = -3.741x + 205.8
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.641 ***
- Linear fit: y = -40.632x + 87.4
- P-value: 0.0000
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.242 *
- Linear fit: y = -0.047x + 95.1
- P-value: 0.0341
- N samples: 77

**Is Open Source:**
- Correlation: 0.185 
- Linear fit: y = 12.028x + 61.6
- P-value: 0.1067
- N samples: 77

**Model Size (B):**
- Correlation: -0.098 
- Linear fit: y = -0.002x + 67.8
- P-value: 0.3982
- N samples: 76

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.726 ***
- Linear fit: y = -1.595x + 78.7
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.385 ***
- Linear fit: y = 11.173x + 14.9
- P-value: 0.0005
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.242 *
- Linear fit: y = -6.861x + 22.8
- P-value: 0.0338
- N samples: 77

**Model Size (B):**
- Correlation: -0.195 
- Linear fit: y = -0.002x + 20.7
- P-value: 0.0910
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.083 
- Linear fit: y = 0.007x + 14.9
- P-value: 0.4755
- N samples: 77

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.813 ***
- Linear fit: y = -10.137x + 535.8
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.549 ***
- Linear fit: y = -88.257x + 203.8
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.313 **
- Linear fit: y = 51.537x + 137.8
- P-value: 0.0056
- N samples: 77

**Model Size (B):**
- Correlation: -0.156 
- Linear fit: y = -0.009x + 164.4
- P-value: 0.1776
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.067 
- Linear fit: y = -0.033x + 178.3
- P-value: 0.5603
- N samples: 77

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.794 ***
- Linear fit: y = -2.477x + 129.7
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.550 ***
- Linear fit: y = -22.092x + 48.9
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.273 *
- Linear fit: y = 11.224x + 33.0
- P-value: 0.0165
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.230 *
- Linear fit: y = -0.028x + 54.8
- P-value: 0.0440
- N samples: 77

**Model Size (B):**
- Correlation: -0.127 
- Linear fit: y = -0.002x + 39.0
- P-value: 0.2727
- N samples: 76

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.544 ***
- Linear fit: y = -1.624x + 88.7
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.325 **
- Linear fit: y = 12.809x + 23.2
- P-value: 0.0039
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.317 **
- Linear fit: y = -12.189x + 34.5
- P-value: 0.0050
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.293 **
- Linear fit: y = 0.035x + 7.0
- P-value: 0.0097
- N samples: 77

**Model Size (B):**
- Correlation: -0.157 
- Linear fit: y = -0.002x + 29.5
- P-value: 0.1745
- N samples: 76

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.761 ***
- Linear fit: y = -3.741x + 205.8
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.641 ***
- Linear fit: y = -40.632x + 87.4
- P-value: 0.0000
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.242 *
- Linear fit: y = -0.047x + 95.1
- P-value: 0.0341
- N samples: 77

**Is Open Source:**
- Correlation: 0.185 
- Linear fit: y = 12.028x + 61.6
- P-value: 0.1067
- N samples: 77

**Model Size (B):**
- Correlation: -0.098 
- Linear fit: y = -0.002x + 67.8
- P-value: 0.3982
- N samples: 76

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.726 ***
- Linear fit: y = -1.595x + 78.7
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.385 ***
- Linear fit: y = 11.173x + 14.9
- P-value: 0.0005
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.242 *
- Linear fit: y = -6.861x + 22.8
- P-value: 0.0338
- N samples: 77

**Model Size (B):**
- Correlation: -0.195 
- Linear fit: y = -0.002x + 20.7
- P-value: 0.0910
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.083 
- Linear fit: y = 0.007x + 14.9
- P-value: 0.4755
- N samples: 77

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.603 ***
- Linear fit: y = -0.496x + 26.6
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.390 ***
- Linear fit: y = 4.232x + 6.5
- P-value: 0.0005
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.357 **
- Linear fit: y = -3.781x + 10.1
- P-value: 0.0015
- N samples: 77

**Model Size (B):**
- Correlation: -0.167 
- Linear fit: y = -0.001x + 8.6
- P-value: 0.1489
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.151 
- Linear fit: y = 0.005x + 5.1
- P-value: 0.1886
- N samples: 77

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.713 ***
- Linear fit: y = -1.574x + 83.7
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.537 ***
- Linear fit: y = -15.296x + 32.9
- P-value: 0.0000
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.437 ***
- Linear fit: y = -0.038x + 48.4
- P-value: 0.0001
- N samples: 77

**Is Open Source:**
- Correlation: 0.103 
- Linear fit: y = 3.004x + 23.8
- P-value: 0.3727
- N samples: 77

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.001x + 25.6
- P-value: 0.6058
- N samples: 76

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.703 ***
- Linear fit: y = -0.407x + 19.5
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.522 ***
- Linear fit: y = 3.989x + 2.7
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.404 ***
- Linear fit: y = -3.015x + 5.9
- P-value: 0.0003
- N samples: 77

**Model Size (B):**
- Correlation: -0.218 
- Linear fit: y = -0.001x + 4.8
- P-value: 0.0582
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.213 
- Linear fit: y = 0.005x + 1.3
- P-value: 0.0631
- N samples: 77

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.622 ***
- Linear fit: y = -0.810x + 38.3
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.336 **
- Linear fit: y = 5.773x + 5.9
- P-value: 0.0028
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.266 *
- Linear fit: y = -4.459x + 10.5
- P-value: 0.0195
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.206 
- Linear fit: y = 0.011x + 1.6
- P-value: 0.0722
- N samples: 77

**Model Size (B):**
- Correlation: -0.100 
- Linear fit: y = -0.001x + 8.6
- P-value: 0.3899
- N samples: 76

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.415 ***
- Linear fit: y = -0.784x + 49.0
- P-value: 0.0002
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.316 **
- Linear fit: y = -7.709x + 23.8
- P-value: 0.0051
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.310 **
- Linear fit: y = 0.023x + 5.6
- P-value: 0.0060
- N samples: 77

**Is Open Source:**
- Correlation: 0.272 *
- Linear fit: y = 6.806x + 17.1
- P-value: 0.0165
- N samples: 77

**Model Size (B):**
- Correlation: -0.173 
- Linear fit: y = -0.001x + 20.6
- P-value: 0.1352
- N samples: 76

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.264 *
- Linear fit: y = -0.029x + 1.3
- P-value: 0.0205
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.175 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.1280
- N samples: 77

**Is Open Source:**
- Correlation: 0.158 
- Linear fit: y = 0.230x + 0.2
- P-value: 0.1703
- N samples: 77

**Model Size (B):**
- Correlation: -0.128 
- Linear fit: y = -0.000x + 0.3
- P-value: 0.2696
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.014 
- Linear fit: y = -0.020x + 0.3
- P-value: 0.9020
- N samples: 77

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.739 ***
- Linear fit: y = -3.040x + 170.7
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.641 ***
- Linear fit: y = -33.952x + 75.0
- P-value: 0.0000
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: -0.322 **
- Linear fit: y = -0.052x + 89.4
- P-value: 0.0043
- N samples: 77

**Is Open Source:**
- Correlation: 0.140 
- Linear fit: y = 7.608x + 54.4
- P-value: 0.2242
- N samples: 77

**Model Size (B):**
- Correlation: -0.076 
- Linear fit: y = -0.001x + 58.3
- P-value: 0.5165
- N samples: 76

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.695 ***
- Linear fit: y = -0.672x + 33.7
- P-value: 0.0000
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.516 ***
- Linear fit: y = -6.429x + 12.1
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.323 **
- Linear fit: y = 4.127x + 7.1
- P-value: 0.0041
- N samples: 77

**Model Size (B):**
- Correlation: -0.178 
- Linear fit: y = -0.001x + 9.2
- P-value: 0.1237
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.133 
- Linear fit: y = 0.005x + 5.6
- P-value: 0.2481
- N samples: 77

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.389 ***
- Linear fit: y = -0.030x + 1.3
- P-value: 0.0005
- N samples: 77

**Is Open Source:**
- Correlation: 0.286 *
- Linear fit: y = 0.294x + 0.1
- P-value: 0.0116
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.251 *
- Linear fit: y = -0.251x + 0.4
- P-value: 0.0276
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.056 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.6293
- N samples: 77

**Model Size (B):**
- Correlation: -0.014 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.9060
- N samples: 76

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.650 ***
- Linear fit: y = -0.674x + 30.5
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.470 ***
- Linear fit: y = 6.440x + 2.9
- P-value: 0.0000
- N samples: 77

**Model Size (B):**
- Correlation: -0.244 *
- Linear fit: y = -0.001x + 6.3
- P-value: 0.0335
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.190 
- Linear fit: y = 0.008x + 0.6
- P-value: 0.0977
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.160 
- Linear fit: y = -2.139x + 6.5
- P-value: 0.1647
- N samples: 77

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.776 ***
- Linear fit: y = -0.833x + 40.7
- P-value: 0.0000
- N samples: 77

**Is Open Source:**
- Correlation: 0.375 ***
- Linear fit: y = 5.316x + 7.6
- P-value: 0.0008
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.310 **
- Linear fit: y = -4.294x + 11.9
- P-value: 0.0060
- N samples: 77

**Model Size (B):**
- Correlation: -0.250 *
- Linear fit: y = -0.001x + 10.6
- P-value: 0.0294
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.026 
- Linear fit: y = -0.001x + 10.4
- P-value: 0.8243
- N samples: 77

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.171 
- Linear fit: y = 0.000x + 3.8
- P-value: 0.1395
- N samples: 76

**Benchmark Score:**
- Correlation: -0.161 
- Linear fit: y = -0.088x + 7.5
- P-value: 0.1621
- N samples: 77

**Is Open Source:**
- Correlation: -0.080 
- Linear fit: y = -0.583x + 4.4
- P-value: 0.4873
- N samples: 77

**Is Reasoning Model:**
- Correlation: -0.060 
- Linear fit: y = -0.428x + 4.4
- P-value: 0.6013
- N samples: 77

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 3.9
- P-value: 0.8537
- N samples: 77

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.813, y = -10.137x + 535.8

**category1_input_misalignment vs Benchmark Score:**
  r = -0.794, y = -2.477x + 129.7

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.776, y = -0.833x + 40.7

**category3_logical_errors vs Benchmark Score:**
  r = -0.761, y = -3.741x + 205.8

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.739, y = -3.040x + 170.7

**category4_technical_errors vs Benchmark Score:**
  r = -0.726, y = -1.595x + 78.7

**1b_context_omission vs Benchmark Score:**
  r = -0.713, y = -1.574x + 83.7

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.703, y = -0.407x + 19.5

**3b_self_contradiction vs Benchmark Score:**
  r = -0.695, y = -0.672x + 33.7

**4a_syntax_error vs Benchmark Score:**
  r = -0.650, y = -0.674x + 30.5

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.641, y = -40.632x + 87.4

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.641, y = -33.952x + 75.0

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.622, y = -0.810x + 38.3

**1a_instruction_override vs Benchmark Score:**
  r = -0.603, y = -0.496x + 26.6

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.550, y = -22.092x + 48.9

**total_hallucinations vs Is Reasoning Model:**
  r = -0.549, y = -88.257x + 203.8

**category2_factual_errors vs Benchmark Score:**
  r = -0.544, y = -1.624x + 88.7

**1b_context_omission vs Is Reasoning Model:**
  r = -0.537, y = -15.296x + 32.9

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.522, y = 3.989x + 2.7

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.516, y = -6.429x + 12.1

**4a_syntax_error vs Is Open Source:**
  r = 0.470, y = 6.440x + 2.9

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.437, y = -0.038x + 48.4

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.415, y = -0.784x + 49.0

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.404, y = -3.015x + 5.9

**1a_instruction_override vs Is Open Source:**
  r = 0.390, y = 4.232x + 6.5

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.389, y = -0.030x + 1.3

**category4_technical_errors vs Is Open Source:**
  r = 0.385, y = 11.173x + 14.9

**4b_model_semantics_breach vs Is Open Source:**
  r = 0.375, y = 5.316x + 7.6

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.357, y = -3.781x + 10.1

**2a_concept_fabrication vs Is Open Source:**
  r = 0.336, y = 5.773x + 5.9

**category2_factual_errors vs Is Open Source:**
  r = 0.325, y = 12.809x + 23.2

**3b_self_contradiction vs Is Open Source:**
  r = 0.323, y = 4.127x + 7.1

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.322, y = -0.052x + 89.4

**category2_factual_errors vs Is Reasoning Model:**
  r = -0.317, y = -12.189x + 34.5

**2b_spurious_numeric vs Is Reasoning Model:**
  r = -0.316, y = -7.709x + 23.8

**total_hallucinations vs Is Open Source:**
  r = 0.313, y = 51.537x + 137.8

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.310, y = -4.294x + 11.9

**2b_spurious_numeric vs Days Since 2024-01-01:**
  r = 0.310, y = 0.023x + 5.6


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
- Correlation: 0.459 ***
- Linear fit: y = 0.368x + 13.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.829 ***
- Linear fit: y = 1.237x + 18.0

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.534 ***
- Linear fit: y = 0.320x + 5.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.618 ***
- Linear fit: y = 1.152x + 33.6

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.681 ***
- Linear fit: y = 0.509x + 3.8

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.635 ***
- Linear fit: y = 0.255x + 1.1

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.992 ***, y = 0.838x + 1.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.951 ***, y = 0.715x + -1.3

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.940 ***, y = 0.603x + 2.9

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.915 ***, y = 0.457x + 1.1

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.876 ***, y = 0.398x + -2.2

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.868 ***, y = 0.378x + -2.8

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.829 ***, y = 1.237x + 18.0

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.826 ***, y = 1.043x + 16.5

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.822 ***, y = 0.156x + -1.5

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.801 ***, y = 1.344x + 21.3

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.777 ***, y = 0.392x + 0.4

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.773 ***, y = 1.338x + 3.2

**1c: Prompt Contradiction vs 4b: Model Semantics Breach:**
  r = 0.768 ***, y = 1.408x + 3.4

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.743 ***, y = 0.166x + -0.7

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.741 ***, y = 0.785x + 2.4

**Category 4: Technical Errors vs 2a: Concept Fabrication:**
  r = 0.737 ***, y = 0.429x + -0.1

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.728 ***, y = 1.559x + 1.1

**Category 4: Technical Errors vs 1c: Prompt Contradiction:**
  r = 0.726 ***, y = 0.198x + 0.6

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.726 ***, y = 0.256x + 1.7

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.723 ***, y = 0.168x + 1.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
