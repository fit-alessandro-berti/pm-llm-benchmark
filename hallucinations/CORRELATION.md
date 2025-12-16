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
- Correlation: -0.796 ***
- Linear fit: y = -2.487x + 129.4
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.563 ***
- Linear fit: y = -26.759x + 55.7
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.253 ***
- Linear fit: y = 12.038x + 36.4
- P-value: 0.0007
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: -0.204 **
- Linear fit: y = -0.033x + 59.8
- P-value: 0.0057
- N samples: 183

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 44.6
- P-value: 0.0651
- N samples: 179

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.537 ***
- Linear fit: y = -1.514x + 81.2
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.299 ***
- Linear fit: y = 0.044x + 6.0
- P-value: 0.0000
- N samples: 183

**Is Reasoning Model:**
- Correlation: -0.246 **
- Linear fit: y = -10.539x + 33.6
- P-value: 0.0010
- N samples: 176

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 9.997x + 23.2
- P-value: 0.0019
- N samples: 176

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.003x + 29.7
- P-value: 0.1197
- N samples: 179

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.770 ***
- Linear fit: y = -3.451x + 196.7
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.657 ***
- Linear fit: y = -44.798x + 98.0
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.189 *
- Linear fit: y = 12.881x + 69.7
- P-value: 0.0122
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: -0.142 
- Linear fit: y = -0.033x + 93.4
- P-value: 0.0550
- N samples: 183

**Model Size (B):**
- Correlation: -0.120 
- Linear fit: y = -0.004x + 79.1
- P-value: 0.1102
- N samples: 179

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.359x + 67.0
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.315 ***
- Linear fit: y = -9.442x + 24.2
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.230 **
- Linear fit: y = 6.916x + 16.0
- P-value: 0.0021
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.176 *
- Linear fit: y = 0.018x + 10.2
- P-value: 0.0175
- N samples: 183

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.002x + 20.4
- P-value: 0.0771
- N samples: 179

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.807 ***
- Linear fit: y = -9.593x + 510.4
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.550 ***
- Linear fit: y = -99.570x + 224.1
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.255 ***
- Linear fit: y = 46.274x + 151.6
- P-value: 0.0006
- N samples: 176

**Model Size (B):**
- Correlation: -0.144 
- Linear fit: y = -0.014x + 183.1
- P-value: 0.0536
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: -0.001 
- Linear fit: y = -0.001x + 176.1
- P-value: 0.9883
- N samples: 183

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.796 ***
- Linear fit: y = -2.487x + 129.4
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.563 ***
- Linear fit: y = -26.759x + 55.7
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.253 ***
- Linear fit: y = 12.038x + 36.4
- P-value: 0.0007
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: -0.204 **
- Linear fit: y = -0.033x + 59.8
- P-value: 0.0057
- N samples: 183

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.004x + 44.6
- P-value: 0.0651
- N samples: 179

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.537 ***
- Linear fit: y = -1.514x + 81.2
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.299 ***
- Linear fit: y = 0.044x + 6.0
- P-value: 0.0000
- N samples: 183

**Is Reasoning Model:**
- Correlation: -0.246 **
- Linear fit: y = -10.539x + 33.6
- P-value: 0.0010
- N samples: 176

**Is Open Source:**
- Correlation: 0.232 **
- Linear fit: y = 9.997x + 23.2
- P-value: 0.0019
- N samples: 176

**Model Size (B):**
- Correlation: -0.117 
- Linear fit: y = -0.003x + 29.7
- P-value: 0.1197
- N samples: 179

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.770 ***
- Linear fit: y = -3.451x + 196.7
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.657 ***
- Linear fit: y = -44.798x + 98.0
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.189 *
- Linear fit: y = 12.881x + 69.7
- P-value: 0.0122
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: -0.142 
- Linear fit: y = -0.033x + 93.4
- P-value: 0.0550
- N samples: 183

