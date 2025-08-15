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
- Correlation: -0.767 ***
- Linear fit: y = -2.151x + 106.6
- P-value: 0.0000
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.582 ***
- Linear fit: y = -0.095x + 83.3
- P-value: 0.0000
- N samples: 154

**Is Reasoning Model:**
- Correlation: -0.559 ***
- Linear fit: y = -20.430x + 51.7
- P-value: 0.0000
- N samples: 151

**Is Open Source:**
- Correlation: 0.196 *
- Linear fit: y = 7.306x + 37.4
- P-value: 0.0157
- N samples: 151

**Model Size (B):**
- Correlation: -0.168 *
- Linear fit: y = -0.004x + 43.1
- P-value: 0.0373
- N samples: 154

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.543 ***
- Linear fit: y = -1.034x + 54.2
- P-value: 0.0000
- N samples: 151

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 5.865x + 19.6
- P-value: 0.0042
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.160 *
- Linear fit: y = -3.973x + 25.0
- P-value: 0.0496
- N samples: 151

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.002x + 24.2
- P-value: 0.0987
- N samples: 154

**Days Since 2024-01-01:**
- Correlation: 0.030 
- Linear fit: y = 0.003x + 21.9
- P-value: 0.7139
- N samples: 154

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.800 ***
- Linear fit: y = -3.292x + 175.8
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.699 ***
- Linear fit: y = -37.463x + 94.9
- P-value: 0.0000
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.322 ***
- Linear fit: y = -0.077x + 110.5
- P-value: 0.0000
- N samples: 154

**Is Open Source:**
- Correlation: 0.170 *
- Linear fit: y = 9.256x + 71.0
- P-value: 0.0375
- N samples: 151

**Model Size (B):**
- Correlation: -0.129 
- Linear fit: y = -0.004x + 78.3
- P-value: 0.1096
- N samples: 154

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.533 ***
- Linear fit: y = -0.792x + 41.1
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.225 **
- Linear fit: y = -4.364x + 19.4
- P-value: 0.0054
- N samples: 151

**Model Size (B):**
- Correlation: -0.129 
- Linear fit: y = -0.002x + 18.1
- P-value: 0.1100
- N samples: 154

**Is Open Source:**
- Correlation: 0.124 
- Linear fit: y = 2.446x + 15.8
- P-value: 0.1293
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.016 
- Linear fit: y = -0.001x + 18.1
- P-value: 0.8438
- N samples: 154

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.866 ***
- Linear fit: y = -7.840x + 402.8
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.601 ***
- Linear fit: y = -70.965x + 201.2
- P-value: 0.0000
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.334 ***
- Linear fit: y = -0.178x + 245.2
- P-value: 0.0000
- N samples: 154

**Is Open Source:**
- Correlation: 0.225 **
- Linear fit: y = 27.022x + 150.3
- P-value: 0.0055
- N samples: 151

**Model Size (B):**
- Correlation: -0.174 *
- Linear fit: y = -0.013x + 171.9
- P-value: 0.0308
- N samples: 154

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.767 ***
- Linear fit: y = -2.151x + 106.6
- P-value: 0.0000
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.582 ***
- Linear fit: y = -0.095x + 83.3
- P-value: 0.0000
- N samples: 154

**Is Reasoning Model:**
- Correlation: -0.559 ***
- Linear fit: y = -20.430x + 51.7
- P-value: 0.0000
- N samples: 151

**Is Open Source:**
- Correlation: 0.196 *
- Linear fit: y = 7.306x + 37.4
- P-value: 0.0157
- N samples: 151

**Model Size (B):**
- Correlation: -0.168 *
- Linear fit: y = -0.004x + 43.1
- P-value: 0.0373
- N samples: 154

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.543 ***
- Linear fit: y = -1.034x + 54.2
- P-value: 0.0000
- N samples: 151

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 5.865x + 19.6
- P-value: 0.0042
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.160 *
- Linear fit: y = -3.973x + 25.0
- P-value: 0.0496
- N samples: 151

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.002x + 24.2
- P-value: 0.0987
- N samples: 154

