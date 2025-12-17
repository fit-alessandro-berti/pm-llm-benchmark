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
- Correlation: -0.794 ***
- Linear fit: y = -2.491x + 129.6
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.567 ***
- Linear fit: y = -26.919x + 55.7
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.240 **
- Linear fit: y = 11.439x + 36.7
- P-value: 0.0012
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: -0.196 **
- Linear fit: y = -0.032x + 59.2
- P-value: 0.0077
- N samples: 184

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0640
- N samples: 180

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.537 ***
- Linear fit: y = -1.515x + 81.3
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.299 ***
- Linear fit: y = 0.044x + 6.1
- P-value: 0.0000
- N samples: 184

**Is Reasoning Model:**
- Correlation: -0.247 ***
- Linear fit: y = -10.558x + 33.6
- P-value: 0.0009
- N samples: 178

**Is Open Source:**
- Correlation: 0.228 **
- Linear fit: y = 9.753x + 23.3
- P-value: 0.0022
- N samples: 178

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.003x + 29.7
- P-value: 0.1184
- N samples: 180

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.770 ***
- Linear fit: y = -3.455x + 196.8
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.657 ***
- Linear fit: y = -44.618x + 97.8
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.183 *
- Linear fit: y = 12.436x + 69.8
- P-value: 0.0146
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: -0.141 
- Linear fit: y = -0.033x + 93.1
- P-value: 0.0571
- N samples: 184

**Model Size (B):**
- Correlation: -0.120 
- Linear fit: y = -0.004x + 79.1
- P-value: 0.1091
- N samples: 180

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.363x + 67.1
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.319 ***
- Linear fit: y = -9.511x + 24.2
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.223 **
- Linear fit: y = 6.680x + 16.0
- P-value: 0.0027
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.175 *
- Linear fit: y = 0.018x + 10.3
- P-value: 0.0176
- N samples: 184

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.002x + 20.4
- P-value: 0.0762
- N samples: 180

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.807 ***
- Linear fit: y = -9.608x + 510.8
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.553 ***
- Linear fit: y = -99.641x + 223.9
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.247 ***
- Linear fit: y = 44.614x + 152.3
- P-value: 0.0009
- N samples: 178

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.014x + 183.2
- P-value: 0.0528
- N samples: 180

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.001x + 175.5
- P-value: 0.9848
- N samples: 184

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.794 ***
- Linear fit: y = -2.491x + 129.6
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.567 ***
- Linear fit: y = -26.919x + 55.7
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.240 **
- Linear fit: y = 11.439x + 36.7
- P-value: 0.0012
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: -0.196 **
- Linear fit: y = -0.032x + 59.2
- P-value: 0.0077
- N samples: 184

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0640
- N samples: 180

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.537 ***
- Linear fit: y = -1.515x + 81.3
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.299 ***
- Linear fit: y = 0.044x + 6.1
- P-value: 0.0000
- N samples: 184

**Is Reasoning Model:**
- Correlation: -0.247 ***
- Linear fit: y = -10.558x + 33.6
- P-value: 0.0009
- N samples: 178

**Is Open Source:**
- Correlation: 0.228 **
- Linear fit: y = 9.753x + 23.3
- P-value: 0.0022
- N samples: 178

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.003x + 29.7
- P-value: 0.1184
- N samples: 180

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.770 ***
- Linear fit: y = -3.455x + 196.8
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.657 ***
- Linear fit: y = -44.618x + 97.8
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.183 *
- Linear fit: y = 12.436x + 69.8
- P-value: 0.0146
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: -0.141 
- Linear fit: y = -0.033x + 93.1
- P-value: 0.0571
- N samples: 184

**Model Size (B):**
- Correlation: -0.120 
- Linear fit: y = -0.004x + 79.1
- P-value: 0.1091
- N samples: 180

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.363x + 67.1
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.319 ***
- Linear fit: y = -9.511x + 24.2
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.223 **
- Linear fit: y = 6.680x + 16.0
- P-value: 0.0027
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.175 *
- Linear fit: y = 0.018x + 10.3
- P-value: 0.0176
- N samples: 184

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.002x + 20.4
- P-value: 0.0762
- N samples: 180

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.650 ***
- Linear fit: y = -0.483x + 24.4
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.395 ***
- Linear fit: y = -4.443x + 9.7
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.288 ***
- Linear fit: y = 3.249x + 5.8
- P-value: 0.0001
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.150 *
- Linear fit: y = 0.006x + 4.5
- P-value: 0.0421
- N samples: 184

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.001x + 7.7
- P-value: 0.1602
- N samples: 180

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.719 ***
- Linear fit: y = -1.609x + 87.1
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.564 ***
- Linear fit: y = -19.094x + 40.2
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: -0.380 ***
- Linear fit: y = -0.044x + 54.0
- P-value: 0.0000
- N samples: 184

