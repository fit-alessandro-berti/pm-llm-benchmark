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
- Linear fit: y = -2.446x + 128.4
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.561 ***
- Linear fit: y = -26.412x + 55.6
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.237 **
- Linear fit: y = 11.169x + 37.0
- P-value: 0.0013
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.191 **
- Linear fit: y = -0.031x + 58.8
- P-value: 0.0087
- N samples: 187

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0638
- N samples: 181

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.533 ***
- Linear fit: y = -1.492x + 80.6
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.293 ***
- Linear fit: y = 0.042x + 6.7
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.245 ***
- Linear fit: y = -10.385x + 33.5
- P-value: 0.0009
- N samples: 181

**Is Open Source:**
- Correlation: 0.227 **
- Linear fit: y = 9.609x + 23.4
- P-value: 0.0022
- N samples: 181

**Model Size (B):**
- Correlation: -0.116 
- Linear fit: y = -0.003x + 29.6
- P-value: 0.1191
- N samples: 181

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.771 ***
- Linear fit: y = -3.437x + 196.3
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.655 ***
- Linear fit: y = -44.239x + 97.5
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.190 *
- Linear fit: y = 12.853x + 69.4
- P-value: 0.0103
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.150 *
- Linear fit: y = -0.034x + 93.9
- P-value: 0.0405
- N samples: 187

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.004x + 78.9
- P-value: 0.1118
- N samples: 181

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.353x + 66.8
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.319 ***
- Linear fit: y = -9.463x + 24.1
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.228 **
- Linear fit: y = 6.753x + 16.0
- P-value: 0.0021
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.164 *
- Linear fit: y = 0.017x + 10.8
- P-value: 0.0249
- N samples: 187

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0763
- N samples: 181

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.804 ***
- Linear fit: y = -9.510x + 508.1
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.550 ***
- Linear fit: y = -98.455x + 223.2
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.250 ***
- Linear fit: y = 44.777x + 152.1
- P-value: 0.0007
- N samples: 181

**Model Size (B):**
- Correlation: -0.144 
- Linear fit: y = -0.014x + 182.9
- P-value: 0.0535
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.005 
- Linear fit: y = -0.003x + 177.2
- P-value: 0.9409
- N samples: 187

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.786 ***
- Linear fit: y = -2.446x + 128.4
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.561 ***
- Linear fit: y = -26.412x + 55.6
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.237 **
- Linear fit: y = 11.169x + 37.0
- P-value: 0.0013
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.191 **
- Linear fit: y = -0.031x + 58.8
- P-value: 0.0087
- N samples: 187

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 44.7
- P-value: 0.0638
- N samples: 181

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.533 ***
- Linear fit: y = -1.492x + 80.6
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.293 ***
- Linear fit: y = 0.042x + 6.7
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.245 ***
- Linear fit: y = -10.385x + 33.5
- P-value: 0.0009
- N samples: 181

**Is Open Source:**
- Correlation: 0.227 **
- Linear fit: y = 9.609x + 23.4
- P-value: 0.0022
- N samples: 181

**Model Size (B):**
- Correlation: -0.116 
- Linear fit: y = -0.003x + 29.6
- P-value: 0.1191
- N samples: 181

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.771 ***
- Linear fit: y = -3.437x + 196.3
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.655 ***
- Linear fit: y = -44.239x + 97.5
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.190 *
- Linear fit: y = 12.853x + 69.4
- P-value: 0.0103
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.150 *
- Linear fit: y = -0.034x + 93.9
- P-value: 0.0405
- N samples: 187

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.004x + 78.9
- P-value: 0.1118
- N samples: 181

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.353x + 66.8
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.319 ***
- Linear fit: y = -9.463x + 24.1
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.228 **
- Linear fit: y = 6.753x + 16.0
- P-value: 0.0021
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.164 *
- Linear fit: y = 0.017x + 10.8
- P-value: 0.0249
- N samples: 187

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0763
- N samples: 181

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.639 ***
- Linear fit: y = -0.472x + 24.1
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.395 ***
- Linear fit: y = -4.416x + 9.7
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.280 ***
- Linear fit: y = 3.136x + 5.9
- P-value: 0.0001
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.154 *
- Linear fit: y = 0.006x + 4.5
- P-value: 0.0358
- N samples: 187

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.001x + 7.7
- P-value: 0.1604
- N samples: 181

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.713 ***
- Linear fit: y = -1.582x + 86.4
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.556 ***
- Linear fit: y = -18.681x + 40.1
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.375 ***
- Linear fit: y = -0.043x + 53.5
- P-value: 0.0000
- N samples: 187