**Days Since 2024-01-01:**
- Correlation: 0.030 
- Linear fit: y = 0.003x + 21.9
- P-value: 0.7139
- N samples: 154

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.800 ***
- Linear fit: y = -3.292x + 175.8
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.699 ***
- Linear fit: y = -37.463x + 94.9
- P-value: 0.0000
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.322 ***
- Linear fit: y = -0.077x + 110.5
- P-value: 0.0000
- N samples: 154

**Is Open Source:**
- Correlation: 0.170 *
- Linear fit: y = 9.256x + 71.0
- P-value: 0.0375
- N samples: 151

**Model Size (B):**
- Correlation: -0.129 
- Linear fit: y = -0.004x + 78.3
- P-value: 0.1096
- N samples: 154

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.533 ***
- Linear fit: y = -0.792x + 41.1
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.225 **
- Linear fit: y = -4.364x + 19.4
- P-value: 0.0054
- N samples: 151

**Model Size (B):**
- Correlation: -0.129 
- Linear fit: y = -0.002x + 18.1
- P-value: 0.1100
- N samples: 154

**Is Open Source:**
- Correlation: 0.124 
- Linear fit: y = 2.446x + 15.8
- P-value: 0.1293
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.016 
- Linear fit: y = -0.001x + 18.1
- P-value: 0.8438
- N samples: 154

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.629 ***
- Linear fit: y = -0.367x + 17.3
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.277 ***
- Linear fit: y = -2.110x + 7.3
- P-value: 0.0006
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.269 ***
- Linear fit: y = -0.009x + 10.3
- P-value: 0.0008
- N samples: 154

**Is Open Source:**
- Correlation: 0.238 **
- Linear fit: y = 1.847x + 5.2
- P-value: 0.0032
- N samples: 151

**Model Size (B):**
- Correlation: -0.131 
- Linear fit: y = -0.001x + 6.5
- P-value: 0.1062
- N samples: 154

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.666 ***
- Linear fit: y = -1.545x + 78.6
- P-value: 0.0000
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.644 ***
- Linear fit: y = -0.087x + 70.1
- P-value: 0.0000
- N samples: 154

**Is Reasoning Model:**
- Correlation: -0.547 ***
- Linear fit: y = -16.509x + 40.1
- P-value: 0.0000
- N samples: 151

**Model Size (B):**
- Correlation: -0.142 
- Linear fit: y = -0.003x + 33.0
- P-value: 0.0788
- N samples: 154

**Is Open Source:**
- Correlation: 0.123 
- Linear fit: y = 3.790x + 29.8
- P-value: 0.1319
- N samples: 151

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.591 ***
- Linear fit: y = -0.239x + 10.6
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.343 ***
- Linear fit: y = -1.811x + 4.3
- P-value: 0.0000
- N samples: 151

**Is Open Source:**
- Correlation: 0.311 ***
- Linear fit: y = 1.668x + 2.4
- P-value: 0.0001
- N samples: 151

**Model Size (B):**
- Correlation: -0.159 *
- Linear fit: y = -0.001x + 3.6
- P-value: 0.0482
- N samples: 154

**Days Since 2024-01-01:**
- Correlation: 0.053 
- Linear fit: y = 0.001x + 2.9
- P-value: 0.5114
- N samples: 154

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.410 ***
- Linear fit: y = -0.337x + 15.8
- P-value: 0.0000
- N samples: 151

**Is Open Source:**
- Correlation: 0.190 *
- Linear fit: y = 2.079x + 4.4
- P-value: 0.0193
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.161 *
- Linear fit: y = -1.723x + 6.5
- P-value: 0.0488
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: 0.109 
- Linear fit: y = 0.005x + 3.4
- P-value: 0.1781
- N samples: 154

**Model Size (B):**
- Correlation: -0.047 
- Linear fit: y = -0.000x + 5.9
- P-value: 0.5651
- N samples: 154

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.522 ***
- Linear fit: y = -0.626x + 35.6
- P-value: 0.0000
- N samples: 151

**Is Open Source:**
- Correlation: 0.257 **
- Linear fit: y = 4.094x + 14.3
- P-value: 0.0014
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.157 
- Linear fit: y = -2.449x + 17.9
- P-value: 0.0546
- N samples: 151

