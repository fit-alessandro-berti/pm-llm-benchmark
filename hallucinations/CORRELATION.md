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
- Correlation: -0.610 ***
- Linear fit: y = -0.088x + 132.4
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.513 ***
- Linear fit: y = -2.912x + 160.0
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.413 ***
- Linear fit: y = -21.942x + 86.1
- P-value: 0.0000
- N samples: 118

**Is Open Source:**
- Correlation: -0.134 
- Linear fit: y = -7.236x + 76.2
- P-value: 0.1471
- N samples: 118

**Model Size (B):**
- Correlation: 0.106 
- Linear fit: y = 0.002x + 72.7
- P-value: 0.2617
- N samples: 113

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.303 ***
- Linear fit: y = -1.657x + 97.6
- P-value: 0.0009
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.194 *
- Linear fit: y = -9.948x + 54.1
- P-value: 0.0356
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.054 
- Linear fit: y = 0.008x + 43.3
- P-value: 0.5623
- N samples: 118

**Model Size (B):**
- Correlation: -0.049 
- Linear fit: y = -0.001x + 48.7
- P-value: 0.6042
- N samples: 113

**Is Open Source:**
- Correlation: -0.033 
- Linear fit: y = -1.710x + 49.0
- P-value: 0.7240
- N samples: 118

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.477 ***
- Linear fit: y = -20.104x + 115.3
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.369 ***
- Linear fit: y = -1.657x + 153.0
- P-value: 0.0000
- N samples: 118

**Is Open Source:**
- Correlation: -0.239 **
- Linear fit: y = -10.224x + 107.7
- P-value: 0.0090
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.095 
- Linear fit: y = -0.011x + 111.0
- P-value: 0.3040
- N samples: 118

**Model Size (B):**
- Correlation: 0.081 
- Linear fit: y = 0.001x + 102.7
- P-value: 0.3943
- N samples: 113

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.447 ***
- Linear fit: y = -1.121x + 64.1
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.276 **
- Linear fit: y = -6.504x + 34.5
- P-value: 0.0025
- N samples: 118

**Model Size (B):**
- Correlation: -0.208 *
- Linear fit: y = -0.002x + 32.3
- P-value: 0.0271
- N samples: 113

**Days Since 2024-01-01:**
- Correlation: -0.077 
- Linear fit: y = -0.005x + 34.0
- P-value: 0.4048
- N samples: 118

**Is Open Source:**
- Correlation: -0.058 
- Linear fit: y = -1.380x + 31.2
- P-value: 0.5338
- N samples: 118

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.611 ***
- Linear fit: y = -7.921x + 499.8
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.516 ***
- Linear fit: y = -62.772x + 300.4
- P-value: 0.0000
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.304 ***
- Linear fit: y = -0.100x + 331.3
- P-value: 0.0008
- N samples: 118

**Is Open Source:**
- Correlation: -0.164 
- Linear fit: y = -20.150x + 272.0
- P-value: 0.0769
- N samples: 118

**Model Size (B):**
- Correlation: 0.006 
- Linear fit: y = 0.000x + 264.8
- P-value: 0.9523
- N samples: 113

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.610 ***
- Linear fit: y = -0.088x + 132.4
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.513 ***
- Linear fit: y = -2.912x + 160.0
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.413 ***
- Linear fit: y = -21.942x + 86.1
- P-value: 0.0000
- N samples: 118

**Is Open Source:**
- Correlation: -0.134 
- Linear fit: y = -7.236x + 76.2
- P-value: 0.1471
- N samples: 118

**Model Size (B):**
- Correlation: 0.106 
- Linear fit: y = 0.002x + 72.7
- P-value: 0.2617
- N samples: 113

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.303 ***
- Linear fit: y = -1.657x + 97.6
- P-value: 0.0009
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.194 *
- Linear fit: y = -9.948x + 54.1
- P-value: 0.0356
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.054 
- Linear fit: y = 0.008x + 43.3
- P-value: 0.5623
- N samples: 118

**Model Size (B):**
- Correlation: -0.049 
- Linear fit: y = -0.001x + 48.7
- P-value: 0.6042
- N samples: 113

