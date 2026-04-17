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
- Correlation: -0.537 ***
- Linear fit: y = -0.080x + 127.7
- P-value: 0.0000
- N samples: 123

**Benchmark Score:**
- Correlation: -0.482 ***
- Linear fit: y = -2.389x + 143.3
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.442 ***
- Linear fit: y = -23.265x + 88.3
- P-value: 0.0000
- N samples: 123

**Model Size (B):**
- Correlation: 0.122 
- Linear fit: y = 0.003x + 74.6
- P-value: 0.1846
- N samples: 119

**Is Open Source:**
- Correlation: -0.071 
- Linear fit: y = -3.736x + 77.1
- P-value: 0.4357
- N samples: 123

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.304 ***
- Linear fit: y = -1.486x + 94.0
- P-value: 0.0006
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.143 
- Linear fit: y = -7.434x + 56.0
- P-value: 0.1139
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: 0.094 
- Linear fit: y = 0.014x + 42.9
- P-value: 0.3012
- N samples: 123

**Is Open Source:**
- Correlation: 0.063 
- Linear fit: y = 3.290x + 50.4
- P-value: 0.4860
- N samples: 123

**Model Size (B):**
- Correlation: -0.061 
- Linear fit: y = -0.001x + 52.3
- P-value: 0.5122
- N samples: 119

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.457 ***
- Linear fit: y = -18.347x + 115.6
- P-value: 0.0000
- N samples: 123

**Benchmark Score:**
- Correlation: -0.238 **
- Linear fit: y = -0.900x + 131.0
- P-value: 0.0079
- N samples: 123

**Is Open Source:**
- Correlation: -0.227 *
- Linear fit: y = -9.115x + 109.5
- P-value: 0.0115
- N samples: 123

**Model Size (B):**
- Correlation: 0.110 
- Linear fit: y = 0.002x + 104.3
- P-value: 0.2322
- N samples: 119

**Days Since 2024-01-01:**
- Correlation: -0.001 
- Linear fit: y = -0.000x + 105.5
- P-value: 0.9919
- N samples: 123

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.502 ***
- Linear fit: y = -1.147x + 65.2
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.243 **
- Linear fit: y = -5.898x + 35.9
- P-value: 0.0068
- N samples: 123

**Model Size (B):**
- Correlation: -0.228 *
- Linear fit: y = -0.002x + 34.1
- P-value: 0.0128
- N samples: 119

**Is Open Source:**
- Correlation: 0.053 
- Linear fit: y = 1.294x + 32.1
- P-value: 0.5582
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.015 
- Linear fit: y = -0.001x + 33.3
- P-value: 0.8730
- N samples: 123

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.584 ***
- Linear fit: y = -6.409x + 456.3
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.504 ***
- Linear fit: y = -58.784x + 306.9
- P-value: 0.0000
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.210 *
- Linear fit: y = -0.070x + 319.5
- P-value: 0.0197
- N samples: 123

**Is Open Source:**
- Correlation: -0.060 
- Linear fit: y = -6.958x + 277.5
- P-value: 0.5120
- N samples: 123

**Model Size (B):**
- Correlation: 0.008 
- Linear fit: y = 0.000x + 274.6
- P-value: 0.9285
- N samples: 119

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.537 ***
- Linear fit: y = -0.080x + 127.7
- P-value: 0.0000
- N samples: 123

**Benchmark Score:**
- Correlation: -0.482 ***
- Linear fit: y = -2.389x + 143.3
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.442 ***
- Linear fit: y = -23.265x + 88.3
- P-value: 0.0000
- N samples: 123

**Model Size (B):**
- Correlation: 0.122 
- Linear fit: y = 0.003x + 74.6
- P-value: 0.1846
- N samples: 119

**Is Open Source:**
- Correlation: -0.071 
- Linear fit: y = -3.736x + 77.1
- P-value: 0.4357
- N samples: 123

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.304 ***
- Linear fit: y = -1.486x + 94.0
- P-value: 0.0006
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.143 
- Linear fit: y = -7.434x + 56.0
- P-value: 0.1139
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: 0.094 
- Linear fit: y = 0.014x + 42.9
- P-value: 0.3012
- N samples: 123

