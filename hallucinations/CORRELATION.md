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
- Correlation: -0.535 ***
- Linear fit: y = -0.081x + 127.8
- P-value: 0.0000
- N samples: 120

**Benchmark Score:**
- Correlation: -0.486 ***
- Linear fit: y = -2.407x + 143.9
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.443 ***
- Linear fit: y = -23.488x + 88.7
- P-value: 0.0000
- N samples: 120

**Model Size (B):**
- Correlation: 0.122 
- Linear fit: y = 0.003x + 75.0
- P-value: 0.1932
- N samples: 116

**Is Open Source:**
- Correlation: -0.083 
- Linear fit: y = -4.403x + 77.8
- P-value: 0.3660
- N samples: 120

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.304 ***
- Linear fit: y = -1.494x + 94.1
- P-value: 0.0007
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.145 
- Linear fit: y = -7.616x + 56.1
- P-value: 0.1138
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: 0.096 
- Linear fit: y = 0.014x + 42.6
- P-value: 0.2973
- N samples: 120

**Is Open Source:**
- Correlation: 0.064 
- Linear fit: y = 3.334x + 50.3
- P-value: 0.4899
- N samples: 120

**Model Size (B):**
- Correlation: -0.058 
- Linear fit: y = -0.001x + 52.2
- P-value: 0.5366
- N samples: 116

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.461 ***
- Linear fit: y = -18.694x + 115.6
- P-value: 0.0000
- N samples: 120

**Benchmark Score:**
- Correlation: -0.244 **
- Linear fit: y = -0.926x + 131.6
- P-value: 0.0073
- N samples: 120

**Is Open Source:**
- Correlation: -0.226 *
- Linear fit: y = -9.169x + 109.6
- P-value: 0.0129
- N samples: 120

**Model Size (B):**
- Correlation: 0.106 
- Linear fit: y = 0.002x + 104.3
- P-value: 0.2561
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.005 
- Linear fit: y = -0.001x + 105.7
- P-value: 0.9578
- N samples: 120

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.515 ***
- Linear fit: y = -1.178x + 65.9
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.247 **
- Linear fit: y = -6.045x + 35.8
- P-value: 0.0065
- N samples: 120

**Model Size (B):**
- Correlation: -0.237 *
- Linear fit: y = -0.002x + 34.0
- P-value: 0.0105
- N samples: 116

**Is Open Source:**
- Correlation: 0.066 
- Linear fit: y = 1.613x + 31.8
- P-value: 0.4737
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: -0.029 
- Linear fit: y = -0.002x + 33.8
- P-value: 0.7523
- N samples: 120

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.588 ***
- Linear fit: y = -6.484x + 458.1
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.507 ***
- Linear fit: y = -59.785x + 307.5
- P-value: 0.0000
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: -0.209 *
- Linear fit: y = -0.070x + 319.8
- P-value: 0.0219
- N samples: 120

**Is Open Source:**
- Correlation: -0.064 
- Linear fit: y = -7.519x + 278.0
- P-value: 0.4882
- N samples: 120

**Model Size (B):**
- Correlation: 0.007 
- Linear fit: y = 0.000x + 274.9
- P-value: 0.9421
- N samples: 116

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.535 ***
- Linear fit: y = -0.081x + 127.8
- P-value: 0.0000
- N samples: 120

**Benchmark Score:**
- Correlation: -0.486 ***
- Linear fit: y = -2.407x + 143.9
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.443 ***
- Linear fit: y = -23.488x + 88.7
- P-value: 0.0000
- N samples: 120

**Model Size (B):**
- Correlation: 0.122 
- Linear fit: y = 0.003x + 75.0
- P-value: 0.1932
- N samples: 116

**Is Open Source:**
- Correlation: -0.083 
- Linear fit: y = -4.403x + 77.8
- P-value: 0.3660
- N samples: 120

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.304 ***
- Linear fit: y = -1.494x + 94.1
- P-value: 0.0007
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.145 
- Linear fit: y = -7.616x + 56.1
- P-value: 0.1138
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: 0.096 
- Linear fit: y = 0.014x + 42.6
- P-value: 0.2973
- N samples: 120

