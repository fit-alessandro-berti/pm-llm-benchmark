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
- Correlation: -0.788 ***
- Linear fit: y = -2.430x + 127.4
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.560 ***
- Linear fit: y = -26.088x + 55.3
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.235 **
- Linear fit: y = 10.991x + 37.0
- P-value: 0.0019
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: -0.213 **
- Linear fit: y = -0.034x + 60.3
- P-value: 0.0042
- N samples: 179

**Model Size (B):**
- Correlation: -0.137 
- Linear fit: y = -0.003x + 44.2
- P-value: 0.0686
- N samples: 178

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.532 ***
- Linear fit: y = -1.520x + 81.5
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.316 ***
- Linear fit: y = 0.047x + 4.7
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.249 **
- Linear fit: y = -10.731x + 33.8
- P-value: 0.0010
- N samples: 171

**Is Open Source:**
- Correlation: 0.214 **
- Linear fit: y = 9.275x + 23.6
- P-value: 0.0049
- N samples: 171

**Model Size (B):**
- Correlation: -0.113 
- Linear fit: y = -0.003x + 29.5
- P-value: 0.1317
- N samples: 178

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.762 ***
- Linear fit: y = -3.396x + 195.2
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.662 ***
- Linear fit: y = -44.605x + 98.3
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.163 *
- Linear fit: y = 10.984x + 71.2
- P-value: 0.0336
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: -0.127 
- Linear fit: y = -0.029x + 91.9
- P-value: 0.0904
- N samples: 179

**Model Size (B):**
- Correlation: -0.118 
- Linear fit: y = -0.004x + 78.8
- P-value: 0.1159
- N samples: 178

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.679 ***
- Linear fit: y = -1.292x + 64.5
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.312 ***
- Linear fit: y = -8.960x + 23.8
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.204 **
- Linear fit: y = 5.878x + 16.4
- P-value: 0.0075
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.172 *
- Linear fit: y = 0.017x + 10.6
- P-value: 0.0215
- N samples: 179

**Model Size (B):**
- Correlation: -0.127 
- Linear fit: y = -0.002x + 19.9
- P-value: 0.0915
- N samples: 178

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.797 ***
- Linear fit: y = -9.399x + 503.9
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.552 ***
- Linear fit: y = -98.294x + 223.8
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.230 **
- Linear fit: y = 41.152x + 154.9
- P-value: 0.0024
- N samples: 171

**Model Size (B):**
- Correlation: -0.141 
- Linear fit: y = -0.014x + 181.6
- P-value: 0.0601
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.007 
- Linear fit: y = 0.004x + 174.1
- P-value: 0.9255
- N samples: 179

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.788 ***
- Linear fit: y = -2.430x + 127.4
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.560 ***
- Linear fit: y = -26.088x + 55.3
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.235 **
- Linear fit: y = 10.991x + 37.0
- P-value: 0.0019
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: -0.213 **
- Linear fit: y = -0.034x + 60.3
- P-value: 0.0042
- N samples: 179

**Model Size (B):**
- Correlation: -0.137 
- Linear fit: y = -0.003x + 44.2
- P-value: 0.0686
- N samples: 178

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.532 ***
- Linear fit: y = -1.520x + 81.5
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.316 ***
- Linear fit: y = 0.047x + 4.7
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.249 **
- Linear fit: y = -10.731x + 33.8
- P-value: 0.0010
- N samples: 171

**Is Open Source:**
- Correlation: 0.214 **
- Linear fit: y = 9.275x + 23.6
- P-value: 0.0049
- N samples: 171

**Model Size (B):**
- Correlation: -0.113 
- Linear fit: y = -0.003x + 29.5
- P-value: 0.1317
- N samples: 178

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.762 ***
- Linear fit: y = -3.396x + 195.2
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.662 ***
- Linear fit: y = -44.605x + 98.3
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.163 *
- Linear fit: y = 10.984x + 71.2
- P-value: 0.0336
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: -0.127 
- Linear fit: y = -0.029x + 91.9
- P-value: 0.0904
- N samples: 179

**Model Size (B):**
- Correlation: -0.118 
- Linear fit: y = -0.004x + 78.8
- P-value: 0.1159
- N samples: 178

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.679 ***
- Linear fit: y = -1.292x + 64.5
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.312 ***
- Linear fit: y = -8.960x + 23.8
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.204 **
- Linear fit: y = 5.878x + 16.4
- P-value: 0.0075
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.172 *
- Linear fit: y = 0.017x + 10.6
- P-value: 0.0215
- N samples: 179

**Model Size (B):**
- Correlation: -0.127 
- Linear fit: y = -0.002x + 19.9
- P-value: 0.0915
- N samples: 178

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.640 ***
- Linear fit: y = -0.463x + 23.5
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.381 ***
- Linear fit: y = -4.162x + 9.4
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.291 ***
- Linear fit: y = 3.183x + 5.7
- P-value: 0.0001
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.139 
- Linear fit: y = 0.005x + 4.8
- P-value: 0.0640
- N samples: 179