**Is Open Source:**
- Correlation: 0.154 *
- Linear fit: y = 5.237x + 28.3
- P-value: 0.0397
- N samples: 178

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.002x + 32.5
- P-value: 0.1118
- N samples: 180

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.700 ***
- Linear fit: y = -0.399x + 18.1
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.392 ***
- Linear fit: y = -3.382x + 5.8
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.341 ***
- Linear fit: y = 2.953x + 2.6
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.228 **
- Linear fit: y = 0.007x + 0.7
- P-value: 0.0019
- N samples: 184

**Model Size (B):**
- Correlation: -0.156 *
- Linear fit: y = -0.001x + 4.5
- P-value: 0.0366
- N samples: 180

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.498 ***
- Linear fit: y = -0.763x + 34.8
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.307 ***
- Linear fit: y = 0.024x + -4.2
- P-value: 0.0000
- N samples: 184

**Is Reasoning Model:**
- Correlation: -0.253 ***
- Linear fit: y = -5.876x + 11.1
- P-value: 0.0007
- N samples: 178

**Is Open Source:**
- Correlation: 0.224 **
- Linear fit: y = 5.205x + 5.5
- P-value: 0.0027
- N samples: 178

**Model Size (B):**
- Correlation: -0.059 
- Linear fit: y = -0.001x + 8.6
- P-value: 0.4337
- N samples: 180

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.472 ***
- Linear fit: y = -0.703x + 44.1
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.260 ***
- Linear fit: y = 0.020x + 9.2
- P-value: 0.0004
- N samples: 184

**Is Reasoning Model:**
- Correlation: -0.216 **
- Linear fit: y = -4.865x + 21.9
- P-value: 0.0038
- N samples: 178

**Is Open Source:**
- Correlation: 0.209 **
- Linear fit: y = 4.708x + 17.1
- P-value: 0.0052
- N samples: 178

**Model Size (B):**
- Correlation: -0.141 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0596
- N samples: 180

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.123 
- Linear fit: y = -0.050x + 2.4
- P-value: 0.1006
- N samples: 178

**Model Size (B):**
- Correlation: -0.073 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.3310
- N samples: 180

**Days Since 2024-01-01:**
- Correlation: -0.037 
- Linear fit: y = -0.001x + 1.1
- P-value: 0.6224
- N samples: 184

**Is Reasoning Model:**
- Correlation: 0.030 
- Linear fit: y = 0.183x + 0.6
- P-value: 0.6898
- N samples: 178

**Is Open Source:**
- Correlation: -0.026 
- Linear fit: y = -0.161x + 0.7
- P-value: 0.7268
- N samples: 178

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.758 ***
- Linear fit: y = -2.840x + 165.7
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.666 ***
- Linear fit: y = -37.794x + 84.8
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: -0.229 **
- Linear fit: y = -0.044x + 89.5
- P-value: 0.0017
- N samples: 184

**Is Open Source:**
- Correlation: 0.157 *
- Linear fit: y = 8.934x + 62.0
- P-value: 0.0362
- N samples: 178

**Model Size (B):**
- Correlation: -0.107 
- Linear fit: y = -0.003x + 68.9
- P-value: 0.1517
- N samples: 180

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.631 ***
- Linear fit: y = -0.578x + 29.5
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.471 ***
- Linear fit: y = -6.541x + 12.5
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.231 **
- Linear fit: y = 3.218x + 7.6
- P-value: 0.0019
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.225 **
- Linear fit: y = 0.011x + 3.9
- P-value: 0.0021
- N samples: 184

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.001x + 9.9
- P-value: 0.0608
- N samples: 180

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.344 ***
- Linear fit: y = -0.036x + 1.6
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.220 **
- Linear fit: y = 0.001x + -0.3
- P-value: 0.0027
- N samples: 184

**Is Reasoning Model:**
- Correlation: -0.178 *
- Linear fit: y = -0.284x + 0.5
- P-value: 0.0172
- N samples: 178

**Is Open Source:**
- Correlation: 0.178 *
- Linear fit: y = 0.284x + 0.2
- P-value: 0.0173
- N samples: 178

**Model Size (B):**
- Correlation: -0.056 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4558
- N samples: 180

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.616 ***
- Linear fit: y = -0.633x + 27.3
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.302 ***
- Linear fit: y = 4.718x + 2.7
- P-value: 0.0000
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.257 ***
- Linear fit: y = 0.014x + -1.8
- P-value: 0.0004
- N samples: 184

**Model Size (B):**
- Correlation: -0.158 *
- Linear fit: y = -0.001x + 5.8
- P-value: 0.0346
- N samples: 180

**Is Reasoning Model:**
- Correlation: -0.145 
- Linear fit: y = -2.262x + 6.3
- P-value: 0.0530
- N samples: 178

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.707 ***
- Linear fit: y = -0.682x + 34.2
- P-value: 0.0000
- N samples: 178

