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
- Correlation: -0.486 ***
- Linear fit: y = -0.075x + 123.4
- P-value: 0.0000
- N samples: 106

**Benchmark Score:**
- Correlation: -0.475 ***
- Linear fit: y = -2.196x + 137.6
- P-value: 0.0000
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.449 ***
- Linear fit: y = -22.811x + 88.4
- P-value: 0.0000
- N samples: 106

**Model Size (B):**
- Correlation: 0.127 
- Linear fit: y = 0.002x + 74.7
- P-value: 0.2025
- N samples: 102

**Is Open Source:**
- Correlation: -0.081 
- Linear fit: y = -4.111x + 77.6
- P-value: 0.4085
- N samples: 106

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.308 **
- Linear fit: y = -1.528x + 95.8
- P-value: 0.0013
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: 0.126 
- Linear fit: y = 0.021x + 39.5
- P-value: 0.1995
- N samples: 106

**Is Open Source:**
- Correlation: 0.092 
- Linear fit: y = 4.976x + 50.5
- P-value: 0.3503
- N samples: 106

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.001x + 53.4
- P-value: 0.5467
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.042 
- Linear fit: y = -2.309x + 54.0
- P-value: 0.6658
- N samples: 106

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.407 ***
- Linear fit: y = -16.744x + 115.7
- P-value: 0.0000
- N samples: 106

**Is Open Source:**
- Correlation: -0.253 **
- Linear fit: y = -10.368x + 111.0
- P-value: 0.0089
- N samples: 106

**Benchmark Score:**
- Correlation: -0.240 *
- Linear fit: y = -0.897x + 131.6
- P-value: 0.0134
- N samples: 106

**Model Size (B):**
- Correlation: 0.116 
- Linear fit: y = 0.002x + 105.1
- P-value: 0.2470
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: 0.018 
- Linear fit: y = 0.002x + 104.9
- P-value: 0.8582
- N samples: 106

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.530 ***
- Linear fit: y = -1.204x + 66.7
- P-value: 0.0000
- N samples: 106

**Model Size (B):**
- Correlation: -0.248 *
- Linear fit: y = -0.002x + 34.5
- P-value: 0.0118
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.217 *
- Linear fit: y = -5.397x + 35.8
- P-value: 0.0257
- N samples: 106

**Is Open Source:**
- Correlation: 0.062 
- Linear fit: y = 1.539x + 32.1
- P-value: 0.5286
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: -0.020 
- Linear fit: y = -0.001x + 33.7
- P-value: 0.8420
- N samples: 106

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.587 ***
- Linear fit: y = -6.311x + 454.6
- P-value: 0.0000
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.431 ***
- Linear fit: y = -50.797x + 305.0
- P-value: 0.0000
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: -0.152 
- Linear fit: y = -0.055x + 311.4
- P-value: 0.1197
- N samples: 106

**Is Open Source:**
- Correlation: -0.059 
- Linear fit: y = -7.001x + 279.9
- P-value: 0.5448
- N samples: 106

**Model Size (B):**
- Correlation: 0.008 
- Linear fit: y = 0.000x + 277.1
- P-value: 0.9403
- N samples: 102

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.486 ***
- Linear fit: y = -0.075x + 123.4
- P-value: 0.0000
- N samples: 106

**Benchmark Score:**
- Correlation: -0.475 ***
- Linear fit: y = -2.196x + 137.6
- P-value: 0.0000
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.449 ***
- Linear fit: y = -22.811x + 88.4
- P-value: 0.0000
- N samples: 106

**Model Size (B):**
- Correlation: 0.127 
- Linear fit: y = 0.002x + 74.7
- P-value: 0.2025
- N samples: 102

**Is Open Source:**
- Correlation: -0.081 
- Linear fit: y = -4.111x + 77.6
- P-value: 0.4085
- N samples: 106

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.308 **
- Linear fit: y = -1.528x + 95.8
- P-value: 0.0013
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: 0.126 
- Linear fit: y = 0.021x + 39.5
- P-value: 0.1995
- N samples: 106

