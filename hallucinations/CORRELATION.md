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
- Correlation: -0.760 ***
- Linear fit: y = -2.191x + 107.7
- P-value: 0.0000
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.596 ***
- Linear fit: y = -0.100x + 84.9
- P-value: 0.0000
- N samples: 145

**Is Reasoning Model:**
- Correlation: -0.545 ***
- Linear fit: y = -20.010x + 51.9
- P-value: 0.0000
- N samples: 141

**Model Size (B):**
- Correlation: -0.177 *
- Linear fit: y = -0.004x + 43.8
- P-value: 0.0379
- N samples: 138

**Is Open Source:**
- Correlation: 0.168 *
- Linear fit: y = 6.307x + 38.4
- P-value: 0.0463
- N samples: 141

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.514 ***
- Linear fit: y = -0.993x + 52.8
- P-value: 0.0000
- N samples: 141

**Is Open Source:**
- Correlation: 0.192 *
- Linear fit: y = 4.821x + 20.2
- P-value: 0.0228
- N samples: 141

**Model Size (B):**
- Correlation: -0.148 
- Linear fit: y = -0.002x + 24.0
- P-value: 0.0830
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.112 
- Linear fit: y = -2.761x + 24.5
- P-value: 0.1856
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: 0.046 
- Linear fit: y = 0.005x + 21.1
- P-value: 0.5853
- N samples: 145

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.785 ***
- Linear fit: y = -3.268x + 174.8
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.684 ***
- Linear fit: y = -36.305x + 94.7
- P-value: 0.0000
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.324 ***
- Linear fit: y = -0.078x + 110.7
- P-value: 0.0001
- N samples: 145

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 78.3
- P-value: 0.1075
- N samples: 138

**Is Open Source:**
- Correlation: 0.119 
- Linear fit: y = 6.468x + 73.2
- P-value: 0.1584
- N samples: 141

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.529 ***
- Linear fit: y = -0.807x + 41.4
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.193 *
- Linear fit: y = -3.744x + 19.1
- P-value: 0.0221
- N samples: 141

**Model Size (B):**
- Correlation: -0.126 
- Linear fit: y = -0.002x + 17.8
- P-value: 0.1424
- N samples: 138

**Is Open Source:**
- Correlation: 0.101 
- Linear fit: y = 1.999x + 16.1
- P-value: 0.2346
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.014 
- Linear fit: y = -0.001x + 18.0
- P-value: 0.8678
- N samples: 145

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.859 ***
- Linear fit: y = -7.829x + 401.7
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.579 ***
- Linear fit: y = -67.207x + 200.2
- P-value: 0.0000
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.339 ***
- Linear fit: y = -0.181x + 246.0
- P-value: 0.0000
- N samples: 145

**Model Size (B):**
- Correlation: -0.188 *
- Linear fit: y = -0.013x + 172.1
- P-value: 0.0271
- N samples: 138

**Is Open Source:**
- Correlation: 0.180 *
- Linear fit: y = 21.325x + 154.9
- P-value: 0.0329
- N samples: 141

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.760 ***
- Linear fit: y = -2.191x + 107.7
- P-value: 0.0000
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.596 ***
- Linear fit: y = -0.100x + 84.9
- P-value: 0.0000
- N samples: 145

**Is Reasoning Model:**
- Correlation: -0.545 ***
- Linear fit: y = -20.010x + 51.9
- P-value: 0.0000
- N samples: 141

**Model Size (B):**
- Correlation: -0.177 *
- Linear fit: y = -0.004x + 43.8
- P-value: 0.0379
- N samples: 138

**Is Open Source:**
- Correlation: 0.168 *
- Linear fit: y = 6.307x + 38.4
- P-value: 0.0463
- N samples: 141

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.514 ***
- Linear fit: y = -0.993x + 52.8
- P-value: 0.0000
- N samples: 141

**Is Open Source:**
- Correlation: 0.192 *
- Linear fit: y = 4.821x + 20.2
- P-value: 0.0228
- N samples: 141