**Is Open Source:**
- Correlation: 0.153 *
- Linear fit: y = 5.142x + 28.4
- P-value: 0.0399
- N samples: 181

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.002x + 32.5
- P-value: 0.1114
- N samples: 181

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.693 ***
- Linear fit: y = -0.392x + 17.9
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.387 ***
- Linear fit: y = -3.315x + 5.8
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.337 ***
- Linear fit: y = 2.892x + 2.7
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.225 **
- Linear fit: y = 0.007x + 0.8
- P-value: 0.0020
- N samples: 187

**Model Size (B):**
- Correlation: -0.156 *
- Linear fit: y = -0.001x + 4.5
- P-value: 0.0365
- N samples: 181

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.491 ***
- Linear fit: y = -0.748x + 34.4
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.303 ***
- Linear fit: y = 0.024x + -4.0
- P-value: 0.0000
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.252 ***
- Linear fit: y = -5.811x + 11.1
- P-value: 0.0006
- N samples: 181

**Is Open Source:**
- Correlation: 0.220 **
- Linear fit: y = 5.080x + 5.6
- P-value: 0.0029
- N samples: 181

**Model Size (B):**
- Correlation: -0.058 
- Linear fit: y = -0.001x + 8.5
- P-value: 0.4378
- N samples: 181

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.470 ***
- Linear fit: y = -0.694x + 43.8
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.254 ***
- Linear fit: y = 0.019x + 9.6
- P-value: 0.0005
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.213 **
- Linear fit: y = -4.746x + 21.9
- P-value: 0.0041
- N samples: 181

**Is Open Source:**
- Correlation: 0.209 **
- Linear fit: y = 4.664x + 17.1
- P-value: 0.0048
- N samples: 181

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0592
- N samples: 181

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
- P-value: 0.3315
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.041 
- Linear fit: y = -0.001x + 1.1
- P-value: 0.5791
- N samples: 187

**Is Reasoning Model:**
- Correlation: 0.029 
- Linear fit: y = 0.172x + 0.6
- P-value: 0.7033
- N samples: 181

**Is Open Source:**
- Correlation: -0.022 
- Linear fit: y = -0.134x + 0.7
- P-value: 0.7661
- N samples: 181

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.759 ***
- Linear fit: y = -2.831x + 165.4
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.665 ***
- Linear fit: y = -37.533x + 84.5
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: -0.239 **
- Linear fit: y = -0.046x + 90.0
- P-value: 0.0010
- N samples: 187

**Is Open Source:**
- Correlation: 0.166 *
- Linear fit: y = 9.380x + 61.5
- P-value: 0.0255
- N samples: 181

**Model Size (B):**
- Correlation: -0.106 
- Linear fit: y = -0.003x + 68.7
- P-value: 0.1559
- N samples: 181

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.627 ***
- Linear fit: y = -0.571x + 29.3
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.466 ***
- Linear fit: y = -6.412x + 12.4
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 3.194x + 7.7
- P-value: 0.0017
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.218 **
- Linear fit: y = 0.010x + 4.1
- P-value: 0.0027
- N samples: 187

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.001x + 9.9
- P-value: 0.0606
- N samples: 181

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.341 ***
- Linear fit: y = -0.036x + 1.6
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.216 **
- Linear fit: y = 0.001x + -0.2
- P-value: 0.0030
- N samples: 187

**Is Reasoning Model:**
- Correlation: -0.186 *
- Linear fit: y = -0.294x + 0.5
- P-value: 0.0123
- N samples: 181

**Is Open Source:**
- Correlation: 0.176 *
- Linear fit: y = 0.279x + 0.2
- P-value: 0.0176
- N samples: 181

**Model Size (B):**
- Correlation: -0.055 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4589
- N samples: 181

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.616 ***
- Linear fit: y = -0.629x + 27.2
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.306 ***
- Linear fit: y = 4.732x + 2.7
- P-value: 0.0000
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.244 ***
- Linear fit: y = 0.013x + -1.4
- P-value: 0.0007
- N samples: 187