**Is Open Source:**
- Correlation: 0.064 
- Linear fit: y = 3.334x + 50.3
- P-value: 0.4899
- N samples: 120

**Model Size (B):**
- Correlation: -0.058 
- Linear fit: y = -0.001x + 52.2
- P-value: 0.5366
- N samples: 116

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.461 ***
- Linear fit: y = -18.694x + 115.6
- P-value: 0.0000
- N samples: 120

**Benchmark Score:**
- Correlation: -0.244 **
- Linear fit: y = -0.926x + 131.6
- P-value: 0.0073
- N samples: 120

**Is Open Source:**
- Correlation: -0.226 *
- Linear fit: y = -9.169x + 109.6
- P-value: 0.0129
- N samples: 120

**Model Size (B):**
- Correlation: 0.106 
- Linear fit: y = 0.002x + 104.3
- P-value: 0.2561
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.005 
- Linear fit: y = -0.001x + 105.7
- P-value: 0.9578
- N samples: 120

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.515 ***
- Linear fit: y = -1.178x + 65.9
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.247 **
- Linear fit: y = -6.045x + 35.8
- P-value: 0.0065
- N samples: 120

**Model Size (B):**
- Correlation: -0.237 *
- Linear fit: y = -0.002x + 34.0
- P-value: 0.0105
- N samples: 116

**Is Open Source:**
- Correlation: 0.066 
- Linear fit: y = 1.613x + 31.8
- P-value: 0.4737
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: -0.029 
- Linear fit: y = -0.002x + 33.8
- P-value: 0.7523
- N samples: 120

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.615 ***
- Linear fit: y = -0.524x + 26.5
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.312 ***
- Linear fit: y = -2.847x + 13.2
- P-value: 0.0005
- N samples: 120

**Is Open Source:**
- Correlation: 0.247 **
- Linear fit: y = 2.245x + 10.6
- P-value: 0.0066
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: -0.123 
- Linear fit: y = -0.003x + 13.7
- P-value: 0.1808
- N samples: 120

**Model Size (B):**
- Correlation: 0.064 
- Linear fit: y = 0.000x + 11.6
- P-value: 0.4964
- N samples: 116

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.573 ***
- Linear fit: y = -0.075x + 106.8
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.389 ***
- Linear fit: y = -17.788x + 68.5
- P-value: 0.0000
- N samples: 120

**Benchmark Score:**
- Correlation: -0.324 ***
- Linear fit: y = -1.383x + 97.9
- P-value: 0.0003
- N samples: 120

**Is Open Source:**
- Correlation: -0.181 *
- Linear fit: y = -8.271x + 62.5
- P-value: 0.0475
- N samples: 120

**Model Size (B):**
- Correlation: 0.149 
- Linear fit: y = 0.003x + 57.8
- P-value: 0.1103
- N samples: 116

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.703 ***
- Linear fit: y = -0.500x + 19.5
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.375 ***
- Linear fit: y = -2.854x + 6.9
- P-value: 0.0000
- N samples: 120

**Is Open Source:**
- Correlation: 0.214 *
- Linear fit: y = 1.624x + 4.6
- P-value: 0.0190
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.003x + 7.3
- P-value: 0.1297
- N samples: 120

**Model Size (B):**
- Correlation: -0.121 
- Linear fit: y = -0.000x + 5.6
- P-value: 0.1967
- N samples: 116

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.256 **
- Linear fit: y = -0.637x + 40.9
- P-value: 0.0047
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: 0.197 *
- Linear fit: y = 0.015x + 13.2
- P-value: 0.0311
- N samples: 120

**Is Open Source:**
- Correlation: 0.079 
- Linear fit: y = 2.102x + 21.9
- P-value: 0.3901
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.061 
- Linear fit: y = -1.631x + 23.7
- P-value: 0.5057
- N samples: 120

**Model Size (B):**
- Correlation: -0.002 
- Linear fit: y = -0.000x + 22.5
- P-value: 0.9823
- N samples: 116

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.305 ***
- Linear fit: y = -0.829x + 51.6
- P-value: 0.0007
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.209 *
- Linear fit: y = -6.066x + 31.4
- P-value: 0.0221
- N samples: 120

