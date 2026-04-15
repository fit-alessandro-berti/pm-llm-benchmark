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
- Correlation: -0.493 ***
- Linear fit: y = -2.321x + 140.5
- P-value: 0.0000
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.490 ***
- Linear fit: y = -0.075x + 123.2
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.423 ***
- Linear fit: y = -21.523x + 86.7
- P-value: 0.0000
- N samples: 116

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.002x + 73.9
- P-value: 0.2511
- N samples: 112

**Is Open Source:**
- Correlation: -0.052 
- Linear fit: y = -2.645x + 75.7
- P-value: 0.5771
- N samples: 116

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.305 ***
- Linear fit: y = -1.512x + 94.8
- P-value: 0.0009
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.147 
- Linear fit: y = -7.861x + 56.3
- P-value: 0.1153
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: 0.080 
- Linear fit: y = 0.013x + 43.5
- P-value: 0.3950
- N samples: 116

**Is Open Source:**
- Correlation: 0.054 
- Linear fit: y = 2.854x + 50.5
- P-value: 0.5671
- N samples: 116

**Model Size (B):**
- Correlation: -0.048 
- Linear fit: y = -0.001x + 52.0
- P-value: 0.6120
- N samples: 112

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.481 ***
- Linear fit: y = -19.925x + 116.9
- P-value: 0.0000
- N samples: 116

**Benchmark Score:**
- Correlation: -0.253 **
- Linear fit: y = -0.971x + 133.2
- P-value: 0.0061
- N samples: 116

**Is Open Source:**
- Correlation: -0.235 *
- Linear fit: y = -9.685x + 110.0
- P-value: 0.0110
- N samples: 116

**Model Size (B):**
- Correlation: 0.111 
- Linear fit: y = 0.002x + 104.4
- P-value: 0.2450
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.024 
- Linear fit: y = -0.003x + 107.5
- P-value: 0.7991
- N samples: 116

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.522 ***
- Linear fit: y = -1.201x + 66.7
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.253 **
- Linear fit: y = -6.292x + 36.1
- P-value: 0.0061
- N samples: 116

**Model Size (B):**
- Correlation: -0.244 **
- Linear fit: y = -0.002x + 34.1
- P-value: 0.0096
- N samples: 112

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 1.407x + 31.9
- P-value: 0.5435
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.043 
- Linear fit: y = -0.003x + 34.6
- P-value: 0.6497
- N samples: 116

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.586 ***
- Linear fit: y = -6.494x + 458.2
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.499 ***
- Linear fit: y = -59.683x + 307.4
- P-value: 0.0000
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.194 *
- Linear fit: y = -0.070x + 318.7
- P-value: 0.0374
- N samples: 116

**Is Open Source:**
- Correlation: -0.058 
- Linear fit: y = -6.927x + 276.6
- P-value: 0.5344
- N samples: 116

**Model Size (B):**
- Correlation: 0.003 
- Linear fit: y = 0.000x + 273.8
- P-value: 0.9737
- N samples: 112

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.493 ***
- Linear fit: y = -2.321x + 140.5
- P-value: 0.0000
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.490 ***
- Linear fit: y = -0.075x + 123.2
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.423 ***
- Linear fit: y = -21.523x + 86.7
- P-value: 0.0000
- N samples: 116

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.002x + 73.9
- P-value: 0.2511
- N samples: 112

**Is Open Source:**
- Correlation: -0.052 
- Linear fit: y = -2.645x + 75.7
- P-value: 0.5771
- N samples: 116

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.305 ***
- Linear fit: y = -1.512x + 94.8
- P-value: 0.0009
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.147 
- Linear fit: y = -7.861x + 56.3
- P-value: 0.1153
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: 0.080 
- Linear fit: y = 0.013x + 43.5
- P-value: 0.3950
- N samples: 116

**Is Open Source:**
- Correlation: 0.054 
- Linear fit: y = 2.854x + 50.5
- P-value: 0.5671
- N samples: 116

