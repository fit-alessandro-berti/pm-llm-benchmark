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
- Correlation: -0.189 *
- Linear fit: y = -0.036x + 1.3
- P-value: 0.0168
- N samples: 159

**Model Size (B):**
- Correlation: 0.020 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.8117
- N samples: 139

**Is Reasoning Model:**
- Correlation: 0.018 
- Linear fit: y = 0.034x + 0.2
- P-value: 0.8227
- N samples: 159

**Is Open Source:**
- Correlation: 0.010 
- Linear fit: y = 0.018x + 0.2
- P-value: 0.9031
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: 0.002 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.9799
- N samples: 159

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.137 
- Linear fit: y = -0.000x + 2.6
- P-value: 0.1086
- N samples: 139

**Benchmark Score:**
- Correlation: -0.091 
- Linear fit: y = -0.048x + 3.8
- P-value: 0.2560
- N samples: 159

**Is Reasoning Model:**
- Correlation: 0.031 
- Linear fit: y = 0.166x + 2.3
- P-value: 0.6980
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.031 
- Linear fit: y = -0.000x + 2.7
- P-value: 0.6989
- N samples: 159

**Is Open Source:**
- Correlation: 0.013 
- Linear fit: y = 0.069x + 2.3
- P-value: 0.8711
- N samples: 159

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.166 *
- Linear fit: y = -0.003x + 7.5
- P-value: 0.0365
- N samples: 159

**Benchmark Score:**
- Correlation: -0.122 
- Linear fit: y = -0.088x + 7.9
- P-value: 0.1261
- N samples: 159

**Is Reasoning Model:**
- Correlation: -0.084 
- Linear fit: y = -0.605x + 5.6
- P-value: 0.2938
- N samples: 159

**Model Size (B):**
- Correlation: -0.037 
- Linear fit: y = -0.000x + 5.4
- P-value: 0.6693
- N samples: 139

**Is Open Source:**
- Correlation: 0.015 
- Linear fit: y = 0.108x + 5.2
- P-value: 0.8519
- N samples: 159

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.105 
- Linear fit: y = -0.331x + 0.8
- P-value: 0.1884
- N samples: 159

**Is Reasoning Model:**
- Correlation: 0.088 
- Linear fit: y = 0.279x + 0.5
- P-value: 0.2685
- N samples: 159

**Benchmark Score:**
- Correlation: -0.063 
- Linear fit: y = -0.020x + 1.2
- P-value: 0.4321
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.062 
- Linear fit: y = -0.001x + 1.0
- P-value: 0.4379
- N samples: 159

**Model Size (B):**
- Correlation: -0.005 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.9569
- N samples: 139

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.164 *
- Linear fit: y = -0.190x + 14.2
- P-value: 0.0389
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.134 
- Linear fit: y = -0.004x + 11.5
- P-value: 0.0910
- N samples: 159

**Model Size (B):**
- Correlation: -0.079 
- Linear fit: y = -0.000x + 9.0
- P-value: 0.3574
- N samples: 139

**Is Open Source:**
- Correlation: -0.013 
- Linear fit: y = -0.156x + 8.5
- P-value: 0.8662
- N samples: 159

**Is Reasoning Model:**
- Correlation: -0.009 
- Linear fit: y = -0.105x + 8.5
- P-value: 0.9099
- N samples: 159

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.189 *
- Linear fit: y = -0.036x + 1.3
- P-value: 0.0168
- N samples: 159

**Model Size (B):**
- Correlation: 0.020 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.8117
- N samples: 139

**Is Reasoning Model:**
- Correlation: 0.018 
- Linear fit: y = 0.034x + 0.2
- P-value: 0.8227
- N samples: 159

**Is Open Source:**
- Correlation: 0.010 
- Linear fit: y = 0.018x + 0.2
- P-value: 0.9031
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: 0.002 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.9799
- N samples: 159

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.137 
- Linear fit: y = -0.000x + 2.6
- P-value: 0.1086
- N samples: 139

**Benchmark Score:**
- Correlation: -0.091 
- Linear fit: y = -0.048x + 3.8
- P-value: 0.2560
- N samples: 159

**Is Reasoning Model:**
- Correlation: 0.031 
- Linear fit: y = 0.166x + 2.3
- P-value: 0.6980
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.031 
- Linear fit: y = -0.000x + 2.7
- P-value: 0.6989
- N samples: 159

**Is Open Source:**
- Correlation: 0.013 
- Linear fit: y = 0.069x + 2.3
- P-value: 0.8711
- N samples: 159

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.166 *
- Linear fit: y = -0.003x + 7.5
- P-value: 0.0365
- N samples: 159

**Benchmark Score:**
- Correlation: -0.122 
- Linear fit: y = -0.088x + 7.9
- P-value: 0.1261
- N samples: 159

**Is Reasoning Model:**
- Correlation: -0.084 
- Linear fit: y = -0.605x + 5.6
- P-value: 0.2938
- N samples: 159