**Is Open Source:**
- Correlation: 0.063 
- Linear fit: y = 3.290x + 50.4
- P-value: 0.4860
- N samples: 123

**Model Size (B):**
- Correlation: -0.061 
- Linear fit: y = -0.001x + 52.3
- P-value: 0.5122
- N samples: 119

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.457 ***
- Linear fit: y = -18.347x + 115.6
- P-value: 0.0000
- N samples: 123

**Benchmark Score:**
- Correlation: -0.238 **
- Linear fit: y = -0.900x + 131.0
- P-value: 0.0079
- N samples: 123

**Is Open Source:**
- Correlation: -0.227 *
- Linear fit: y = -9.115x + 109.5
- P-value: 0.0115
- N samples: 123

**Model Size (B):**
- Correlation: 0.110 
- Linear fit: y = 0.002x + 104.3
- P-value: 0.2322
- N samples: 119

**Days Since 2024-01-01:**
- Correlation: -0.001 
- Linear fit: y = -0.000x + 105.5
- P-value: 0.9919
- N samples: 123

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.502 ***
- Linear fit: y = -1.147x + 65.2
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.243 **
- Linear fit: y = -5.898x + 35.9
- P-value: 0.0068
- N samples: 123

**Model Size (B):**
- Correlation: -0.228 *
- Linear fit: y = -0.002x + 34.1
- P-value: 0.0128
- N samples: 119

**Is Open Source:**
- Correlation: 0.053 
- Linear fit: y = 1.294x + 32.1
- P-value: 0.5582
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.015 
- Linear fit: y = -0.001x + 33.3
- P-value: 0.8730
- N samples: 123

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.602 ***
- Linear fit: y = -0.515x + 26.3
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.317 ***
- Linear fit: y = -2.883x + 13.2
- P-value: 0.0004
- N samples: 123

**Is Open Source:**
- Correlation: 0.248 **
- Linear fit: y = 2.259x + 10.6
- P-value: 0.0056
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.003x + 13.8
- P-value: 0.1589
- N samples: 123

**Model Size (B):**
- Correlation: 0.074 
- Linear fit: y = 0.000x + 11.5
- P-value: 0.4259
- N samples: 119

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.573 ***
- Linear fit: y = -0.074x + 106.4
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.386 ***
- Linear fit: y = -17.517x + 68.2
- P-value: 0.0000
- N samples: 123

**Benchmark Score:**
- Correlation: -0.322 ***
- Linear fit: y = -1.375x + 97.5
- P-value: 0.0003
- N samples: 123

**Is Open Source:**
- Correlation: -0.169 
- Linear fit: y = -7.675x + 61.9
- P-value: 0.0615
- N samples: 123

**Model Size (B):**
- Correlation: 0.149 
- Linear fit: y = 0.003x + 57.5
- P-value: 0.1066
- N samples: 119

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.703 ***
- Linear fit: y = -0.499x + 19.5
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.379 ***
- Linear fit: y = -2.865x + 6.9
- P-value: 0.0000
- N samples: 123

**Is Open Source:**
- Correlation: 0.223 *
- Linear fit: y = 1.681x + 4.6
- P-value: 0.0133
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.151 
- Linear fit: y = -0.003x + 7.4
- P-value: 0.0964
- N samples: 123

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.000x + 5.6
- P-value: 0.1784
- N samples: 119

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.259 **
- Linear fit: y = -0.643x + 41.1
- P-value: 0.0038
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: 0.192 *
- Linear fit: y = 0.014x + 13.5
- P-value: 0.0336
- N samples: 123

**Is Open Source:**
- Correlation: 0.079 
- Linear fit: y = 2.096x + 21.9
- P-value: 0.3821
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.061 
- Linear fit: y = -1.603x + 23.7
- P-value: 0.5042
- N samples: 123

**Model Size (B):**
- Correlation: -0.010 
- Linear fit: y = -0.000x + 22.6
- P-value: 0.9121
- N samples: 119

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.304 ***
- Linear fit: y = -0.821x + 51.4
- P-value: 0.0006
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.206 *
- Linear fit: y = -5.919x + 31.3
- P-value: 0.0222
- N samples: 123

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.001x + 28.7
- P-value: 0.3073
- N samples: 119

