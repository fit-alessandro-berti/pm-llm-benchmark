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
- Correlation: -0.789 ***
- Linear fit: y = -2.427x + 126.9
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.554 ***
- Linear fit: y = -25.912x + 55.1
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: -0.243 **
- Linear fit: y = -0.040x + 62.6
- P-value: 0.0012
- N samples: 174

**Is Open Source:**
- Correlation: 0.227 **
- Linear fit: y = 10.636x + 36.6
- P-value: 0.0031
- N samples: 168

**Model Size (B):**
- Correlation: -0.131 
- Linear fit: y = -0.003x + 44.0
- P-value: 0.0861
- N samples: 173

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.541 ***
- Linear fit: y = -1.491x + 79.6
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.276 ***
- Linear fit: y = 0.041x + 7.3
- P-value: 0.0002
- N samples: 174

**Is Reasoning Model:**
- Correlation: -0.220 **
- Linear fit: y = -9.233x + 32.2
- P-value: 0.0041
- N samples: 168

**Is Open Source:**
- Correlation: 0.212 **
- Linear fit: y = 8.919x + 22.9
- P-value: 0.0057
- N samples: 168

**Model Size (B):**
- Correlation: -0.104 
- Linear fit: y = -0.002x + 28.5
- P-value: 0.1727
- N samples: 173

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.766 ***
- Linear fit: y = -3.376x + 193.8
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.655 ***
- Linear fit: y = -43.862x + 97.6
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: -0.168 *
- Linear fit: y = -0.039x + 95.9
- P-value: 0.0270
- N samples: 174

**Is Open Source:**
- Correlation: 0.159 *
- Linear fit: y = 10.702x + 70.4
- P-value: 0.0393
- N samples: 168

**Model Size (B):**
- Correlation: -0.111 
- Linear fit: y = -0.004x + 77.9
- P-value: 0.1448
- N samples: 173

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.683 ***
- Linear fit: y = -1.278x + 63.6
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.301 ***
- Linear fit: y = -8.560x + 23.3
- P-value: 0.0001
- N samples: 168

**Is Open Source:**
- Correlation: 0.206 **
- Linear fit: y = 5.893x + 15.9
- P-value: 0.0073
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.144 
- Linear fit: y = 0.014x + 11.7
- P-value: 0.0588
- N samples: 174

**Model Size (B):**
- Correlation: -0.122 
- Linear fit: y = -0.002x + 19.6
- P-value: 0.1109
- N samples: 173

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.804 ***
- Linear fit: y = -9.329x + 499.0
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.541 ***
- Linear fit: y = -95.421x + 220.6
- P-value: 0.0000
- N samples: 168

**Is Open Source:**
- Correlation: 0.227 **
- Linear fit: y = 40.163x + 152.3
- P-value: 0.0031
- N samples: 168

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.013x + 179.1
- P-value: 0.0792
- N samples: 173

**Days Since 2024-01-01:**
- Correlation: -0.035 
- Linear fit: y = -0.022x + 184.4
- P-value: 0.6485
- N samples: 174

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.789 ***
- Linear fit: y = -2.427x + 126.9
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.554 ***
- Linear fit: y = -25.912x + 55.1
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: -0.243 **
- Linear fit: y = -0.040x + 62.6
- P-value: 0.0012
- N samples: 174

**Is Open Source:**
- Correlation: 0.227 **
- Linear fit: y = 10.636x + 36.6
- P-value: 0.0031
- N samples: 168

**Model Size (B):**
- Correlation: -0.131 
- Linear fit: y = -0.003x + 44.0
- P-value: 0.0861
- N samples: 173

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.541 ***
- Linear fit: y = -1.491x + 79.6
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.276 ***
- Linear fit: y = 0.041x + 7.3
- P-value: 0.0002
- N samples: 174

**Is Reasoning Model:**
- Correlation: -0.220 **
- Linear fit: y = -9.233x + 32.2
- P-value: 0.0041
- N samples: 168

**Is Open Source:**
- Correlation: 0.212 **
- Linear fit: y = 8.919x + 22.9
- P-value: 0.0057
- N samples: 168

