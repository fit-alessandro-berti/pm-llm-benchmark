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
- Correlation: -0.608 ***
- Linear fit: y = -0.086x + 130.8
- P-value: 0.0000
- N samples: 160

**Benchmark Score:**
- Correlation: -0.584 ***
- Linear fit: y = -3.056x + 161.6
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.433 ***
- Linear fit: y = -22.643x + 82.8
- P-value: 0.0000
- N samples: 160

**Is Open Source:**
- Correlation: -0.073 
- Linear fit: y = -3.797x + 70.8
- P-value: 0.3622
- N samples: 160

**Model Size (B):**
- Correlation: 0.067 
- Linear fit: y = 0.001x + 70.7
- P-value: 0.4361
- N samples: 139

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.372 ***
- Linear fit: y = -1.908x + 105.6
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.194 *
- Linear fit: y = -9.939x + 53.9
- P-value: 0.0139
- N samples: 160

**Model Size (B):**
- Correlation: -0.099 
- Linear fit: y = -0.002x + 50.9
- P-value: 0.2471
- N samples: 139

**Days Since 2024-01-01:**
- Correlation: -0.047 
- Linear fit: y = -0.007x + 52.7
- P-value: 0.5534
- N samples: 160

**Is Open Source:**
- Correlation: 0.046 
- Linear fit: y = 2.385x + 47.1
- P-value: 0.5594
- N samples: 160

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.459 ***
- Linear fit: y = -18.923x + 114.3
- P-value: 0.0000
- N samples: 160

**Benchmark Score:**
- Correlation: -0.392 ***
- Linear fit: y = -1.618x + 152.0
- P-value: 0.0000
- N samples: 160

**Is Open Source:**
- Correlation: -0.224 **
- Linear fit: y = -9.234x + 106.8
- P-value: 0.0045
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: -0.149 
- Linear fit: y = -0.017x + 115.0
- P-value: 0.0593
- N samples: 160

**Model Size (B):**
- Correlation: 0.031 
- Linear fit: y = 0.001x + 102.7
- P-value: 0.7148
- N samples: 139

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.518 ***
- Linear fit: y = -1.300x + 69.5
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.301 ***
- Linear fit: y = -7.544x + 34.7
- P-value: 0.0001
- N samples: 160

**Model Size (B):**
- Correlation: -0.228 **
- Linear fit: y = -0.002x + 32.2
- P-value: 0.0069
- N samples: 139

**Days Since 2024-01-01:**
- Correlation: -0.132 
- Linear fit: y = -0.009x + 36.7
- P-value: 0.0954
- N samples: 160

**Is Open Source:**
- Correlation: -0.053 
- Linear fit: y = -1.344x + 30.8
- P-value: 0.5018
- N samples: 160

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.668 ***
- Linear fit: y = -8.466x + 514.1
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.501 ***
- Linear fit: y = -63.351x + 296.0
- P-value: 0.0000
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: -0.361 ***
- Linear fit: y = -0.123x + 346.8
- P-value: 0.0000
- N samples: 160

**Is Open Source:**
- Correlation: -0.086 
- Linear fit: y = -10.875x + 262.8
- P-value: 0.2806
- N samples: 160

**Model Size (B):**
- Correlation: -0.057 
- Linear fit: y = -0.003x + 265.0
- P-value: 0.5052
- N samples: 139

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.608 ***
- Linear fit: y = -0.086x + 130.8
- P-value: 0.0000
- N samples: 160

**Benchmark Score:**
- Correlation: -0.584 ***
- Linear fit: y = -3.056x + 161.6
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.433 ***
- Linear fit: y = -22.643x + 82.8
- P-value: 0.0000
- N samples: 160

**Is Open Source:**
- Correlation: -0.073 
- Linear fit: y = -3.797x + 70.8
- P-value: 0.3622
- N samples: 160

**Model Size (B):**
- Correlation: 0.067 
- Linear fit: y = 0.001x + 70.7
- P-value: 0.4361
- N samples: 139

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.372 ***
- Linear fit: y = -1.908x + 105.6
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.194 *
- Linear fit: y = -9.939x + 53.9
- P-value: 0.0139
- N samples: 160

**Model Size (B):**
- Correlation: -0.099 
- Linear fit: y = -0.002x + 50.9
- P-value: 0.2471
- N samples: 139

**Days Since 2024-01-01:**
- Correlation: -0.047 
- Linear fit: y = -0.007x + 52.7
- P-value: 0.5534
- N samples: 160

