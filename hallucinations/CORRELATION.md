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
- Correlation: -0.489 ***
- Linear fit: y = -2.309x + 140.2
- P-value: 0.0000
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.487 ***
- Linear fit: y = -0.075x + 123.1
- P-value: 0.0000
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.459 ***
- Linear fit: y = -23.560x + 88.6
- P-value: 0.0000
- N samples: 115

**Model Size (B):**
- Correlation: 0.117 
- Linear fit: y = 0.002x + 74.0
- P-value: 0.2207
- N samples: 111

**Is Open Source:**
- Correlation: -0.059 
- Linear fit: y = -2.978x + 76.0
- P-value: 0.5322
- N samples: 115

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.313 ***
- Linear fit: y = -1.551x + 95.7
- P-value: 0.0007
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.081 
- Linear fit: y = -4.352x + 54.2
- P-value: 0.3916
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: 0.076 
- Linear fit: y = 0.012x + 43.8
- P-value: 0.4221
- N samples: 115

**Is Open Source:**
- Correlation: 0.060 
- Linear fit: y = 3.184x + 50.2
- P-value: 0.5254
- N samples: 115

**Model Size (B):**
- Correlation: -0.055 
- Linear fit: y = -0.001x + 51.9
- P-value: 0.5651
- N samples: 111

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.437 ***
- Linear fit: y = -18.257x + 116.2
- P-value: 0.0000
- N samples: 115

**Benchmark Score:**
- Correlation: -0.260 **
- Linear fit: y = -1.000x + 133.8
- P-value: 0.0050
- N samples: 115

**Is Open Source:**
- Correlation: -0.231 *
- Linear fit: y = -9.523x + 109.8
- P-value: 0.0130
- N samples: 115

**Model Size (B):**
- Correlation: 0.105 
- Linear fit: y = 0.002x + 104.3
- P-value: 0.2713
- N samples: 111

**Days Since 2024-01-01:**
- Correlation: -0.028 
- Linear fit: y = -0.004x + 107.7
- P-value: 0.7635
- N samples: 115

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.528 ***
- Linear fit: y = -1.219x + 67.1
- P-value: 0.0000
- N samples: 115

**Model Size (B):**
- Correlation: -0.250 **
- Linear fit: y = -0.002x + 34.0
- P-value: 0.0082
- N samples: 111

**Is Reasoning Model:**
- Correlation: -0.230 *
- Linear fit: y = -5.763x + 35.9
- P-value: 0.0136
- N samples: 115

**Is Open Source:**
- Correlation: 0.061 
- Linear fit: y = 1.522x + 31.7
- P-value: 0.5138
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.003x + 34.7
- P-value: 0.6252
- N samples: 115

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.592 ***
- Linear fit: y = -6.577x + 460.1
- P-value: 0.0000
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.461 ***
- Linear fit: y = -55.708x + 306.1
- P-value: 0.0000
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.197 *
- Linear fit: y = -0.071x + 319.3
- P-value: 0.0351
- N samples: 115

**Is Open Source:**
- Correlation: -0.055 
- Linear fit: y = -6.582x + 276.2
- P-value: 0.5579
- N samples: 115

**Model Size (B):**
- Correlation: -0.000 
- Linear fit: y = -0.000x + 273.7
- P-value: 0.9971
- N samples: 111

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.489 ***
- Linear fit: y = -2.309x + 140.2
- P-value: 0.0000
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.487 ***
- Linear fit: y = -0.075x + 123.1
- P-value: 0.0000
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.459 ***
- Linear fit: y = -23.560x + 88.6
- P-value: 0.0000
- N samples: 115

**Model Size (B):**
- Correlation: 0.117 
- Linear fit: y = 0.002x + 74.0
- P-value: 0.2207
- N samples: 111

**Is Open Source:**
- Correlation: -0.059 
- Linear fit: y = -2.978x + 76.0
- P-value: 0.5322
- N samples: 115

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.313 ***
- Linear fit: y = -1.551x + 95.7
- P-value: 0.0007
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.081 
- Linear fit: y = -4.352x + 54.2
- P-value: 0.3916
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: 0.076 
- Linear fit: y = 0.012x + 43.8
- P-value: 0.4221
- N samples: 115