**Model Size (B):**
- Correlation: -0.048 
- Linear fit: y = -0.001x + 52.0
- P-value: 0.6120
- N samples: 112

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.481 ***
- Linear fit: y = -19.925x + 116.9
- P-value: 0.0000
- N samples: 116

**Benchmark Score:**
- Correlation: -0.253 **
- Linear fit: y = -0.971x + 133.2
- P-value: 0.0061
- N samples: 116

**Is Open Source:**
- Correlation: -0.235 *
- Linear fit: y = -9.685x + 110.0
- P-value: 0.0110
- N samples: 116

**Model Size (B):**
- Correlation: 0.111 
- Linear fit: y = 0.002x + 104.4
- P-value: 0.2450
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.024 
- Linear fit: y = -0.003x + 107.5
- P-value: 0.7991
- N samples: 116

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.522 ***
- Linear fit: y = -1.201x + 66.7
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.253 **
- Linear fit: y = -6.292x + 36.1
- P-value: 0.0061
- N samples: 116

**Model Size (B):**
- Correlation: -0.244 **
- Linear fit: y = -0.002x + 34.1
- P-value: 0.0096
- N samples: 112

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 1.407x + 31.9
- P-value: 0.5435
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.043 
- Linear fit: y = -0.003x + 34.6
- P-value: 0.6497
- N samples: 116

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.615 ***
- Linear fit: y = -0.501x + 25.7
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.271 **
- Linear fit: y = -2.386x + 12.8
- P-value: 0.0032
- N samples: 116

**Is Open Source:**
- Correlation: 0.265 **
- Linear fit: y = 2.314x + 10.4
- P-value: 0.0041
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.093 
- Linear fit: y = -0.002x + 13.0
- P-value: 0.3216
- N samples: 116

**Model Size (B):**
- Correlation: 0.078 
- Linear fit: y = 0.000x + 11.3
- P-value: 0.4128
- N samples: 112

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.522 ***
- Linear fit: y = -0.069x + 102.7
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.371 ***
- Linear fit: y = -16.348x + 67.1
- P-value: 0.0000
- N samples: 116

**Benchmark Score:**
- Correlation: -0.325 ***
- Linear fit: y = -1.325x + 95.4
- P-value: 0.0004
- N samples: 116

**Is Open Source:**
- Correlation: -0.151 
- Linear fit: y = -6.608x + 60.8
- P-value: 0.1056
- N samples: 116

**Model Size (B):**
- Correlation: 0.131 
- Linear fit: y = 0.002x + 57.1
- P-value: 0.1676
- N samples: 112

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.707 ***
- Linear fit: y = -0.496x + 19.4
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.368 ***
- Linear fit: y = -2.789x + 6.9
- P-value: 0.0000
- N samples: 116

**Is Open Source:**
- Correlation: 0.219 *
- Linear fit: y = 1.649x + 4.5
- P-value: 0.0181
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.147 
- Linear fit: y = -0.003x + 7.5
- P-value: 0.1151
- N samples: 116

**Model Size (B):**
- Correlation: -0.116 
- Linear fit: y = -0.000x + 5.5
- P-value: 0.2240
- N samples: 112

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.258 **
- Linear fit: y = -0.643x + 41.1
- P-value: 0.0052
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: 0.168 
- Linear fit: y = 0.014x + 14.0
- P-value: 0.0713
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.064 
- Linear fit: y = -1.729x + 23.8
- P-value: 0.4937
- N samples: 116

**Is Open Source:**
- Correlation: 0.059 
- Linear fit: y = 1.587x + 22.1
- P-value: 0.5275
- N samples: 116

**Model Size (B):**
- Correlation: 0.013 
- Linear fit: y = 0.000x + 22.4
- P-value: 0.8890
- N samples: 112

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.306 ***
- Linear fit: y = -0.841x + 52.0
- P-value: 0.0008
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.209 *
- Linear fit: y = -6.201x + 31.6
- P-value: 0.0242
- N samples: 116

**Model Size (B):**
- Correlation: -0.092 
- Linear fit: y = -0.001x + 28.7
- P-value: 0.3336
- N samples: 112