**Is Open Source:**
- Correlation: 0.092 
- Linear fit: y = 4.976x + 50.5
- P-value: 0.3503
- N samples: 106

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.001x + 53.4
- P-value: 0.5467
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.042 
- Linear fit: y = -2.309x + 54.0
- P-value: 0.6658
- N samples: 106

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.407 ***
- Linear fit: y = -16.744x + 115.7
- P-value: 0.0000
- N samples: 106

**Is Open Source:**
- Correlation: -0.253 **
- Linear fit: y = -10.368x + 111.0
- P-value: 0.0089
- N samples: 106

**Benchmark Score:**
- Correlation: -0.240 *
- Linear fit: y = -0.897x + 131.6
- P-value: 0.0134
- N samples: 106

**Model Size (B):**
- Correlation: 0.116 
- Linear fit: y = 0.002x + 105.1
- P-value: 0.2470
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: 0.018 
- Linear fit: y = 0.002x + 104.9
- P-value: 0.8582
- N samples: 106

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.530 ***
- Linear fit: y = -1.204x + 66.7
- P-value: 0.0000
- N samples: 106

**Model Size (B):**
- Correlation: -0.248 *
- Linear fit: y = -0.002x + 34.5
- P-value: 0.0118
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.217 *
- Linear fit: y = -5.397x + 35.8
- P-value: 0.0257
- N samples: 106

**Is Open Source:**
- Correlation: 0.062 
- Linear fit: y = 1.539x + 32.1
- P-value: 0.5286
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: -0.020 
- Linear fit: y = -0.001x + 33.7
- P-value: 0.8420
- N samples: 106

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.632 ***
- Linear fit: y = -0.511x + 25.8
- P-value: 0.0000
- N samples: 106

**Is Open Source:**
- Correlation: 0.272 **
- Linear fit: y = 2.405x + 10.3
- P-value: 0.0048
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.248 *
- Linear fit: y = -2.202x + 12.7
- P-value: 0.0103
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: -0.101 
- Linear fit: y = -0.003x + 13.2
- P-value: 0.3035
- N samples: 106

**Model Size (B):**
- Correlation: 0.086 
- Linear fit: y = 0.000x + 11.2
- P-value: 0.3874
- N samples: 102

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.511 ***
- Linear fit: y = -0.068x + 102.4
- P-value: 0.0000
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.403 ***
- Linear fit: y = -17.707x + 68.9
- P-value: 0.0000
- N samples: 106

**Benchmark Score:**
- Correlation: -0.297 **
- Linear fit: y = -1.186x + 92.5
- P-value: 0.0020
- N samples: 106

**Is Open Source:**
- Correlation: -0.185 
- Linear fit: y = -8.103x + 62.7
- P-value: 0.0576
- N samples: 106

**Model Size (B):**
- Correlation: 0.148 
- Linear fit: y = 0.002x + 57.9
- P-value: 0.1371
- N samples: 102

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.710 ***
- Linear fit: y = -0.500x + 19.3
- P-value: 0.0000
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.376 ***
- Linear fit: y = -2.902x + 6.9
- P-value: 0.0001
- N samples: 106

**Is Open Source:**
- Correlation: 0.206 *
- Linear fit: y = 1.587x + 4.5
- P-value: 0.0343
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.004x + 7.9
- P-value: 0.0718
- N samples: 106

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.000x + 5.6
- P-value: 0.2927
- N samples: 102

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.277 **
- Linear fit: y = -0.691x + 42.5
- P-value: 0.0041
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: 0.197 *
- Linear fit: y = 0.016x + 12.6
- P-value: 0.0432
- N samples: 106

**Is Open Source:**
- Correlation: 0.077 
- Linear fit: y = 2.098x + 22.1
- P-value: 0.4350
- N samples: 106

**Model Size (B):**
- Correlation: 0.008 
- Linear fit: y = 0.000x + 22.7
- P-value: 0.9334
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.007 
- Linear fit: y = -0.195x + 23.1
- P-value: 0.9422
- N samples: 106

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.299 **
- Linear fit: y = -0.812x + 51.6
- P-value: 0.0019
- N samples: 106

