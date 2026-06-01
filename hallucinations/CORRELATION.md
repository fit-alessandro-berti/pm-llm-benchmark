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
- Correlation: -0.563 ***
- Linear fit: y = -0.080x + 127.9
- P-value: 0.0000
- N samples: 138

**Benchmark Score:**
- Correlation: -0.532 ***
- Linear fit: y = -2.860x + 157.1
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.446 ***
- Linear fit: y = -23.097x + 86.2
- P-value: 0.0000
- N samples: 138

**Model Size (B):**
- Correlation: 0.091 
- Linear fit: y = 0.002x + 71.8
- P-value: 0.2978
- N samples: 132

**Is Open Source:**
- Correlation: -0.077 
- Linear fit: y = -3.983x + 74.3
- P-value: 0.3710
- N samples: 138

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.298 ***
- Linear fit: y = -1.609x + 97.7
- P-value: 0.0004
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.214 *
- Linear fit: y = -11.132x + 56.7
- P-value: 0.0118
- N samples: 138

**Model Size (B):**
- Correlation: -0.084 
- Linear fit: y = -0.002x + 51.0
- P-value: 0.3407
- N samples: 132

**Days Since 2024-01-01:**
- Correlation: 0.055 
- Linear fit: y = 0.008x + 44.8
- P-value: 0.5202
- N samples: 138

**Is Open Source:**
- Correlation: 0.014 
- Linear fit: y = 0.740x + 49.9
- P-value: 0.8689
- N samples: 138

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.458 ***
- Linear fit: y = -18.576x + 115.4
- P-value: 0.0000
- N samples: 138

**Benchmark Score:**
- Correlation: -0.361 ***
- Linear fit: y = -1.523x + 149.4
- P-value: 0.0000
- N samples: 138

**Is Open Source:**
- Correlation: -0.205 *
- Linear fit: y = -8.324x + 107.9
- P-value: 0.0161
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: -0.090 
- Linear fit: y = -0.010x + 111.4
- P-value: 0.2937
- N samples: 138

**Model Size (B):**
- Correlation: 0.049 
- Linear fit: y = 0.001x + 103.5
- P-value: 0.5759
- N samples: 132

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.504 ***
- Linear fit: y = -1.273x + 68.9
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.262 **
- Linear fit: y = -6.370x + 35.1
- P-value: 0.0019
- N samples: 138

**Model Size (B):**
- Correlation: -0.233 **
- Linear fit: y = -0.002x + 32.9
- P-value: 0.0071
- N samples: 132

**Days Since 2024-01-01:**
- Correlation: -0.041 
- Linear fit: y = -0.003x + 33.3
- P-value: 0.6305
- N samples: 138

**Is Open Source:**
- Correlation: -0.009 
- Linear fit: y = -0.226x + 31.5
- P-value: 0.9142
- N samples: 138

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.622 ***
- Linear fit: y = -7.832x + 498.0
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.525 ***
- Linear fit: y = -63.719x + 304.4
- P-value: 0.0000
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: -0.265 **
- Linear fit: y = -0.089x + 328.0
- P-value: 0.0017
- N samples: 138

**Is Open Source:**
- Correlation: -0.088 
- Linear fit: y = -10.704x + 271.3
- P-value: 0.3048
- N samples: 138

**Model Size (B):**
- Correlation: -0.035 
- Linear fit: y = -0.002x + 267.8
- P-value: 0.6865
- N samples: 132

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.563 ***
- Linear fit: y = -0.080x + 127.9
- P-value: 0.0000
- N samples: 138

**Benchmark Score:**
- Correlation: -0.532 ***
- Linear fit: y = -2.860x + 157.1
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.446 ***
- Linear fit: y = -23.097x + 86.2
- P-value: 0.0000
- N samples: 138

**Model Size (B):**
- Correlation: 0.091 
- Linear fit: y = 0.002x + 71.8
- P-value: 0.2978
- N samples: 132

**Is Open Source:**
- Correlation: -0.077 
- Linear fit: y = -3.983x + 74.3
- P-value: 0.3710
- N samples: 138

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.298 ***
- Linear fit: y = -1.609x + 97.7
- P-value: 0.0004
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.214 *
- Linear fit: y = -11.132x + 56.7
- P-value: 0.0118
- N samples: 138

