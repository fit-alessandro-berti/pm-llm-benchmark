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
- Correlation: -0.776 ***
- Linear fit: y = -2.407x + 126.4
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.553 ***
- Linear fit: y = -25.636x + 55.0
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.257 ***
- Linear fit: y = 11.908x + 36.4
- P-value: 0.0008
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: -0.226 **
- Linear fit: y = -0.037x + 61.3
- P-value: 0.0028
- N samples: 174

**Model Size (B):**
- Correlation: -0.121 
- Linear fit: y = -0.003x + 44.0
- P-value: 0.1125
- N samples: 173

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.529 ***
- Linear fit: y = -1.455x + 78.0
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.275 ***
- Linear fit: y = 0.040x + 7.2
- P-value: 0.0002
- N samples: 174

**Is Reasoning Model:**
- Correlation: -0.235 **
- Linear fit: y = -9.657x + 32.1
- P-value: 0.0022
- N samples: 167

**Is Open Source:**
- Correlation: 0.214 **
- Linear fit: y = 8.820x + 22.7
- P-value: 0.0054
- N samples: 167

**Model Size (B):**
- Correlation: -0.096 
- Linear fit: y = -0.002x + 28.1
- P-value: 0.2077
- N samples: 173

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.754 ***
- Linear fit: y = -3.334x + 192.9
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.650 ***
- Linear fit: y = -42.914x + 97.6
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.196 *
- Linear fit: y = 12.931x + 70.1
- P-value: 0.0112
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: -0.137 
- Linear fit: y = -0.032x + 92.8
- P-value: 0.0719
- N samples: 174

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.004x + 78.5
- P-value: 0.1688
- N samples: 173

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.675 ***
- Linear fit: y = -1.252x + 62.6
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.309 ***
- Linear fit: y = -8.547x + 23.2
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.218 **
- Linear fit: y = 6.040x + 15.9
- P-value: 0.0047
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.143 
- Linear fit: y = 0.014x + 11.7
- P-value: 0.0594
- N samples: 174

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.002x + 19.5
- P-value: 0.1249
- N samples: 173

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.793 ***
- Linear fit: y = -9.211x + 495.1
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.545 ***
- Linear fit: y = -94.530x + 220.2
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.253 ***
- Linear fit: y = 43.874x + 151.6
- P-value: 0.0010
- N samples: 167

**Model Size (B):**
- Correlation: -0.126 
- Linear fit: y = -0.012x + 179.1
- P-value: 0.0983
- N samples: 173

**Days Since 2024-01-01:**
- Correlation: -0.019 
- Linear fit: y = -0.012x + 180.0
- P-value: 0.8037
- N samples: 174

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.776 ***
- Linear fit: y = -2.407x + 126.4
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.553 ***
- Linear fit: y = -25.636x + 55.0
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.257 ***
- Linear fit: y = 11.908x + 36.4
- P-value: 0.0008
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: -0.226 **
- Linear fit: y = -0.037x + 61.3
- P-value: 0.0028
- N samples: 174

**Model Size (B):**
- Correlation: -0.121 
- Linear fit: y = -0.003x + 44.0
- P-value: 0.1125
- N samples: 173

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.529 ***
- Linear fit: y = -1.455x + 78.0
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.275 ***
- Linear fit: y = 0.040x + 7.2
- P-value: 0.0002
- N samples: 174

**Is Reasoning Model:**
- Correlation: -0.235 **
- Linear fit: y = -9.657x + 32.1
- P-value: 0.0022
- N samples: 167

**Is Open Source:**
- Correlation: 0.214 **
- Linear fit: y = 8.820x + 22.7
- P-value: 0.0054
- N samples: 167

**Model Size (B):**
- Correlation: -0.096 
- Linear fit: y = -0.002x + 28.1
- P-value: 0.2077
- N samples: 173

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.754 ***
- Linear fit: y = -3.334x + 192.9
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.650 ***
- Linear fit: y = -42.914x + 97.6
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.196 *
- Linear fit: y = 12.931x + 70.1
- P-value: 0.0112
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: -0.137 
- Linear fit: y = -0.032x + 92.8
- P-value: 0.0719
- N samples: 174

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.004x + 78.5
- P-value: 0.1688
- N samples: 173

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.675 ***
- Linear fit: y = -1.252x + 62.6
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.309 ***
- Linear fit: y = -8.547x + 23.2
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.218 **
- Linear fit: y = 6.040x + 15.9
- P-value: 0.0047
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.143 
- Linear fit: y = 0.014x + 11.7
- P-value: 0.0594
- N samples: 174

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.002x + 19.5
- P-value: 0.1249
- N samples: 173

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.659 ***
- Linear fit: y = -0.452x + 22.9
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.363 ***
- Linear fit: y = -3.717x + 9.0
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.299 ***
- Linear fit: y = 3.068x + 5.5
- P-value: 0.0001
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.082 
- Linear fit: y = 0.003x + 5.6
- P-value: 0.2846
- N samples: 174