**Model Size (B):**
- Correlation: -0.104 
- Linear fit: y = -0.002x + 28.5
- P-value: 0.1727
- N samples: 173

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.766 ***
- Linear fit: y = -3.376x + 193.8
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.655 ***
- Linear fit: y = -43.862x + 97.6
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: -0.168 *
- Linear fit: y = -0.039x + 95.9
- P-value: 0.0270
- N samples: 174

**Is Open Source:**
- Correlation: 0.159 *
- Linear fit: y = 10.702x + 70.4
- P-value: 0.0393
- N samples: 168

**Model Size (B):**
- Correlation: -0.111 
- Linear fit: y = -0.004x + 77.9
- P-value: 0.1448
- N samples: 173

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.683 ***
- Linear fit: y = -1.278x + 63.6
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.301 ***
- Linear fit: y = -8.560x + 23.3
- P-value: 0.0001
- N samples: 168

**Is Open Source:**
- Correlation: 0.206 **
- Linear fit: y = 5.893x + 15.9
- P-value: 0.0073
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.144 
- Linear fit: y = 0.014x + 11.7
- P-value: 0.0588
- N samples: 174

**Model Size (B):**
- Correlation: -0.122 
- Linear fit: y = -0.002x + 19.6
- P-value: 0.1109
- N samples: 173

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.673 ***
- Linear fit: y = -0.456x + 23.0
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.359 ***
- Linear fit: y = -3.697x + 9.0
- P-value: 0.0000
- N samples: 168

**Is Open Source:**
- Correlation: 0.277 ***
- Linear fit: y = 2.864x + 5.6
- P-value: 0.0003
- N samples: 168

**Model Size (B):**
- Correlation: -0.090 
- Linear fit: y = -0.001x + 7.3
- P-value: 0.2381
- N samples: 173

**Days Since 2024-01-01:**
- Correlation: 0.069 
- Linear fit: y = 0.002x + 5.9
- P-value: 0.3675
- N samples: 174

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.710 ***
- Linear fit: y = -1.574x + 86.0
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.564 ***
- Linear fit: y = -19.015x + 40.4
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: -0.410 ***
- Linear fit: y = -0.049x + 55.9
- P-value: 0.0000
- N samples: 174

**Is Open Source:**
- Correlation: 0.145 
- Linear fit: y = 4.900x + 28.5
- P-value: 0.0611
- N samples: 168

**Model Size (B):**
- Correlation: -0.116 
- Linear fit: y = -0.002x + 32.3
- P-value: 0.1277
- N samples: 173

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.698 ***
- Linear fit: y = -0.396x + 17.9
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.371 ***
- Linear fit: y = -3.199x + 5.7
- P-value: 0.0000
- N samples: 168

**Is Open Source:**
- Correlation: 0.332 ***
- Linear fit: y = 2.872x + 2.5
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.214 **
- Linear fit: y = 0.006x + 0.8
- P-value: 0.0046
- N samples: 174

**Model Size (B):**
- Correlation: -0.147 
- Linear fit: y = -0.001x + 4.3
- P-value: 0.0538
- N samples: 173

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.485 ***
- Linear fit: y = -0.750x + 34.2
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.311 ***
- Linear fit: y = 0.026x + -4.8
- P-value: 0.0000
- N samples: 174

**Is Reasoning Model:**
- Correlation: -0.233 **
- Linear fit: y = -5.474x + 10.8
- P-value: 0.0024
- N samples: 168

**Is Open Source:**
- Correlation: 0.212 **
- Linear fit: y = 4.993x + 5.4
- P-value: 0.0059
- N samples: 168

**Model Size (B):**
- Correlation: -0.051 
- Linear fit: y = -0.001x + 8.3
- P-value: 0.5058
- N samples: 173

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.505 ***
- Linear fit: y = -0.691x + 43.0
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.214 **
- Linear fit: y = 0.016x + 11.0
- P-value: 0.0045
- N samples: 174

**Is Open Source:**
- Correlation: 0.197 *
- Linear fit: y = 4.110x + 16.7
- P-value: 0.0106
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.190 *
- Linear fit: y = -3.957x + 20.9
- P-value: 0.0136
- N samples: 168