**Is Open Source:**
- Correlation: 0.033 
- Linear fit: y = 0.953x + 27.6
- P-value: 0.7156
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.019 
- Linear fit: y = -0.002x + 29.1
- P-value: 0.8346
- N samples: 123

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.124 
- Linear fit: y = 0.001x + 0.3
- P-value: 0.1715
- N samples: 123

**Is Open Source:**
- Correlation: 0.082 
- Linear fit: y = 0.241x + 0.9
- P-value: 0.3666
- N samples: 123

**Benchmark Score:**
- Correlation: -0.079 
- Linear fit: y = -0.022x + 1.6
- P-value: 0.3866
- N samples: 123

**Model Size (B):**
- Correlation: -0.051 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.5834
- N samples: 119

**Is Reasoning Model:**
- Correlation: 0.030 
- Linear fit: y = 0.087x + 0.9
- P-value: 0.7441
- N samples: 123

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.402 ***
- Linear fit: y = -13.892x + 102.8
- P-value: 0.0000
- N samples: 123

**Is Open Source:**
- Correlation: -0.351 ***
- Linear fit: y = -12.155x + 100.6
- P-value: 0.0001
- N samples: 123

**Model Size (B):**
- Correlation: 0.202 *
- Linear fit: y = 0.003x + 93.3
- P-value: 0.0279
- N samples: 119

**Benchmark Score:**
- Correlation: -0.088 
- Linear fit: y = -0.285x + 103.2
- P-value: 0.3349
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.007 
- Linear fit: y = -0.001x + 95.6
- P-value: 0.9400
- N samples: 123

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.641 ***
- Linear fit: y = -0.606x + 27.4
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.441 ***
- Linear fit: y = -4.430x + 12.6
- P-value: 0.0000
- N samples: 123

**Is Open Source:**
- Correlation: 0.301 ***
- Linear fit: y = 3.016x + 8.8
- P-value: 0.0007
- N samples: 123

**Model Size (B):**
- Correlation: -0.259 **
- Linear fit: y = -0.001x + 10.9
- P-value: 0.0045
- N samples: 119

**Days Since 2024-01-01:**
- Correlation: 0.022 
- Linear fit: y = 0.001x + 9.8
- P-value: 0.8128
- N samples: 123

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.154 
- Linear fit: y = -0.009x + 0.4
- P-value: 0.0890
- N samples: 123

**Model Size (B):**
- Correlation: 0.072 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.4386
- N samples: 119

**Is Reasoning Model:**
- Correlation: -0.038 
- Linear fit: y = -0.024x + 0.1
- P-value: 0.6757
- N samples: 123

**Is Open Source:**
- Correlation: 0.038 
- Linear fit: y = 0.024x + 0.1
- P-value: 0.6757
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.7761
- N samples: 123

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.379 ***
- Linear fit: y = -0.385x + 18.6
- P-value: 0.0000
- N samples: 123

**Model Size (B):**
- Correlation: -0.222 *
- Linear fit: y = -0.001x + 8.4
- P-value: 0.0151
- N samples: 119

**Is Open Source:**
- Correlation: 0.202 *
- Linear fit: y = 2.177x + 6.7
- P-value: 0.0251
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: 0.092 
- Linear fit: y = 0.003x + 5.9
- P-value: 0.3104
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.077 
- Linear fit: y = -0.829x + 8.2
- P-value: 0.3982
- N samples: 123

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.641 ***
- Linear fit: y = -0.777x + 40.1
- P-value: 0.0000
- N samples: 123

**Model Size (B):**
- Correlation: -0.302 ***
- Linear fit: y = -0.002x + 19.1
- P-value: 0.0008
- N samples: 119

**Is Reasoning Model:**
- Correlation: -0.292 **
- Linear fit: y = -3.760x + 20.1
- P-value: 0.0011
- N samples: 123

**Is Open Source:**
- Correlation: 0.233 **
- Linear fit: y = 3.003x + 16.7
- P-value: 0.0095
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.043 
- Linear fit: y = -0.002x + 19.1
- P-value: 0.6344
- N samples: 123

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.357 ***
- Linear fit: y = -3.887x + 8.6
- P-value: 0.0000
- N samples: 123

**Is Reasoning Model:**
- Correlation: -0.120 
- Linear fit: y = -1.309x + 7.6
- P-value: 0.1846
- N samples: 123

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.002x + 8.4
- P-value: 0.4248
- N samples: 123