**Model Size (B):**
- Correlation: -0.080 
- Linear fit: y = -0.000x + 7.3
- P-value: 0.2925
- N samples: 173

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.695 ***
- Linear fit: y = -1.559x + 85.6
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.557 ***
- Linear fit: y = -18.641x + 40.4
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: -0.390 ***
- Linear fit: y = -0.047x + 55.0
- P-value: 0.0000
- N samples: 174

**Is Open Source:**
- Correlation: 0.178 *
- Linear fit: y = 5.965x + 28.3
- P-value: 0.0214
- N samples: 167

**Model Size (B):**
- Correlation: -0.107 
- Linear fit: y = -0.002x + 32.5
- P-value: 0.1603
- N samples: 173

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.692 ***
- Linear fit: y = -0.396x + 17.9
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.384 ***
- Linear fit: y = -3.279x + 5.7
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.336 ***
- Linear fit: y = 2.874x + 2.6
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.217 **
- Linear fit: y = 0.007x + 0.8
- P-value: 0.0040
- N samples: 174

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.001x + 4.3
- P-value: 0.0661
- N samples: 173

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.475 ***
- Linear fit: y = -0.735x + 33.5
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.310 ***
- Linear fit: y = 0.025x + -4.7
- P-value: 0.0000
- N samples: 174

**Is Reasoning Model:**
- Correlation: -0.247 **
- Linear fit: y = -5.698x + 10.7
- P-value: 0.0013
- N samples: 167

**Is Open Source:**
- Correlation: 0.215 **
- Linear fit: y = 4.967x + 5.4
- P-value: 0.0053
- N samples: 167

**Model Size (B):**
- Correlation: -0.044 
- Linear fit: y = -0.001x + 8.1
- P-value: 0.5673
- N samples: 173

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.489 ***
- Linear fit: y = -0.676x + 42.3
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.214 **
- Linear fit: y = 0.016x + 10.8
- P-value: 0.0046
- N samples: 174

**Is Reasoning Model:**
- Correlation: -0.200 **
- Linear fit: y = -4.134x + 20.8
- P-value: 0.0094
- N samples: 167

**Is Open Source:**
- Correlation: 0.196 *
- Linear fit: y = 4.059x + 16.6
- P-value: 0.0109
- N samples: 167

**Model Size (B):**
- Correlation: -0.121 
- Linear fit: y = -0.001x + 19.2
- P-value: 0.1133
- N samples: 173

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.109 
- Linear fit: y = -0.045x + 2.2
- P-value: 0.1621
- N samples: 167

**Model Size (B):**
- Correlation: -0.071 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.3550
- N samples: 173

**Days Since 2024-01-01:**
- Correlation: -0.044 
- Linear fit: y = -0.001x + 1.1
- P-value: 0.5636
- N samples: 174

**Is Open Source:**
- Correlation: -0.033 
- Linear fit: y = -0.206x + 0.8
- P-value: 0.6717
- N samples: 167

**Is Reasoning Model:**
- Correlation: 0.028 
- Linear fit: y = 0.174x + 0.6
- P-value: 0.7194
- N samples: 167

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.744 ***
- Linear fit: y = -2.751x + 163.1
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.662 ***
- Linear fit: y = -36.526x + 85.0
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: -0.222 **
- Linear fit: y = -0.044x + 89.1
- P-value: 0.0032
- N samples: 174

**Is Open Source:**
- Correlation: 0.172 *
- Linear fit: y = 9.534x + 62.4
- P-value: 0.0258
- N samples: 167

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.003x + 68.6
- P-value: 0.2179
- N samples: 173

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.607 ***
- Linear fit: y = -0.546x + 28.1
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.456 ***
- Linear fit: y = -6.118x + 12.1
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 3.120x + 7.5
- P-value: 0.0025
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.213 **
- Linear fit: y = 0.010x + 4.1
- P-value: 0.0047
- N samples: 174

**Model Size (B):**
- Correlation: -0.122 
- Linear fit: y = -0.001x + 9.5
- P-value: 0.1098
- N samples: 173

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.342 ***
- Linear fit: y = -0.037x + 1.6
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.254 ***
- Linear fit: y = 0.001x + -0.4
- P-value: 0.0007
- N samples: 174

**Is Open Source:**
- Correlation: 0.171 *
- Linear fit: y = 0.278x + 0.2
- P-value: 0.0273
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.166 *
- Linear fit: y = -0.270x + 0.5
- P-value: 0.0318
- N samples: 167

**Model Size (B):**
- Correlation: -0.055 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4733
- N samples: 173

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.600 ***
- Linear fit: y = -0.578x + 25.0
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.309 ***
- Linear fit: y = 4.444x + 2.6
- P-value: 0.0000
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: 0.244 **
- Linear fit: y = 0.013x + -1.4
- P-value: 0.0012
- N samples: 174

**Model Size (B):**
- Correlation: -0.150 *
- Linear fit: y = -0.001x + 5.3
- P-value: 0.0484
- N samples: 173