**Is Open Source:**
- Correlation: 0.046 
- Linear fit: y = 2.385x + 47.1
- P-value: 0.5594
- N samples: 160

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.459 ***
- Linear fit: y = -18.923x + 114.3
- P-value: 0.0000
- N samples: 160

**Benchmark Score:**
- Correlation: -0.392 ***
- Linear fit: y = -1.618x + 152.0
- P-value: 0.0000
- N samples: 160

**Is Open Source:**
- Correlation: -0.224 **
- Linear fit: y = -9.234x + 106.8
- P-value: 0.0045
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: -0.149 
- Linear fit: y = -0.017x + 115.0
- P-value: 0.0593
- N samples: 160

**Model Size (B):**
- Correlation: 0.031 
- Linear fit: y = 0.001x + 102.7
- P-value: 0.7148
- N samples: 139

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.518 ***
- Linear fit: y = -1.300x + 69.5
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.301 ***
- Linear fit: y = -7.544x + 34.7
- P-value: 0.0001
- N samples: 160

**Model Size (B):**
- Correlation: -0.228 **
- Linear fit: y = -0.002x + 32.2
- P-value: 0.0069
- N samples: 139

**Days Since 2024-01-01:**
- Correlation: -0.132 
- Linear fit: y = -0.009x + 36.7
- P-value: 0.0954
- N samples: 160

**Is Open Source:**
- Correlation: -0.053 
- Linear fit: y = -1.344x + 30.8
- P-value: 0.5018
- N samples: 160

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.588 ***
- Linear fit: y = -0.550x + 27.6
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.395 ***
- Linear fit: y = -3.690x + 13.2
- P-value: 0.0000
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: -0.171 *
- Linear fit: y = -0.004x + 14.1
- P-value: 0.0311
- N samples: 160

**Is Open Source:**
- Correlation: 0.146 
- Linear fit: y = 1.365x + 10.4
- P-value: 0.0657
- N samples: 160

**Model Size (B):**
- Correlation: 0.036 
- Linear fit: y = 0.000x + 11.0
- P-value: 0.6753
- N samples: 139

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.629 ***
- Linear fit: y = -0.076x + 108.4
- P-value: 0.0000
- N samples: 160

**Benchmark Score:**
- Correlation: -0.442 ***
- Linear fit: y = -1.991x + 113.9
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.358 ***
- Linear fit: y = -16.082x + 63.3
- P-value: 0.0000
- N samples: 160

**Is Open Source:**
- Correlation: -0.142 
- Linear fit: y = -6.396x + 56.3
- P-value: 0.0730
- N samples: 160

**Model Size (B):**
- Correlation: 0.096 
- Linear fit: y = 0.002x + 54.5
- P-value: 0.2600
- N samples: 139

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.721 ***
- Linear fit: y = -0.515x + 20.1
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.403 ***
- Linear fit: y = -2.871x + 6.3
- P-value: 0.0000
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: -0.271 ***
- Linear fit: y = -0.005x + 8.3
- P-value: 0.0005
- N samples: 160

**Is Open Source:**
- Correlation: 0.173 *
- Linear fit: y = 1.234x + 4.1
- P-value: 0.0289
- N samples: 160

**Model Size (B):**
- Correlation: -0.162 
- Linear fit: y = -0.000x + 5.2
- P-value: 0.0572
- N samples: 139

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.295 ***
- Linear fit: y = -0.759x + 43.9
- P-value: 0.0001
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.087 
- Linear fit: y = -2.224x + 22.3
- P-value: 0.2748
- N samples: 160

**Model Size (B):**
- Correlation: -0.041 
- Linear fit: y = -0.000x + 21.6
- P-value: 0.6306
- N samples: 139

**Days Since 2024-01-01:**
- Correlation: 0.040 
- Linear fit: y = 0.003x + 19.0
- P-value: 0.6164
- N samples: 160

**Is Open Source:**
- Correlation: 0.039 
- Linear fit: y = 1.010x + 20.6
- P-value: 0.6212
- N samples: 160

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.387 ***
- Linear fit: y = -1.106x + 59.7
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.268 ***
- Linear fit: y = -7.632x + 30.8
- P-value: 0.0006
- N samples: 160

**Model Size (B):**
- Correlation: -0.135 
- Linear fit: y = -0.002x + 28.4
- P-value: 0.1125
- N samples: 139

