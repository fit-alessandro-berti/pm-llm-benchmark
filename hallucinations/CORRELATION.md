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
- Correlation: -0.799 ***
- Linear fit: y = -2.488x + 129.8
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.512 ***
- Linear fit: y = -24.595x + 55.0
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.241 ***
- Linear fit: y = 11.584x + 36.8
- P-value: 0.0009
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: -0.167 *
- Linear fit: y = -0.027x + 57.0
- P-value: 0.0198
- N samples: 194

**Model Size (B):**
- Correlation: -0.144 *
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0451
- N samples: 194

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.564 ***
- Linear fit: y = -1.582x + 83.9
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.295 ***
- Linear fit: y = 0.042x + 6.5
- P-value: 0.0000
- N samples: 194

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 10.068x + 23.3
- P-value: 0.0014
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.214 **
- Linear fit: y = -9.274x + 33.2
- P-value: 0.0032
- N samples: 187

**Model Size (B):**
- Correlation: -0.125 
- Linear fit: y = -0.003x + 29.9
- P-value: 0.0822
- N samples: 194

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.769 ***
- Linear fit: y = -3.370x + 193.1
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.632 ***
- Linear fit: y = -42.685x + 96.3
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.184 *
- Linear fit: y = 12.442x + 68.9
- P-value: 0.0118
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: -0.163 *
- Linear fit: y = -0.037x + 94.8
- P-value: 0.0228
- N samples: 194

**Model Size (B):**
- Correlation: -0.127 
- Linear fit: y = -0.005x + 77.7
- P-value: 0.0779
- N samples: 194

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.703 ***
- Linear fit: y = -1.355x + 66.8
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.297 ***
- Linear fit: y = -8.819x + 23.9
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 6.892x + 15.9
- P-value: 0.0014
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.158 *
- Linear fit: y = 0.016x + 11.2
- P-value: 0.0275
- N samples: 194

**Model Size (B):**
- Correlation: -0.144 *
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0446
- N samples: 194

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.813 ***
- Linear fit: y = -9.534x + 507.9
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.515 ***
- Linear fit: y = -93.115x + 220.7
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.249 ***
- Linear fit: y = 45.147x + 151.3
- P-value: 0.0006
- N samples: 187

**Model Size (B):**
- Correlation: -0.153 *
- Linear fit: y = -0.016x + 181.7
- P-value: 0.0331
- N samples: 194

**Days Since 2024-01-01:**
- Correlation: -0.006 
- Linear fit: y = -0.004x + 177.3
- P-value: 0.9292
- N samples: 194

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.799 ***
- Linear fit: y = -2.488x + 129.8
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.512 ***
- Linear fit: y = -24.595x + 55.0
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.241 ***
- Linear fit: y = 11.584x + 36.8
- P-value: 0.0009
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: -0.167 *
- Linear fit: y = -0.027x + 57.0
- P-value: 0.0198
- N samples: 194

**Model Size (B):**
- Correlation: -0.144 *
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0451
- N samples: 194

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.564 ***
- Linear fit: y = -1.582x + 83.9
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.295 ***
- Linear fit: y = 0.042x + 6.5
- P-value: 0.0000
- N samples: 194

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 10.068x + 23.3
- P-value: 0.0014
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.214 **
- Linear fit: y = -9.274x + 33.2
- P-value: 0.0032
- N samples: 187

**Model Size (B):**
- Correlation: -0.125 
- Linear fit: y = -0.003x + 29.9
- P-value: 0.0822
- N samples: 194

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.769 ***
- Linear fit: y = -3.370x + 193.1
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.632 ***
- Linear fit: y = -42.685x + 96.3
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.184 *
- Linear fit: y = 12.442x + 68.9
- P-value: 0.0118
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: -0.163 *
- Linear fit: y = -0.037x + 94.8
- P-value: 0.0228
- N samples: 194

**Model Size (B):**
- Correlation: -0.127 
- Linear fit: y = -0.005x + 77.7
- P-value: 0.0779
- N samples: 194

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.703 ***
- Linear fit: y = -1.355x + 66.8
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.297 ***
- Linear fit: y = -8.819x + 23.9
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 6.892x + 15.9
- P-value: 0.0014
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.158 *
- Linear fit: y = 0.016x + 11.2
- P-value: 0.0275
- N samples: 194

**Model Size (B):**
- Correlation: -0.144 *
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0446
- N samples: 194

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.660 ***
- Linear fit: y = -0.505x + 25.3
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.334 ***
- Linear fit: y = -3.942x + 9.7
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.284 ***
- Linear fit: y = 3.357x + 5.9
- P-value: 0.0001
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.184 *
- Linear fit: y = 0.007x + 3.9
- P-value: 0.0102
- N samples: 194