**Is Reasoning Model:**
- Correlation: -0.133 
- Linear fit: y = -1.911x + 5.9
- P-value: 0.0869
- N samples: 167

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.687 ***
- Linear fit: y = -0.644x + 32.7
- P-value: 0.0000
- N samples: 167

**Is Reasoning Model:**
- Correlation: -0.400 ***
- Linear fit: y = -5.603x + 13.0
- P-value: 0.0000
- N samples: 167

**Is Open Source:**
- Correlation: 0.228 **
- Linear fit: y = 3.198x + 8.6
- P-value: 0.0030
- N samples: 167

**Model Size (B):**
- Correlation: -0.180 *
- Linear fit: y = -0.001x + 10.7
- P-value: 0.0179
- N samples: 173

**Days Since 2024-01-01:**
- Correlation: 0.046 
- Linear fit: y = 0.002x + 9.0
- P-value: 0.5469
- N samples: 174

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.254 ***
- Linear fit: y = -1.602x + 4.7
- P-value: 0.0009
- N samples: 167

**Model Size (B):**
- Correlation: 0.223 **
- Linear fit: y = 0.001x + 3.4
- P-value: 0.0032
- N samples: 173

**Is Reasoning Model:**
- Correlation: -0.164 *
- Linear fit: y = -1.033x + 4.3
- P-value: 0.0340
- N samples: 167

**Benchmark Score:**
- Correlation: -0.071 
- Linear fit: y = -0.030x + 4.9
- P-value: 0.3591
- N samples: 167

**Days Since 2024-01-01:**
- Correlation: -0.027 
- Linear fit: y = -0.001x + 4.0
- P-value: 0.7223
- N samples: 174

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.793, y = -9.211x + 495.1

**category1_input_misalignment vs Benchmark Score:**
  r = -0.776, y = -2.407x + 126.4

**category3_logical_errors vs Benchmark Score:**
  r = -0.754, y = -3.334x + 192.9

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.744, y = -2.751x + 163.1

**1b_context_omission vs Benchmark Score:**
  r = -0.695, y = -1.559x + 85.6

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.692, y = -0.396x + 17.9

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.687, y = -0.644x + 32.7

**category4_technical_errors vs Benchmark Score:**
  r = -0.675, y = -1.252x + 62.6

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.662, y = -36.526x + 85.0

**1a_instruction_override vs Benchmark Score:**
  r = -0.659, y = -0.452x + 22.9

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.650, y = -42.914x + 97.6

**3b_self_contradiction vs Benchmark Score:**
  r = -0.607, y = -0.546x + 28.1

**4a_syntax_error vs Benchmark Score:**
  r = -0.600, y = -0.578x + 25.0

**1b_context_omission vs Is Reasoning Model:**
  r = -0.557, y = -18.641x + 40.4

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.553, y = -25.636x + 55.0

**total_hallucinations vs Is Reasoning Model:**
  r = -0.545, y = -94.530x + 220.2

**category2_factual_errors vs Benchmark Score:**
  r = -0.529, y = -1.455x + 78.0

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.489, y = -0.676x + 42.3

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.475, y = -0.735x + 33.5

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.456, y = -6.118x + 12.1

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.400, y = -5.603x + 13.0

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.390, y = -0.047x + 55.0

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.384, y = -3.279x + 5.7

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.363, y = -3.717x + 9.0

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.342, y = -0.037x + 1.6

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.336, y = 2.874x + 2.6

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.310, y = 0.025x + -4.7

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.309, y = -8.547x + 23.2

**4a_syntax_error vs Is Open Source:**
  r = 0.309, y = 4.444x + 2.6


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
- Correlation: 0.518 ***
- Linear fit: y = 0.455x + 7.8

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.812 ***
- Linear fit: y = 1.149x + 27.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.613 ***
- Linear fit: y = 0.366x + 3.1

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.624 ***
- Linear fit: y = 1.004x + 49.5

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.730 ***
- Linear fit: y = 0.495x + 5.3

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.707 ***
- Linear fit: y = 0.298x + -4.2

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.988 ***, y = 0.828x + 3.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.953 ***, y = 0.692x + 2.0

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.898 ***, y = 0.505x + -5.8

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.889 ***, y = 0.449x + 1.7

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.878 ***, y = 0.443x + 6.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.863 ***, y = 0.445x + -3.5

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.812 ***, y = 1.149x + 27.8

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.803 ***, y = 0.952x + 26.7

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.799 ***, y = 0.163x + -3.3

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.789 ***, y = 1.238x + 4.1

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.788 ***, y = 0.459x + 5.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.786 ***, y = 0.173x + -0.3

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.779 ***, y = 1.272x + 27.2

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.768 ***, y = 0.251x + 2.3

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.766 ***, y = 0.477x + 1.1

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.761 ***, y = 0.367x + 2.3

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.758 ***, y = 0.389x + 1.6

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.756 ***, y = 2.039x + -0.3

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.746 ***, y = 0.619x + -0.4

**Category 2: Factual Errors vs 4a: Syntax Error:**
  r = 0.738 ***, y = 0.258x + -2.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