**Model Size (B):**
- Correlation: -0.148 
- Linear fit: y = -0.002x + 24.0
- P-value: 0.0830
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.112 
- Linear fit: y = -2.761x + 24.5
- P-value: 0.1856
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: 0.046 
- Linear fit: y = 0.005x + 21.1
- P-value: 0.5853
- N samples: 145

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.785 ***
- Linear fit: y = -3.268x + 174.8
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.684 ***
- Linear fit: y = -36.305x + 94.7
- P-value: 0.0000
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.324 ***
- Linear fit: y = -0.078x + 110.7
- P-value: 0.0001
- N samples: 145

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 78.3
- P-value: 0.1075
- N samples: 138

**Is Open Source:**
- Correlation: 0.119 
- Linear fit: y = 6.468x + 73.2
- P-value: 0.1584
- N samples: 141

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.529 ***
- Linear fit: y = -0.807x + 41.4
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.193 *
- Linear fit: y = -3.744x + 19.1
- P-value: 0.0221
- N samples: 141

**Model Size (B):**
- Correlation: -0.126 
- Linear fit: y = -0.002x + 17.8
- P-value: 0.1424
- N samples: 138

**Is Open Source:**
- Correlation: 0.101 
- Linear fit: y = 1.999x + 16.1
- P-value: 0.2346
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.014 
- Linear fit: y = -0.001x + 18.0
- P-value: 0.8678
- N samples: 145

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.622 ***
- Linear fit: y = -0.365x + 17.1
- P-value: 0.0000
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.307 ***
- Linear fit: y = -0.010x + 10.8
- P-value: 0.0002
- N samples: 145

**Is Reasoning Model:**
- Correlation: -0.254 **
- Linear fit: y = -1.902x + 7.1
- P-value: 0.0024
- N samples: 141

**Is Open Source:**
- Correlation: 0.222 **
- Linear fit: y = 1.698x + 5.2
- P-value: 0.0081
- N samples: 141

**Model Size (B):**
- Correlation: -0.130 
- Linear fit: y = -0.001x + 6.5
- P-value: 0.1273
- N samples: 138

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.660 ***
- Linear fit: y = -1.580x + 79.9
- P-value: 0.0000
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.643 ***
- Linear fit: y = -0.089x + 70.9
- P-value: 0.0000
- N samples: 145

**Is Reasoning Model:**
- Correlation: -0.539 ***
- Linear fit: y = -16.442x + 40.6
- P-value: 0.0000
- N samples: 141

**Model Size (B):**
- Correlation: -0.156 
- Linear fit: y = -0.003x + 33.8
- P-value: 0.0677
- N samples: 138

**Is Open Source:**
- Correlation: 0.097 
- Linear fit: y = 3.020x + 30.8
- P-value: 0.2530
- N samples: 141

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.614 ***
- Linear fit: y = -0.246x + 10.7
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.326 ***
- Linear fit: y = -1.666x + 4.1
- P-value: 0.0001
- N samples: 141

**Is Open Source:**
- Correlation: 0.305 ***
- Linear fit: y = 1.590x + 2.4
- P-value: 0.0002
- N samples: 141

**Model Size (B):**
- Correlation: -0.151 
- Linear fit: y = -0.000x + 3.5
- P-value: 0.0776
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: 0.006 
- Linear fit: y = 0.000x + 3.3
- P-value: 0.9408
- N samples: 145

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.389 ***
- Linear fit: y = -0.319x + 15.1
- P-value: 0.0000
- N samples: 141

**Is Open Source:**
- Correlation: 0.166 *
- Linear fit: y = 1.765x + 4.5
- P-value: 0.0498
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.123 
- Linear fit: y = -1.282x + 6.2
- P-value: 0.1470
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.005x + 3.5
- P-value: 0.2334
- N samples: 145

**Model Size (B):**
- Correlation: -0.042 
- Linear fit: y = -0.000x + 5.4
- P-value: 0.6277
- N samples: 138

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.492 ***
- Linear fit: y = -0.602x + 34.9
- P-value: 0.0000
- N samples: 141

**Is Open Source:**
- Correlation: 0.216 *
- Linear fit: y = 3.437x + 14.8
- P-value: 0.0102
- N samples: 141