**Days Since 2024-01-01:**
- Correlation: -0.123 
- Linear fit: y = -0.009x + 33.0
- P-value: 0.1203
- N samples: 160

**Is Open Source:**
- Correlation: 0.047 
- Linear fit: y = 1.349x + 25.7
- P-value: 0.5533
- N samples: 160

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.179 *
- Linear fit: y = -0.043x + 2.1
- P-value: 0.0232
- N samples: 160

**Model Size (B):**
- Correlation: -0.063 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.4597
- N samples: 139

**Is Reasoning Model:**
- Correlation: -0.034 
- Linear fit: y = -0.083x + 0.9
- P-value: 0.6658
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: 0.032 
- Linear fit: y = 0.000x + 0.7
- P-value: 0.6856
- N samples: 160

**Is Open Source:**
- Correlation: 0.011 
- Linear fit: y = 0.026x + 0.8
- P-value: 0.8920
- N samples: 160

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.405 ***
- Linear fit: y = -14.272x + 102.5
- P-value: 0.0000
- N samples: 160

**Is Open Source:**
- Correlation: -0.323 ***
- Linear fit: y = -11.385x + 98.5
- P-value: 0.0000
- N samples: 160

**Benchmark Score:**
- Correlation: -0.278 ***
- Linear fit: y = -0.982x + 123.6
- P-value: 0.0004
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.013x + 103.5
- P-value: 0.0790
- N samples: 160

**Model Size (B):**
- Correlation: 0.106 
- Linear fit: y = 0.002x + 92.6
- P-value: 0.2139
- N samples: 139

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.661 ***
- Linear fit: y = -0.640x + 28.3
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.479 ***
- Linear fit: y = -4.628x + 11.8
- P-value: 0.0000
- N samples: 160

**Model Size (B):**
- Correlation: -0.262 **
- Linear fit: y = -0.001x + 10.0
- P-value: 0.0019
- N samples: 139

**Is Open Source:**
- Correlation: 0.228 **
- Linear fit: y = 2.203x + 8.1
- P-value: 0.0038
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: -0.132 
- Linear fit: y = -0.003x + 11.5
- P-value: 0.0950
- N samples: 160

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.170 *
- Linear fit: y = 0.000x + 0.1
- P-value: 0.0449
- N samples: 139

**Is Open Source:**
- Correlation: -0.088 
- Linear fit: y = -0.052x + 0.1
- P-value: 0.2710
- N samples: 160

**Benchmark Score:**
- Correlation: 0.061 
- Linear fit: y = 0.004x + -0.0
- P-value: 0.4430
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: 0.044 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.5779
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.040 
- Linear fit: y = -0.023x + 0.1
- P-value: 0.6194
- N samples: 160

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.334 ***
- Linear fit: y = -0.382x + 18.7
- P-value: 0.0000
- N samples: 160

**Model Size (B):**
- Correlation: -0.205 *
- Linear fit: y = -0.001x + 7.8
- P-value: 0.0155
- N samples: 139

**Is Open Source:**
- Correlation: 0.130 
- Linear fit: y = 1.484x + 6.5
- P-value: 0.1026
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.122 
- Linear fit: y = -1.396x + 8.0
- P-value: 0.1240
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: 0.076 
- Linear fit: y = 0.002x + 5.5
- P-value: 0.3421
- N samples: 160

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.626 ***
- Linear fit: y = -0.795x + 40.5
- P-value: 0.0000
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.353 ***
- Linear fit: y = -4.466x + 19.1
- P-value: 0.0000
- N samples: 160

**Model Size (B):**
- Correlation: -0.299 ***
- Linear fit: y = -0.002x + 17.9
- P-value: 0.0003
- N samples: 139

**Days Since 2024-01-01:**
- Correlation: -0.177 *
- Linear fit: y = -0.006x + 20.8
- P-value: 0.0255
- N samples: 160

**Is Open Source:**
- Correlation: 0.090 
- Linear fit: y = 1.141x + 16.0
- P-value: 0.2582
- N samples: 160

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.367 ***
- Linear fit: y = -3.969x + 8.2
- P-value: 0.0000
- N samples: 160

**Days Since 2024-01-01:**
- Correlation: -0.180 *
- Linear fit: y = -0.005x + 10.4
- P-value: 0.0224
- N samples: 160

**Is Reasoning Model:**
- Correlation: -0.156 *
- Linear fit: y = -1.683x + 7.7
- P-value: 0.0487
- N samples: 160

