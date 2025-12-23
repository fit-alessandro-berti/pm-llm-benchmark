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
- Linear fit: y = -2.447x + 128.3
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.552 ***
- Linear fit: y = -25.962x + 55.2
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 10.940x + 37.0
- P-value: 0.0016
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: -0.202 **
- Linear fit: y = -0.032x + 59.3
- P-value: 0.0052
- N samples: 190

**Model Size (B):**
- Correlation: -0.137 
- Linear fit: y = -0.004x + 44.5
- P-value: 0.0628
- N samples: 184

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.539 ***
- Linear fit: y = -1.503x + 80.8
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.279 ***
- Linear fit: y = 0.040x + 7.7
- P-value: 0.0001
- N samples: 190

**Is Reasoning Model:**
- Correlation: -0.239 **
- Linear fit: y = -10.083x + 33.1
- P-value: 0.0011
- N samples: 182

**Is Open Source:**
- Correlation: 0.217 **
- Linear fit: y = 9.162x + 23.4
- P-value: 0.0032
- N samples: 182

**Model Size (B):**
- Correlation: -0.116 
- Linear fit: y = -0.003x + 29.5
- P-value: 0.1171
- N samples: 184

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.772 ***
- Linear fit: y = -3.461x + 196.7
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.643 ***
- Linear fit: y = -43.612x + 96.6
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.179 *
- Linear fit: y = 12.164x + 69.3
- P-value: 0.0154
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: -0.167 *
- Linear fit: y = -0.038x + 95.4
- P-value: 0.0213
- N samples: 190

**Model Size (B):**
- Correlation: -0.118 
- Linear fit: y = -0.004x + 78.4
- P-value: 0.1120
- N samples: 184

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.692 ***
- Linear fit: y = -1.353x + 66.8
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.316 ***
- Linear fit: y = -9.355x + 24.0
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.230 **
- Linear fit: y = 6.797x + 16.0
- P-value: 0.0018
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.150 *
- Linear fit: y = 0.015x + 11.5
- P-value: 0.0387
- N samples: 190

**Model Size (B):**
- Correlation: -0.133 
- Linear fit: y = -0.002x + 20.2
- P-value: 0.0723
- N samples: 184

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.807 ***
- Linear fit: y = -9.548x + 508.7
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.540 ***
- Linear fit: y = -96.776x + 221.2
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.242 ***
- Linear fit: y = 43.403x + 152.0
- P-value: 0.0010
- N samples: 182

**Model Size (B):**
- Correlation: -0.143 
- Linear fit: y = -0.014x + 181.8
- P-value: 0.0521
- N samples: 184

**Days Since 2024-01-01:**
- Correlation: -0.022 
- Linear fit: y = -0.013x + 181.3
- P-value: 0.7620
- N samples: 190

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.787 ***
- Linear fit: y = -2.447x + 128.3
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.552 ***
- Linear fit: y = -25.962x + 55.2
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 10.940x + 37.0
- P-value: 0.0016
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: -0.202 **
- Linear fit: y = -0.032x + 59.3
- P-value: 0.0052
- N samples: 190

**Model Size (B):**
- Correlation: -0.137 
- Linear fit: y = -0.004x + 44.5
- P-value: 0.0628
- N samples: 184

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.539 ***
- Linear fit: y = -1.503x + 80.8
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.279 ***
- Linear fit: y = 0.040x + 7.7
- P-value: 0.0001
- N samples: 190

**Is Reasoning Model:**
- Correlation: -0.239 **
- Linear fit: y = -10.083x + 33.1
- P-value: 0.0011
- N samples: 182

**Is Open Source:**
- Correlation: 0.217 **
- Linear fit: y = 9.162x + 23.4
- P-value: 0.0032
- N samples: 182

**Model Size (B):**
- Correlation: -0.116 
- Linear fit: y = -0.003x + 29.5
- P-value: 0.1171
- N samples: 184

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.772 ***
- Linear fit: y = -3.461x + 196.7
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.643 ***
- Linear fit: y = -43.612x + 96.6
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.179 *
- Linear fit: y = 12.164x + 69.3
- P-value: 0.0154
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: -0.167 *
- Linear fit: y = -0.038x + 95.4
- P-value: 0.0213
- N samples: 190

**Model Size (B):**
- Correlation: -0.118 
- Linear fit: y = -0.004x + 78.4
- P-value: 0.1120
- N samples: 184

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.692 ***
- Linear fit: y = -1.353x + 66.8
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.316 ***
- Linear fit: y = -9.355x + 24.0
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.230 **
- Linear fit: y = 6.797x + 16.0
- P-value: 0.0018
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.150 *
- Linear fit: y = 0.015x + 11.5
- P-value: 0.0387
- N samples: 190

**Model Size (B):**
- Correlation: -0.133 
- Linear fit: y = -0.002x + 20.2
- P-value: 0.0723
- N samples: 184

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.640 ***
- Linear fit: y = -0.473x + 24.1
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.394 ***
- Linear fit: y = -4.401x + 9.6
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.273 ***
- Linear fit: y = 3.049x + 5.9
- P-value: 0.0002
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.141 
- Linear fit: y = 0.005x + 4.7
- P-value: 0.0529
- N samples: 190