**Model Size (B):**
- Correlation: -0.099 
- Linear fit: y = -0.001x + 7.6
- P-value: 0.1879
- N samples: 178

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.709 ***
- Linear fit: y = -1.567x + 85.7
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.557 ***
- Linear fit: y = -18.584x + 40.1
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: -0.404 ***
- Linear fit: y = -0.047x + 55.1
- P-value: 0.0000
- N samples: 179

**Is Open Source:**
- Correlation: 0.145 
- Linear fit: y = 4.866x + 28.6
- P-value: 0.0577
- N samples: 171

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.002x + 32.2
- P-value: 0.1151
- N samples: 178

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.694 ***
- Linear fit: y = -0.400x + 18.1
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.383 ***
- Linear fit: y = -3.342x + 5.8
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.337 ***
- Linear fit: y = 2.942x + 2.6
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.246 ***
- Linear fit: y = 0.007x + 0.4
- P-value: 0.0009
- N samples: 179

**Model Size (B):**
- Correlation: -0.151 *
- Linear fit: y = -0.001x + 4.4
- P-value: 0.0436
- N samples: 178

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.487 ***
- Linear fit: y = -0.757x + 34.7
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.327 ***
- Linear fit: y = 0.026x + -5.1
- P-value: 0.0000
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.245 **
- Linear fit: y = -5.756x + 11.1
- P-value: 0.0012
- N samples: 171

**Is Open Source:**
- Correlation: 0.215 **
- Linear fit: y = 5.075x + 5.6
- P-value: 0.0047
- N samples: 171

**Model Size (B):**
- Correlation: -0.057 
- Linear fit: y = -0.001x + 8.5
- P-value: 0.4534
- N samples: 178

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.478 ***
- Linear fit: y = -0.713x + 44.4
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.273 ***
- Linear fit: y = 0.021x + 8.8
- P-value: 0.0002
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.230 **
- Linear fit: y = -5.175x + 22.1
- P-value: 0.0025
- N samples: 171

**Is Open Source:**
- Correlation: 0.195 *
- Linear fit: y = 4.402x + 17.2
- P-value: 0.0107
- N samples: 171

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.002x + 20.2
- P-value: 0.0666
- N samples: 178

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.121 
- Linear fit: y = -0.049x + 2.4
- P-value: 0.1159
- N samples: 171

**Model Size (B):**
- Correlation: -0.072 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.3372
- N samples: 178

**Is Open Source:**
- Correlation: -0.032 
- Linear fit: y = -0.201x + 0.8
- P-value: 0.6738
- N samples: 171

**Is Reasoning Model:**
- Correlation: 0.032 
- Linear fit: y = 0.200x + 0.6
- P-value: 0.6752
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: -0.032 
- Linear fit: y = -0.001x + 1.0
- P-value: 0.6749
- N samples: 179

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.752 ***
- Linear fit: y = -2.801x + 164.9
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.674 ***
- Linear fit: y = -37.907x + 85.5
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: -0.214 **
- Linear fit: y = -0.041x + 88.3
- P-value: 0.0041
- N samples: 179

**Is Open Source:**
- Correlation: 0.137 
- Linear fit: y = 7.742x + 63.3
- P-value: 0.0735
- N samples: 171

**Model Size (B):**
- Correlation: -0.107 
- Linear fit: y = -0.003x + 68.7
- P-value: 0.1555
- N samples: 178

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.616 ***
- Linear fit: y = -0.559x + 28.7
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.468 ***
- Linear fit: y = -6.419x + 12.3
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.227 **
- Linear fit: y = 0.011x + 3.9
- P-value: 0.0023
- N samples: 179

**Is Open Source:**
- Correlation: 0.216 **
- Linear fit: y = 2.964x + 7.7
- P-value: 0.0046
- N samples: 171

**Model Size (B):**
- Correlation: -0.135 
- Linear fit: y = -0.001x + 9.7
- P-value: 0.0727
- N samples: 178

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.335 ***
- Linear fit: y = -0.036x + 1.6
- P-value: 0.0000
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.235 **
- Linear fit: y = 0.001x + -0.3
- P-value: 0.0015
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.173 *
- Linear fit: y = -0.279x + 0.5
- P-value: 0.0239
- N samples: 171

**Is Open Source:**
- Correlation: 0.172 *
- Linear fit: y = 0.279x + 0.2
- P-value: 0.0244
- N samples: 171

**Model Size (B):**
- Correlation: -0.056 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4565
- N samples: 178

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.609 ***
- Linear fit: y = -0.589x + 25.6
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.295 ***
- Linear fit: y = 4.321x + 2.7
- P-value: 0.0001
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.255 ***
- Linear fit: y = 0.013x + -1.5
- P-value: 0.0006
- N samples: 179