**Benchmark Score:**
- Correlation: -0.114 
- Linear fit: y = -0.123x + 10.4
- P-value: 0.1504
- N samples: 160

**Model Size (B):**
- Correlation: 0.029 
- Linear fit: y = 0.000x + 6.5
- P-value: 0.7387
- N samples: 139

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.721, y = -0.515x + 20.1

**total_hallucinations vs Benchmark Score:**
  r = -0.668, y = -8.466x + 514.1

**3b_self_contradiction vs Benchmark Score:**
  r = -0.661, y = -0.640x + 28.3

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.629, y = -0.076x + 108.4

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.626, y = -0.795x + 40.5

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.608, y = -0.086x + 130.8

**1a_instruction_override vs Benchmark Score:**
  r = -0.588, y = -0.550x + 27.6

**category1_input_misalignment vs Benchmark Score:**
  r = -0.584, y = -3.056x + 161.6

**category4_technical_errors vs Benchmark Score:**
  r = -0.518, y = -1.300x + 69.5

**total_hallucinations vs Is Reasoning Model:**
  r = -0.501, y = -63.351x + 296.0

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.479, y = -4.628x + 11.8

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.459, y = -18.923x + 114.3

**1b_context_omission vs Benchmark Score:**
  r = -0.442, y = -1.991x + 113.9

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.433, y = -22.643x + 82.8

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.405, y = -14.272x + 102.5

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.403, y = -2.871x + 6.3

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.395, y = -3.690x + 13.2

**category3_logical_errors vs Benchmark Score:**
  r = -0.392, y = -1.618x + 152.0

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.387, y = -1.106x + 59.7

**category2_factual_errors vs Benchmark Score:**
  r = -0.372, y = -1.908x + 105.6

**4c_visual_descr_mismatch vs Is Open Source:**
  r = -0.367, y = -3.969x + 8.2

**total_hallucinations vs Days Since 2024-01-01:**
  r = -0.361, y = -0.123x + 346.8

**1b_context_omission vs Is Reasoning Model:**
  r = -0.358, y = -16.082x + 63.3

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.353, y = -4.466x + 19.1

**4a_syntax_error vs Benchmark Score:**
  r = -0.334, y = -0.382x + 18.7

**3a_unsupported_leap vs Is Open Source:**
  r = -0.323, y = -11.385x + 98.5

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.301, y = -7.544x + 34.7


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
- Correlation: -0.058 
- Linear fit: y = -0.055x + 51.4

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.216 **
- Linear fit: y = 0.173x + 91.0

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.210 **
- Linear fit: y = 0.101x + 23.0

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.658 ***
- Linear fit: y = 0.548x + 76.7

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.550 ***
- Linear fit: y = 0.275x + 16.8

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.597 ***
- Linear fit: y = 0.358x + -6.9

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.981 ***, y = 0.841x + 7.2

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.968 ***, y = 0.831x + -4.0

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.933 ***, y = 0.521x + 1.2

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.913 ***, y = 0.455x + -0.8

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.815 ***, y = 0.410x + 4.1

**2a: Concept Fabrication vs 2b: Spurious Numeric:**
  r = 0.710 ***, y = 0.795x + 9.4

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.704 ***, y = 0.328x + -2.8

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.691 ***, y = 0.158x + -7.2

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.658 ***, y = 0.548x + 76.7

**2b: Spurious Numeric vs 3b: Self Contradiction:**
  r = 0.657 ***, y = 0.224x + 3.2

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.634 ***, y = 0.121x + 3.3

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.632 ***, y = 0.423x + -17.6

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.623 ***, y = 0.262x + -1.3

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.600 ***, y = 0.428x + 73.4

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.597 ***, y = 0.358x + -6.9

**3b: Self Contradiction vs 4b: Model Semantics Breach:**
  r = 0.585 ***, y = 0.774x + 9.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.583 ***, y = 0.221x + 2.4

**Category 3: Logical Errors vs 2a: Concept Fabrication:**
  r = 0.572 ***, y = 0.342x + -14.3

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.563 ***, y = 0.720x + 75.1

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.562 ***, y = 0.769x + 5.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**1b: Context Omission vs 2c: False Citation:**
  r = -0.254 ***, y = -0.013x + 1.5
  (Models good at one tend to be worse at the other)

**1b: Context Omission vs 2a: Concept Fabrication:**
  r = -0.220 **, y = -0.123x + 27.3
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
