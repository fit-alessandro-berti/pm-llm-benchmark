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
- Correlation: -0.787 ***
- Linear fit: y = -2.449x + 128.5
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.559 ***
- Linear fit: y = -26.406x + 55.7
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.242 **
- Linear fit: y = 11.457x + 37.0
- P-value: 0.0011
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: -0.191 **
- Linear fit: y = -0.031x + 58.8
- P-value: 0.0091
- N samples: 186

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0640
- N samples: 180

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.532 ***
- Linear fit: y = -1.491x + 80.6
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.297 ***
- Linear fit: y = 0.043x + 6.4
- P-value: 0.0000
- N samples: 186

**Is Reasoning Model:**
- Correlation: -0.243 **
- Linear fit: y = -10.337x + 33.6
- P-value: 0.0011
- N samples: 179

**Is Open Source:**
- Correlation: 0.228 **
- Linear fit: y = 9.706x + 23.5
- P-value: 0.0022
- N samples: 179

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.003x + 29.7
- P-value: 0.1184
- N samples: 180

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.770 ***
- Linear fit: y = -3.430x + 196.1
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.656 ***
- Linear fit: y = -44.388x + 97.8
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.191 *
- Linear fit: y = 12.928x + 69.6
- P-value: 0.0105
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: -0.145 *
- Linear fit: y = -0.033x + 93.5
- P-value: 0.0480
- N samples: 186

**Model Size (B):**
- Correlation: -0.120 
- Linear fit: y = -0.004x + 79.1
- P-value: 0.1091
- N samples: 180

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.352x + 66.8
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.317 ***
- Linear fit: y = -9.426x + 24.2
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.233 **
- Linear fit: y = 6.928x + 16.0
- P-value: 0.0017
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.167 *
- Linear fit: y = 0.017x + 10.7
- P-value: 0.0228
- N samples: 186

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.002x + 20.4
- P-value: 0.0762
- N samples: 180

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.804 ***
- Linear fit: y = -9.503x + 508.1
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.549 ***
- Linear fit: y = -98.575x + 223.9
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.253 ***
- Linear fit: y = 45.475x + 152.4
- P-value: 0.0006
- N samples: 179

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.014x + 183.2
- P-value: 0.0528
- N samples: 180

**Days Since 2024-01-01:**
- Correlation: -0.002 
- Linear fit: y = -0.001x + 176.2
- P-value: 0.9832
- N samples: 186

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.787 ***
- Linear fit: y = -2.449x + 128.5
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.559 ***
- Linear fit: y = -26.406x + 55.7
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.242 **
- Linear fit: y = 11.457x + 37.0
- P-value: 0.0011
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: -0.191 **
- Linear fit: y = -0.031x + 58.8
- P-value: 0.0091
- N samples: 186

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0640
- N samples: 180

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.532 ***
- Linear fit: y = -1.491x + 80.6
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.297 ***
- Linear fit: y = 0.043x + 6.4
- P-value: 0.0000
- N samples: 186

**Is Reasoning Model:**
- Correlation: -0.243 **
- Linear fit: y = -10.337x + 33.6
- P-value: 0.0011
- N samples: 179

**Is Open Source:**
- Correlation: 0.228 **
- Linear fit: y = 9.706x + 23.5
- P-value: 0.0022
- N samples: 179

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.003x + 29.7
- P-value: 0.1184
- N samples: 180

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.770 ***
- Linear fit: y = -3.430x + 196.1
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.656 ***
- Linear fit: y = -44.388x + 97.8
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.191 *
- Linear fit: y = 12.928x + 69.6
- P-value: 0.0105
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: -0.145 *
- Linear fit: y = -0.033x + 93.5
- P-value: 0.0480
- N samples: 186

**Model Size (B):**
- Correlation: -0.120 
- Linear fit: y = -0.004x + 79.1
- P-value: 0.1091
- N samples: 180

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.352x + 66.8
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.317 ***
- Linear fit: y = -9.426x + 24.2
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.233 **
- Linear fit: y = 6.928x + 16.0
- P-value: 0.0017
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.167 *
- Linear fit: y = 0.017x + 10.7
- P-value: 0.0228
- N samples: 186

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.002x + 20.4
- P-value: 0.0762
- N samples: 180

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.639 ***
- Linear fit: y = -0.472x + 24.1
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.384 ***
- Linear fit: y = -4.306x + 9.7
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.284 ***
- Linear fit: y = 3.190x + 5.9
- P-value: 0.0001
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.156 *
- Linear fit: y = 0.006x + 4.5
- P-value: 0.0332
- N samples: 186

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.001x + 7.7
- P-value: 0.1602
- N samples: 180

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.714 ***
- Linear fit: y = -1.584x + 86.5
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.557 ***
- Linear fit: y = -18.782x + 40.2
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: -0.375 ***
- Linear fit: y = -0.043x + 53.6
- P-value: 0.0000
- N samples: 186