**Model Size (B):**
- Correlation: -0.120 
- Linear fit: y = -0.004x + 79.1
- P-value: 0.1102
- N samples: 179

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.691 ***
- Linear fit: y = -1.359x + 67.0
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.315 ***
- Linear fit: y = -9.442x + 24.2
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.230 **
- Linear fit: y = 6.916x + 16.0
- P-value: 0.0021
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.176 *
- Linear fit: y = 0.018x + 10.2
- P-value: 0.0175
- N samples: 183

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.002x + 20.4
- P-value: 0.0771
- N samples: 179

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.651 ***
- Linear fit: y = -0.483x + 24.3
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.390 ***
- Linear fit: y = -4.403x + 9.6
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.299 ***
- Linear fit: y = 3.379x + 5.7
- P-value: 0.0001
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.145 
- Linear fit: y = 0.006x + 4.6
- P-value: 0.0504
- N samples: 183

**Model Size (B):**
- Correlation: -0.105 
- Linear fit: y = -0.001x + 7.7
- P-value: 0.1623
- N samples: 179

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.721 ***
- Linear fit: y = -1.605x + 87.0
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.559 ***
- Linear fit: y = -18.960x + 40.2
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: -0.390 ***
- Linear fit: y = -0.046x + 54.5
- P-value: 0.0000
- N samples: 183

**Is Open Source:**
- Correlation: 0.166 *
- Linear fit: y = 5.652x + 28.1
- P-value: 0.0273
- N samples: 176

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.002x + 32.4
- P-value: 0.1134
- N samples: 179

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.700 ***
- Linear fit: y = -0.399x + 18.1
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.392 ***
- Linear fit: y = -3.396x + 5.8
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.346 ***
- Linear fit: y = 3.007x + 2.6
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.229 **
- Linear fit: y = 0.007x + 0.7
- P-value: 0.0018
- N samples: 183

**Model Size (B):**
- Correlation: -0.156 *
- Linear fit: y = -0.001x + 4.5
- P-value: 0.0371
- N samples: 179

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.497 ***
- Linear fit: y = -0.762x + 34.8
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.309 ***
- Linear fit: y = 0.025x + -4.3
- P-value: 0.0000
- N samples: 183

**Is Reasoning Model:**
- Correlation: -0.253 ***
- Linear fit: y = -5.894x + 11.1
- P-value: 0.0007
- N samples: 176

**Is Open Source:**
- Correlation: 0.227 **
- Linear fit: y = 5.305x + 5.4
- P-value: 0.0025
- N samples: 176

**Model Size (B):**
- Correlation: -0.059 
- Linear fit: y = -0.001x + 8.6
- P-value: 0.4346
- N samples: 179

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.472 ***
- Linear fit: y = -0.702x + 44.0
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.258 ***
- Linear fit: y = 0.020x + 9.3
- P-value: 0.0004
- N samples: 183

**Is Open Source:**
- Correlation: 0.214 **
- Linear fit: y = 4.856x + 17.0
- P-value: 0.0043
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.213 **
- Linear fit: y = -4.831x + 21.9
- P-value: 0.0044
- N samples: 176

**Model Size (B):**
- Correlation: -0.141 
- Linear fit: y = -0.002x + 20.3
- P-value: 0.0606
- N samples: 179

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.123 
- Linear fit: y = -0.049x + 2.4
- P-value: 0.1036
- N samples: 176

**Model Size (B):**
- Correlation: -0.073 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.3315
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: -0.035 
- Linear fit: y = -0.001x + 1.0
- P-value: 0.6376
- N samples: 183

**Is Reasoning Model:**
- Correlation: 0.030 
- Linear fit: y = 0.186x + 0.6
- P-value: 0.6887
- N samples: 176