**Model Size (B):**
- Correlation: -0.111 
- Linear fit: y = -0.001x + 8.0
- P-value: 0.1225
- N samples: 194

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.721 ***
- Linear fit: y = -1.579x + 86.1
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.523 ***
- Linear fit: y = -17.669x + 39.6
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: -0.362 ***
- Linear fit: y = -0.041x + 52.5
- P-value: 0.0000
- N samples: 194

**Is Open Source:**
- Correlation: 0.157 *
- Linear fit: y = 5.295x + 28.2
- P-value: 0.0324
- N samples: 187

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.002x + 32.2
- P-value: 0.0860
- N samples: 194

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.720 ***
- Linear fit: y = -0.405x + 18.4
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.344 ***
- Linear fit: y = -2.984x + 5.7
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.338 ***
- Linear fit: y = 2.932x + 2.7
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.238 ***
- Linear fit: y = 0.007x + 0.6
- P-value: 0.0008
- N samples: 194

**Model Size (B):**
- Correlation: -0.162 *
- Linear fit: y = -0.001x + 4.6
- P-value: 0.0240
- N samples: 194

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.534 ***
- Linear fit: y = -0.832x + 37.5
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.308 ***
- Linear fit: y = 0.025x + -4.4
- P-value: 0.0000
- N samples: 194

**Is Open Source:**
- Correlation: 0.226 **
- Linear fit: y = 5.440x + 5.5
- P-value: 0.0018
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.201 **
- Linear fit: y = -4.814x + 10.8
- P-value: 0.0059
- N samples: 187

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.001x + 8.8
- P-value: 0.3418
- N samples: 194

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.482 ***
- Linear fit: y = -0.700x + 44.1
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.251 ***
- Linear fit: y = 0.019x + 9.8
- P-value: 0.0004
- N samples: 194

**Is Open Source:**
- Correlation: 0.212 **
- Linear fit: y = 4.760x + 17.1
- P-value: 0.0036
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.208 **
- Linear fit: y = -4.665x + 21.9
- P-value: 0.0043
- N samples: 187

**Model Size (B):**
- Correlation: -0.148 *
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0397
- N samples: 194

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.130 
- Linear fit: y = -0.050x + 2.4
- P-value: 0.0766
- N samples: 187

**Model Size (B):**
- Correlation: -0.076 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.2953
- N samples: 194

**Days Since 2024-01-01:**
- Correlation: -0.043 
- Linear fit: y = -0.001x + 1.1
- P-value: 0.5517
- N samples: 194

**Is Reasoning Model:**
- Correlation: 0.035 
- Linear fit: y = 0.205x + 0.5
- P-value: 0.6386
- N samples: 187

**Is Open Source:**
- Correlation: -0.022 
- Linear fit: y = -0.131x + 0.7
- P-value: 0.7644
- N samples: 187

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.753 ***
- Linear fit: y = -2.761x + 162.1
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.642 ***
- Linear fit: y = -36.304x + 83.5
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: -0.255 ***
- Linear fit: y = -0.048x + 90.9
- P-value: 0.0003
- N samples: 194

**Is Open Source:**
- Correlation: 0.157 *
- Linear fit: y = 8.873x + 61.1
- P-value: 0.0323
- N samples: 187

**Model Size (B):**
- Correlation: -0.113 
- Linear fit: y = -0.004x + 67.4
- P-value: 0.1153
- N samples: 194

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.639 ***
- Linear fit: y = -0.573x + 29.4
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.442 ***
- Linear fit: y = -6.111x + 12.4
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.237 **
- Linear fit: y = 3.285x + 7.7
- P-value: 0.0011
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.221 **
- Linear fit: y = 0.010x + 4.1
- P-value: 0.0019
- N samples: 194

**Model Size (B):**
- Correlation: -0.149 *
- Linear fit: y = -0.001x + 9.9
- P-value: 0.0385
- N samples: 194

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.355 ***
- Linear fit: y = -0.036x + 1.6
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.203 **
- Linear fit: y = 0.001x + -0.2
- P-value: 0.0045
- N samples: 194

**Is Open Source:**
- Correlation: 0.181 *
- Linear fit: y = 0.285x + 0.2
- P-value: 0.0129
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.173 *
- Linear fit: y = -0.270x + 0.5
- P-value: 0.0180
- N samples: 187

**Model Size (B):**
- Correlation: -0.061 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.3980
- N samples: 194

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.623 ***
- Linear fit: y = -0.622x + 27.0
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.304 ***
- Linear fit: y = 4.697x + 2.8
- P-value: 0.0000
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: 0.250 ***
- Linear fit: y = 0.013x + -1.4
- P-value: 0.0004
- N samples: 194

**Model Size (B):**
- Correlation: -0.163 *
- Linear fit: y = -0.001x + 5.8
- P-value: 0.0234
- N samples: 194