**Model Size (B):**
- Correlation: -0.150 
- Linear fit: y = -0.002x + 17.5
- P-value: 0.0627
- N samples: 154

**Days Since 2024-01-01:**
- Correlation: -0.008 
- Linear fit: y = -0.001x + 17.2
- P-value: 0.9246
- N samples: 154

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.141 
- Linear fit: y = -0.071x + 2.8
- P-value: 0.0845
- N samples: 151

**Model Size (B):**
- Correlation: -0.075 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.3553
- N samples: 154

**Days Since 2024-01-01:**
- Correlation: -0.047 
- Linear fit: y = -0.001x + 1.3
- P-value: 0.5665
- N samples: 154

**Is Open Source:**
- Correlation: -0.046 
- Linear fit: y = -0.308x + 0.9
- P-value: 0.5729
- N samples: 151

**Is Reasoning Model:**
- Correlation: 0.030 
- Linear fit: y = 0.199x + 0.6
- P-value: 0.7109
- N samples: 151

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.811 ***
- Linear fit: y = -3.008x + 159.1
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.701 ***
- Linear fit: y = -33.853x + 85.0
- P-value: 0.0000
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.376 ***
- Linear fit: y = -0.081x + 104.1
- P-value: 0.0000
- N samples: 154

**Is Open Source:**
- Correlation: 0.173 *
- Linear fit: y = 8.516x + 63.3
- P-value: 0.0336
- N samples: 151

**Model Size (B):**
- Correlation: -0.125 
- Linear fit: y = -0.004x + 69.9
- P-value: 0.1234
- N samples: 154

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.430 ***
- Linear fit: y = -0.286x + 16.6
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.415 ***
- Linear fit: y = -3.592x + 9.7
- P-value: 0.0000
- N samples: 151

**Model Size (B):**
- Correlation: -0.111 
- Linear fit: y = -0.001x + 8.2
- P-value: 0.1720
- N samples: 154

**Is Open Source:**
- Correlation: 0.078 
- Linear fit: y = 0.687x + 7.6
- P-value: 0.3413
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: 0.075 
- Linear fit: y = 0.003x + 6.7
- P-value: 0.3559
- N samples: 154

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.243 **
- Linear fit: y = 0.001x + -0.3
- P-value: 0.0024
- N samples: 154

**Is Open Source:**
- Correlation: 0.045 
- Linear fit: y = 0.053x + 0.2
- P-value: 0.5861
- N samples: 151

**Model Size (B):**
- Correlation: 0.037 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.6498
- N samples: 154

**Benchmark Score:**
- Correlation: 0.023 
- Linear fit: y = 0.002x + 0.2
- P-value: 0.7809
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.016 
- Linear fit: y = -0.018x + 0.2
- P-value: 0.8500
- N samples: 151

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.421 ***
- Linear fit: y = -0.292x + 12.4
- P-value: 0.0000
- N samples: 151

**Is Open Source:**
- Correlation: 0.210 **
- Linear fit: y = 1.935x + 2.4
- P-value: 0.0096
- N samples: 151

**Model Size (B):**
- Correlation: -0.144 
- Linear fit: y = -0.001x + 4.2
- P-value: 0.0752
- N samples: 154

**Is Reasoning Model:**
- Correlation: 0.077 
- Linear fit: y = 0.698x + 3.2
- P-value: 0.3460
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: 0.026 
- Linear fit: y = 0.001x + 3.3
- P-value: 0.7475
- N samples: 154

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.546 ***
- Linear fit: y = -0.511x + 25.5
- P-value: 0.0000
- N samples: 151

**Is Reasoning Model:**
- Correlation: -0.319 ***
- Linear fit: y = -3.893x + 12.0
- P-value: 0.0001
- N samples: 151

**Model Size (B):**
- Correlation: -0.195 *
- Linear fit: y = -0.002x + 10.6
- P-value: 0.0154
- N samples: 154

**Is Open Source:**
- Correlation: 0.162 *
- Linear fit: y = 2.014x + 8.9
- P-value: 0.0467
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.040 
- Linear fit: y = -0.002x + 11.0
- P-value: 0.6191
- N samples: 154

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.245 **
- Linear fit: y = -1.503x + 4.5
- P-value: 0.0024
- N samples: 151

