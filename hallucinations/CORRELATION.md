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
- Correlation: -0.786 ***
- Linear fit: y = -2.442x + 128.3
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.556 ***
- Linear fit: y = -26.133x + 55.4
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.243 ***
- Linear fit: y = 11.444x + 37.0
- P-value: 0.0010
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.192 **
- Linear fit: y = -0.031x + 58.8
- P-value: 0.0082
- N samples: 188

**Model Size (B):**
- Correlation: -0.139 
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0613
- N samples: 182

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.532 ***
- Linear fit: y = -1.490x + 80.6
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.291 ***
- Linear fit: y = 0.042x + 6.9
- P-value: 0.0001
- N samples: 188

**Is Reasoning Model:**
- Correlation: -0.242 **
- Linear fit: y = -10.270x + 33.4
- P-value: 0.0010
- N samples: 181

**Is Open Source:**
- Correlation: 0.229 **
- Linear fit: y = 9.716x + 23.4
- P-value: 0.0019
- N samples: 181

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.003x + 29.6
- P-value: 0.1170
- N samples: 182

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.771 ***
- Linear fit: y = -3.433x + 196.2
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.651 ***
- Linear fit: y = -43.883x + 97.1
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.196 **
- Linear fit: y = 13.222x + 69.3
- P-value: 0.0082
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.152 *
- Linear fit: y = -0.035x + 94.0
- P-value: 0.0377
- N samples: 188

**Model Size (B):**
- Correlation: -0.120 
- Linear fit: y = -0.004x + 78.9
- P-value: 0.1065
- N samples: 182

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.350x + 66.8
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.312 ***
- Linear fit: y = -9.244x + 24.0
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.235 **
- Linear fit: y = 6.962x + 16.0
- P-value: 0.0014
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.160 *
- Linear fit: y = 0.016x + 11.0
- P-value: 0.0278
- N samples: 188

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0723
- N samples: 182

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.804 ***
- Linear fit: y = -9.497x + 507.9
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.545 ***
- Linear fit: y = -97.345x + 222.4
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.257 ***
- Linear fit: y = 45.881x + 152.0
- P-value: 0.0005
- N samples: 181

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.014x + 182.8
- P-value: 0.0505
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: -0.008 
- Linear fit: y = -0.005x + 177.8
- P-value: 0.9126
- N samples: 188

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.786 ***
- Linear fit: y = -2.442x + 128.3
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.556 ***
- Linear fit: y = -26.133x + 55.4
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.243 ***
- Linear fit: y = 11.444x + 37.0
- P-value: 0.0010
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.192 **
- Linear fit: y = -0.031x + 58.8
- P-value: 0.0082
- N samples: 188

**Model Size (B):**
- Correlation: -0.139 
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0613
- N samples: 182

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.532 ***
- Linear fit: y = -1.490x + 80.6
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.291 ***
- Linear fit: y = 0.042x + 6.9
- P-value: 0.0001
- N samples: 188

**Is Reasoning Model:**
- Correlation: -0.242 **
- Linear fit: y = -10.270x + 33.4
- P-value: 0.0010
- N samples: 181

**Is Open Source:**
- Correlation: 0.229 **
- Linear fit: y = 9.716x + 23.4
- P-value: 0.0019
- N samples: 181

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.003x + 29.6
- P-value: 0.1170
- N samples: 182

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.771 ***
- Linear fit: y = -3.433x + 196.2
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.651 ***
- Linear fit: y = -43.883x + 97.1
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.196 **
- Linear fit: y = 13.222x + 69.3
- P-value: 0.0082
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.152 *
- Linear fit: y = -0.035x + 94.0
- P-value: 0.0377
- N samples: 188

**Model Size (B):**
- Correlation: -0.120 
- Linear fit: y = -0.004x + 78.9
- P-value: 0.1065
- N samples: 182

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.350x + 66.8
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.312 ***
- Linear fit: y = -9.244x + 24.0
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.235 **
- Linear fit: y = 6.962x + 16.0
- P-value: 0.0014
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.160 *
- Linear fit: y = 0.016x + 11.0
- P-value: 0.0278
- N samples: 188

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0723
- N samples: 182

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.638 ***
- Linear fit: y = -0.471x + 24.0
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.393 ***
- Linear fit: y = -4.383x + 9.7
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.283 ***
- Linear fit: y = 3.165x + 5.9
- P-value: 0.0001
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.153 *
- Linear fit: y = 0.006x + 4.5
- P-value: 0.0355
- N samples: 188