**Is Open Source:**
- Correlation: -0.033 
- Linear fit: y = -1.710x + 49.0
- P-value: 0.7240
- N samples: 118

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.477 ***
- Linear fit: y = -20.104x + 115.3
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.369 ***
- Linear fit: y = -1.657x + 153.0
- P-value: 0.0000
- N samples: 118

**Is Open Source:**
- Correlation: -0.239 **
- Linear fit: y = -10.224x + 107.7
- P-value: 0.0090
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.095 
- Linear fit: y = -0.011x + 111.0
- P-value: 0.3040
- N samples: 118

**Model Size (B):**
- Correlation: 0.081 
- Linear fit: y = 0.001x + 102.7
- P-value: 0.3943
- N samples: 113

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.447 ***
- Linear fit: y = -1.121x + 64.1
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.276 **
- Linear fit: y = -6.504x + 34.5
- P-value: 0.0025
- N samples: 118

**Model Size (B):**
- Correlation: -0.208 *
- Linear fit: y = -0.002x + 32.3
- P-value: 0.0271
- N samples: 113

**Days Since 2024-01-01:**
- Correlation: -0.077 
- Linear fit: y = -0.005x + 34.0
- P-value: 0.4048
- N samples: 118

**Is Open Source:**
- Correlation: -0.058 
- Linear fit: y = -1.380x + 31.2
- P-value: 0.5338
- N samples: 118

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.595 ***
- Linear fit: y = -0.578x + 28.1
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.363 ***
- Linear fit: y = -3.309x + 12.8
- P-value: 0.0001
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.206 *
- Linear fit: y = -0.005x + 14.3
- P-value: 0.0255
- N samples: 118

**Is Open Source:**
- Correlation: 0.138 
- Linear fit: y = 1.277x + 10.4
- P-value: 0.1356
- N samples: 118

**Model Size (B):**
- Correlation: 0.090 
- Linear fit: y = 0.000x + 10.7
- P-value: 0.3434
- N samples: 113

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.625 ***
- Linear fit: y = -0.078x + 110.4
- P-value: 0.0000
- N samples: 118

**Benchmark Score:**
- Correlation: -0.381 ***
- Linear fit: y = -1.875x + 113.7
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.349 ***
- Linear fit: y = -16.136x + 67.2
- P-value: 0.0001
- N samples: 118

**Is Open Source:**
- Correlation: -0.195 *
- Linear fit: y = -9.104x + 61.4
- P-value: 0.0348
- N samples: 118

**Model Size (B):**
- Correlation: 0.120 
- Linear fit: y = 0.002x + 57.2
- P-value: 0.2058
- N samples: 113

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.674 ***
- Linear fit: y = -0.459x + 18.3
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.391 ***
- Linear fit: y = -2.497x + 6.1
- P-value: 0.0000
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.266 **
- Linear fit: y = -0.005x + 7.7
- P-value: 0.0036
- N samples: 118

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.000x + 4.9
- P-value: 0.2670
- N samples: 113

**Is Open Source:**
- Correlation: 0.091 
- Linear fit: y = 0.591x + 4.4
- P-value: 0.3246
- N samples: 118

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.245 **
- Linear fit: y = -0.664x + 40.7
- P-value: 0.0076
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.144 
- Linear fit: y = 0.010x + 14.2
- P-value: 0.1188
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.109 
- Linear fit: y = -2.770x + 22.5
- P-value: 0.2410
- N samples: 118

**Is Open Source:**
- Correlation: -0.019 
- Linear fit: y = -0.481x + 21.1
- P-value: 0.8413
- N samples: 118

**Model Size (B):**
- Correlation: 0.015 
- Linear fit: y = 0.000x + 20.5
- P-value: 0.8776
- N samples: 113

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.311 ***
- Linear fit: y = -0.953x + 54.9
- P-value: 0.0006
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.252 **
- Linear fit: y = -7.245x + 30.8
- P-value: 0.0059
- N samples: 118

**Model Size (B):**
- Correlation: -0.095 
- Linear fit: y = -0.001x + 27.3
- P-value: 0.3155
- N samples: 113