**Model Size (B):**
- Correlation: -0.037 
- Linear fit: y = -0.000x + 5.4
- P-value: 0.6693
- N samples: 139

**Is Open Source:**
- Correlation: 0.015 
- Linear fit: y = 0.108x + 5.2
- P-value: 0.8519
- N samples: 159

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.105 
- Linear fit: y = -0.331x + 0.8
- P-value: 0.1884
- N samples: 159

**Is Reasoning Model:**
- Correlation: 0.088 
- Linear fit: y = 0.279x + 0.5
- P-value: 0.2685
- N samples: 159

**Benchmark Score:**
- Correlation: -0.063 
- Linear fit: y = -0.020x + 1.2
- P-value: 0.4321
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.062 
- Linear fit: y = -0.001x + 1.0
- P-value: 0.4379
- N samples: 159

**Model Size (B):**
- Correlation: -0.005 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.9569
- N samples: 139

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.163 *
- Linear fit: y = -0.000x + 0.1
- P-value: 0.0404
- N samples: 159

**Benchmark Score:**
- Correlation: -0.094 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.2387
- N samples: 159

**Model Size (B):**
- Correlation: -0.054 
- Linear fit: y = -0.000x + 0.0
- P-value: 0.5289
- N samples: 139

**Is Open Source:**
- Correlation: 0.022 
- Linear fit: y = 0.005x + 0.0
- P-value: 0.7789
- N samples: 159

**Is Reasoning Model:**
- Correlation: -0.022 
- Linear fit: y = -0.005x + 0.0
- P-value: 0.7789
- N samples: 159

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.201 *
- Linear fit: y = -0.035x + 1.3
- P-value: 0.0109
- N samples: 159

**Is Open Source:**
- Correlation: 0.020 
- Linear fit: y = 0.034x + 0.2
- P-value: 0.8072
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: 0.014 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.8652
- N samples: 159

**Model Size (B):**
- Correlation: 0.012 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.8877
- N samples: 139

**Is Reasoning Model:**
- Correlation: 0.010 
- Linear fit: y = 0.018x + 0.2
- P-value: 0.8987
- N samples: 159

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.080 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.3495
- N samples: 139

**Is Reasoning Model:**
- Correlation: 0.065 
- Linear fit: y = 0.021x + 0.0
- P-value: 0.4135
- N samples: 159

**Is Open Source:**
- Correlation: -0.065 
- Linear fit: y = -0.021x + 0.0
- P-value: 0.4135
- N samples: 159

**Benchmark Score:**
- Correlation: 0.055 
- Linear fit: y = 0.002x + -0.0
- P-value: 0.4891
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: 0.052 
- Linear fit: y = 0.000x + -0.0
- P-value: 0.5124
- N samples: 159

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.187 *
- Linear fit: y = -0.017x + 0.7
- P-value: 0.0183
- N samples: 159

**Is Reasoning Model:**
- Correlation: -0.153 
- Linear fit: y = -0.139x + 0.3
- P-value: 0.0542
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.071 
- Linear fit: y = -0.000x + 0.3
- P-value: 0.3723
- N samples: 159

**Model Size (B):**
- Correlation: 0.016 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.8526
- N samples: 139

**Is Open Source:**
- Correlation: 0.009 
- Linear fit: y = 0.009x + 0.2
- P-value: 0.9065
- N samples: 159

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.000x + 2.4
- P-value: 0.1040
- N samples: 139

**Benchmark Score:**
- Correlation: -0.063 
- Linear fit: y = -0.032x + 3.1
- P-value: 0.4316
- N samples: 159

**Is Reasoning Model:**
- Correlation: 0.062 
- Linear fit: y = 0.321x + 2.0
- P-value: 0.4379
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.025 
- Linear fit: y = -0.000x + 2.4
- P-value: 0.7527
- N samples: 159

**Is Open Source:**
- Correlation: 0.024 
- Linear fit: y = 0.124x + 2.1
- P-value: 0.7643
- N samples: 159

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.140 
- Linear fit: y = -0.063x + 0.1
- P-value: 0.0782
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: 0.066 
- Linear fit: y = 0.000x + -0.0
- P-value: 0.4085
- N samples: 159

**Model Size (B):**
- Correlation: -0.054 
- Linear fit: y = -0.000x + 0.0
- P-value: 0.5260
- N samples: 139

**Is Reasoning Model:**
- Correlation: -0.034 
- Linear fit: y = -0.015x + 0.0
- P-value: 0.6712
- N samples: 159

**Benchmark Score:**
- Correlation: 0.023 
- Linear fit: y = 0.001x + 0.0
- P-value: 0.7739
- N samples: 159

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.161 *
- Linear fit: y = -0.003x + 6.7
- P-value: 0.0427
- N samples: 159

**Benchmark Score:**
- Correlation: -0.140 
- Linear fit: y = -0.096x + 7.5
- P-value: 0.0779
- N samples: 159