**Model Size (B):**
- Correlation: -0.103 
- Linear fit: y = -0.001x + 7.7
- P-value: 0.1631
- N samples: 184

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.712 ***
- Linear fit: y = -1.581x + 86.3
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.546 ***
- Linear fit: y = -18.328x + 39.8
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: -0.382 ***
- Linear fit: y = -0.043x + 53.6
- P-value: 0.0000
- N samples: 190

**Is Open Source:**
- Correlation: 0.152 *
- Linear fit: y = 5.120x + 28.3
- P-value: 0.0399
- N samples: 182

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.002x + 32.3
- P-value: 0.1080
- N samples: 184

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.702 ***
- Linear fit: y = -0.393x + 17.9
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.382 ***
- Linear fit: y = -3.234x + 5.7
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.327 ***
- Linear fit: y = 2.771x + 2.7
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.217 **
- Linear fit: y = 0.006x + 0.9
- P-value: 0.0027
- N samples: 190

**Model Size (B):**
- Correlation: -0.154 *
- Linear fit: y = -0.001x + 4.4
- P-value: 0.0370
- N samples: 184

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.497 ***
- Linear fit: y = -0.752x + 34.4
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.292 ***
- Linear fit: y = 0.022x + -3.5
- P-value: 0.0000
- N samples: 190

**Is Reasoning Model:**
- Correlation: -0.243 ***
- Linear fit: y = -5.568x + 10.8
- P-value: 0.0009
- N samples: 182

**Is Open Source:**
- Correlation: 0.213 **
- Linear fit: y = 4.865x + 5.6
- P-value: 0.0040
- N samples: 182

**Model Size (B):**
- Correlation: -0.058 
- Linear fit: y = -0.001x + 8.5
- P-value: 0.4342
- N samples: 184

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.475 ***
- Linear fit: y = -0.701x + 44.0
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.240 ***
- Linear fit: y = 0.018x + 10.1
- P-value: 0.0009
- N samples: 190

**Is Reasoning Model:**
- Correlation: -0.212 **
- Linear fit: y = -4.725x + 21.7
- P-value: 0.0041
- N samples: 182

**Is Open Source:**
- Correlation: 0.199 **
- Linear fit: y = 4.433x + 17.1
- P-value: 0.0072
- N samples: 182

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.002x + 20.2
- P-value: 0.0587
- N samples: 184

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.125 
- Linear fit: y = -0.050x + 2.4
- P-value: 0.0914
- N samples: 182

**Model Size (B):**
- Correlation: -0.073 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.3231
- N samples: 184

**Days Since 2024-01-01:**
- Correlation: -0.043 
- Linear fit: y = -0.001x + 1.1
- P-value: 0.5602
- N samples: 190

**Is Reasoning Model:**
- Correlation: 0.035 
- Linear fit: y = 0.210x + 0.5
- P-value: 0.6391
- N samples: 182

**Is Open Source:**
- Correlation: -0.023 
- Linear fit: y = -0.136x + 0.7
- P-value: 0.7612
- N samples: 182

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.761 ***
- Linear fit: y = -2.849x + 165.7
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.651 ***
- Linear fit: y = -36.896x + 83.8
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: -0.254 ***
- Linear fit: y = -0.048x + 91.1
- P-value: 0.0004
- N samples: 190

**Is Open Source:**
- Correlation: 0.156 *
- Linear fit: y = 8.871x + 61.4
- P-value: 0.0349
- N samples: 182

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.003x + 68.2
- P-value: 0.1558
- N samples: 184

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.632 ***
- Linear fit: y = -0.576x + 29.4
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.466 ***
- Linear fit: y = -6.428x + 12.3
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.218 **
- Linear fit: y = 3.012x + 7.7
- P-value: 0.0031
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.202 **
- Linear fit: y = 0.009x + 4.5
- P-value: 0.0052
- N samples: 190

**Model Size (B):**
- Correlation: -0.139 
- Linear fit: y = -0.001x + 9.8
- P-value: 0.0606
- N samples: 184

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.344 ***
- Linear fit: y = -0.036x + 1.6
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.202 **
- Linear fit: y = 0.001x + -0.2
- P-value: 0.0051
- N samples: 190

**Is Reasoning Model:**
- Correlation: -0.183 *
- Linear fit: y = -0.289x + 0.5
- P-value: 0.0134
- N samples: 182

**Is Open Source:**
- Correlation: 0.178 *
- Linear fit: y = 0.281x + 0.2
- P-value: 0.0161
- N samples: 182

**Model Size (B):**
- Correlation: -0.057 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4443
- N samples: 184

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.615 ***
- Linear fit: y = -0.627x + 27.1
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.303 ***
- Linear fit: y = 4.680x + 2.8
- P-value: 0.0000
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.243 ***
- Linear fit: y = 0.013x + -1.3
- P-value: 0.0007
- N samples: 190