**Model Size (B):**
- Correlation: -0.173 *
- Linear fit: y = -0.002x + 17.9
- P-value: 0.0419
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.113 
- Linear fit: y = -1.754x + 17.7
- P-value: 0.1841
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: 0.025 
- Linear fit: y = 0.002x + 16.3
- P-value: 0.7651
- N samples: 145

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.137 
- Linear fit: y = -0.073x + 2.9
- P-value: 0.1045
- N samples: 141

**Model Size (B):**
- Correlation: -0.067 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.4327
- N samples: 138

**Is Open Source:**
- Correlation: -0.055 
- Linear fit: y = -0.381x + 0.9
- P-value: 0.5148
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.045 
- Linear fit: y = -0.001x + 1.3
- P-value: 0.5894
- N samples: 145

**Is Reasoning Model:**
- Correlation: 0.041 
- Linear fit: y = 0.276x + 0.5
- P-value: 0.6308
- N samples: 141

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.795 ***
- Linear fit: y = -2.986x + 158.4
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.689 ***
- Linear fit: y = -32.992x + 85.1
- P-value: 0.0000
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.369 ***
- Linear fit: y = -0.080x + 103.7
- P-value: 0.0000
- N samples: 145

**Model Size (B):**
- Correlation: -0.135 
- Linear fit: y = -0.004x + 70.2
- P-value: 0.1154
- N samples: 138

**Is Open Source:**
- Correlation: 0.128 
- Linear fit: y = 6.254x + 65.4
- P-value: 0.1306
- N samples: 141

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.446 ***
- Linear fit: y = -0.287x + 16.3
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.402 ***
- Linear fit: y = -3.297x + 9.4
- P-value: 0.0000
- N samples: 141

**Model Size (B):**
- Correlation: -0.113 
- Linear fit: y = -0.001x + 7.9
- P-value: 0.1872
- N samples: 138

**Days Since 2024-01-01:**
- Correlation: 0.035 
- Linear fit: y = 0.001x + 7.3
- P-value: 0.6734
- N samples: 145

**Is Open Source:**
- Correlation: 0.017 
- Linear fit: y = 0.145x + 7.7
- P-value: 0.8386
- N samples: 141

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.216 **
- Linear fit: y = 0.001x + -0.3
- P-value: 0.0091
- N samples: 145

**Model Size (B):**
- Correlation: 0.094 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.2719
- N samples: 138

**Is Open Source:**
- Correlation: 0.061 
- Linear fit: y = 0.069x + 0.1
- P-value: 0.4731
- N samples: 141

**Benchmark Score:**
- Correlation: 0.060 
- Linear fit: y = 0.005x + 0.0
- P-value: 0.4820
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.014 
- Linear fit: y = -0.015x + 0.2
- P-value: 0.8708
- N samples: 141

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.406 ***
- Linear fit: y = -0.292x + 12.3
- P-value: 0.0000
- N samples: 141

**Is Open Source:**
- Correlation: 0.196 *
- Linear fit: y = 1.836x + 2.4
- P-value: 0.0200
- N samples: 141

**Model Size (B):**
- Correlation: -0.151 
- Linear fit: y = -0.001x + 4.1
- P-value: 0.0777
- N samples: 138

**Is Reasoning Model:**
- Correlation: 0.109 
- Linear fit: y = 1.005x + 3.1
- P-value: 0.1964
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: 0.033 
- Linear fit: y = 0.002x + 3.1
- P-value: 0.6901
- N samples: 145

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.553 ***
- Linear fit: y = -0.528x + 25.9
- P-value: 0.0000
- N samples: 141

**Is Reasoning Model:**
- Correlation: -0.295 ***
- Linear fit: y = -3.588x + 11.8
- P-value: 0.0004
- N samples: 141

**Model Size (B):**
- Correlation: -0.189 *
- Linear fit: y = -0.001x + 10.4
- P-value: 0.0261
- N samples: 138

**Is Open Source:**
- Correlation: 0.144 
- Linear fit: y = 1.788x + 9.0
- P-value: 0.0890
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.048 
- Linear fit: y = -0.003x + 11.2
- P-value: 0.5686
- N samples: 145

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.259 **
- Linear fit: y = -1.625x + 4.6
- P-value: 0.0019
- N samples: 141