**Is Reasoning Model:**
- Correlation: -0.066 
- Linear fit: y = -0.449x + 4.9
- P-value: 0.4103
- N samples: 159

**Model Size (B):**
- Correlation: -0.036 
- Linear fit: y = -0.000x + 4.8
- P-value: 0.6728
- N samples: 139

**Is Open Source:**
- Correlation: 0.035 
- Linear fit: y = 0.240x + 4.5
- P-value: 0.6605
- N samples: 159

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.091 
- Linear fit: y = -0.156x + 0.7
- P-value: 0.2535
- N samples: 159

**Is Open Source:**
- Correlation: -0.077 
- Linear fit: y = -0.132x + 0.7
- P-value: 0.3338
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.058 
- Linear fit: y = -0.000x + 0.8
- P-value: 0.4654
- N samples: 159

**Benchmark Score:**
- Correlation: 0.046 
- Linear fit: y = 0.008x + 0.4
- P-value: 0.5659
- N samples: 159

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 0.6
- P-value: 0.9016
- N samples: 139

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: nan 
- Linear fit: y = 0.000x + 0.0
- P-value: nan
- N samples: 139

**Is Open Source:**
- Correlation: nan 
- Linear fit: y = 0.000x + 0.0
- P-value: nan
- N samples: 159

**Is Reasoning Model:**
- Correlation: nan 
- Linear fit: y = 0.000x + 0.0
- P-value: nan
- N samples: 159

**Benchmark Score:**
- Correlation: nan 
- Linear fit: y = 0.000x + 0.0
- P-value: nan
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: nan 
- Linear fit: y = 0.000x + 0.0
- P-value: nan
- N samples: 159

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.136 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.0869
- N samples: 159

**Is Reasoning Model:**
- Correlation: -0.073 
- Linear fit: y = -0.026x + 0.0
- P-value: 0.3634
- N samples: 159

**Benchmark Score:**
- Correlation: -0.072 
- Linear fit: y = -0.003x + 0.1
- P-value: 0.3704
- N samples: 159

**Model Size (B):**
- Correlation: -0.035 
- Linear fit: y = -0.000x + 0.0
- P-value: 0.6853
- N samples: 139

**Is Open Source:**
- Correlation: -0.001 
- Linear fit: y = -0.000x + 0.0
- P-value: 0.9908
- N samples: 159

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.121 
- Linear fit: y = -0.021x + 1.0
- P-value: 0.1285
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.034 
- Linear fit: y = -0.000x + 0.5
- P-value: 0.6687
- N samples: 159

**Is Reasoning Model:**
- Correlation: 0.032 
- Linear fit: y = 0.057x + 0.4
- P-value: 0.6849
- N samples: 159

**Model Size (B):**
- Correlation: 0.020 
- Linear fit: y = 0.000x + 0.4
- P-value: 0.8197
- N samples: 139

**Is Open Source:**
- Correlation: -0.002 
- Linear fit: y = -0.004x + 0.4
- P-value: 0.9755
- N samples: 159

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.144 
- Linear fit: y = -0.326x + 0.3
- P-value: 0.0706
- N samples: 159

**Is Reasoning Model:**
- Correlation: 0.109 
- Linear fit: y = 0.248x + 0.0
- P-value: 0.1706
- N samples: 159

**Days Since 2024-01-01:**
- Correlation: -0.039 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.6299
- N samples: 159

**Benchmark Score:**
- Correlation: 0.017 
- Linear fit: y = 0.004x + 0.1
- P-value: 0.8309
- N samples: 159

**Model Size (B):**
- Correlation: -0.016 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.8544
- N samples: 139

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------

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
- Correlation: 0.098 
- Linear fit: y = 0.270x + 2.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.061 
- Linear fit: y = 0.235x + 5.1

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.288 ***
- Linear fit: y = 0.476x + 0.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.305 ***
- Linear fit: y = 0.428x + 4.1

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.110 
- Linear fit: y = 0.066x + 0.5

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.095 
- Linear fit: y = 0.041x + 0.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.981 ***, y = 0.952x + -0.1

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.978 ***, y = 0.916x + -0.0

**Category 4: Technical Errors vs 4c: Visual Descr Mismatch:**
  r = 0.787 ***, y = 0.542x + -0.2

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.730 ***, y = 0.444x + 0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.373 ***, y = 0.067x + 0.0

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.974 ***, y = 0.915x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.375 ***, y = 0.085x + 0.1

**Category 4: Technical Errors vs 1b: Context Omission:**
  r = 0.317 ***, y = 0.180x + 0.1

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.307 ***, y = 0.405x + 3.6

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.305 ***, y = 0.428x + 4.1

**1a: Instruction Override vs 4a: Syntax Error:**
  r = 0.304 ***, y = 0.476x + 0.0

**1b: Context Omission vs 4b: Model Semantics Breach:**
  r = 0.333 ***, y = 0.358x + 0.4

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