**Is Open Source:**
- Correlation: -0.043 
- Linear fit: y = -1.243x + 27.1
- P-value: 0.6464
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.040 
- Linear fit: y = -0.003x + 28.7
- P-value: 0.6647
- N samples: 118

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.147 
- Linear fit: y = -0.040x + 2.0
- P-value: 0.1116
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.098 
- Linear fit: y = 0.001x + 0.4
- P-value: 0.2907
- N samples: 118

**Model Size (B):**
- Correlation: -0.049 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.6072
- N samples: 113

**Is Reasoning Model:**
- Correlation: 0.026 
- Linear fit: y = 0.068x + 0.8
- P-value: 0.7759
- N samples: 118

**Is Open Source:**
- Correlation: 0.006 
- Linear fit: y = 0.014x + 0.8
- P-value: 0.9520
- N samples: 118

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.430 ***
- Linear fit: y = -15.527x + 103.4
- P-value: 0.0000
- N samples: 118

**Is Open Source:**
- Correlation: -0.323 ***
- Linear fit: y = -11.824x + 99.0
- P-value: 0.0004
- N samples: 118

**Benchmark Score:**
- Correlation: -0.276 **
- Linear fit: y = -1.063x + 126.0
- P-value: 0.0025
- N samples: 118

**Model Size (B):**
- Correlation: 0.152 
- Linear fit: y = 0.002x + 92.8
- P-value: 0.1071
- N samples: 113

**Days Since 2024-01-01:**
- Correlation: -0.102 
- Linear fit: y = -0.010x + 101.1
- P-value: 0.2737
- N samples: 118

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.610 ***
- Linear fit: y = -0.595x + 26.9
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.495 ***
- Linear fit: y = -4.530x + 11.8
- P-value: 0.0000
- N samples: 118

**Model Size (B):**
- Correlation: -0.240 *
- Linear fit: y = -0.001x + 9.9
- P-value: 0.0106
- N samples: 113

**Is Open Source:**
- Correlation: 0.178 
- Linear fit: y = 1.646x + 8.5
- P-value: 0.0543
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.040 
- Linear fit: y = -0.001x + 9.8
- P-value: 0.6664
- N samples: 118

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.133 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.1613
- N samples: 113

**Is Reasoning Model:**
- Correlation: -0.079 
- Linear fit: y = -0.046x + 0.1
- P-value: 0.3952
- N samples: 118

**Is Open Source:**
- Correlation: -0.077 
- Linear fit: y = -0.046x + 0.1
- P-value: 0.4073
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.027 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.7714
- N samples: 118

**Benchmark Score:**
- Correlation: 0.019 
- Linear fit: y = 0.001x + 0.1
- P-value: 0.8351
- N samples: 118

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.280 **
- Linear fit: y = -0.308x + 16.0
- P-value: 0.0022
- N samples: 118

**Model Size (B):**
- Correlation: -0.194 *
- Linear fit: y = -0.001x + 7.5
- P-value: 0.0391
- N samples: 113

**Is Open Source:**
- Correlation: 0.120 
- Linear fit: y = 1.255x + 6.4
- P-value: 0.1960
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: 0.064 
- Linear fit: y = 0.002x + 5.7
- P-value: 0.4906
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.060 
- Linear fit: y = -0.617x + 7.2
- P-value: 0.5207
- N samples: 118

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.546 ***
- Linear fit: y = -0.689x + 37.4
- P-value: 0.0000
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.369 ***
- Linear fit: y = -4.366x + 19.4
- P-value: 0.0000
- N samples: 118

**Model Size (B):**
- Correlation: -0.279 **
- Linear fit: y = -0.001x + 17.9
- P-value: 0.0027
- N samples: 113

**Days Since 2024-01-01:**
- Correlation: -0.094 
- Linear fit: y = -0.003x + 18.9
- P-value: 0.3125
- N samples: 118

**Is Open Source:**
- Correlation: 0.082 
- Linear fit: y = 0.980x + 16.5
- P-value: 0.3793
- N samples: 118

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.323 ***
- Linear fit: y = -3.616x + 8.3
- P-value: 0.0004
- N samples: 118