**Is Open Source:**
- Correlation: 0.060 
- Linear fit: y = 3.184x + 50.2
- P-value: 0.5254
- N samples: 115

**Model Size (B):**
- Correlation: -0.055 
- Linear fit: y = -0.001x + 51.9
- P-value: 0.5651
- N samples: 111

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.437 ***
- Linear fit: y = -18.257x + 116.2
- P-value: 0.0000
- N samples: 115

**Benchmark Score:**
- Correlation: -0.260 **
- Linear fit: y = -1.000x + 133.8
- P-value: 0.0050
- N samples: 115

**Is Open Source:**
- Correlation: -0.231 *
- Linear fit: y = -9.523x + 109.8
- P-value: 0.0130
- N samples: 115

**Model Size (B):**
- Correlation: 0.105 
- Linear fit: y = 0.002x + 104.3
- P-value: 0.2713
- N samples: 111

**Days Since 2024-01-01:**
- Correlation: -0.028 
- Linear fit: y = -0.004x + 107.7
- P-value: 0.7635
- N samples: 115

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.528 ***
- Linear fit: y = -1.219x + 67.1
- P-value: 0.0000
- N samples: 115

**Model Size (B):**
- Correlation: -0.250 **
- Linear fit: y = -0.002x + 34.0
- P-value: 0.0082
- N samples: 111

**Is Reasoning Model:**
- Correlation: -0.230 *
- Linear fit: y = -5.763x + 35.9
- P-value: 0.0136
- N samples: 115

**Is Open Source:**
- Correlation: 0.061 
- Linear fit: y = 1.522x + 31.7
- P-value: 0.5138
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.003x + 34.7
- P-value: 0.6252
- N samples: 115

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.618 ***
- Linear fit: y = -0.505x + 25.8
- P-value: 0.0000
- N samples: 115

**Is Open Source:**
- Correlation: 0.267 **
- Linear fit: y = 2.341x + 10.3
- P-value: 0.0039
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.256 **
- Linear fit: y = -2.281x + 12.8
- P-value: 0.0057
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.094 
- Linear fit: y = -0.002x + 13.0
- P-value: 0.3184
- N samples: 115

**Model Size (B):**
- Correlation: 0.077 
- Linear fit: y = 0.000x + 11.3
- P-value: 0.4194
- N samples: 111

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.519 ***
- Linear fit: y = -0.069x + 102.6
- P-value: 0.0000
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.411 ***
- Linear fit: y = -18.232x + 68.7
- P-value: 0.0000
- N samples: 115

**Benchmark Score:**
- Correlation: -0.320 ***
- Linear fit: y = -1.306x + 95.0
- P-value: 0.0005
- N samples: 115

**Is Open Source:**
- Correlation: -0.159 
- Linear fit: y = -6.959x + 61.1
- P-value: 0.0897
- N samples: 115

**Model Size (B):**
- Correlation: 0.140 
- Linear fit: y = 0.002x + 57.2
- P-value: 0.1422
- N samples: 111

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.707 ***
- Linear fit: y = -0.497x + 19.4
- P-value: 0.0000
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.398 ***
- Linear fit: y = -3.048x + 7.1
- P-value: 0.0000
- N samples: 115

**Is Open Source:**
- Correlation: 0.217 *
- Linear fit: y = 1.640x + 4.5
- P-value: 0.0197
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.145 
- Linear fit: y = -0.003x + 7.5
- P-value: 0.1211
- N samples: 115

**Model Size (B):**
- Correlation: -0.113 
- Linear fit: y = -0.000x + 5.5
- P-value: 0.2360
- N samples: 111

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.262 **
- Linear fit: y = -0.655x + 41.4
- P-value: 0.0047
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: 0.166 
- Linear fit: y = 0.014x + 14.0
- P-value: 0.0759
- N samples: 115

**Is Open Source:**
- Correlation: 0.063 
- Linear fit: y = 1.682x + 22.0
- P-value: 0.5063
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.020 
- Linear fit: y = -0.533x + 23.1
- P-value: 0.8356
- N samples: 115

**Model Size (B):**
- Correlation: 0.010 
- Linear fit: y = 0.000x + 22.4
- P-value: 0.9188
- N samples: 111

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.316 ***
- Linear fit: y = -0.868x + 52.6
- P-value: 0.0006
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.132 
- Linear fit: y = -3.932x + 30.3
- P-value: 0.1608
- N samples: 115