**Model Size (B):**
- Correlation: 0.071 
- Linear fit: y = 0.000x + 6.7
- P-value: 0.4444
- N samples: 119

**Benchmark Score:**
- Correlation: 0.015 
- Linear fit: y = 0.015x + 6.5
- P-value: 0.8697
- N samples: 123

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.703, y = -0.499x + 19.5

**3b_self_contradiction vs Benchmark Score:**
  r = -0.641, y = -0.606x + 27.4

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.641, y = -0.777x + 40.1

**1a_instruction_override vs Benchmark Score:**
  r = -0.602, y = -0.515x + 26.3

**total_hallucinations vs Benchmark Score:**
  r = -0.584, y = -6.409x + 456.3

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.573, y = -0.074x + 106.4

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.537, y = -0.080x + 127.7

**total_hallucinations vs Is Reasoning Model:**
  r = -0.504, y = -58.784x + 306.9

**category4_technical_errors vs Benchmark Score:**
  r = -0.502, y = -1.147x + 65.2

**category1_input_misalignment vs Benchmark Score:**
  r = -0.482, y = -2.389x + 143.3

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.457, y = -18.347x + 115.6

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.442, y = -23.265x + 88.3

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.441, y = -4.430x + 12.6

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.402, y = -13.892x + 102.8

**1b_context_omission vs Is Reasoning Model:**
  r = -0.386, y = -17.517x + 68.2

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.379, y = -2.865x + 6.9

**4a_syntax_error vs Benchmark Score:**
  r = -0.379, y = -0.385x + 18.6

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.357, y = -3.887x + 8.6

**3a_unsupported_leap vs Is Open Source:**
  r = -0.351, y = -12.155x + 100.6

**1b_context_omission vs Benchmark Score:**
  r = -0.322, y = -1.375x + 97.5

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.317, y = -2.883x + 13.2

**category2_factual_errors vs Benchmark Score:**
  r = -0.304, y = -1.486x + 94.0

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.304, y = -0.821x + 51.4

**4b_model_semantics_breach vs Model Size (B):**
  r = -0.302, y = -0.002x + 19.1

**3b_self_contradiction vs Is Open Source:**
  r = 0.301, y = 3.016x + 8.8


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
- Linear fit: y = -0.221x + 69.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.045 
- Linear fit: y = 0.034x + 103.0

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.051 
- Linear fit: y = 0.022x + 30.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.628 ***
- Linear fit: y = 0.478x + 80.5

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.531 ***
- Linear fit: y = 0.242x + 20.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.467 ***
- Linear fit: y = 0.279x + 3.2

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.971 ***, y = 0.836x + 6.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.966 ***, y = 0.822x + -3.8

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.923 ***, y = 0.507x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.910 ***, y = 0.459x + -1.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.817 ***, y = 0.436x + 3.9

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.709 ***, y = 0.316x + -2.5

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.686 ***, y = 0.748x + 11.2

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.628 ***, y = 0.478x + 80.5

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.622 ***, y = 0.162x + -6.6

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.606 ***, y = 0.120x + 4.2

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.600 ***, y = 0.433x + -17.4

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.598 ***, y = 0.215x + 4.4

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.578 ***, y = 0.101x + 4.2

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.576 ***, y = 0.473x + -0.1

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.566 ***, y = 0.761x + 6.3

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.564 ***, y = 0.692x + 10.9

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.552 ***, y = 0.365x + -15.7

**Category 2: Factual Errors vs 2c: False Citation:**
  r = 0.550 ***, y = 0.034x + -0.7

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.550 ***, y = 0.248x + -1.3

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.545 ***, y = 0.238x + 2.7

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.379 ***, y = -0.026x + 2.6
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.364 ***, y = -0.210x + 35.3
  (Models good at one tend to be worse at the other)

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = -0.356 ***, y = -0.311x + 75.4
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2c: False Citation:**
  r = -0.301 ***, y = -0.018x + 2.4
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = -0.273 **, y = -0.172x + 38.5
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = -0.242 **, y = -0.119x + 32.0
  (Models good at one tend to be worse at the other)

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = -0.226 *, y = -0.221x + 69.2
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