**Is Open Source:**
- Correlation: -0.027 
- Linear fit: y = -0.164x + 0.8
- P-value: 0.7248
- N samples: 176

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.758 ***
- Linear fit: y = -2.835x + 165.6
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.666 ***
- Linear fit: y = -37.916x + 85.0
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: -0.231 **
- Linear fit: y = -0.045x + 89.7
- P-value: 0.0017
- N samples: 183

**Is Open Source:**
- Correlation: 0.163 *
- Linear fit: y = 9.311x + 61.9
- P-value: 0.0304
- N samples: 176

**Model Size (B):**
- Correlation: -0.107 
- Linear fit: y = -0.003x + 68.9
- P-value: 0.1528
- N samples: 179

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.632 ***
- Linear fit: y = -0.579x + 29.5
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.473 ***
- Linear fit: y = -6.595x + 12.5
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.235 **
- Linear fit: y = 3.283x + 7.6
- P-value: 0.0017
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.222 **
- Linear fit: y = 0.011x + 3.9
- P-value: 0.0025
- N samples: 183

**Model Size (B):**
- Correlation: -0.140 
- Linear fit: y = -0.001x + 9.8
- P-value: 0.0618
- N samples: 179

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.344 ***
- Linear fit: y = -0.036x + 1.6
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.225 **
- Linear fit: y = 0.001x + -0.3
- P-value: 0.0022
- N samples: 183

**Is Reasoning Model:**
- Correlation: -0.179 *
- Linear fit: y = -0.287x + 0.5
- P-value: 0.0172
- N samples: 176

**Is Open Source:**
- Correlation: 0.179 *
- Linear fit: y = 0.287x + 0.2
- P-value: 0.0175
- N samples: 176

**Model Size (B):**
- Correlation: -0.056 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4549
- N samples: 179

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.616 ***
- Linear fit: y = -0.633x + 27.3
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.304 ***
- Linear fit: y = 4.768x + 2.7
- P-value: 0.0000
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.260 ***
- Linear fit: y = 0.014x + -1.9
- P-value: 0.0004
- N samples: 183

**Model Size (B):**
- Correlation: -0.158 *
- Linear fit: y = -0.001x + 5.8
- P-value: 0.0349
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.146 
- Linear fit: y = -2.285x + 6.4
- P-value: 0.0531
- N samples: 176

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.707 ***
- Linear fit: y = -0.680x + 34.1
- P-value: 0.0000
- N samples: 176

**Is Reasoning Model:**
- Correlation: -0.407 ***
- Linear fit: y = -5.957x + 13.3
- P-value: 0.0000
- N samples: 176

**Is Open Source:**
- Correlation: 0.245 **
- Linear fit: y = 3.594x + 8.5
- P-value: 0.0010
- N samples: 176

**Model Size (B):**
- Correlation: -0.189 *
- Linear fit: y = -0.002x + 11.0
- P-value: 0.0112
- N samples: 179

**Days Since 2024-01-01:**
- Correlation: 0.077 
- Linear fit: y = 0.004x + 8.4
- P-value: 0.3004
- N samples: 183

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.222 **
- Linear fit: y = -1.446x + 4.7
- P-value: 0.0030
- N samples: 176

**Model Size (B):**
- Correlation: 0.193 **
- Linear fit: y = 0.001x + 3.6
- P-value: 0.0095
- N samples: 179

**Is Reasoning Model:**
- Correlation: -0.185 *
- Linear fit: y = -1.199x + 4.5
- P-value: 0.0140
- N samples: 176

**Benchmark Score:**
- Correlation: -0.109 
- Linear fit: y = -0.047x + 5.6
- P-value: 0.1486
- N samples: 176

**Days Since 2024-01-01:**
- Correlation: 0.012 
- Linear fit: y = 0.000x + 3.7
- P-value: 0.8702
- N samples: 183

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**total_hallucinations vs Benchmark Score:**
  r = -0.807, y = -9.593x + 510.4

**category1_input_misalignment vs Benchmark Score:**
  r = -0.796, y = -2.487x + 129.4