**Model Size (B):**
- Correlation: -0.084 
- Linear fit: y = -0.002x + 51.0
- P-value: 0.3407
- N samples: 132

**Days Since 2024-01-01:**
- Correlation: 0.055 
- Linear fit: y = 0.008x + 44.8
- P-value: 0.5202
- N samples: 138

**Is Open Source:**
- Correlation: 0.014 
- Linear fit: y = 0.740x + 49.9
- P-value: 0.8689
- N samples: 138

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.458 ***
- Linear fit: y = -18.576x + 115.4
- P-value: 0.0000
- N samples: 138

**Benchmark Score:**
- Correlation: -0.361 ***
- Linear fit: y = -1.523x + 149.4
- P-value: 0.0000
- N samples: 138

**Is Open Source:**
- Correlation: -0.205 *
- Linear fit: y = -8.324x + 107.9
- P-value: 0.0161
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: -0.090 
- Linear fit: y = -0.010x + 111.4
- P-value: 0.2937
- N samples: 138

**Model Size (B):**
- Correlation: 0.049 
- Linear fit: y = 0.001x + 103.5
- P-value: 0.5759
- N samples: 132

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.504 ***
- Linear fit: y = -1.273x + 68.9
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.262 **
- Linear fit: y = -6.370x + 35.1
- P-value: 0.0019
- N samples: 138

**Model Size (B):**
- Correlation: -0.233 **
- Linear fit: y = -0.002x + 32.9
- P-value: 0.0071
- N samples: 132

**Days Since 2024-01-01:**
- Correlation: -0.041 
- Linear fit: y = -0.003x + 33.3
- P-value: 0.6305
- N samples: 138

**Is Open Source:**
- Correlation: -0.009 
- Linear fit: y = -0.226x + 31.5
- P-value: 0.9142
- N samples: 138

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.607 ***
- Linear fit: y = -0.578x + 28.3
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.409 ***
- Linear fit: y = -3.747x + 13.4
- P-value: 0.0000
- N samples: 138

**Is Open Source:**
- Correlation: 0.169 *
- Linear fit: y = 1.551x + 10.6
- P-value: 0.0480
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: -0.133 
- Linear fit: y = -0.003x + 13.6
- P-value: 0.1186
- N samples: 138

**Model Size (B):**
- Correlation: 0.045 
- Linear fit: y = 0.000x + 11.0
- P-value: 0.6093
- N samples: 132

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.597 ***
- Linear fit: y = -0.074x + 107.0
- P-value: 0.0000
- N samples: 138

**Benchmark Score:**
- Correlation: -0.379 ***
- Linear fit: y = -1.758x + 108.3
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.365 ***
- Linear fit: y = -16.309x + 66.0
- P-value: 0.0000
- N samples: 138

**Is Open Source:**
- Correlation: -0.155 
- Linear fit: y = -6.940x + 59.2
- P-value: 0.0699
- N samples: 138

**Model Size (B):**
- Correlation: 0.123 
- Linear fit: y = 0.002x + 55.4
- P-value: 0.1607
- N samples: 132

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.702 ***
- Linear fit: y = -0.524x + 20.5
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.423 ***
- Linear fit: y = -3.042x + 6.8
- P-value: 0.0000
- N samples: 138

**Is Open Source:**
- Correlation: 0.195 *
- Linear fit: y = 1.406x + 4.5
- P-value: 0.0219
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: -0.169 *
- Linear fit: y = -0.003x + 7.3
- P-value: 0.0479
- N samples: 138

**Model Size (B):**
- Correlation: -0.159 
- Linear fit: y = -0.000x + 5.4
- P-value: 0.0680
- N samples: 132

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.243 **
- Linear fit: y = -0.651x + 40.9
- P-value: 0.0040
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: 0.122 
- Linear fit: y = 0.009x + 15.7
- P-value: 0.1550
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.112 
- Linear fit: y = -2.899x + 23.4
- P-value: 0.1894
- N samples: 138

**Model Size (B):**
- Correlation: -0.021 
- Linear fit: y = -0.000x + 21.5
- P-value: 0.8137
- N samples: 132