**Model Size (B):**
- Correlation: -0.129 
- Linear fit: y = -0.001x + 19.4
- P-value: 0.0897
- N samples: 173

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.121 
- Linear fit: y = -0.050x + 2.4
- P-value: 0.1189
- N samples: 168

**Model Size (B):**
- Correlation: -0.074 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.3357
- N samples: 173

**Days Since 2024-01-01:**
- Correlation: -0.034 
- Linear fit: y = -0.001x + 1.0
- P-value: 0.6545
- N samples: 174

**Is Reasoning Model:**
- Correlation: 0.032 
- Linear fit: y = 0.199x + 0.6
- P-value: 0.6821
- N samples: 168

**Is Open Source:**
- Correlation: -0.029 
- Linear fit: y = -0.184x + 0.8
- P-value: 0.7055
- N samples: 168

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.755 ***
- Linear fit: y = -2.791x + 163.9
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.667 ***
- Linear fit: y = -37.488x + 85.0
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: -0.253 ***
- Linear fit: y = -0.050x + 91.7
- P-value: 0.0007
- N samples: 174

**Is Open Source:**
- Correlation: 0.132 
- Linear fit: y = 7.459x + 62.7
- P-value: 0.0873
- N samples: 168

**Model Size (B):**
- Correlation: -0.100 
- Linear fit: y = -0.003x + 68.1
- P-value: 0.1886
- N samples: 173

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.619 ***
- Linear fit: y = -0.550x + 28.3
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.451 ***
- Linear fit: y = -6.094x + 12.1
- P-value: 0.0000
- N samples: 168

**Is Open Source:**
- Correlation: 0.220 **
- Linear fit: y = 2.979x + 7.5
- P-value: 0.0042
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.194 *
- Linear fit: y = 0.009x + 4.5
- P-value: 0.0105
- N samples: 174

**Model Size (B):**
- Correlation: -0.127 
- Linear fit: y = -0.001x + 9.5
- P-value: 0.0948
- N samples: 173

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.339 ***
- Linear fit: y = -0.036x + 1.6
- P-value: 0.0000
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.241 **
- Linear fit: y = 0.001x + -0.3
- P-value: 0.0014
- N samples: 174

**Is Reasoning Model:**
- Correlation: -0.173 *
- Linear fit: y = -0.281x + 0.5
- P-value: 0.0246
- N samples: 168

**Is Open Source:**
- Correlation: 0.163 *
- Linear fit: y = 0.265x + 0.2
- P-value: 0.0350
- N samples: 168

**Model Size (B):**
- Correlation: -0.055 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4720
- N samples: 173

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.605 ***
- Linear fit: y = -0.583x + 25.3
- P-value: 0.0000
- N samples: 168

**Is Open Source:**
- Correlation: 0.306 ***
- Linear fit: y = 4.493x + 2.6
- P-value: 0.0001
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: 0.247 ***
- Linear fit: y = 0.013x + -1.4
- P-value: 0.0010
- N samples: 174

**Model Size (B):**
- Correlation: -0.153 *
- Linear fit: y = -0.001x + 5.4
- P-value: 0.0451
- N samples: 173

**Is Reasoning Model:**
- Correlation: -0.126 
- Linear fit: y = -1.845x + 5.9
- P-value: 0.1039
- N samples: 168

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.696 ***
- Linear fit: y = -0.658x + 33.2
- P-value: 0.0000
- N samples: 168

**Is Reasoning Model:**
- Correlation: -0.392 ***
- Linear fit: y = -5.635x + 13.0
- P-value: 0.0000
- N samples: 168

**Is Open Source:**
- Correlation: 0.212 **
- Linear fit: y = 3.053x + 8.6
- P-value: 0.0059
- N samples: 168

**Model Size (B):**
- Correlation: -0.182 *
- Linear fit: y = -0.001x + 10.8
- P-value: 0.0166
- N samples: 173

**Days Since 2024-01-01:**
- Correlation: 0.045 
- Linear fit: y = 0.002x + 9.0
- P-value: 0.5516
- N samples: 174

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.262 ***
- Linear fit: y = -1.652x + 4.7
- P-value: 0.0006
- N samples: 168