**Model Size (B):**
- Correlation: 0.232 **
- Linear fit: y = 0.001x + 3.3
- P-value: 0.0062
- N samples: 138

**Is Reasoning Model:**
- Correlation: -0.189 *
- Linear fit: y = -1.161x + 4.2
- P-value: 0.0246
- N samples: 141

**Benchmark Score:**
- Correlation: 0.029 
- Linear fit: y = 0.014x + 3.2
- P-value: 0.7334
- N samples: 141

**Days Since 2024-01-01:**
- Correlation: -0.016 
- Linear fit: y = -0.000x + 3.8
- P-value: 0.8472
- N samples: 145

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.859, y = -7.829x + 401.7

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.795, y = -2.986x + 158.4

**category3_logical_errors vs Benchmark Score:**
  r = -0.785, y = -3.268x + 174.8

**category1_input_misalignment vs Benchmark Score:**
  r = -0.760, y = -2.191x + 107.7

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.689, y = -32.992x + 85.1

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.684, y = -36.305x + 94.7

**1b_context_omission vs Benchmark Score:**
  r = -0.660, y = -1.580x + 79.9

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.643, y = -0.089x + 70.9

**1a_instruction_override vs Benchmark Score:**
  r = -0.622, y = -0.365x + 17.1

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.614, y = -0.246x + 10.7

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.596, y = -0.100x + 84.9

**total_hallucinations vs Is Reasoning Model:**
  r = -0.579, y = -67.207x + 200.2

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.553, y = -0.528x + 25.9

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.545, y = -20.010x + 51.9

**1b_context_omission vs Is Reasoning Model:**
  r = -0.539, y = -16.442x + 40.6

**category4_technical_errors vs Benchmark Score:**
  r = -0.529, y = -0.807x + 41.4

**category2_factual_errors vs Benchmark Score:**
  r = -0.514, y = -0.993x + 52.8

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.492, y = -0.602x + 34.9

**3b_self_contradiction vs Benchmark Score:**
  r = -0.446, y = -0.287x + 16.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.406, y = -0.292x + 12.3

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.402, y = -3.297x + 9.4

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.389, y = -0.319x + 15.1

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.369, y = -0.080x + 103.7

**total_hallucinations vs Days Since 2024-01-01:**
  r = -0.339, y = -0.181x + 246.0

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.326, y = -1.666x + 4.1

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.324, y = -0.078x + 110.7

**1a_instruction_override vs Days Since 2024-01-01:**
  r = -0.307, y = -0.010x + 10.8

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.305, y = 1.590x + 2.4


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
- Correlation: 0.206 *
- Linear fit: y = 0.145x + 17.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.708 ***
- Linear fit: y = 1.021x + 34.2

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.278 ***
- Linear fit: y = 0.159x + 10.8

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.452 ***
- Linear fit: y = 0.923x + 55.5

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.557 ***
- Linear fit: y = 0.451x + 6.9

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.544 ***
- Linear fit: y = 0.215x + 0.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.992 ***, y = 0.896x + -0.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.964 ***, y = 0.802x + -1.2

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.878 ***, y = 0.557x + 4.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.805 ***, y = 0.467x + 1.9

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.751 ***, y = 0.313x + -1.7

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.739 ***, y = 0.963x + 28.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.724 ***, y = 0.401x + -3.2

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.708 ***, y = 1.021x + 34.2

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.683 ***, y = 1.071x + 34.3

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.668 ***, y = 0.103x + -0.1

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.644 ***, y = 0.371x + 3.9

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.635 ***, y = 0.146x + -1.2

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.634 ***, y = 0.129x + 0.8

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.627 ***, y = 0.159x + -1.0

**Category 3: Logical Errors vs 1c: Prompt Contradiction:**
  r = 0.619 ***, y = 0.060x + -1.3

**1c: Prompt Contradiction vs 3a: Unsupported Leap:**
  r = 0.596 ***, y = 5.576x + 50.6

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.567 ***, y = 0.097x + 1.1

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.557 ***, y = 0.451x + 6.9

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.544 ***, y = 0.215x + 0.8

**1c: Prompt Contradiction vs 4b: Model Semantics Breach:**
  r = 0.536 ***, y = 1.277x + 5.8

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