**Is Open Source:**
- Correlation: 0.012 
- Linear fit: y = 0.321x + 21.5
- P-value: 0.8853
- N samples: 138

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.306 ***
- Linear fit: y = -0.922x + 54.9
- P-value: 0.0003
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.282 ***
- Linear fit: y = -8.207x + 32.5
- P-value: 0.0008
- N samples: 138

**Model Size (B):**
- Correlation: -0.126 
- Linear fit: y = -0.002x + 28.6
- P-value: 0.1510
- N samples: 132

**Days Since 2024-01-01:**
- Correlation: -0.017 
- Linear fit: y = -0.001x + 28.6
- P-value: 0.8463
- N samples: 138

**Is Open Source:**
- Correlation: 0.013 
- Linear fit: y = 0.368x + 27.5
- P-value: 0.8830
- N samples: 138

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.141 
- Linear fit: y = -0.036x + 1.9
- P-value: 0.0989
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: 0.089 
- Linear fit: y = 0.001x + 0.4
- P-value: 0.2977
- N samples: 138

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.4969
- N samples: 132

**Is Open Source:**
- Correlation: 0.021 
- Linear fit: y = 0.051x + 0.8
- P-value: 0.8083
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.010 
- Linear fit: y = -0.025x + 0.9
- P-value: 0.9045
- N samples: 138

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.398 ***
- Linear fit: y = -13.771x + 103.0
- P-value: 0.0000
- N samples: 138

**Is Open Source:**
- Correlation: -0.310 ***
- Linear fit: y = -10.769x + 99.3
- P-value: 0.0002
- N samples: 138

**Benchmark Score:**
- Correlation: -0.245 **
- Linear fit: y = -0.881x + 120.9
- P-value: 0.0037
- N samples: 138

**Model Size (B):**
- Correlation: 0.128 
- Linear fit: y = 0.002x + 93.2
- P-value: 0.1426
- N samples: 132

**Days Since 2024-01-01:**
- Correlation: -0.097 
- Linear fit: y = -0.009x + 101.3
- P-value: 0.2596
- N samples: 138

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.634 ***
- Linear fit: y = -0.644x + 28.5
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.491 ***
- Linear fit: y = -4.804x + 12.3
- P-value: 0.0000
- N samples: 138

**Model Size (B):**
- Correlation: -0.259 **
- Linear fit: y = -0.001x + 10.2
- P-value: 0.0027
- N samples: 132

**Is Open Source:**
- Correlation: 0.255 **
- Linear fit: y = 2.501x + 8.5
- P-value: 0.0025
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: -0.033 
- Linear fit: y = -0.001x + 10.1
- P-value: 0.7044
- N samples: 138

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.136 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.1209
- N samples: 132

**Is Open Source:**
- Correlation: -0.098 
- Linear fit: y = -0.056x + 0.1
- P-value: 0.2532
- N samples: 138

**Benchmark Score:**
- Correlation: 0.042 
- Linear fit: y = 0.002x + 0.0
- P-value: 0.6285
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: 0.019 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.8280
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.002 
- Linear fit: y = -0.001x + 0.1
- P-value: 0.9789
- N samples: 138

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.371 ***
- Linear fit: y = -0.422x + 19.6
- P-value: 0.0000
- N samples: 138

**Model Size (B):**
- Correlation: -0.220 *
- Linear fit: y = -0.001x + 7.9
- P-value: 0.0113
- N samples: 132

**Is Open Source:**
- Correlation: 0.183 *
- Linear fit: y = 2.015x + 6.4
- P-value: 0.0315
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: 0.115 
- Linear fit: y = 0.003x + 4.8
- P-value: 0.1801
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.095 
- Linear fit: y = -1.042x + 7.8
- P-value: 0.2679
- N samples: 138

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.599 ***
- Linear fit: y = -0.768x + 39.9
- P-value: 0.0000
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.325 ***
- Linear fit: y = -4.006x + 19.6
- P-value: 0.0001
- N samples: 138

**Model Size (B):**
- Correlation: -0.302 ***
- Linear fit: y = -0.002x + 18.3
- P-value: 0.0004
- N samples: 132