**Model Size (B):**
- Correlation: -0.101 
- Linear fit: y = -0.001x + 28.6
- P-value: 0.2905
- N samples: 111

**Is Open Source:**
- Correlation: 0.041 
- Linear fit: y = 1.214x + 27.4
- P-value: 0.6619
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.022 
- Linear fit: y = -0.002x + 29.2
- P-value: 0.8182
- N samples: 115

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.101 
- Linear fit: y = -0.028x + 1.7
- P-value: 0.2815
- N samples: 115

**Is Open Source:**
- Correlation: 0.097 
- Linear fit: y = 0.288x + 0.8
- P-value: 0.3013
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: 0.066 
- Linear fit: y = 0.001x + 0.6
- P-value: 0.4823
- N samples: 115

**Model Size (B):**
- Correlation: -0.064 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.5046
- N samples: 111

**Is Reasoning Model:**
- Correlation: 0.038 
- Linear fit: y = 0.113x + 0.9
- P-value: 0.6898
- N samples: 115

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.386 ***
- Linear fit: y = -13.878x + 103.3
- P-value: 0.0000
- N samples: 115

**Is Open Source:**
- Correlation: -0.350 ***
- Linear fit: y = -12.424x + 100.8
- P-value: 0.0001
- N samples: 115

**Model Size (B):**
- Correlation: 0.193 *
- Linear fit: y = 0.003x + 93.4
- P-value: 0.0426
- N samples: 111

**Benchmark Score:**
- Correlation: -0.111 
- Linear fit: y = -0.366x + 105.5
- P-value: 0.2392
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.025 
- Linear fit: y = -0.003x + 96.9
- P-value: 0.7873
- N samples: 115

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.658 ***
- Linear fit: y = -0.623x + 27.9
- P-value: 0.0000
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.423 ***
- Linear fit: y = -4.354x + 12.8
- P-value: 0.0000
- N samples: 115

**Is Open Source:**
- Correlation: 0.282 **
- Linear fit: y = 2.865x + 8.9
- P-value: 0.0023
- N samples: 115

**Model Size (B):**
- Correlation: -0.251 **
- Linear fit: y = -0.001x + 10.9
- P-value: 0.0079
- N samples: 111

**Days Since 2024-01-01:**
- Correlation: -0.023 
- Linear fit: y = -0.001x + 10.6
- P-value: 0.8113
- N samples: 115

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.191 *
- Linear fit: y = -0.011x + 0.4
- P-value: 0.0404
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.059 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.5291
- N samples: 115

**Model Size (B):**
- Correlation: 0.057 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.5506
- N samples: 111

**Is Open Source:**
- Correlation: 0.056 
- Linear fit: y = 0.035x + 0.1
- P-value: 0.5553
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.038 
- Linear fit: y = -0.025x + 0.1
- P-value: 0.6839
- N samples: 115

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.438 ***
- Linear fit: y = -0.438x + 20.0
- P-value: 0.0000
- N samples: 115

**Model Size (B):**
- Correlation: -0.260 **
- Linear fit: y = -0.001x + 8.3
- P-value: 0.0058
- N samples: 111

**Is Open Source:**
- Correlation: 0.234 *
- Linear fit: y = 2.505x + 6.4
- P-value: 0.0119
- N samples: 115

**Is Reasoning Model:**
- Correlation: -0.096 
- Linear fit: y = -1.044x + 8.2
- P-value: 0.3066
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: 0.014 
- Linear fit: y = 0.000x + 7.3
- P-value: 0.8830
- N samples: 115

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.651 ***
- Linear fit: y = -0.796x + 40.5
- P-value: 0.0000
- N samples: 115

**Model Size (B):**
- Correlation: -0.312 ***
- Linear fit: y = -0.002x + 18.9
- P-value: 0.0009
- N samples: 111

**Is Reasoning Model:**
- Correlation: -0.303 **
- Linear fit: y = -4.027x + 20.3
- P-value: 0.0010
- N samples: 115

**Is Open Source:**
- Correlation: 0.233 *
- Linear fit: y = 3.063x + 16.5
- P-value: 0.0120
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.066 
- Linear fit: y = -0.003x + 19.6
- P-value: 0.4805
- N samples: 115

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.365 ***
- Linear fit: y = -4.046x + 8.8
- P-value: 0.0001
- N samples: 115