**Model Size (B):**
- Correlation: -0.155 *
- Linear fit: y = -0.001x + 5.8
- P-value: 0.0356
- N samples: 184

**Is Reasoning Model:**
- Correlation: -0.149 *
- Linear fit: y = -2.302x + 6.3
- P-value: 0.0443
- N samples: 182

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.709 ***
- Linear fit: y = -0.680x + 34.1
- P-value: 0.0000
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.409 ***
- Linear fit: y = -5.936x + 13.2
- P-value: 0.0000
- N samples: 182

**Is Open Source:**
- Correlation: 0.242 **
- Linear fit: y = 3.509x + 8.5
- P-value: 0.0010
- N samples: 182

**Model Size (B):**
- Correlation: -0.190 **
- Linear fit: y = -0.002x + 10.9
- P-value: 0.0099
- N samples: 184

**Days Since 2024-01-01:**
- Correlation: 0.049 
- Linear fit: y = 0.002x + 9.0
- P-value: 0.5013
- N samples: 190

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.217 **
- Linear fit: y = -1.393x + 4.7
- P-value: 0.0032
- N samples: 182

**Model Size (B):**
- Correlation: 0.188 *
- Linear fit: y = 0.001x + 3.6
- P-value: 0.0108
- N samples: 184

**Is Reasoning Model:**
- Correlation: -0.174 *
- Linear fit: y = -1.117x + 4.5
- P-value: 0.0185
- N samples: 182

**Benchmark Score:**
- Correlation: -0.109 
- Linear fit: y = -0.046x + 5.6
- P-value: 0.1434
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.000 
- Linear fit: y = 0.000x + 3.8
- P-value: 0.9990
- N samples: 190

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.807, y = -9.548x + 508.7

**category1_input_misalignment vs Benchmark Score:**
  r = -0.787, y = -2.447x + 128.3

**category3_logical_errors vs Benchmark Score:**
  r = -0.772, y = -3.461x + 196.7

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.761, y = -2.849x + 165.7

**1b_context_omission vs Benchmark Score:**
  r = -0.712, y = -1.581x + 86.3

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.709, y = -0.680x + 34.1

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.702, y = -0.393x + 17.9

**category4_technical_errors vs Benchmark Score:**
  r = -0.692, y = -1.353x + 66.8

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.651, y = -36.896x + 83.8

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.643, y = -43.612x + 96.6

**1a_instruction_override vs Benchmark Score:**
  r = -0.640, y = -0.473x + 24.1

**3b_self_contradiction vs Benchmark Score:**
  r = -0.632, y = -0.576x + 29.4

**4a_syntax_error vs Benchmark Score:**
  r = -0.615, y = -0.627x + 27.1

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.552, y = -25.962x + 55.2

**1b_context_omission vs Is Reasoning Model:**
  r = -0.546, y = -18.328x + 39.8

**total_hallucinations vs Is Reasoning Model:**
  r = -0.540, y = -96.776x + 221.2

**category2_factual_errors vs Benchmark Score:**
  r = -0.539, y = -1.503x + 80.8

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.497, y = -0.752x + 34.4

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.475, y = -0.701x + 44.0

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.466, y = -6.428x + 12.3

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.409, y = -5.936x + 13.2

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.394, y = -4.401x + 9.6

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.382, y = -0.043x + 53.6

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.382, y = -3.234x + 5.7

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.344, y = -0.036x + 1.6

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.327, y = 2.771x + 2.7

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.316, y = -9.355x + 24.0

**4a_syntax_error vs Is Open Source:**
  r = 0.303, y = 4.680x + 2.8


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
- Correlation: 0.525 ***
- Linear fit: y = 0.469x + 8.1

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.817 ***
- Linear fit: y = 1.170x + 25.7

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.645 ***
- Linear fit: y = 0.404x + 1.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.633 ***
- Linear fit: y = 1.015x + 47.1

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.725 ***
- Linear fit: y = 0.509x + 4.8

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.710 ***
- Linear fit: y = 0.311x + -4.3

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.988 ***, y = 0.827x + 3.4

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.949 ***, y = 0.681x + 2.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.900 ***, y = 0.441x + 1.7

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.889 ***, y = 0.483x + -5.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.884 ***, y = 0.468x + 6.2

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.876 ***, y = 0.455x + -3.6

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.817 ***, y = 1.170x + 25.7

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.805 ***, y = 0.164x + -3.1

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.802 ***, y = 0.962x + 25.0

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.790 ***, y = 1.274x + 4.0

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.781 ***, y = 0.470x + 5.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.781 ***, y = 0.185x + -0.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.779 ***, y = 0.362x + 2.3

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.777 ***, y = 1.299x + 25.7

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.770 ***, y = 0.251x + 2.2

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.769 ***, y = 2.064x + -0.4

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.761 ***, y = 0.381x + 2.3

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.744 ***, y = 0.567x + -0.1

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.742 ***, y = 0.498x + 1.1

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.741 ***, y = 0.134x + -1.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