**Is Open Source:**
- Correlation: 0.139 
- Linear fit: y = 1.720x + 16.5
- P-value: 0.1040
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: -0.062 
- Linear fit: y = -0.002x + 18.7
- P-value: 0.4734
- N samples: 138

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.355 ***
- Linear fit: y = -3.960x + 8.6
- P-value: 0.0000
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: -0.135 
- Linear fit: y = -0.004x + 9.8
- P-value: 0.1142
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.119 
- Linear fit: y = -1.322x + 7.8
- P-value: 0.1653
- N samples: 138

**Benchmark Score:**
- Correlation: -0.072 
- Linear fit: y = -0.083x + 9.4
- P-value: 0.4020
- N samples: 138

**Model Size (B):**
- Correlation: 0.038 
- Linear fit: y = 0.000x + 6.7
- P-value: 0.6637
- N samples: 132

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.702, y = -0.524x + 20.5

**3b_self_contradiction vs Benchmark Score:**
  r = -0.634, y = -0.644x + 28.5

**total_hallucinations vs Benchmark Score:**
  r = -0.622, y = -7.832x + 498.0

**1a_instruction_override vs Benchmark Score:**
  r = -0.607, y = -0.578x + 28.3

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.599, y = -0.768x + 39.9

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.597, y = -0.074x + 107.0

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.563, y = -0.080x + 127.9

**category1_input_misalignment vs Benchmark Score:**
  r = -0.532, y = -2.860x + 157.1

**total_hallucinations vs Is Reasoning Model:**
  r = -0.525, y = -63.719x + 304.4

**category4_technical_errors vs Benchmark Score:**
  r = -0.504, y = -1.273x + 68.9

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.491, y = -4.804x + 12.3

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.458, y = -18.576x + 115.4

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.446, y = -23.097x + 86.2

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.423, y = -3.042x + 6.8

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.409, y = -3.747x + 13.4

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.398, y = -13.771x + 103.0

**1b_context_omission vs Benchmark Score:**
  r = -0.379, y = -1.758x + 108.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.371, y = -0.422x + 19.6

**1b_context_omission vs Is Reasoning Model:**
  r = -0.365, y = -16.309x + 66.0

**category3_logical_errors vs Benchmark Score:**
  r = -0.361, y = -1.523x + 149.4

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.355, y = -3.960x + 8.6

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.325, y = -4.006x + 19.6

**3a_unsupported_leap vs Is Open Source:**
  r = -0.310, y = -10.769x + 99.3

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.306, y = -0.922x + 54.9

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.302, y = -0.002x + 18.3


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
- Correlation: -0.170 *
- Linear fit: y = -0.169x + 62.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.123 
- Linear fit: y = 0.096x + 97.7

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.118 
- Linear fit: y = 0.056x + 27.4

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.666 ***
- Linear fit: y = 0.523x + 78.3

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.540 ***
- Linear fit: y = 0.257x + 18.5

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.537 ***
- Linear fit: y = 0.326x + -2.6

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.978 ***, y = 0.837x + 7.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.967 ***, y = 0.834x + -4.3

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.933 ***, y = 0.520x + 1.5

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.913 ***, y = 0.455x + -1.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.810 ***, y = 0.407x + 4.3

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.708 ***, y = 0.793x + 10.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.695 ***, y = 0.322x + -2.7

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.675 ***, y = 0.162x + -7.5

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.666 ***, y = 0.523x + 78.3

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.640 ***, y = 0.455x + -20.0

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.639 ***, y = 0.216x + 3.5

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.617 ***, y = 0.116x + 3.6

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.606 ***, y = 0.407x + 74.7

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.601 ***, y = 0.271x + -1.6

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.580 ***, y = 0.369x + -16.8

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.574 ***, y = 0.728x + 10.2

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.569 ***, y = 0.685x + 76.2

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.561 ***, y = 0.222x + 2.4

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.542 ***, y = 0.097x + 4.3

**2a: Concept Fabrication vs 3a: Unsupported Leap:**
  r = 0.542 ***, y = 0.730x + 79.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.344 ***, y = -0.019x + 1.9
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.300 ***, y = -0.261x + 68.9
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.296 ***, y = -0.169x + 31.2
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.272 **, y = -0.013x + 1.8
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.246 **, y = -0.157x + 36.4
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