**Model Size (B):**
- Correlation: 0.220 **
- Linear fit: y = 0.001x + 3.3
- P-value: 0.0061
- N samples: 154

**Is Reasoning Model:**
- Correlation: -0.194 *
- Linear fit: y = -1.169x + 4.2
- P-value: 0.0169
- N samples: 151

**Days Since 2024-01-01:**
- Correlation: -0.023 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.7750
- N samples: 154

**Benchmark Score:**
- Correlation: 0.023 
- Linear fit: y = 0.011x + 3.3
- P-value: 0.7790
- N samples: 151

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.866, y = -7.840x + 402.8

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.811, y = -3.008x + 159.1

**category3_logical_errors vs Benchmark Score:**
  r = -0.800, y = -3.292x + 175.8

**category1_input_misalignment vs Benchmark Score:**
  r = -0.767, y = -2.151x + 106.6

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.701, y = -33.853x + 85.0

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.699, y = -37.463x + 94.9

**1b_context_omission vs Benchmark Score:**
  r = -0.666, y = -1.545x + 78.6

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.644, y = -0.087x + 70.1

**1a_instruction_override vs Benchmark Score:**
  r = -0.629, y = -0.367x + 17.3

**total_hallucinations vs Is Reasoning Model:**
  r = -0.601, y = -70.965x + 201.2

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.591, y = -0.239x + 10.6

**category1_input_misalignment vs Days Since 2024-01-01:**
  r = -0.582, y = -0.095x + 83.3

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.559, y = -20.430x + 51.7

**1b_context_omission vs Is Reasoning Model:**
  r = -0.547, y = -16.509x + 40.1

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.546, y = -0.511x + 25.5

**category2_factual_errors vs Benchmark Score:**
  r = -0.543, y = -1.034x + 54.2

**category4_technical_errors vs Benchmark Score:**
  r = -0.533, y = -0.792x + 41.1

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.522, y = -0.626x + 35.6

**3b_self_contradiction vs Benchmark Score:**
  r = -0.430, y = -0.286x + 16.6

**4a_syntax_error vs Benchmark Score:**
  r = -0.421, y = -0.292x + 12.4

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.415, y = -3.592x + 9.7

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.410, y = -0.337x + 15.8

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.376, y = -0.081x + 104.1

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.343, y = -1.811x + 4.3

**total_hallucinations vs Days Since 2024-01-01:**
  r = -0.334, y = -0.178x + 245.2

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.322, y = -0.077x + 110.5

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.319, y = -3.893x + 12.0

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.311, y = 1.668x + 2.4


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
- Correlation: 0.236 **
- Linear fit: y = 0.169x + 16.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.717 ***
- Linear fit: y = 1.053x + 32.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.290 ***
- Linear fit: y = 0.165x + 10.6

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.489 ***
- Linear fit: y = 1.002x + 53.3

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.572 ***
- Linear fit: y = 0.455x + 6.8

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.553 ***
- Linear fit: y = 0.215x + 1.0

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.990 ***, y = 0.893x + 0.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.961 ***, y = 0.795x + -1.2

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.879 ***, y = 0.555x + 4.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.810 ***, y = 0.474x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.757 ***, y = 0.321x + -1.8

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.749 ***, y = 0.991x + 27.2

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.724 ***, y = 0.397x + -3.1

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.717 ***, y = 1.053x + 32.8

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.688 ***, y = 1.099x + 33.3

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.659 ***, y = 0.107x + -0.2

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.645 ***, y = 0.364x + 4.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.636 ***, y = 0.133x + 0.8

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.634 ***, y = 0.144x + -1.0

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.621 ***, y = 0.157x + -0.7

**Category 3: Logical Errors vs 1c: Prompt Contradiction:**
  r = 0.617 ***, y = 0.061x + -1.2

**1c: Prompt Contradiction vs 3a: Unsupported Leap:**
  r = 0.585 ***, y = 5.335x + 50.1

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.572 ***, y = 0.455x + 6.8

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.553 ***, y = 0.215x + 1.0

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.551 ***, y = 0.099x + 1.3

**1c: Prompt Contradiction vs 4b: Model Semantics Breach:**
  r = 0.538 ***, y = 1.238x + 5.8

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