**Model Size (B):**
- Correlation: -0.095 
- Linear fit: y = -0.001x + 28.7
- P-value: 0.3117
- N samples: 116

**Is Open Source:**
- Correlation: 0.031 
- Linear fit: y = 0.908x + 27.7
- P-value: 0.7344
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: -0.017 
- Linear fit: y = -0.001x + 29.0
- P-value: 0.8570
- N samples: 120

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.111 
- Linear fit: y = 0.324x + 0.8
- P-value: 0.2264
- N samples: 120

**Benchmark Score:**
- Correlation: -0.101 
- Linear fit: y = -0.028x + 1.7
- P-value: 0.2715
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: 0.096 
- Linear fit: y = 0.001x + 0.4
- P-value: 0.2955
- N samples: 120

**Model Size (B):**
- Correlation: -0.072 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.4415
- N samples: 116

**Is Reasoning Model:**
- Correlation: 0.028 
- Linear fit: y = 0.081x + 0.9
- P-value: 0.7643
- N samples: 120

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.403 ***
- Linear fit: y = -14.077x + 102.8
- P-value: 0.0000
- N samples: 120

**Is Open Source:**
- Correlation: -0.349 ***
- Linear fit: y = -12.182x + 100.6
- P-value: 0.0001
- N samples: 120

**Model Size (B):**
- Correlation: 0.196 *
- Linear fit: y = 0.003x + 93.2
- P-value: 0.0349
- N samples: 116

**Benchmark Score:**
- Correlation: -0.094 
- Linear fit: y = -0.309x + 103.8
- P-value: 0.3046
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: -0.015 
- Linear fit: y = -0.001x + 96.0
- P-value: 0.8738
- N samples: 120

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.640 ***
- Linear fit: y = -0.606x + 27.4
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.452 ***
- Linear fit: y = -4.577x + 12.8
- P-value: 0.0000
- N samples: 120

**Is Open Source:**
- Correlation: 0.295 **
- Linear fit: y = 2.978x + 8.9
- P-value: 0.0011
- N samples: 120

**Model Size (B):**
- Correlation: -0.254 **
- Linear fit: y = -0.001x + 11.0
- P-value: 0.0059
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: 0.034 
- Linear fit: y = 0.001x + 9.6
- P-value: 0.7133
- N samples: 120

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.181 *
- Linear fit: y = -0.011x + 0.4
- P-value: 0.0473
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.062 
- Linear fit: y = -0.039x + 0.1
- P-value: 0.5013
- N samples: 120

**Is Open Source:**
- Correlation: 0.056 
- Linear fit: y = 0.035x + 0.1
- P-value: 0.5431
- N samples: 120

**Model Size (B):**
- Correlation: 0.053 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.5713
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.047 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.6134
- N samples: 120

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.403 ***
- Linear fit: y = -0.407x + 19.1
- P-value: 0.0000
- N samples: 120

**Model Size (B):**
- Correlation: -0.244 **
- Linear fit: y = -0.001x + 8.3
- P-value: 0.0082
- N samples: 116

**Is Open Source:**
- Correlation: 0.228 *
- Linear fit: y = 2.450x + 6.5
- P-value: 0.0124
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.080 
- Linear fit: y = -0.862x + 8.1
- P-value: 0.3853
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: 0.069 
- Linear fit: y = 0.002x + 6.2
- P-value: 0.4513
- N samples: 120

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.648 ***
- Linear fit: y = -0.790x + 40.4
- P-value: 0.0000
- N samples: 120

**Model Size (B):**
- Correlation: -0.305 ***
- Linear fit: y = -0.002x + 19.0
- P-value: 0.0009
- N samples: 116

**Is Reasoning Model:**
- Correlation: -0.297 ***
- Linear fit: y = -3.872x + 20.1
- P-value: 0.0010
- N samples: 120

**Is Open Source:**
- Correlation: 0.243 **
- Linear fit: y = 3.155x + 16.6
- P-value: 0.0076
- N samples: 120

**Days Since 2024-01-01:**
- Correlation: -0.052 
- Linear fit: y = -0.002x + 19.2
- P-value: 0.5705
- N samples: 120

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.364 ***
- Linear fit: y = -3.993x + 8.7
- P-value: 0.0000
- N samples: 120