**Model Size (B):**
- Correlation: -0.157 *
- Linear fit: y = -0.001x + 5.7
- P-value: 0.0348
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.146 
- Linear fit: y = -2.252x + 6.3
- P-value: 0.0503
- N samples: 181

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.706 ***
- Linear fit: y = -0.678x + 34.1
- P-value: 0.0000
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.415 ***
- Linear fit: y = -6.034x + 13.3
- P-value: 0.0000
- N samples: 181

**Is Open Source:**
- Correlation: 0.239 **
- Linear fit: y = 3.478x + 8.6
- P-value: 0.0012
- N samples: 181

**Model Size (B):**
- Correlation: -0.189 *
- Linear fit: y = -0.002x + 11.0
- P-value: 0.0110
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.069 
- Linear fit: y = 0.003x + 8.6
- P-value: 0.3498
- N samples: 187

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.226 **
- Linear fit: y = -1.457x + 4.7
- P-value: 0.0022
- N samples: 181

**Model Size (B):**
- Correlation: 0.192 **
- Linear fit: y = 0.001x + 3.6
- P-value: 0.0095
- N samples: 181

**Is Reasoning Model:**
- Correlation: -0.183 *
- Linear fit: y = -1.177x + 4.5
- P-value: 0.0136
- N samples: 181

**Benchmark Score:**
- Correlation: -0.109 
- Linear fit: y = -0.046x + 5.6
- P-value: 0.1442
- N samples: 181

**Days Since 2024-01-01:**
- Correlation: 0.015 
- Linear fit: y = 0.000x + 3.7
- P-value: 0.8353
- N samples: 187

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.804, y = -9.510x + 508.1

**category1_input_misalignment vs Benchmark Score:**
  r = -0.786, y = -2.446x + 128.4

**category3_logical_errors vs Benchmark Score:**
  r = -0.771, y = -3.437x + 196.3

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.759, y = -2.831x + 165.4

**1b_context_omission vs Benchmark Score:**
  r = -0.713, y = -1.582x + 86.4

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.706, y = -0.678x + 34.1

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.693, y = -0.392x + 17.9

**category4_technical_errors vs Benchmark Score:**
  r = -0.691, y = -1.353x + 66.8

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.665, y = -37.533x + 84.5

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.655, y = -44.239x + 97.5

**1a_instruction_override vs Benchmark Score:**
  r = -0.639, y = -0.472x + 24.1

**3b_self_contradiction vs Benchmark Score:**
  r = -0.627, y = -0.571x + 29.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.616, y = -0.629x + 27.2

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.561, y = -26.412x + 55.6

**1b_context_omission vs Is Reasoning Model:**
  r = -0.556, y = -18.681x + 40.1

**total_hallucinations vs Is Reasoning Model:**
  r = -0.550, y = -98.455x + 223.2

**category2_factual_errors vs Benchmark Score:**
  r = -0.533, y = -1.492x + 80.6

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.491, y = -0.748x + 34.4

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.470, y = -0.694x + 43.8

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.466, y = -6.412x + 12.4

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.415, y = -6.034x + 13.3

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.395, y = -4.416x + 9.7

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.387, y = -3.315x + 5.8

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.375, y = -0.043x + 53.5

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.341, y = -0.036x + 1.6

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.337, y = 2.892x + 2.7

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.319, y = -9.463x + 24.1

**4a_syntax_error vs Is Open Source:**
  r = 0.306, y = 4.732x + 2.7

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.303, y = 0.024x + -4.0


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
- Linear fit: y = 1.007x + 47.7

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
  r = 0.949 ***, y = 0.680x + 2.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.900 ***, y = 0.440x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.889 ***, y = 0.483x + -5.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.883 ***, y = 0.467x + 6.2

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.879 ***, y = 0.457x + -3.7

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.816 ***, y = 1.163x + 26.2

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.804 ***, y = 0.164x + -3.2

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.801 ***, y = 0.956x + 25.5

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.790 ***, y = 1.270x + 4.1

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.782 ***, y = 0.468x + 5.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.780 ***, y = 0.185x + -0.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.778 ***, y = 0.361x + 2.4

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.775 ***, y = 1.290x + 26.1

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.769 ***, y = 2.066x + -0.4

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.769 ***, y = 0.250x + 2.3

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.759 ***, y = 0.382x + 2.2

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.743 ***, y = 0.568x + -0.1

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.743 ***, y = 0.499x + 1.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.742 ***, y = 0.134x + -1.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