**Model Size (B):**
- Correlation: -0.155 *
- Linear fit: y = -0.001x + 5.5
- P-value: 0.0392
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.131 
- Linear fit: y = -1.914x + 6.0
- P-value: 0.0880
- N samples: 171

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.693 ***
- Linear fit: y = -0.661x + 33.4
- P-value: 0.0000
- N samples: 171

**Is Reasoning Model:**
- Correlation: -0.402 ***
- Linear fit: y = -5.791x + 13.2
- P-value: 0.0000
- N samples: 171

**Is Open Source:**
- Correlation: 0.221 **
- Linear fit: y = 3.194x + 8.7
- P-value: 0.0036
- N samples: 171

**Model Size (B):**
- Correlation: -0.186 *
- Linear fit: y = -0.001x + 10.9
- P-value: 0.0130
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.075 
- Linear fit: y = 0.004x + 8.4
- P-value: 0.3170
- N samples: 179

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.251 ***
- Linear fit: y = -1.637x + 4.9
- P-value: 0.0009
- N samples: 171

**Model Size (B):**
- Correlation: 0.195 **
- Linear fit: y = 0.001x + 3.6
- P-value: 0.0091
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.193 *
- Linear fit: y = -1.256x + 4.6
- P-value: 0.0115
- N samples: 171

**Benchmark Score:**
- Correlation: -0.097 
- Linear fit: y = -0.042x + 5.4
- P-value: 0.2068
- N samples: 171

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 3.6
- P-value: 0.7791
- N samples: 179

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.797, y = -9.399x + 503.9

**category1_input_misalignment vs Benchmark Score:**
  r = -0.788, y = -2.430x + 127.4

**category3_logical_errors vs Benchmark Score:**
  r = -0.762, y = -3.396x + 195.2

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.752, y = -2.801x + 164.9

**1b_context_omission vs Benchmark Score:**
  r = -0.709, y = -1.567x + 85.7

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.694, y = -0.400x + 18.1

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.693, y = -0.661x + 33.4

**category4_technical_errors vs Benchmark Score:**
  r = -0.679, y = -1.292x + 64.5

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.674, y = -37.907x + 85.5

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.662, y = -44.605x + 98.3

**1a_instruction_override vs Benchmark Score:**
  r = -0.640, y = -0.463x + 23.5

**3b_self_contradiction vs Benchmark Score:**
  r = -0.616, y = -0.559x + 28.7

**4a_syntax_error vs Benchmark Score:**
  r = -0.609, y = -0.589x + 25.6

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.560, y = -26.088x + 55.3

**1b_context_omission vs Is Reasoning Model:**
  r = -0.557, y = -18.584x + 40.1

**total_hallucinations vs Is Reasoning Model:**
  r = -0.552, y = -98.294x + 223.8

**category2_factual_errors vs Benchmark Score:**
  r = -0.532, y = -1.520x + 81.5

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.487, y = -0.757x + 34.7

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.478, y = -0.713x + 44.4

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.468, y = -6.419x + 12.3

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.404, y = -0.047x + 55.1

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.402, y = -5.791x + 13.2

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.383, y = -3.342x + 5.8

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.381, y = -4.162x + 9.4

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.337, y = 2.942x + 2.6

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.335, y = -0.036x + 1.6

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.327, y = 0.026x + -5.1

**category2_factual_errors vs Days Since 2024-01-01:**
  r = 0.316, y = 0.047x + 4.7

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.312, y = -8.960x + 23.8


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
- Correlation: 0.528 ***
- Linear fit: y = 0.485x + 7.6

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.815 ***
- Linear fit: y = 1.171x + 26.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.624 ***
- Linear fit: y = 0.384x + 2.7

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.634 ***
- Linear fit: y = 0.991x + 48.8

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.744 ***
- Linear fit: y = 0.499x + 5.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.707 ***
- Linear fit: y = 0.303x + -4.1

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.988 ***, y = 0.827x + 3.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.946 ***, y = 0.683x + 2.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.897 ***, y = 0.449x + 1.7

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.893 ***, y = 0.486x + -5.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.885 ***, y = 0.464x + 6.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.867 ***, y = 0.439x + -3.4

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.815 ***, y = 1.171x + 26.8

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.806 ***, y = 0.164x + -3.3

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.806 ***, y = 0.969x + 25.8

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.790 ***, y = 1.239x + 4.1

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.788 ***, y = 0.461x + 5.5

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.781 ***, y = 0.248x + 2.2

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.776 ***, y = 0.484x + 1.0

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.774 ***, y = 1.290x + 27.0

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.767 ***, y = 0.180x + -0.3

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.765 ***, y = 2.052x + -0.3

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.764 ***, y = 0.363x + 2.3

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.753 ***, y = 0.378x + 2.2

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.751 ***, y = 0.599x + -0.2

**Category 4: Technical Errors vs 1c: Prompt Contradiction:**
  r = 0.747 ***, y = 0.226x + -0.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