**Is Open Source:**
- Correlation: 0.033 
- Linear fit: y = 0.982x + 27.6
- P-value: 0.7225
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.016 
- Linear fit: y = -0.001x + 29.0
- P-value: 0.8674
- N samples: 116

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.101 
- Linear fit: y = -0.028x + 1.7
- P-value: 0.2827
- N samples: 116

**Is Open Source:**
- Correlation: 0.097 
- Linear fit: y = 0.285x + 0.8
- P-value: 0.3026
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: 0.066 
- Linear fit: y = 0.001x + 0.6
- P-value: 0.4796
- N samples: 116

**Model Size (B):**
- Correlation: -0.063 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.5072
- N samples: 112

**Is Reasoning Model:**
- Correlation: 0.023 
- Linear fit: y = 0.070x + 0.9
- P-value: 0.8024
- N samples: 116

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.425 ***
- Linear fit: y = -15.138x + 103.8
- P-value: 0.0000
- N samples: 116

**Is Open Source:**
- Correlation: -0.353 ***
- Linear fit: y = -12.506x + 100.9
- P-value: 0.0001
- N samples: 116

**Model Size (B):**
- Correlation: 0.197 *
- Linear fit: y = 0.003x + 93.4
- P-value: 0.0374
- N samples: 112

**Benchmark Score:**
- Correlation: -0.105 
- Linear fit: y = -0.347x + 105.1
- P-value: 0.2610
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.022 
- Linear fit: y = -0.002x + 96.7
- P-value: 0.8183
- N samples: 116

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.648 ***
- Linear fit: y = -0.612x + 27.6
- P-value: 0.0000
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.464 ***
- Linear fit: y = -4.738x + 12.9
- P-value: 0.0000
- N samples: 116

**Is Open Source:**
- Correlation: 0.274 **
- Linear fit: y = 2.783x + 9.0
- P-value: 0.0029
- N samples: 116

**Model Size (B):**
- Correlation: -0.243 **
- Linear fit: y = -0.001x + 10.9
- P-value: 0.0099
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.018 
- Linear fit: y = -0.001x + 10.6
- P-value: 0.8497
- N samples: 116

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.193 *
- Linear fit: y = -0.011x + 0.4
- P-value: 0.0374
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.077 
- Linear fit: y = -0.049x + 0.1
- P-value: 0.4109
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.061 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.5132
- N samples: 116

**Is Open Source:**
- Correlation: 0.058 
- Linear fit: y = 0.037x + 0.1
- P-value: 0.5351
- N samples: 116

**Model Size (B):**
- Correlation: 0.054 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.5726
- N samples: 112

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.415 ***
- Linear fit: y = -0.419x + 19.6
- P-value: 0.0000
- N samples: 116

**Model Size (B):**
- Correlation: -0.239 *
- Linear fit: y = -0.001x + 8.3
- P-value: 0.0113
- N samples: 112

**Is Open Source:**
- Correlation: 0.214 *
- Linear fit: y = 2.321x + 6.6
- P-value: 0.0211
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.096 
- Linear fit: y = -1.048x + 8.3
- P-value: 0.3050
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: 0.025 
- Linear fit: y = 0.001x + 7.1
- P-value: 0.7863
- N samples: 116

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.648 ***
- Linear fit: y = -0.790x + 40.4
- P-value: 0.0000
- N samples: 116

**Model Size (B):**
- Correlation: -0.311 ***
- Linear fit: y = -0.002x + 18.9
- P-value: 0.0009
- N samples: 112

**Is Reasoning Model:**
- Correlation: -0.289 **
- Linear fit: y = -3.802x + 20.1
- P-value: 0.0016
- N samples: 116

**Is Open Source:**
- Correlation: 0.232 *
- Linear fit: y = 3.039x + 16.5
- P-value: 0.0120
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.066 
- Linear fit: y = -0.003x + 19.6
- P-value: 0.4802
- N samples: 116

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.358 ***
- Linear fit: y = -3.954x + 8.7
- P-value: 0.0001
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.130 
- Linear fit: y = -1.442x + 7.8
- P-value: 0.1654
- N samples: 116