**Is Reasoning Model:**
- Correlation: -0.134 
- Linear fit: y = -2.071x + 6.3
- P-value: 0.0667
- N samples: 187

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.720 ***
- Linear fit: y = -0.685x + 34.3
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.385 ***
- Linear fit: y = -5.641x + 13.1
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.247 ***
- Linear fit: y = 3.633x + 8.4
- P-value: 0.0006
- N samples: 187

**Model Size (B):**
- Correlation: -0.200 **
- Linear fit: y = -0.002x + 11.0
- P-value: 0.0051
- N samples: 194

**Days Since 2024-01-01:**
- Correlation: 0.060 
- Linear fit: y = 0.003x + 8.7
- P-value: 0.4033
- N samples: 194

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.224 **
- Linear fit: y = -1.438x + 4.7
- P-value: 0.0020
- N samples: 187

**Model Size (B):**
- Correlation: 0.177 *
- Linear fit: y = 0.001x + 3.5
- P-value: 0.0133
- N samples: 194

**Is Reasoning Model:**
- Correlation: -0.173 *
- Linear fit: y = -1.107x + 4.4
- P-value: 0.0178
- N samples: 187

**Benchmark Score:**
- Correlation: -0.114 
- Linear fit: y = -0.047x + 5.6
- P-value: 0.1188
- N samples: 187

**Days Since 2024-01-01:**
- Correlation: -0.003 
- Linear fit: y = -0.000x + 3.8
- P-value: 0.9652
- N samples: 194

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.813, y = -9.534x + 507.9

**category1_input_misalignment vs Benchmark Score:**
  r = -0.799, y = -2.488x + 129.8

**category3_logical_errors vs Benchmark Score:**
  r = -0.769, y = -3.370x + 193.1

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.753, y = -2.761x + 162.1

**1b_context_omission vs Benchmark Score:**
  r = -0.721, y = -1.579x + 86.1

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.720, y = -0.685x + 34.3

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.720, y = -0.405x + 18.4

**category4_technical_errors vs Benchmark Score:**
  r = -0.703, y = -1.355x + 66.8

**1a_instruction_override vs Benchmark Score:**
  r = -0.660, y = -0.505x + 25.3

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.642, y = -36.304x + 83.5

**3b_self_contradiction vs Benchmark Score:**
  r = -0.639, y = -0.573x + 29.4

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.632, y = -42.685x + 96.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.623, y = -0.622x + 27.0

**category2_factual_errors vs Benchmark Score:**
  r = -0.564, y = -1.582x + 83.9

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.534, y = -0.832x + 37.5

**1b_context_omission vs Is Reasoning Model:**
  r = -0.523, y = -17.669x + 39.6

**total_hallucinations vs Is Reasoning Model:**
  r = -0.515, y = -93.115x + 220.7

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.512, y = -24.595x + 55.0

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.482, y = -0.700x + 44.1

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.442, y = -6.111x + 12.4

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.385, y = -5.641x + 13.1

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.362, y = -0.041x + 52.5

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.355, y = -0.036x + 1.6

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.344, y = -2.984x + 5.7

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.338, y = 2.932x + 2.7

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.334, y = -3.942x + 9.7

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.308, y = 0.025x + -4.4

**4a_syntax_error vs Is Open Source:**
  r = 0.304, y = 4.697x + 2.8


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
- Correlation: 0.555 ***
- Linear fit: y = 0.499x + 7.1

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.812 ***
- Linear fit: y = 1.137x + 26.7

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.658 ***
- Linear fit: y = 0.407x + 1.8

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.633 ***
- Linear fit: y = 0.985x + 47.5

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.731 ***
- Linear fit: y = 0.502x + 4.9

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.711 ***
- Linear fit: y = 0.314x + -4.4

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.988 ***, y = 0.827x + 3.3

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.947 ***, y = 0.669x + 2.3

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.899 ***, y = 0.443x + 1.7

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.895 ***, y = 0.496x + -5.8

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.881 ***, y = 0.457x + 6.5

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.878 ***, y = 0.454x + -3.5

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.812 ***, y = 1.137x + 26.7

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.799 ***, y = 0.164x + -3.0

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.794 ***, y = 1.256x + 4.1

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.793 ***, y = 0.930x + 25.8

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.789 ***, y = 0.194x + -0.7

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.785 ***, y = 2.158x + -0.7

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.778 ***, y = 1.291x + 25.7

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.778 ***, y = 0.361x + 2.4

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.776 ***, y = 0.446x + 5.6

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.773 ***, y = 0.246x + 2.3

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.764 ***, y = 0.386x + 2.0

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.763 ***, y = 0.564x + -0.1

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.755 ***, y = 0.137x + -1.7

**Category 4: Technical Errors vs 1c: Prompt Contradiction:**
  r = 0.745 ***, y = 0.219x + 0.0

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