**Is Open Source:**
- Correlation: 0.158 *
- Linear fit: y = 5.333x + 28.4
- P-value: 0.0345
- N samples: 179

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.002x + 32.5
- P-value: 0.1118
- N samples: 180

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.693 ***
- Linear fit: y = -0.393x + 17.9
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.386 ***
- Linear fit: y = -3.317x + 5.8
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.341 ***
- Linear fit: y = 2.933x + 2.7
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.228 **
- Linear fit: y = 0.007x + 0.8
- P-value: 0.0017
- N samples: 186

**Model Size (B):**
- Correlation: -0.156 *
- Linear fit: y = -0.001x + 4.5
- P-value: 0.0366
- N samples: 180

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.489 ***
- Linear fit: y = -0.746x + 34.4
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.309 ***
- Linear fit: y = 0.024x + -4.2
- P-value: 0.0000
- N samples: 186

**Is Reasoning Model:**
- Correlation: -0.245 ***
- Linear fit: y = -5.681x + 11.1
- P-value: 0.0009
- N samples: 179

**Is Open Source:**
- Correlation: 0.221 **
- Linear fit: y = 5.118x + 5.6
- P-value: 0.0030
- N samples: 179

**Model Size (B):**
- Correlation: -0.059 
- Linear fit: y = -0.001x + 8.6
- P-value: 0.4337
- N samples: 180

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.470 ***
- Linear fit: y = -0.695x + 43.9
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.256 ***
- Linear fit: y = 0.020x + 9.5
- P-value: 0.0004
- N samples: 186

**Is Reasoning Model:**
- Correlation: -0.215 **
- Linear fit: y = -4.831x + 21.9
- P-value: 0.0038
- N samples: 179

**Is Open Source:**
- Correlation: 0.210 **
- Linear fit: y = 4.724x + 17.1
- P-value: 0.0047
- N samples: 179

**Model Size (B):**
- Correlation: -0.141 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0596
- N samples: 180

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.125 
- Linear fit: y = -0.050x + 2.4
- P-value: 0.0960
- N samples: 179

**Model Size (B):**
- Correlation: -0.073 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.3310
- N samples: 180

**Days Since 2024-01-01:**
- Correlation: -0.039 
- Linear fit: y = -0.001x + 1.1
- P-value: 0.5926
- N samples: 186

**Is Reasoning Model:**
- Correlation: 0.029 
- Linear fit: y = 0.174x + 0.6
- P-value: 0.7023
- N samples: 179

**Is Open Source:**
- Correlation: -0.023 
- Linear fit: y = -0.137x + 0.7
- P-value: 0.7646
- N samples: 179

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.758 ***
- Linear fit: y = -2.821x + 165.2
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.665 ***
- Linear fit: y = -37.573x + 84.8
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: -0.234 **
- Linear fit: y = -0.045x + 89.7
- P-value: 0.0013
- N samples: 186

**Is Open Source:**
- Correlation: 0.167 *
- Linear fit: y = 9.450x + 61.7
- P-value: 0.0254
- N samples: 179

**Model Size (B):**
- Correlation: -0.107 
- Linear fit: y = -0.003x + 68.9
- P-value: 0.1517
- N samples: 180

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.629 ***
- Linear fit: y = -0.573x + 29.4
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.472 ***
- Linear fit: y = -6.540x + 12.5
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.231 **
- Linear fit: y = 3.196x + 7.7
- P-value: 0.0019
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.221 **
- Linear fit: y = 0.010x + 4.0
- P-value: 0.0025
- N samples: 186

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.001x + 9.9
- P-value: 0.0608
- N samples: 180

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.339 ***
- Linear fit: y = -0.035x + 1.6
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.220 **
- Linear fit: y = 0.001x + -0.3
- P-value: 0.0025
- N samples: 186

**Is Open Source:**
- Correlation: 0.177 *
- Linear fit: y = 0.282x + 0.2
- P-value: 0.0177
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.173 *
- Linear fit: y = -0.275x + 0.5
- P-value: 0.0207
- N samples: 179

**Model Size (B):**
- Correlation: -0.056 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4558
- N samples: 180

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.615 ***
- Linear fit: y = -0.629x + 27.2
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.307 ***
- Linear fit: y = 4.770x + 2.7
- P-value: 0.0000
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.249 ***
- Linear fit: y = 0.013x + -1.6
- P-value: 0.0006
- N samples: 186

**Model Size (B):**
- Correlation: -0.158 *
- Linear fit: y = -0.001x + 5.8
- P-value: 0.0346
- N samples: 180