**Is Reasoning Model:**
- Correlation: -0.412 ***
- Linear fit: y = -6.017x + 13.3
- P-value: 0.0000
- N samples: 178

**Is Open Source:**
- Correlation: 0.235 **
- Linear fit: y = 3.434x + 8.6
- P-value: 0.0016
- N samples: 178

**Model Size (B):**
- Correlation: -0.189 *
- Linear fit: y = -0.002x + 11.0
- P-value: 0.0109
- N samples: 180

**Days Since 2024-01-01:**
- Correlation: 0.079 
- Linear fit: y = 0.004x + 8.3
- P-value: 0.2844
- N samples: 184

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.227 **
- Linear fit: y = -1.471x + 4.7
- P-value: 0.0023
- N samples: 178

**Model Size (B):**
- Correlation: 0.193 **
- Linear fit: y = 0.001x + 3.6
- P-value: 0.0093
- N samples: 180

**Is Reasoning Model:**
- Correlation: -0.190 *
- Linear fit: y = -1.233x + 4.5
- P-value: 0.0109
- N samples: 178

**Benchmark Score:**
- Correlation: -0.112 
- Linear fit: y = -0.048x + 5.6
- P-value: 0.1380
- N samples: 178

**Days Since 2024-01-01:**
- Correlation: 0.012 
- Linear fit: y = 0.000x + 3.7
- P-value: 0.8667
- N samples: 184

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.807, y = -9.608x + 510.8

**category1_input_misalignment vs Benchmark Score:**
  r = -0.794, y = -2.491x + 129.6

**category3_logical_errors vs Benchmark Score:**
  r = -0.770, y = -3.455x + 196.8

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.758, y = -2.840x + 165.7

**1b_context_omission vs Benchmark Score:**
  r = -0.719, y = -1.609x + 87.1

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.707, y = -0.682x + 34.2

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.700, y = -0.399x + 18.1

**category4_technical_errors vs Benchmark Score:**
  r = -0.691, y = -1.363x + 67.1

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.666, y = -37.794x + 84.8

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.657, y = -44.618x + 97.8

**1a_instruction_override vs Benchmark Score:**
  r = -0.650, y = -0.483x + 24.4

**3b_self_contradiction vs Benchmark Score:**
  r = -0.631, y = -0.578x + 29.5

**4a_syntax_error vs Benchmark Score:**
  r = -0.616, y = -0.633x + 27.3

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.567, y = -26.919x + 55.7

**1b_context_omission vs Is Reasoning Model:**
  r = -0.564, y = -19.094x + 40.2

**total_hallucinations vs Is Reasoning Model:**
  r = -0.553, y = -99.641x + 223.9

**category2_factual_errors vs Benchmark Score:**
  r = -0.537, y = -1.515x + 81.3

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.498, y = -0.763x + 34.8

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.472, y = -0.703x + 44.1

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.471, y = -6.541x + 12.5

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.412, y = -6.017x + 13.3

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.395, y = -4.443x + 9.7

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.392, y = -3.382x + 5.8

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.380, y = -0.044x + 54.0

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.344, y = -0.036x + 1.6

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.341, y = 2.953x + 2.6

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.319, y = -9.511x + 24.2

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.307, y = 0.024x + -4.2

**4a_syntax_error vs Is Open Source:**
  r = 0.302, y = 4.718x + 2.7


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
- Correlation: 0.523 ***
- Linear fit: y = 0.468x + 8.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.818 ***
- Linear fit: y = 1.164x + 26.5

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.645 ***
- Linear fit: y = 0.405x + 2.0

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.634 ***
- Linear fit: y = 1.007x + 48.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.726 ***
- Linear fit: y = 0.509x + 5.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.709 ***
- Linear fit: y = 0.313x + -4.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.988 ***, y = 0.826x + 3.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.949 ***, y = 0.681x + 2.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.900 ***, y = 0.439x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.890 ***, y = 0.483x + -5.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.884 ***, y = 0.467x + 6.2

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.879 ***, y = 0.457x + -3.7

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.818 ***, y = 1.164x + 26.5

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.806 ***, y = 0.165x + -3.3

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.804 ***, y = 0.957x + 25.7

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.790 ***, y = 1.271x + 4.1

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.783 ***, y = 0.470x + 5.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.782 ***, y = 0.185x + -0.5

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.779 ***, y = 0.361x + 2.4

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.778 ***, y = 1.292x + 26.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.769 ***, y = 0.250x + 2.3

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.769 ***, y = 2.064x + -0.4

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.762 ***, y = 0.384x + 1.9

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.745 ***, y = 0.501x + 1.1

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.744 ***, y = 0.570x + -0.1

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.742 ***, y = 0.134x + -1.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