**Is Reasoning Model:**
- Correlation: -0.138 
- Linear fit: y = -1.521x + 7.8
- P-value: 0.1374
- N samples: 118

**Days Since 2024-01-01:**
- Correlation: -0.124 
- Linear fit: y = -0.004x + 9.4
- P-value: 0.1797
- N samples: 118

**Benchmark Score:**
- Correlation: -0.105 
- Linear fit: y = -0.124x + 10.6
- P-value: 0.2581
- N samples: 118

**Model Size (B):**
- Correlation: 0.040 
- Linear fit: y = 0.000x + 6.9
- P-value: 0.6754
- N samples: 113

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.674, y = -0.459x + 18.3

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.625, y = -0.078x + 110.4

**total_hallucinations vs Benchmark Score:**
  r = -0.611, y = -7.921x + 499.8

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.610, y = -0.088x + 132.4

**3b_self_contradiction vs Benchmark Score:**
  r = -0.610, y = -0.595x + 26.9

**1a_instruction_override vs Benchmark Score:**
  r = -0.595, y = -0.578x + 28.1

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.546, y = -0.689x + 37.4

**total_hallucinations vs Is Reasoning Model:**
  r = -0.516, y = -62.772x + 300.4

**category1_input_misalignment vs Benchmark Score:**
  r = -0.513, y = -2.912x + 160.0

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.495, y = -4.530x + 11.8

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.477, y = -20.104x + 115.3

**category4_technical_errors vs Benchmark Score:**
  r = -0.447, y = -1.121x + 64.1

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.430, y = -15.527x + 103.4

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.413, y = -21.942x + 86.1

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.391, y = -2.497x + 6.1

**1b_context_omission vs Benchmark Score:**
  r = -0.381, y = -1.875x + 113.7

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.369, y = -4.366x + 19.4

**category3_logical_errors vs Benchmark Score:**
  r = -0.369, y = -1.657x + 153.0

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.363, y = -3.309x + 12.8

**1b_context_omission vs Is Reasoning Model:**
  r = -0.349, y = -16.136x + 67.2

**3a_unsupported_leap vs Is Open Source:**
  r = -0.323, y = -11.824x + 99.0

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.323, y = -3.616x + 8.3

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.311, y = -0.953x + 54.9

**total_hallucinations vs Days Since 2024-01-01:**
  r = -0.304, y = -0.100x + 331.3

**category2_factual_errors vs Benchmark Score:**
  r = -0.303, y = -1.657x + 97.6


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
- Correlation: -0.189 *
- Linear fit: y = -0.182x + 61.7

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.131 
- Linear fit: y = 0.104x + 96.1

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.044 
- Linear fit: y = 0.019x + 29.3

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.675 ***
- Linear fit: y = 0.554x + 76.9

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.618 ***
- Linear fit: y = 0.283x + 17.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.539 ***
- Linear fit: y = 0.301x + -0.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.984 ***, y = 0.844x + 6.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.972 ***, y = 0.844x + -4.1

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.932 ***, y = 0.522x + 1.4

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.913 ***, y = 0.453x + -1.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.808 ***, y = 0.407x + 4.4

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.714 ***, y = 0.155x + -6.9

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.706 ***, y = 0.797x + 9.9

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.675 ***, y = 0.554x + 76.9

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.669 ***, y = 0.294x + -2.1

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.653 ***, y = 0.208x + 3.6

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.645 ***, y = 0.440x + -19.1

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.644 ***, y = 0.115x + 3.6

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.639 ***, y = 0.300x + -2.3

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.624 ***, y = 0.439x + 73.2

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.618 ***, y = 0.283x + 17.0

**Category 4: Technical Errors vs 2a: Concept Fabrication:**
  r = 0.592 ***, y = 0.640x + 1.3

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.592 ***, y = 0.357x + -16.1

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.587 ***, y = 0.738x + 74.8

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.578 ***, y = 0.146x + -4.6

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.573 ***, y = 0.223x + 2.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.377 ***, y = -0.021x + 2.0
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.315 ***, y = -0.015x + 1.9
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.305 ***, y = -0.274x + 71.1
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.295 **, y = -0.163x + 30.3
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.249 **, y = -0.155x + 35.6
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