**Is Reasoning Model:**
- Correlation: -0.147 *
- Linear fit: y = -2.286x + 6.3
- P-value: 0.0492
- N samples: 179

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.706 ***
- Linear fit: y = -0.676x + 34.1
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.409 ***
- Linear fit: y = -5.950x + 13.3
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.245 ***
- Linear fit: y = 3.565x + 8.6
- P-value: 0.0010
- N samples: 179

**Model Size (B):**
- Correlation: -0.189 *
- Linear fit: y = -0.002x + 11.0
- P-value: 0.0109
- N samples: 180

**Days Since 2024-01-01:**
- Correlation: 0.072 
- Linear fit: y = 0.004x + 8.5
- P-value: 0.3264
- N samples: 186

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.219 **
- Linear fit: y = -1.408x + 4.7
- P-value: 0.0033
- N samples: 179

**Model Size (B):**
- Correlation: 0.193 **
- Linear fit: y = 0.001x + 3.6
- P-value: 0.0093
- N samples: 180

**Is Reasoning Model:**
- Correlation: -0.185 *
- Linear fit: y = -1.190x + 4.5
- P-value: 0.0132
- N samples: 179

**Benchmark Score:**
- Correlation: -0.110 
- Linear fit: y = -0.047x + 5.6
- P-value: 0.1420
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.011 
- Linear fit: y = 0.000x + 3.7
- P-value: 0.8848
- N samples: 186

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.804, y = -9.503x + 508.1

**category1_input_misalignment vs Benchmark Score:**
  r = -0.787, y = -2.449x + 128.5

**category3_logical_errors vs Benchmark Score:**
  r = -0.770, y = -3.430x + 196.1

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.758, y = -2.821x + 165.2

**1b_context_omission vs Benchmark Score:**
  r = -0.714, y = -1.584x + 86.5

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.706, y = -0.676x + 34.1

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.693, y = -0.393x + 17.9

**category4_technical_errors vs Benchmark Score:**
  r = -0.691, y = -1.352x + 66.8

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.665, y = -37.573x + 84.8

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.656, y = -44.388x + 97.8

**1a_instruction_override vs Benchmark Score:**
  r = -0.639, y = -0.472x + 24.1

**3b_self_contradiction vs Benchmark Score:**
  r = -0.629, y = -0.573x + 29.4

**4a_syntax_error vs Benchmark Score:**
  r = -0.615, y = -0.629x + 27.2

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.559, y = -26.406x + 55.7

**1b_context_omission vs Is Reasoning Model:**
  r = -0.557, y = -18.782x + 40.2

**total_hallucinations vs Is Reasoning Model:**
  r = -0.549, y = -98.575x + 223.9

**category2_factual_errors vs Benchmark Score:**
  r = -0.532, y = -1.491x + 80.6

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.489, y = -0.746x + 34.4

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.472, y = -6.540x + 12.5

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.470, y = -0.695x + 43.9

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.409, y = -5.950x + 13.3

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.386, y = -3.317x + 5.8

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.384, y = -4.306x + 9.7

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.375, y = -0.043x + 53.6

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.341, y = 2.933x + 2.7

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.339, y = -0.035x + 1.6

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.317, y = -9.426x + 24.2

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.309, y = 0.024x + -4.2

**4a_syntax_error vs Is Open Source:**
  r = 0.307, y = 4.770x + 2.7


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
- Correlation: 0.523 ***
- Linear fit: y = 0.468x + 8.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.816 ***
- Linear fit: y = 1.162x + 26.4

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.643 ***
- Linear fit: y = 0.404x + 1.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.632 ***
- Linear fit: y = 1.005x + 47.8

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.724 ***
- Linear fit: y = 0.508x + 4.9

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.709 ***
- Linear fit: y = 0.313x + -4.6

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.988 ***, y = 0.826x + 3.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.949 ***, y = 0.681x + 2.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.900 ***, y = 0.440x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.889 ***, y = 0.483x + -5.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.883 ***, y = 0.467x + 6.2

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.879 ***, y = 0.457x + -3.7

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.816 ***, y = 1.162x + 26.4

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.805 ***, y = 0.165x + -3.2

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.802 ***, y = 0.955x + 25.6

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.790 ***, y = 1.270x + 4.1

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.782 ***, y = 0.469x + 5.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.780 ***, y = 0.185x + -0.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.778 ***, y = 0.361x + 2.4

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.776 ***, y = 1.289x + 26.3

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.769 ***, y = 2.064x + -0.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.769 ***, y = 0.250x + 2.2

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.760 ***, y = 0.383x + 2.1

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.743 ***, y = 0.568x + -0.1

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.743 ***, y = 0.499x + 1.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.742 ***, y = 0.134x + -1.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