**Is Reasoning Model:**
- Correlation: -0.119 
- Linear fit: y = -1.311x + 7.6
- P-value: 0.1945
- N samples: 120

**Model Size (B):**
- Correlation: 0.074 
- Linear fit: y = 0.000x + 6.7
- P-value: 0.4283
- N samples: 116

**Days Since 2024-01-01:**
- Correlation: -0.071 
- Linear fit: y = -0.002x + 8.3
- P-value: 0.4416
- N samples: 120

**Benchmark Score:**
- Correlation: 0.018 
- Linear fit: y = 0.018x + 6.4
- P-value: 0.8471
- N samples: 120

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.703, y = -0.500x + 19.5

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.648, y = -0.790x + 40.4

**3b_self_contradiction vs Benchmark Score:**
  r = -0.640, y = -0.606x + 27.4

**1a_instruction_override vs Benchmark Score:**
  r = -0.615, y = -0.524x + 26.5

**total_hallucinations vs Benchmark Score:**
  r = -0.588, y = -6.484x + 458.1

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.573, y = -0.075x + 106.8

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.535, y = -0.081x + 127.8

**category4_technical_errors vs Benchmark Score:**
  r = -0.515, y = -1.178x + 65.9

**total_hallucinations vs Is Reasoning Model:**
  r = -0.507, y = -59.785x + 307.5

**category1_input_misalignment vs Benchmark Score:**
  r = -0.486, y = -2.407x + 143.9

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.461, y = -18.694x + 115.6

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.452, y = -4.577x + 12.8

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.443, y = -23.488x + 88.7

**4a_syntax_error vs Benchmark Score:**
  r = -0.403, y = -0.407x + 19.1

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.403, y = -14.077x + 102.8

**1b_context_omission vs Is Reasoning Model:**
  r = -0.389, y = -17.788x + 68.5

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.375, y = -2.854x + 6.9

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.364, y = -3.993x + 8.7

**3a_unsupported_leap vs Is Open Source:**
  r = -0.349, y = -12.182x + 100.6

**1b_context_omission vs Benchmark Score:**
  r = -0.324, y = -1.383x + 97.9

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.312, y = -2.847x + 13.2

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.305, y = -0.002x + 19.0

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.305, y = -0.829x + 51.6

**category2_factual_errors vs Benchmark Score:**
  r = -0.304, y = -1.494x + 94.1


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
- Correlation: -0.226 *
- Linear fit: y = -0.222x + 69.4

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.045 
- Linear fit: y = 0.034x + 102.9

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.058 
- Linear fit: y = 0.026x + 30.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.630 ***
- Linear fit: y = 0.480x + 80.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.534 ***
- Linear fit: y = 0.242x + 19.8

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.467 ***
- Linear fit: y = 0.278x + 3.1

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.971 ***, y = 0.836x + 6.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.966 ***, y = 0.823x + -3.9

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.924 ***, y = 0.508x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.911 ***, y = 0.458x + -1.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.817 ***, y = 0.437x + 3.9

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.708 ***, y = 0.313x + -2.5

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.688 ***, y = 0.752x + 11.2

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.630 ***, y = 0.480x + 80.4

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.628 ***, y = 0.163x + -6.6

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.608 ***, y = 0.120x + 4.3

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.601 ***, y = 0.434x + -17.4

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.598 ***, y = 0.215x + 4.4

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.578 ***, y = 0.477x + -0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.573 ***, y = 0.100x + 4.2

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.571 ***, y = 0.701x + 10.7

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.566 ***, y = 0.763x + 6.3

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.560 ***, y = 0.034x + -0.8

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.556 ***, y = 0.242x + 2.7

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.556 ***, y = 0.367x + -15.8

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.553 ***, y = 0.250x + -1.4

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.378 ***, y = -0.026x + 2.6
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.362 ***, y = -0.210x + 35.4
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.357 ***, y = -0.310x + 75.6
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.297 ***, y = -0.018x + 2.4
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.276 **, y = -0.175x + 38.8
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.239 **, y = -0.118x + 32.0
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.226 *, y = -0.222x + 69.4
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