**Model Size (B):**
- Correlation: 0.217 **
- Linear fit: y = 0.001x + 3.5
- P-value: 0.0041
- N samples: 173

**Is Reasoning Model:**
- Correlation: -0.172 *
- Linear fit: y = -1.079x + 4.4
- P-value: 0.0261
- N samples: 168

**Benchmark Score:**
- Correlation: -0.086 
- Linear fit: y = -0.036x + 5.1
- P-value: 0.2652
- N samples: 168

**Days Since 2024-01-01:**
- Correlation: -0.029 
- Linear fit: y = -0.001x + 4.1
- P-value: 0.7053
- N samples: 174

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.804, y = -9.329x + 499.0

**category1_input_misalignment vs Benchmark Score:**
  r = -0.789, y = -2.427x + 126.9

**category3_logical_errors vs Benchmark Score:**
  r = -0.766, y = -3.376x + 193.8

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.755, y = -2.791x + 163.9

**1b_context_omission vs Benchmark Score:**
  r = -0.710, y = -1.574x + 86.0

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.698, y = -0.396x + 17.9

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.696, y = -0.658x + 33.2

**category4_technical_errors vs Benchmark Score:**
  r = -0.683, y = -1.278x + 63.6

**1a_instruction_override vs Benchmark Score:**
  r = -0.673, y = -0.456x + 23.0

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.667, y = -37.488x + 85.0

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.655, y = -43.862x + 97.6

**3b_self_contradiction vs Benchmark Score:**
  r = -0.619, y = -0.550x + 28.3

**4a_syntax_error vs Benchmark Score:**
  r = -0.605, y = -0.583x + 25.3

**1b_context_omission vs Is Reasoning Model:**
  r = -0.564, y = -19.015x + 40.4

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.554, y = -25.912x + 55.1

**category2_factual_errors vs Benchmark Score:**
  r = -0.541, y = -1.491x + 79.6

**total_hallucinations vs Is Reasoning Model:**
  r = -0.541, y = -95.421x + 220.6

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.505, y = -0.691x + 43.0

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.485, y = -0.750x + 34.2

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.451, y = -6.094x + 12.1

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.410, y = -0.049x + 55.9

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.392, y = -5.635x + 13.0

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.371, y = -3.199x + 5.7

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.359, y = -3.697x + 9.0

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.339, y = -0.036x + 1.6

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.332, y = 2.872x + 2.5

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.311, y = 0.026x + -4.8

**4a_syntax_error vs Is Open Source:**
  r = 0.306, y = 4.493x + 2.6

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.301, y = -8.560x + 23.3


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
- Linear fit: y = 0.466x + 7.7

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.816 ***
- Linear fit: y = 1.163x + 26.7

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.621 ***
- Linear fit: y = 0.377x + 2.8

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.620 ***
- Linear fit: y = 0.992x + 48.9

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.743 ***
- Linear fit: y = 0.506x + 4.9

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.703 ***
- Linear fit: y = 0.300x + -4.0

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.988 ***, y = 0.829x + 3.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.953 ***, y = 0.691x + 2.0

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.903 ***, y = 0.506x + -5.9

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.896 ***, y = 0.452x + 1.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.882 ***, y = 0.440x + 6.7

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.868 ***, y = 0.446x + -3.5

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.816 ***, y = 1.163x + 26.7

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.806 ***, y = 0.964x + 25.8

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.800 ***, y = 0.162x + -3.2

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.790 ***, y = 1.236x + 4.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.788 ***, y = 0.174x + -0.3

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.787 ***, y = 0.453x + 5.4

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.785 ***, y = 1.295x + 26.1

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.776 ***, y = 0.484x + 1.0

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.770 ***, y = 0.249x + 2.2

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.766 ***, y = 0.390x + 1.7

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.764 ***, y = 2.074x + -0.4

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.763 ***, y = 0.361x + 2.3

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.754 ***, y = 0.629x + -0.4

**Category 2: Factual Errors vs 4a: Syntax Error:**
  r = 0.750 ***, y = 0.262x + -2.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