**Model Size (B):**
- Correlation: -0.109 
- Linear fit: y = -0.001x + 29.6
- P-value: 0.2734
- N samples: 102

**Is Open Source:**
- Correlation: 0.083 
- Linear fit: y = 2.480x + 27.6
- P-value: 0.3957
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.078 
- Linear fit: y = -2.326x + 30.0
- P-value: 0.4266
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: 0.037 
- Linear fit: y = 0.003x + 26.6
- P-value: 0.7065
- N samples: 106

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.131 
- Linear fit: y = 0.398x + 0.8
- P-value: 0.1813
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: 0.110 
- Linear fit: y = 0.001x + 0.3
- P-value: 0.2616
- N samples: 106

**Benchmark Score:**
- Correlation: -0.091 
- Linear fit: y = -0.025x + 1.7
- P-value: 0.3537
- N samples: 106

**Model Size (B):**
- Correlation: -0.074 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.4598
- N samples: 102

**Is Reasoning Model:**
- Correlation: 0.070 
- Linear fit: y = 0.212x + 0.9
- P-value: 0.4778
- N samples: 106

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.382 ***
- Linear fit: y = -13.514x + 101.9
- P-value: 0.0001
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.357 ***
- Linear fit: y = -12.648x + 102.9
- P-value: 0.0002
- N samples: 106

**Model Size (B):**
- Correlation: 0.204 *
- Linear fit: y = 0.003x + 93.9
- P-value: 0.0395
- N samples: 102

**Benchmark Score:**
- Correlation: -0.087 
- Linear fit: y = -0.281x + 103.7
- P-value: 0.3748
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: 0.015 
- Linear fit: y = 0.002x + 94.8
- P-value: 0.8756
- N samples: 106

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.650 ***
- Linear fit: y = -0.605x + 27.5
- P-value: 0.0000
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.399 ***
- Linear fit: y = -4.071x + 12.7
- P-value: 0.0000
- N samples: 106

**Is Open Source:**
- Correlation: 0.307 **
- Linear fit: y = 3.125x + 9.0
- P-value: 0.0014
- N samples: 106

**Model Size (B):**
- Correlation: -0.252 *
- Linear fit: y = -0.001x + 11.0
- P-value: 0.0107
- N samples: 102

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.001x + 10.0
- P-value: 0.8288
- N samples: 106

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.198 *
- Linear fit: y = -0.012x + 0.4
- P-value: 0.0414
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: -0.064 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.5160
- N samples: 106

**Model Size (B):**
- Correlation: 0.061 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.5429
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.041 
- Linear fit: y = -0.026x + 0.1
- P-value: 0.6786
- N samples: 106

**Is Open Source:**
- Correlation: 0.034 
- Linear fit: y = 0.022x + 0.1
- P-value: 0.7304
- N samples: 106

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.438 ***
- Linear fit: y = -0.431x + 19.9
- P-value: 0.0000
- N samples: 106

**Model Size (B):**
- Correlation: -0.267 **
- Linear fit: y = -0.001x + 8.5
- P-value: 0.0066
- N samples: 102

**Is Open Source:**
- Correlation: 0.251 **
- Linear fit: y = 2.705x + 6.5
- P-value: 0.0094
- N samples: 106

**Is Reasoning Model:**
- Correlation: -0.070 
- Linear fit: y = -0.755x + 8.1
- P-value: 0.4763
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: 0.046 
- Linear fit: y = 0.002x + 6.8
- P-value: 0.6409
- N samples: 106

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.646 ***
- Linear fit: y = -0.795x + 40.4
- P-value: 0.0000
- N samples: 106

**Model Size (B):**
- Correlation: -0.312 **
- Linear fit: y = -0.002x + 19.1
- P-value: 0.0014
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.289 **
- Linear fit: y = -3.908x + 20.2
- P-value: 0.0026
- N samples: 106

**Is Open Source:**
- Correlation: 0.258 **
- Linear fit: y = 3.472x + 16.5
- P-value: 0.0077
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: -0.048 
- Linear fit: y = -0.002x + 19.3
- P-value: 0.6263
- N samples: 106

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.432 ***
- Linear fit: y = -4.638x + 9.1
- P-value: 0.0000
- N samples: 106