**Model Size (B):**
- Correlation: 0.064 
- Linear fit: y = 0.000x + 6.8
- P-value: 0.5079
- N samples: 111

**Is Reasoning Model:**
- Correlation: -0.062 
- Linear fit: y = -0.692x + 7.4
- P-value: 0.5130
- N samples: 115

**Days Since 2024-01-01:**
- Correlation: -0.038 
- Linear fit: y = -0.001x + 7.8
- P-value: 0.6900
- N samples: 115

**Benchmark Score:**
- Correlation: 0.014 
- Linear fit: y = 0.015x + 6.6
- P-value: 0.8815
- N samples: 115

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.707, y = -0.497x + 19.4

**3b_self_contradiction vs Benchmark Score:**
  r = -0.658, y = -0.623x + 27.9

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.651, y = -0.796x + 40.5

**1a_instruction_override vs Benchmark Score:**
  r = -0.618, y = -0.505x + 25.8

**total_hallucinations vs Benchmark Score:**
  r = -0.592, y = -6.577x + 460.1

**category4_technical_errors vs Benchmark Score:**
  r = -0.528, y = -1.219x + 67.1

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.519, y = -0.069x + 102.6

**category1_input_misalignment vs Benchmark Score:**
  r = -0.489, y = -2.309x + 140.2

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.487, y = -0.075x + 123.1

**total_hallucinations vs Is Reasoning Model:**
  r = -0.461, y = -55.708x + 306.1

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.459, y = -23.560x + 88.6

**4a_syntax_error vs Benchmark Score:**
  r = -0.438, y = -0.438x + 20.0

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.437, y = -18.257x + 116.2

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.423, y = -4.354x + 12.8

**1b_context_omission vs Is Reasoning Model:**
  r = -0.411, y = -18.232x + 68.7

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.398, y = -3.048x + 7.1

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.386, y = -13.878x + 103.3

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.365, y = -4.046x + 8.8

**3a_unsupported_leap vs Is Open Source:**
  r = -0.350, y = -12.424x + 100.8

**1b_context_omission vs Benchmark Score:**
  r = -0.320, y = -1.306x + 95.0

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.316, y = -0.868x + 52.6

**category2_factual_errors vs Benchmark Score:**
  r = -0.313, y = -1.551x + 95.7

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.312, y = -0.002x + 18.9

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.303, y = -4.027x + 20.3


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
- Correlation: -0.225 *
- Linear fit: y = -0.233x + 69.8

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.072 
- Linear fit: y = 0.057x + 101.2

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.080 
- Linear fit: y = 0.037x + 29.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.629 ***
- Linear fit: y = 0.480x + 80.5

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.537 ***
- Linear fit: y = 0.243x + 19.7

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.468 ***
- Linear fit: y = 0.277x + 3.1

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.837x + 6.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.964 ***, y = 0.821x + -3.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.926 ***, y = 0.509x + 1.7

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.912 ***, y = 0.457x + -1.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.819 ***, y = 0.436x + 3.8

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.716 ***, y = 0.311x + -2.5

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.695 ***, y = 0.762x + 10.8

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.630 ***, y = 0.162x + -6.6

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.629 ***, y = 0.480x + 80.5

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.605 ***, y = 0.119x + 4.3

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.605 ***, y = 0.215x + 4.4

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.602 ***, y = 0.434x + -17.6

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.594 ***, y = 0.809x + 6.1

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.588 ***, y = 0.497x + -0.3

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.571 ***, y = 0.703x + 10.6

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.562 ***, y = 0.034x + -0.7

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.561 ***, y = 0.253x + -1.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.557 ***, y = 0.241x + 2.7

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.556 ***, y = 0.365x + -15.7

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.556 ***, y = 0.098x + 4.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.375 ***, y = -0.027x + 2.6
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.360 ***, y = -0.297x + 74.1
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.353 ***, y = -0.215x + 35.5
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.293 **, y = -0.195x + 39.7
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.292 **, y = -0.018x + 2.4
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.226 *, y = -0.117x + 31.8
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.225 *, y = -0.233x + 69.8
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