**Model Size (B):**
- Correlation: -0.104 
- Linear fit: y = -0.001x + 7.7
- P-value: 0.1619
- N samples: 182

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.713 ***
- Linear fit: y = -1.580x + 86.4
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.550 ***
- Linear fit: y = -18.448x + 39.9
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.376 ***
- Linear fit: y = -0.043x + 53.4
- P-value: 0.0000
- N samples: 188

**Is Open Source:**
- Correlation: 0.160 *
- Linear fit: y = 5.377x + 28.3
- P-value: 0.0311
- N samples: 181

**Model Size (B):**
- Correlation: -0.121 
- Linear fit: y = -0.002x + 32.5
- P-value: 0.1050
- N samples: 182

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.692 ***
- Linear fit: y = -0.391x + 17.9
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.386 ***
- Linear fit: y = -3.301x + 5.8
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.339 ***
- Linear fit: y = 2.902x + 2.7
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.225 **
- Linear fit: y = 0.007x + 0.8
- P-value: 0.0019
- N samples: 188

**Model Size (B):**
- Correlation: -0.154 *
- Linear fit: y = -0.001x + 4.5
- P-value: 0.0376
- N samples: 182

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.490 ***
- Linear fit: y = -0.747x + 34.4
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.301 ***
- Linear fit: y = 0.023x + -3.8
- P-value: 0.0000
- N samples: 188

**Is Reasoning Model:**
- Correlation: -0.249 ***
- Linear fit: y = -5.742x + 11.0
- P-value: 0.0007
- N samples: 181

**Is Open Source:**
- Correlation: 0.223 **
- Linear fit: y = 5.144x + 5.6
- P-value: 0.0025
- N samples: 181

**Model Size (B):**
- Correlation: -0.058 
- Linear fit: y = -0.001x + 8.5
- P-value: 0.4335
- N samples: 182

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.470 ***
- Linear fit: y = -0.693x + 43.8
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.252 ***
- Linear fit: y = 0.019x + 9.6
- P-value: 0.0005
- N samples: 188

**Is Reasoning Model:**
- Correlation: -0.211 **
- Linear fit: y = -4.714x + 21.8
- P-value: 0.0044
- N samples: 181

**Is Open Source:**
- Correlation: 0.210 **
- Linear fit: y = 4.692x + 17.1
- P-value: 0.0045
- N samples: 181

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0586
- N samples: 182

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.126 
- Linear fit: y = -0.050x + 2.4
- P-value: 0.0911
- N samples: 181

**Model Size (B):**
- Correlation: -0.073 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.3242
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: -0.042 
- Linear fit: y = -0.001x + 1.1
- P-value: 0.5650
- N samples: 188

**Is Reasoning Model:**
- Correlation: 0.031 
- Linear fit: y = 0.186x + 0.6
- P-value: 0.6797
- N samples: 181

**Is Open Source:**
- Correlation: -0.020 
- Linear fit: y = -0.120x + 0.7
- P-value: 0.7906
- N samples: 181

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.759 ***
- Linear fit: y = -2.826x + 165.3
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.659 ***
- Linear fit: y = -37.163x + 84.2
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.240 ***
- Linear fit: y = -0.046x + 90.0
- P-value: 0.0009
- N samples: 188

**Is Open Source:**
- Correlation: 0.173 *
- Linear fit: y = 9.758x + 61.4
- P-value: 0.0198
- N samples: 181

**Model Size (B):**
- Correlation: -0.108 
- Linear fit: y = -0.003x + 68.7
- P-value: 0.1483
- N samples: 182

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.628 ***
- Linear fit: y = -0.572x + 29.3
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.467 ***
- Linear fit: y = -6.434x + 12.4
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.231 **
- Linear fit: y = 3.177x + 7.7
- P-value: 0.0018
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.217 **
- Linear fit: y = 0.010x + 4.1
- P-value: 0.0028
- N samples: 188

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.001x + 9.9
- P-value: 0.0599
- N samples: 182

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.341 ***
- Linear fit: y = -0.036x + 1.6
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.211 **
- Linear fit: y = 0.001x + -0.2
- P-value: 0.0036
- N samples: 188

**Is Open Source:**
- Correlation: 0.181 *
- Linear fit: y = 0.287x + 0.2
- P-value: 0.0147
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.181 *
- Linear fit: y = -0.287x + 0.5
- P-value: 0.0147
- N samples: 181

**Model Size (B):**
- Correlation: -0.057 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4421
- N samples: 182

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.615 ***
- Linear fit: y = -0.628x + 27.2
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.305 ***
- Linear fit: y = 4.717x + 2.8
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.246 ***
- Linear fit: y = 0.013x + -1.5
- P-value: 0.0007
- N samples: 188