**Model Size (B):**
- Correlation: 0.087 
- Linear fit: y = 0.000x + 6.8
- P-value: 0.3847
- N samples: 102

**Is Reasoning Model:**
- Correlation: -0.068 
- Linear fit: y = -0.735x + 7.4
- P-value: 0.4861
- N samples: 106

**Days Since 2024-01-01:**
- Correlation: -0.031 
- Linear fit: y = -0.001x + 7.7
- P-value: 0.7497
- N samples: 106

**Benchmark Score:**
- Correlation: 0.022 
- Linear fit: y = 0.022x + 6.4
- P-value: 0.8217
- N samples: 106

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.710, y = -0.500x + 19.3

**3b_self_contradiction vs Benchmark Score:**
  r = -0.650, y = -0.605x + 27.5

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.646, y = -0.795x + 40.4

**1a_instruction_override vs Benchmark Score:**
  r = -0.632, y = -0.511x + 25.8

**total_hallucinations vs Benchmark Score:**
  r = -0.587, y = -6.311x + 454.6

**category4_technical_errors vs Benchmark Score:**
  r = -0.530, y = -1.204x + 66.7

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.511, y = -0.068x + 102.4

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.486, y = -0.075x + 123.4

**category1_input_misalignment vs Benchmark Score:**
  r = -0.475, y = -2.196x + 137.6

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.449, y = -22.811x + 88.4

**4a_syntax_error vs Benchmark Score:**
  r = -0.438, y = -0.431x + 19.9

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.432, y = -4.638x + 9.1

**total_hallucinations vs Is Reasoning Model:**
  r = -0.431, y = -50.797x + 305.0

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.407, y = -16.744x + 115.7

**1b_context_omission vs Is Reasoning Model:**
  r = -0.403, y = -17.707x + 68.9

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.399, y = -4.071x + 12.7

**3a_unsupported_leap vs Is Open Source:**
  r = -0.382, y = -13.514x + 101.9

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.376, y = -2.902x + 6.9

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.357, y = -12.648x + 102.9

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.312, y = -0.002x + 19.1

**category2_factual_errors vs Benchmark Score:**
  r = -0.308, y = -1.528x + 95.8

**3b_self_contradiction vs Is Open Source:**
  r = 0.307, y = 3.125x + 9.0


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
- Correlation: -0.256 **
- Linear fit: y = -0.269x + 73.9

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.015 
- Linear fit: y = 0.012x + 105.5

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.047 
- Linear fit: y = 0.022x + 31.0

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.633 ***
- Linear fit: y = 0.471x + 81.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.534 ***
- Linear fit: y = 0.238x + 20.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.453 ***
- Linear fit: y = 0.271x + 3.9

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.971 ***, y = 0.837x + 6.5

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.962 ***, y = 0.819x + -3.3

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.930 ***, y = 0.506x + 2.1

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.919 ***, y = 0.460x + -1.4

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.819 ***, y = 0.446x + 3.5

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.725 ***, y = 0.315x + -2.5

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.714 ***, y = 0.777x + 11.1

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.633 ***, y = 0.471x + 81.4

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.621 ***, y = 0.161x + -6.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.618 ***, y = 0.119x + 4.4

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.602 ***, y = 0.213x + 4.6

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.593 ***, y = 0.434x + -17.1

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.587 ***, y = 0.502x + -0.4

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.578 ***, y = 0.389x + -18.3

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.575 ***, y = 0.724x + 10.3

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.571 ***, y = 0.247x + 2.7

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.566 ***, y = 0.757x + 6.6

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.561 ***, y = 0.034x + -0.7

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.552 ***, y = 0.084x + -1.0

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.549 ***, y = 0.239x + -1.0

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.412 ***, y = -0.031x + 2.9
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.399 ***, y = -0.323x + 77.0
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.380 ***, y = -0.235x + 37.2
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.338 ***, y = -0.227x + 42.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.319 ***, y = -0.020x + 2.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.256 **, y = -0.269x + 73.9
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.245 **, y = -0.129x + 33.0
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = -0.209 *, y = -0.120x + 38.2
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