**category3_logical_errors vs Benchmark Score:**
  r = -0.770, y = -3.451x + 196.7

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.758, y = -2.835x + 165.6

**1b_context_omission vs Benchmark Score:**
  r = -0.721, y = -1.605x + 87.0

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.707, y = -0.680x + 34.1

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.700, y = -0.399x + 18.1

**category4_technical_errors vs Benchmark Score:**
  r = -0.691, y = -1.359x + 67.0

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.666, y = -37.916x + 85.0

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.657, y = -44.798x + 98.0

**1a_instruction_override vs Benchmark Score:**
  r = -0.651, y = -0.483x + 24.3

**3b_self_contradiction vs Benchmark Score:**
  r = -0.632, y = -0.579x + 29.5

**4a_syntax_error vs Benchmark Score:**
  r = -0.616, y = -0.633x + 27.3

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.563, y = -26.759x + 55.7

**1b_context_omission vs Is Reasoning Model:**
  r = -0.559, y = -18.960x + 40.2

**total_hallucinations vs Is Reasoning Model:**
  r = -0.550, y = -99.570x + 224.1

**category2_factual_errors vs Benchmark Score:**
  r = -0.537, y = -1.514x + 81.2

**2a_concept_fabrication vs Benchmark Score:**
  r = -0.497, y = -0.762x + 34.8

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.473, y = -6.595x + 12.5

**2b_spurious_numeric vs Benchmark Score:**
  r = -0.472, y = -0.702x + 44.0

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.407, y = -5.957x + 13.3

**1c_prompt_contradiction vs Is Reasoning Model:**
  r = -0.392, y = -3.396x + 5.8

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.390, y = -4.403x + 9.6

**1b_context_omission vs Days Since 2024-01-01:**
  r = -0.390, y = -0.046x + 54.5

**1c_prompt_contradiction vs Is Open Source:**
  r = 0.346, y = 3.007x + 2.6

**3c_circular_reasoning vs Benchmark Score:**
  r = -0.344, y = -0.036x + 1.6

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.315, y = -9.442x + 24.2

**2a_concept_fabrication vs Days Since 2024-01-01:**
  r = 0.309, y = 0.025x + -4.3

**4a_syntax_error vs Is Open Source:**
  r = 0.304, y = 4.768x + 2.7


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
- Correlation: 0.820 ***
- Linear fit: y = 1.168x + 26.4

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.646 ***
- Linear fit: y = 0.406x + 2.0

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
  r = 0.949 ***, y = 0.680x + 2.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.900 ***, y = 0.439x + 1.8

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.890 ***, y = 0.483x + -5.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.884 ***, y = 0.467x + 6.2

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.879 ***, y = 0.457x + -3.7

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.820 ***, y = 1.168x + 26.4

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.806 ***, y = 0.165x + -3.3

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.806 ***, y = 0.961x + 25.6

**1c: Prompt Contradiction vs 3b: Self Contradiction:**
  r = 0.791 ***, y = 1.271x + 4.1

**2a: Concept Fabrication vs 3b: Self Contradiction:**
  r = 0.784 ***, y = 0.470x + 5.5

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.781 ***, y = 0.185x + -0.5

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.780 ***, y = 1.298x + 26.3

**Category 4: Technical Errors vs 3b: Self Contradiction:**
  r = 0.779 ***, y = 0.361x + 2.3

**Category 2: Factual Errors vs 3b: Self Contradiction:**
  r = 0.770 ***, y = 0.250x + 2.3

**1c: Prompt Contradiction vs 2a: Concept Fabrication:**
  r = 0.769 ***, y = 2.063x + -0.4

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.763 ***, y = 0.384x + 1.9

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.746 ***, y = 0.572x + -0.1

**2a: Concept Fabrication vs 4a: Syntax Error:**
  r = 0.745 ***, y = 0.500x + 1.1

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.743 ***, y = 0.135x + -1.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