**Model Size (B):**
- Correlation: -0.155 *
- Linear fit: y = -0.001x + 5.8
- P-value: 0.0368
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.146 *
- Linear fit: y = -2.258x + 6.3
- P-value: 0.0498
- N samples: 181

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.707 ***
- Linear fit: y = -0.677x + 34.1
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.406 ***
- Linear fit: y = -5.885x + 13.2
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.250 ***
- Linear fit: y = 3.625x + 8.5
- P-value: 0.0007
- N samples: 181

**Model Size (B):**
- Correlation: -0.192 **
- Linear fit: y = -0.002x + 11.0
- P-value: 0.0096
- N samples: 182

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.003x + 8.7
- P-value: 0.3915
- N samples: 188

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.215 **
- Linear fit: y = -1.380x + 4.7
- P-value: 0.0037
- N samples: 181

**Model Size (B):**
- Correlation: 0.187 *
- Linear fit: y = 0.001x + 3.6
- P-value: 0.0114
- N samples: 182

**Is Reasoning Model:**
- Correlation: -0.172 *
- Linear fit: y = -1.102x + 4.5
- P-value: 0.0209
- N samples: 181

**Benchmark Score:**
- Correlation: -0.109 
- Linear fit: y = -0.046x + 5.6
- P-value: 0.1459
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.009 
- Linear fit: y = 0.000x + 3.7
- P-value: 0.9063
- N samples: 188

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.804, y = -9.497x + 507.9

**category1_input_misalignment vs Benchmark Score:**
  r = -0.786, y = -2.442x + 128.3

**category3_logical_errors vs Benchmark Score:**
  r = -0.771, y = -3.433x + 196.2

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.759, y = -2.826x + 165.3

**1b_context_omission vs Benchmark Score:**
  r = -0.713, y = -1.580x + 86.4

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.707, y = -0.677x + 34.1

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.692, y = -0.391x + 17.9

**category4_technical_errors vs Benchmark Score:**
  r = -0.691, y = -1.350x + 66.8

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.659, y = -37.163x + 84.2

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.651, y = -43.883x + 97.1

**1a_instruction_override vs Benchmark Score:**
  r = -0.638, y = -0.471x + 24.0

**3b_self_contradiction vs Benchmark Score:**
  r = -0.628, y = -0.572x + 29.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.615, y = -0.628x + 27.2

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.556, y = -26.133x + 55.4

**1b_context_omission vs Is Reasoning Model:**
  r = -0.550, y = -18.448x + 39.9

**total_hallucinations vs Is Reasoning Model:**
  r = -0.545, y = -97.345x + 222.4

**category2_factual_errors vs Benchmark Score:**
  r = -0.532, y = -1.490x + 80.6

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.490, y = -0.747x + 34.4

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.470, y = -0.693x + 43.8

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.467, y = -6.434x + 12.4

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.406, y = -5.885x + 13.2

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.393, y = -4.383x + 9.7

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.386, y = -3.301x + 5.8

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.376, y = -0.043x + 53.4

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.341, y = -0.036x + 1.6

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.339, y = 2.902x + 2.7

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.312, y = -9.244x + 24.0

**4a_syntax_error vs Is Open Source:**
  r = 0.305, y = 4.717x + 2.8

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.301, y = 0.023x + -3.8


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
- Linear fit: y = 0.469x + 8.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.816 ***
- Linear fit: y = 1.163x + 26.2

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.643 ***
- Linear fit: y = 0.404x + 1.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.632 ***
- Linear fit: y = 1.007x + 47.6

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.724 ***
- Linear fit: y = 0.508x + 4.9

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.709 ***
- Linear fit: y = 0.312x + -4.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.988 ***, y = 0.827x + 3.5

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.949 ***, y = 0.681x + 2.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.899 ***, y = 0.440x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.889 ***, y = 0.483x + -5.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.883 ***, y = 0.467x + 6.2

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.877 ***, y = 0.456x + -3.6

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.816 ***, y = 1.163x + 26.2

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.804 ***, y = 0.164x + -3.2

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.801 ***, y = 0.956x + 25.4

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.790 ***, y = 1.269x + 4.1

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.782 ***, y = 0.468x + 5.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.780 ***, y = 0.185x + -0.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.777 ***, y = 0.360x + 2.4

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.775 ***, y = 1.291x + 26.1

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.769 ***, y = 0.250x + 2.3

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.769 ***, y = 2.065x + -0.4

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.760 ***, y = 0.382x + 2.2

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.743 ***, y = 0.568x + -0.1

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.743 ***, y = 0.499x + 1.1

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.741 ***, y = 0.134x + -1.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