**Model Size (B):**
- Correlation: 0.057 
- Linear fit: y = 0.000x + 6.8
- P-value: 0.5506
- N samples: 112

**Days Since 2024-01-01:**
- Correlation: -0.042 
- Linear fit: y = -0.001x + 7.9
- P-value: 0.6556
- N samples: 116

**Benchmark Score:**
- Correlation: 0.008 
- Linear fit: y = 0.009x + 6.7
- P-value: 0.9293
- N samples: 116

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.707, y = -0.496x + 19.4

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.648, y = -0.790x + 40.4

**3b_self_contradiction vs Benchmark Score:**
  r = -0.648, y = -0.612x + 27.6

**1a_instruction_override vs Benchmark Score:**
  r = -0.615, y = -0.501x + 25.7

**total_hallucinations vs Benchmark Score:**
  r = -0.586, y = -6.494x + 458.2

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.522, y = -0.069x + 102.7

**category4_technical_errors vs Benchmark Score:**
  r = -0.522, y = -1.201x + 66.7

**total_hallucinations vs Is Reasoning Model:**
  r = -0.499, y = -59.683x + 307.4

**category1_input_misalignment vs Benchmark Score:**
  r = -0.493, y = -2.321x + 140.5

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.490, y = -0.075x + 123.2

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.481, y = -19.925x + 116.9

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.464, y = -4.738x + 12.9

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.425, y = -15.138x + 103.8

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.423, y = -21.523x + 86.7

**4a_syntax_error vs Benchmark Score:**
  r = -0.415, y = -0.419x + 19.6

**1b_context_omission vs Is Reasoning Model:**
  r = -0.371, y = -16.348x + 67.1

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.368, y = -2.789x + 6.9

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.358, y = -3.954x + 8.7

**3a_unsupported_leap vs Is Open Source:**
  r = -0.353, y = -12.506x + 100.9

**1b_context_omission vs Benchmark Score:**
  r = -0.325, y = -1.325x + 95.4

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.311, y = -0.002x + 18.9

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.306, y = -0.841x + 52.0

**category2_factual_errors vs Benchmark Score:**
  r = -0.305, y = -1.512x + 94.8


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
- Correlation: -0.229 *
- Linear fit: y = -0.236x + 70.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.067 
- Linear fit: y = 0.053x + 101.7

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.076 
- Linear fit: y = 0.036x + 29.7

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.631 ***
- Linear fit: y = 0.481x + 80.5

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.539 ***
- Linear fit: y = 0.243x + 19.7

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.469 ***
- Linear fit: y = 0.278x + 3.1

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.836x + 6.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.964 ***, y = 0.822x + -3.7

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.926 ***, y = 0.510x + 1.7

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.912 ***, y = 0.456x + -0.9

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.818 ***, y = 0.435x + 3.8

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.713 ***, y = 0.314x + -2.5

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.695 ***, y = 0.765x + 10.8

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.631 ***, y = 0.162x + -6.6

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.631 ***, y = 0.481x + 80.5

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.607 ***, y = 0.216x + 4.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.607 ***, y = 0.119x + 4.3

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.604 ***, y = 0.436x + -17.7

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.590 ***, y = 0.805x + 6.1

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.587 ***, y = 0.497x + -0.3

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.570 ***, y = 0.701x + 10.6

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.561 ***, y = 0.034x + -0.7

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.558 ***, y = 0.242x + 2.7

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.556 ***, y = 0.365x + -15.7

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.556 ***, y = 0.251x + -1.4

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.554 ***, y = 0.097x + 4.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.373 ***, y = -0.027x + 2.6
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.364 ***, y = -0.300x + 74.2
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.355 ***, y = -0.215x + 35.5
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.297 ***, y = -0.198x + 40.0
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.291 **, y = -0.018x + 2.4
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.229 *, y = -0.236x + 70.2
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.228 *, y = -0.118x + 31.8
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
