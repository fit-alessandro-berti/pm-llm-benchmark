A score in the range **22-26** is considered **sufficient**; a score in the range **26-30** is considered **fair**; a score in the range **30-34** is considered **good**; and a score **>34** is considered **excellent**.

**Update**: Since **19-04-2025**, a normalization step is applied to the score.

## Open-Source Leaderboard (1-shot; gemini-2.5-pro-preview-03-25 used as a judge)

| Model                            | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:---------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| nemotron-ultra-253b-v1-thinkenab | **33.3** | :white_check_mark: | :white_check_mark: | :mage_woman: **6.0** | 6.8                  | 5.3                  | 4.5                  | :mage_woman: **5.1** | **5.6**              | 0.0                  |
| qwen-qwq-32b-nostepbystep        | **33.2** | :white_check_mark: | :white_check_mark: | **5.7**              | 6.4                  | :mage_woman: **6.0** | 4.5                  | **4.9**              | :mage_woman: **5.7** | 0.0                  |
| DeepSeek-R1                      | **33.0** | :white_check_mark: | :white_check_mark: | **5.9**              | :mage_woman: **7.4** | 4.7                  | :mage_woman: **5.2** | 4.7                  | 5.1                  | 0.0                  |
| nemotron-super-49b-v1-thinkenab  | **32.5** | :white_check_mark: | :white_check_mark: | 5.0                  | **7.3**              | :mage_woman: **6.0** | 4.8                  | 4.4                  | 5.0                  | 0.0                  |
| qwen-qwq-32b-stepbystep          | **31.9** | :white_check_mark: | :white_check_mark: | 5.6                  | 6.7                  | 4.3                  | 4.6                  | :mage_woman: **5.1** | **5.6**              | 0.0                  |
| DeepSeek-V3-0324                 | **28.9** | :white_check_mark: | :x:                | 5.5                  | 6.2                  | 3.7                  | 4.5                  | 4.5                  | 4.5                  | 0.0                  |
| DeepSeek-R1-Dynamic-Quant        | **28.8** | :white_check_mark: | :white_check_mark: | 5.0                  | 6.9                  | 3.5                  | 4.4                  | **4.9**              | 4.1                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-32B     | **28.2** | :white_check_mark: | :white_check_mark: | 5.0                  | 6.9                  | 3.5                  | 3.6                  | 4.5                  | 4.8                  | 0.0                  |
| r1-1776                          | **28.2** | :white_check_mark: | :white_check_mark: | 4.4                  | **7.2**              | 2.4                  | 4.8                  | **4.8**              | 4.6                  | 0.0                  |
| exaone-deep32b-fp16              | **28.1** | :white_check_mark: | :white_check_mark: | 5.4                  | 6.1                  | 3.5                  | 4.3                  | 4.0                  | 4.8                  | 0.0                  |
| nemotron-70b-instruct            | **26.9** | :white_check_mark: | :x:                | 4.4                  | 5.5                  | 3.5                  | 4.3                  | 4.4                  | 4.8                  | 0.0                  |
| exaone-deep7.8b-fp16             | **26.6** | :white_check_mark: | :white_check_mark: | 4.8                  | 6.4                  | 2.6                  | 3.6                  | 4.3                  | 4.8                  | 0.0                  |
| DeepSeek-V3                      | **26.4** | :white_check_mark: | :x:                | 4.3                  | 5.5                  | 2.8                  | 4.3                  | **5.0**              | 4.5                  | 0.0                  |
| DeepSeek-R1-Distill-Llama-70B    | **26.3** | :white_check_mark: | :white_check_mark: | 4.7                  | 6.1                  | 2.7                  | 4.3                  | 4.0                  | 4.5                  | 0.0                  |
| DeepSeek-R1-Zero                 | **26.3** | :white_check_mark: | :white_check_mark: | 5.0                  | 4.7                  | 3.5                  | 4.0                  | **5.0**              | 4.1                  | 0.0                  |
| QwQ-32B-Preview                  | **26.1** | :white_check_mark: | :white_check_mark: | 4.8                  | 6.2                  | 3.1                  | 3.4                  | **4.9**              | 3.8                  | 0.0                  |
| nemotron-super-49b-v1            | **26.0** | :white_check_mark: | :x:                | 3.6                  | 5.5                  | 3.1                  | 4.5                  | **4.8**              | 4.5                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-14B     | **25.9** | :white_check_mark: | :white_check_mark: | 4.5                  | 6.9                  | 3.8                  | 3.0                  | 3.8                  | 3.9                  | 0.0                  |
| Llama-3.3-70B-Instruct           | **25.6** | :white_check_mark: | :x:                | 4.6                  | 5.4                  | 2.7                  | 4.3                  | 4.2                  | 4.4                  | 0.0                  |
| qwen2.5-72b-instruct             | **25.4** | :white_check_mark: | :x:                | 4.5                  | 5.7                  | 2.9                  | 4.1                  | 3.7                  | 4.7                  | 0.0                  |
| pixtral-large-2411               | **25.2** | :white_check_mark: | :x:                | 5.0                  | 5.0                  | 3.1                  | 3.8                  | 4.2                  | 4.0                  | :mage_woman: **4.6** |
| llama-4-maverick                 | **24.5** | :white_check_mark: | :x:                | 4.3                  | 5.3                  | 2.9                  | 3.6                  | **4.9**              | 3.6                  | 3.7                  |
| mistral-large-2411               | **24.1** | :white_check_mark: | :x:                | 4.0                  | 5.1                  | 2.8                  | 3.6                  | 4.2                  | 4.4                  | 0.0                  |
| mistral-small-2503               | **23.9** | :white_check_mark: | :x:                | 3.1                  | 4.9                  | 2.4                  | 4.3                  | 4.5                  | 4.7                  | 3.6                  |
| WizardLM-2-8x22B                 | **23.7** | :white_check_mark: | :x:                | 3.8                  | 4.7                  | 2.5                  | 3.9                  | 4.7                  | 4.3                  | 0.0                  |
| mistral-small-2501               | **23.5** | :white_check_mark: | :x:                | 3.9                  | 4.8                  | 3.2                  | 3.2                  | 4.3                  | 4.1                  | 0.0                  |
| phi-4                            | **23.4** | :white_check_mark: | :x:                | 4.0                  | 5.0                  | 3.1                  | 3.2                  | 4.0                  | 4.0                  | 0.0                  |
| open-mixtral-8x22b               | **23.3** | :white_check_mark: | :x:                | 4.3                  | 4.8                  | 1.9                  | 3.9                  | 4.2                  | 4.2                  | 0.0                  |
| Qwen2.5-Coder-32B-Instruct       | **23.2** | :white_check_mark: | :x:                | 3.8                  | 4.5                  | 3.1                  | 3.7                  | 4.1                  | 4.0                  | 0.0                  |
| gemma327b-it-q8_0                | **23.1** | :white_check_mark: | :x:                | 4.1                  | 4.4                  | 1.8                  | 3.4                  | 4.7                  | 4.7                  | 2.1                  |
| qwen2.5-32b-instruct             | **23.0** | :white_check_mark: | :x:                | 4.1                  | 5.0                  | 2.0                  | 3.3                  | 4.4                  | 4.1                  | 0.0                  |
| cogito14b-v1-preview-qwen-fp16   | **22.8** | :white_check_mark: | :white_check_mark: | 4.4                  | 4.1                  | 2.7                  | 3.4                  | 3.7                  | 4.5                  | 0.0                  |
| MiniMax-01                       | **21.8** | :white_check_mark: | :x:                | 3.4                  | 4.7                  | 2.5                  | 2.8                  | 4.4                  | 4.0                  | 0.0                  |
| codestral-2501                   | **21.7** | :white_check_mark: | :x:                | 4.0                  | 4.5                  | 2.2                  | 3.4                  | 4.0                  | 3.6                  | 0.0                  |
| gemma312b-it-q8_0                | **21.6** | :white_check_mark: | :x:                | 3.8                  | 3.6                  | 1.9                  | 3.3                  | 4.4                  | 4.6                  | 2.8                  |
| qwen2.5-14b-instruct             | **21.6** | :white_check_mark: | :x:                | 3.4                  | 4.7                  | 2.4                  | 3.0                  | 4.2                  | 4.0                  | 0.0                  |
| Llama-3.2-90B-Vision-Instruct    | **21.4** | :white_check_mark: | :x:                | 3.9                  | 4.2                  | 2.5                  | 3.5                  | 4.2                  | 3.0                  | 2.5                  |
| qwen2.5-14b-instruct-1m          | **21.4** | :white_check_mark: | :x:                | 3.6                  | 4.5                  | 1.7                  | 3.6                  | 4.3                  | 3.7                  | 0.0                  |
| falcon310b-instruct-q8_0         | **21.2** | :white_check_mark: | :x:                | 3.5                  | 4.7                  | 1.9                  | 3.1                  | 4.1                  | 3.8                  | 0.0                  |
| llama-4-scout                    | **20.9** | :white_check_mark: | :x:                | 3.0                  | 3.9                  | 2.8                  | 3.6                  | 4.3                  | 3.3                  | 3.2                  |
| googlegemma-2-9b-it              | **20.6** | :white_check_mark: | :x:                | 3.2                  | 3.5                  | 2.8                  | 3.3                  | 4.4                  | 3.4                  | 0.0                  |
| pixtral-12b-2409                 | **20.4** | :white_check_mark: | :x:                | 2.8                  | 4.3                  | 2.5                  | 3.1                  | 4.0                  | 3.6                  | 4.0                  |
| exaone-deep2.4b-fp16             | **20.1** | :white_check_mark: | :white_check_mark: | 3.7                  | 5.3                  | 1.8                  | 2.9                  | 3.2                  | 3.2                  | 0.0                  |
| falcon37b-instruct-q8_0          | **20.1** | :white_check_mark: | :x:                | 3.0                  | 4.0                  | 2.6                  | 3.0                  | 4.2                  | 3.1                  | 0.0                  |
| DeepSeek-R1-Distill-Llama-8B     | **19.1** | :white_check_mark: | :white_check_mark: | 2.6                  | 4.1                  | 1.9                  | 2.5                  | 4.1                  | 4.0                  | 0.0                  |
| qwen2.5-omni-7b                  | **18.7** | :white_check_mark: | :x:                | 3.2                  | 3.5                  | 1.9                  | 3.0                  | 3.8                  | 3.1                  | 2.2                  |
| qwen2.5-7b-instruct              | **18.6** | :white_check_mark: | :x:                | 3.1                  | 3.5                  | 2.1                  | 3.2                  | 3.6                  | 3.0                  | 0.0                  |
| granite3.28b-instruct-q4_K_M     | **17.5** | :white_check_mark: | :x:                | 2.7                  | 3.0                  | 1.7                  | 3.0                  | 4.0                  | 3.0                  | 0.0                  |
| qwen2.5-7b-instruct-1m           | **17.0** | :white_check_mark: | :x:                | 3.0                  | 3.0                  | 1.9                  | 2.5                  | 3.5                  | 3.0                  | 0.0                  |
| gemma34b-it-q8_0                 | **16.7** | :white_check_mark: | :x:                | 2.2                  | 3.3                  | 1.3                  | 2.8                  | 4.1                  | 3.1                  | 2.0                  |
| command-r7b7b-12-2024-q4_K_M     | **16.6** | :white_check_mark: | :x:                | 2.5                  | 3.0                  | 1.9                  | 2.5                  | 3.4                  | 3.3                  | 0.0                  |
| Llama-3.1-8B-Instruct            | **16.1** | :white_check_mark: | :x:                | 2.4                  | 2.8                  | 1.6                  | 2.3                  | 4.3                  | 2.8                  | 0.0                  |
| falcon33b-instruct-q8_0          | **15.4** | :white_check_mark: | :x:                | 2.5                  | 3.2                  | 1.6                  | 2.2                  | 3.0                  | 2.8                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-7B      | **15.1** | :white_check_mark: | :white_check_mark: | 1.8                  | 2.9                  | 2.4                  | 2.2                  | 3.1                  | 2.8                  | 0.0                  |
| Phi-4-multimodal-instruct        | **14.9** | :white_check_mark: | :x:                | 2.1                  | 3.0                  | 1.2                  | 2.5                  | 3.3                  | 2.9                  | 2.7                  |
| Llama-3.2-11B-Vision-Instruct    | **14.8** | :white_check_mark: | :x:                | 2.8                  | 3.0                  | 1.9                  | 2.0                  | 3.0                  | 2.0                  | 2.1                  |
| olmo27b-1124-instruct-q8_0       | **14.4** | :white_check_mark: | :x:                | 2.2                  | 3.0                  | 1.4                  | 2.0                  | 3.0                  | 2.8                  | 0.0                  |
| Llama-3.2-3B-Instruct            | **14.1** | :white_check_mark: | :x:                | 2.4                  | 2.7                  | 1.3                  | 2.1                  | 3.4                  | 2.1                  | 0.0                  |
| qwen2.53b-instruct-q8_0          | **14.0** | :white_check_mark: | :x:                | 2.1                  | 2.1                  | 1.6                  | 2.1                  | 3.3                  | 2.7                  | 0.0                  |
| qwen2.51.5b-instruct-q6_K        | **11.2** | :white_check_mark: | :x:                | 2.2                  | 1.8                  | 1.1                  | 1.6                  | 2.8                  | 1.7                  | 0.0                  |
| gemma31b-it-q8_0                 | **10.7** | :white_check_mark: | :x:                | 1.1                  | 1.9                  | 1.0                  | 1.4                  | 3.2                  | 2.0                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-1.5B    | **9.1**  | :white_check_mark: | :white_check_mark: | 1.3                  | 1.6                  | 0.9                  | 1.0                  | 2.7                  | 1.6                  | 0.0                  |
| Llama-3.2-1B-Instruct            | **8.9**  | :white_check_mark: | :x:                | 1.3                  | 1.7                  | 0.8                  | 1.1                  | 2.4                  | 1.6                  | 0.0                  |

### nvidiallama-3.1-nemotron-ultra-253b-v1-thinkenab   => 33.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.4 |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     7.4 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     7.4 |
| cat02_08_underfitting_process_tree |     7.1 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |     9.1 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     7.4 |
| cat03_06_petri_net_generation      |     4.8 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     7.4 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     4.8 |
| cat04_05_sql_filt_num_events       |     9.1 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     9.1 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     9.1 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     9.1 |



### qwen-qwq-32b-nostepbystep   => 33.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.1 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     7.4 |
| cat01_05_merge_two_logs            |     6.8 |
| cat01_06_system_logs               |     7.7 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     7.4 |
| cat02_01_conformance_textual       |     7.4 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     5.4 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     7.4 |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     7.4 |
| cat03_01_process_tree_generation   |     7.1 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6.8 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     9.1 |
| cat03_08_powl_discovery            |     7.4 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     1.4 |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     9.1 |
| cat04_07_sql_filt_top_k_vars       |     9.1 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     9.1 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     9.1 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     9.1 |
| cat06_06_bias_mitigation_declare   |     7.4 |
| cat06_07_fair_unfair_powl          |     6.6 |



### deepseek-aiDeepSeek-R1   => 33.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.4 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     9.1 |
| cat01_04_sensor_recordings         |     6.8 |
| cat01_05_merge_two_logs            |     9.1 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     9.1 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     9.1 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     7.6 |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |    10.6 |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     7.6 |
| cat03_07_process_tree_discovery    |     6.6 |
| cat03_08_powl_discovery            |     4.8 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |     9.1 |
| cat04_06_sql_filt_three_df         |     9.1 |
| cat04_07_sql_filt_top_k_vars       |     7.4 |
| cat05_01_hyp_generation_log        |     4.9 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     9.1 |
| cat06_03_bias_powl                 |     6.8 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     7.4 |



### nvidiallama-3.3-nemotron-super-49b-v1-thinkenab   => 32.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10.6 |
| cat01_02_activity_context          |     4.8 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     9.1 |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     3.7 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     9.1 |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |     6.6 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     6.8 |
| cat03_06_petri_net_generation      |     9.1 |
| cat03_07_process_tree_discovery    |     9.1 |
| cat03_08_powl_discovery            |     9.1 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     7.7 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |    10.6 |
| cat04_06_sql_filt_three_df         |     7.4 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     8.3 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     6.6 |



### qwen-qwq-32b-stepbystep   => 31.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     9.1 |
| cat01_04_sensor_recordings         |     7.4 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     7.7 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     7.1 |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     7.6 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |     7.1 |
| cat03_02_powl_generation           |     7.7 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     7.1 |
| cat03_05_temp_profile_generation   |     7.1 |
| cat03_06_petri_net_generation      |     6.6 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |    10.6 |
| cat05_01_hyp_generation_log        |     6.8 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     6.8 |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     9.1 |
| cat06_06_bias_mitigation_declare   |     7.4 |
| cat06_07_fair_unfair_powl          |     7.4 |



### deepseek-aiDeepSeek-V3-0324   => 28.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.5  |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    7.75 |
| cat01_04_sensor_recordings         |    7.75 |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    5.5  |
| cat01_08_tables_to_log             |    7.9  |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    9.25 |
| cat02_04_powl_anomaly_detection    |    7.25 |
| cat02_05_two_powls_anomalies       |    7    |
| cat02_06_root_cause_1              |    8    |
| cat02_07_root_cause_2              |    7.5  |
| cat02_08_underfitting_process_tree |    3.5  |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    6.5  |
| cat03_02_powl_generation           |    7.75 |
| cat03_03_log_skeleton_generation   |    3.5  |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    6.5  |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    8    |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    7.75 |
| cat04_06_sql_filt_three_df         |    8    |
| cat04_07_sql_filt_top_k_vars       |    8    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    5.5  |
| cat05_05_question_gen_nlp          |    7.5  |
| cat05_06_question_pseudo_bpmn      |    8    |
| cat05_07_question_interview        |    8.5  |
| cat06_01_bias_text                 |    8.5  |
| cat06_02_bias_event_log            |    7.5  |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    6.5  |



### DeepSeek-R1-Dynamic-Quant   => 28.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     7.4 |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |     5.4 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     4.8 |
| cat03_04_declare_generation        |     4.2 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     4.2 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     9.1 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     9.1 |
| cat04_07_sql_filt_top_k_vars       |     6.3 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     7.4 |
| cat06_01_bias_text                 |     7.4 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     3.1 |
| cat06_06_bias_mitigation_declare   |     4.8 |
| cat06_07_fair_unfair_powl          |     6   |



### deepseek-aiDeepSeek-R1-Distill-Qwen-32B   => 28.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.1 |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     7.4 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     9.1 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     9.1 |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     7.7 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     7.4 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     5.4 |
| cat04_07_sql_filt_top_k_vars       |     7.4 |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     5.4 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     5.4 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     6.8 |
| cat06_07_fair_unfair_powl          |     7.4 |



### r1-1776   => 28.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.6 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     7.3 |
| cat01_04_sensor_recordings         |     6.8 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     7.7 |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     7.7 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     9.1 |
| cat04_07_sql_filt_top_k_vars       |     7.1 |
| cat05_01_hyp_generation_log        |     3.7 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     9.1 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     9.1 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     4.8 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     7.4 |



### exaone-deep32b-fp16   => 28.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     7.4 |
| cat01_05_merge_two_logs            |     9.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     7.4 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     7.1 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     6   |
| cat03_03_log_skeleton_generation   |     7.4 |
| cat03_04_declare_generation        |     1.4 |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     6.8 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     7.6 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     9.1 |
| cat04_07_sql_filt_top_k_vars       |     4.8 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     7.1 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     7.4 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     7.1 |
| cat06_07_fair_unfair_powl          |     3.7 |



### nvidiaLlama-3.1-Nemotron-70B-Instruct   => 26.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    5    |
| cat01_03_high_level_events         |    7.75 |
| cat01_04_sensor_recordings         |    7    |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    7.25 |
| cat02_03_anomaly_event_log         |    8    |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    6.5  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    9.25 |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    7.4  |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2.5  |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    6    |
| cat04_04_declare_description       |    4.5  |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    9.25 |
| cat05_01_hyp_generation_log        |    4.5  |
| cat05_02_hyp_gen_powl              |    6.5  |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    7.9  |
| cat05_06_question_pseudo_bpmn      |    8.5  |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    5.5  |
| cat06_03_bias_powl                 |    8.5  |
| cat06_04_bias_two_logs             |    7.25 |
| cat06_05_bias_two_logs_2           |    7.6  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    7    |



### exaone-deep7.8b-fp16   => 26.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |     1.4 |
| cat03_02_powl_generation           |     3.1 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     7.1 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     4.2 |
| cat03_08_powl_discovery            |     4.8 |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     3.1 |
| cat04_07_sql_filt_top_k_vars       |     7.1 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     4.8 |
| cat05_05_question_gen_nlp          |     6.8 |
| cat05_06_question_pseudo_bpmn      |     6.8 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     4.2 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     9.1 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     6.6 |



### deepseek-aiDeepSeek-V3   => 26.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7    |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    7.5  |
| cat02_01_conformance_textual       |    7.25 |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    7.75 |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    7.75 |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    7.9  |
| cat03_01_process_tree_generation   |    3.5  |
| cat03_02_powl_generation           |    5    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    4.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    7.25 |
| cat04_02_pseudo_bpmn_open_question |    7    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |   10    |
| cat04_07_sql_filt_top_k_vars       |    3.5  |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    7.5  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    9.25 |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    7.5  |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    6.3  |
| cat06_05_bias_two_logs_2           |    7    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    6    |



### deepseek-aiDeepSeek-R1-Distill-Llama-70B   => 26.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.1 |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     1.4 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     6.6 |
| cat02_08_underfitting_process_tree |     6.6 |
| cat02_09_fix_process_tree          |     7.4 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     5.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     6.8 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     6.8 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     7.4 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     6.8 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     6.6 |
| cat06_05_bias_two_logs_2           |     6.8 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     5.4 |



### DeepSeek-R1-Zero   => 26.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.8 |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     9.1 |
| cat02_01_conformance_textual       |     7.1 |
| cat02_02_conf_desiderata           |     3.3 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     2   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |     7.4 |
| cat02_08_underfitting_process_tree |     7.4 |
| cat02_09_fix_process_tree          |     3.1 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     9.1 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     7.7 |
| cat04_01_pseudo_bpmn_description   |     4.8 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     6.8 |
| cat04_05_sql_filt_num_events       |     7.4 |
| cat04_06_sql_filt_three_df         |     6.8 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     7.6 |
| cat06_01_bias_text                 |     6.7 |
| cat06_02_bias_event_log            |     9.1 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     2   |



### QwenQwQ-32B-Preview   => 26.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     7.7 |
| cat01_03_high_level_events         |     7.6 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     7.4 |
| cat02_04_powl_anomaly_detection    |     4.2 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     7.4 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     6.6 |
| cat04_02_pseudo_bpmn_open_question |     6.6 |
| cat04_03_declare_open_question     |     3.7 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     6.8 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     7.4 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     6.8 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     2   |



### nvidiallama-3.3-nemotron-super-49b-v1   => 26.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    5    |
| cat01_03_high_level_events         |    7    |
| cat01_04_sensor_recordings         |    8    |
| cat01_05_merge_two_logs            |    4.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    9.25 |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    6.5  |
| cat02_04_powl_anomaly_detection    |    7.75 |
| cat02_05_two_powls_anomalies       |    7    |
| cat02_06_root_cause_1              |    4.5  |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7.75 |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    9.25 |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3.5  |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    6.5  |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    5.5  |
| cat04_05_sql_filt_num_events       |    7.75 |
| cat04_06_sql_filt_three_df         |    8    |
| cat04_07_sql_filt_top_k_vars       |    7.25 |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    7.25 |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.5  |
| cat05_06_question_pseudo_bpmn      |    9.25 |
| cat05_07_question_interview        |    9.25 |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    6.8  |
| cat06_06_bias_mitigation_declare   |    5    |
| cat06_07_fair_unfair_powl          |    7.25 |



### DeepSeek-R1-Distill-Qwen-14B   => 25.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10.6 |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     4.2 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     9.1 |
| cat02_03_anomaly_event_log         |     8.3 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     3.1 |
| cat02_07_root_cause_2              |     7.4 |
| cat02_08_underfitting_process_tree |     9.1 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     3.7 |
| cat03_02_powl_generation           |     7.4 |
| cat03_03_log_skeleton_generation   |     9.1 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     9.1 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     3.7 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     9.1 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     6.8 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     6.8 |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     2   |



### meta-llamaLlama-3.3-70B-Instruct   => 25.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.9  |
| cat01_02_activity_context          |    7.25 |
| cat01_03_high_level_events         |    4.5  |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    6    |
| cat01_07_interv_to_pseudo_bpmn     |    5.5  |
| cat01_08_tables_to_log             |    3.5  |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    7.5  |
| cat02_03_anomaly_event_log         |    7.65 |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    5.5  |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    5.5  |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    5    |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    7.5  |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    7.75 |
| cat04_06_sql_filt_three_df         |    7.75 |
| cat04_07_sql_filt_top_k_vars       |    7.25 |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    4    |
| cat05_03_hyp_gen_declare           |    7    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.5  |
| cat05_06_question_pseudo_bpmn      |    8    |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    9.25 |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    5    |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    7.25 |
| cat06_06_bias_mitigation_declare   |    4.5  |
| cat06_07_fair_unfair_powl          |    7.25 |



### qwen2.5-72b-instruct   => 25.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.5  |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    7.5  |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    4.5  |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    6.5  |
| cat02_08_underfitting_process_tree |    6.5  |
| cat02_09_fix_process_tree          |    9.25 |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    6.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3.5  |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    7.75 |
| cat04_06_sql_filt_three_df         |    7.25 |
| cat04_07_sql_filt_top_k_vars       |    7.75 |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    5    |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    7.75 |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    7.4  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    9.25 |



### pixtral-large-2411   => 25.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    9.25 |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    7.5  |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    4.5  |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    6    |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    4.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    8    |
| cat03_02_powl_generation           |    7    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    4.5  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    2    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    9.25 |
| cat04_07_sql_filt_top_k_vars       |    6.5  |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    7    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    7.5  |
| cat05_06_question_pseudo_bpmn      |    7.9  |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    7.25 |
| cat06_02_bias_event_log            |    7    |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    5.5  |
| cat06_07_fair_unfair_powl          |    2.5  |
| cat07_01_ocdfg                     |    3.5  |
| cat07_02_bpmn_orders               |   10.5  |
| cat07_03_bpmn_dispatch             |    8    |
| cat07_04_causal_net                |    7.5  |
| cat07_05_proclets                  |    7    |
| cat07_06_perf_spectrum             |    9.25 |



### meta-llamallama-4-maverick   => 24.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    6.5  |
| cat01_02_activity_context          |    5.5  |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    7.25 |
| cat02_01_conformance_textual       |    7.75 |
| cat02_02_conf_desiderata           |    7.25 |
| cat02_03_anomaly_event_log         |    8    |
| cat02_04_powl_anomaly_detection    |    4.5  |
| cat02_05_two_powls_anomalies       |    5.5  |
| cat02_06_root_cause_1              |    5.5  |
| cat02_07_root_cause_2              |    6.5  |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    5    |
| cat03_01_process_tree_generation   |    5    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3.5  |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    6    |
| cat04_01_pseudo_bpmn_description   |    3.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    8    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    7.75 |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    5.5  |
| cat06_03_bias_powl                 |    3    |
| cat06_04_bias_two_logs             |    6.8  |
| cat06_05_bias_two_logs_2           |    6.5  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    4    |
| cat07_01_ocdfg                     |    5    |
| cat07_02_bpmn_orders               |    7.75 |
| cat07_03_bpmn_dispatch             |    4    |
| cat07_04_causal_net                |    7.75 |
| cat07_05_proclets                  |    5    |
| cat07_06_perf_spectrum             |    7.75 |



### mistral-large-2411   => 24.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    7    |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    7.75 |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    5    |
| cat02_04_powl_anomaly_detection    |    7.9  |
| cat02_05_two_powls_anomalies       |    5    |
| cat02_06_root_cause_1              |    4.5  |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    2.5  |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    6    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    7.5  |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    2.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    6.5  |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    5.5  |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    7.4  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    7    |



### mistral-small-2503   => 23.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    8.75 |
| cat02_03_anomaly_event_log         |    4.5  |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    5    |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10.5  |
| cat04_06_sql_filt_three_df         |    8    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4.5  |
| cat05_05_question_gen_nlp          |    7.9  |
| cat05_06_question_pseudo_bpmn      |    9.25 |
| cat05_07_question_interview        |    8.5  |
| cat06_01_bias_text                 |    9.5  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    7.25 |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    7.75 |
| cat07_01_ocdfg                     |    7    |
| cat07_02_bpmn_orders               |    6    |
| cat07_03_bpmn_dispatch             |    5    |
| cat07_04_causal_net                |    7    |
| cat07_05_proclets                  |    6.5  |
| cat07_06_perf_spectrum             |    4.5  |



### microsoftWizardLM-2-8x22B   => 23.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.5  |
| cat01_02_activity_context          |    4.5  |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    5    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    8    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    7    |
| cat02_07_root_cause_2              |    4.5  |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    5.5  |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    2.5  |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    7.25 |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    5.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    8    |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    7.5  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    9.25 |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    4    |
| cat06_04_bias_two_logs             |    7    |
| cat06_05_bias_two_logs_2           |    4.8  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    8    |



### mistral-small-2501   => 23.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    9.25 |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    3.5  |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4.5  |
| cat01_08_tables_to_log             |    4.5  |
| cat02_01_conformance_textual       |    6.5  |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    7.75 |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    4.5  |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    7.25 |
| cat03_01_process_tree_generation   |    8.75 |
| cat03_02_powl_generation           |    7.75 |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    5    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    7.25 |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    9.75 |
| cat05_07_question_interview        |    8.5  |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    5.5  |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    6    |



### microsoftphi-4   => 23.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    7.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    3.5  |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    7.65 |
| cat02_03_anomaly_event_log         |    6.5  |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    6.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7.75 |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    8    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3.5  |
| cat03_05_temp_profile_generation   |    6    |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    5.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.6  |
| cat05_06_question_pseudo_bpmn      |    7.4  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    7.75 |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    7    |
| cat06_04_bias_two_logs             |    4.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    6    |



### open-mixtral-8x22b   => 23.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.25 |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    9.25 |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    2.5  |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    7.75 |
| cat03_01_process_tree_generation   |    2.5  |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    4.5  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4    |
| cat04_02_pseudo_bpmn_open_question |    6.5  |
| cat04_03_declare_open_question     |    2.5  |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    7.5  |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    2    |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    7    |
| cat06_02_bias_event_log            |    6.8  |
| cat06_03_bias_powl                 |    7    |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    3.5  |



### QwenQwen2.5-Coder-32B-Instruct   => 23.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    5    |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    5.5  |
| cat02_04_powl_anomaly_detection    |    7.25 |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    2.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    5    |
| cat03_02_powl_generation           |    9.25 |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3.5  |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    6.5  |
| cat04_07_sql_filt_top_k_vars       |    7.35 |
| cat05_01_hyp_generation_log        |    3.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.5  |
| cat05_06_question_pseudo_bpmn      |    9.25 |
| cat05_07_question_interview        |    6    |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    5    |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    7    |



### gemma327b-it-q8_0   => 23.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    5    |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    4.5  |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7.4  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7.25 |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    2    |
| cat03_06_petri_net_generation      |    2.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    5.5  |
| cat05_01_hyp_generation_log        |    4.5  |
| cat05_02_hyp_gen_powl              |    6.5  |
| cat05_03_hyp_gen_declare           |    7    |
| cat05_04_hyp_gen_temp_profile      |    4.5  |
| cat05_05_question_gen_nlp          |    8    |
| cat05_06_question_pseudo_bpmn      |    9.25 |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    9.75 |
| cat06_02_bias_event_log            |    7.25 |
| cat06_03_bias_powl                 |    7.25 |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    6    |
| cat07_01_ocdfg                     |    1    |
| cat07_02_bpmn_orders               |    6    |
| cat07_03_bpmn_dispatch             |    1    |
| cat07_04_causal_net                |    4    |
| cat07_05_proclets                  |    5.5  |
| cat07_06_perf_spectrum             |    4    |



### qwen2.5-32b-instruct   => 23.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    6    |
| cat01_02_activity_context          |    7.25 |
| cat01_03_high_level_events         |    4.5  |
| cat01_04_sensor_recordings         |    6.8  |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    5.5  |
| cat01_08_tables_to_log             |    3.5  |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    2.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    9.25 |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    2.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    3.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    6.5  |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    8.5  |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    7.25 |
| cat06_04_bias_two_logs             |    7.75 |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    5    |



### cogito14b-v1-preview-qwen-fp16   => 22.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     9.1 |
| cat01_04_sensor_recordings         |     6.8 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     3.7 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     5.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.4 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     9.1 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     7.1 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     4.8 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     7.4 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     6.8 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     9.1 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     3.1 |
| cat06_07_fair_unfair_powl          |     3.1 |



### MiniMax-01   => 21.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    3    |
| cat01_03_high_level_events         |    7.7  |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    6.5  |
| cat02_02_conf_desiderata           |    6.5  |
| cat02_03_anomaly_event_log         |    7    |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    4    |
| cat03_01_process_tree_generation   |    3.5  |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    4    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    2.5  |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    6.1  |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    9.25 |
| cat05_06_question_pseudo_bpmn      |    6    |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    7.75 |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    3.5  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    8.5  |
| cat06_06_bias_mitigation_declare   |    1.5  |
| cat06_07_fair_unfair_powl          |    6    |



### codestral-2501   => 21.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    8    |
| cat02_01_conformance_textual       |    5    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    4.5  |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    2.5  |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    4    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    4.5  |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10.5  |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.5  |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    6.5  |
| cat06_01_bias_text                 |    4.5  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    3.5  |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    6    |



### gemma312b-it-q8_0   => 21.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    7.25 |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    5.5  |
| cat01_07_interv_to_pseudo_bpmn     |    5.5  |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    2    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    3.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    6    |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    4.5  |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    6    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    3.5  |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    8    |
| cat05_06_question_pseudo_bpmn      |    9.25 |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    7.9  |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    9.25 |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    8    |
| cat07_01_ocdfg                     |    3.5  |
| cat07_02_bpmn_orders               |    4.5  |
| cat07_03_bpmn_dispatch             |    4.5  |
| cat07_04_causal_net                |    4.5  |
| cat07_05_proclets                  |    7.4  |
| cat07_06_perf_spectrum             |    4    |



### qwen2.5-14b-instruct   => 21.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.25 |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    5.5  |
| cat02_04_powl_anomaly_detection    |    7.75 |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    5    |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    1.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    4.5  |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    5    |
| cat04_02_pseudo_bpmn_open_question |    5.5  |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    6.5  |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    5    |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    7.75 |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    7.5  |
| cat05_06_question_pseudo_bpmn      |    7    |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    7    |
| cat06_03_bias_powl                 |    5    |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    7    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    4    |



### meta-llamaLlama-3.2-90B-Vision-Instruct   => 21.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.25 |
| cat01_02_activity_context          |    5    |
| cat01_03_high_level_events         |    4.5  |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    5    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    6    |
| cat03_03_log_skeleton_generation   |    2.5  |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3.5  |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    5    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    7.5  |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    7.6  |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    5.5  |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    4.5  |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    5.5  |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    2.5  |
| cat07_01_ocdfg                     |    5    |
| cat07_02_bpmn_orders               |    6.5  |
| cat07_03_bpmn_dispatch             |    4    |
| cat07_04_causal_net                |    3    |
| cat07_05_proclets                  |    3    |
| cat07_06_perf_spectrum             |    3.5  |



### qwen2.5-14b-instruct-1m   => 21.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    5    |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    5.5  |
| cat02_04_powl_anomaly_detection    |    7.75 |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    4    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    7.25 |
| cat04_02_pseudo_bpmn_open_question |    5.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    6.5  |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    8    |
| cat05_07_question_interview        |    7.4  |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    7.5  |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    5.5  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    3.5  |



### falcon310b-instruct-q8_0   => 21.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    5    |
| cat01_02_activity_context          |    7.25 |
| cat01_03_high_level_events         |    3.5  |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    9.25 |
| cat02_02_conf_desiderata           |    5    |
| cat02_03_anomaly_event_log         |    5    |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    7.75 |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    2.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3.5  |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    5    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    7.25 |
| cat05_06_question_pseudo_bpmn      |    9.75 |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    8.5  |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    2    |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    5    |
| cat06_07_fair_unfair_powl          |    6.5  |



### meta-llamallama-4-scout   => 20.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    3    |
| cat01_04_sensor_recordings         |    5    |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    7.75 |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    5.5  |
| cat03_01_process_tree_generation   |    6.5  |
| cat03_02_powl_generation           |    7    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    6.5  |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    7.25 |
| cat04_06_sql_filt_three_df         |    7.5  |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    5    |
| cat05_02_hyp_gen_powl              |    7    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    9.25 |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    7.75 |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    3    |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    4.5  |
| cat07_01_ocdfg                     |    4.5  |
| cat07_02_bpmn_orders               |    6.5  |
| cat07_03_bpmn_dispatch             |    3.5  |
| cat07_04_causal_net                |    4.5  |
| cat07_05_proclets                  |    6    |
| cat07_06_perf_spectrum             |    7.25 |



### googlegemma-2-9b-it   => 20.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    6.5  |
| cat01_04_sensor_recordings         |    3.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    2    |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    3.5  |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    3.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7.25 |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    7.75 |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    6    |
| cat03_05_temp_profile_generation   |    2.5  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    6.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    8    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    7.5  |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    4.5  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    5.5  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    7.25 |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    4    |



### pixtral-12b-2409   => 20.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    3.5  |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    7    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    5    |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    4.5  |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    6.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    3.5  |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    5.5  |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    7    |
| cat06_01_bias_text                 |    7.6  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    6.8  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    6.5  |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    3    |
| cat07_01_ocdfg                     |    7.75 |
| cat07_02_bpmn_orders               |    6.5  |
| cat07_03_bpmn_dispatch             |    3.5  |
| cat07_04_causal_net                |    6    |
| cat07_05_proclets                  |   10.5  |
| cat07_06_perf_spectrum             |    6    |



### exaone-deep2.4b-fp16   => 20.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     1.4 |
| cat01_03_high_level_events         |     9.1 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     7.6 |
| cat01_06_system_logs               |     4.8 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     4.8 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |     3.1 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     3.7 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     9.1 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     3.7 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     6.8 |
| cat04_06_sql_filt_three_df         |     3.1 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     4.8 |
| cat05_07_question_interview        |     7.4 |
| cat06_01_bias_text                 |     5.4 |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     6.8 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |



### falcon37b-instruct-q8_0   => 20.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    6.5  |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    2.5  |
| cat02_01_conformance_textual       |    5    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    7.75 |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    7    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    5.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    7.75 |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    7.25 |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    2    |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    5    |



### DeepSeek-R1-Distill-Llama-8B   => 19.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |     3.1 |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     4.2 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     3.7 |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |     4.2 |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     4.8 |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     6.8 |
| cat02_08_underfitting_process_tree |     3.1 |
| cat02_09_fix_process_tree          |     7.4 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     7.7 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     9.1 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     6.6 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     5.4 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     2   |



### qwen2.5-omni-7b   => 18.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2.5  |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    2.5  |
| cat02_03_anomaly_event_log         |    4    |
| cat02_04_powl_anomaly_detection    |    7.25 |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    4    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    4.5  |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    8.75 |
| cat05_06_question_pseudo_bpmn      |    8.5  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    6.5  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    4    |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    3.5  |
| cat07_01_ocdfg                     |    3.5  |
| cat07_02_bpmn_orders               |    1    |
| cat07_03_bpmn_dispatch             |    3.5  |
| cat07_04_causal_net                |    3.5  |
| cat07_05_proclets                  |    3.5  |
| cat07_06_perf_spectrum             |    7.25 |



### qwen2.5-7b-instruct   => 18.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    7.25 |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    6    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    4.5  |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    7.25 |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    2.5  |
| cat02_07_root_cause_2              |    4.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    6    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    4    |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    5    |
| cat04_03_declare_open_question     |    2    |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8    |
| cat05_06_question_pseudo_bpmn      |    5.5  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    6.5  |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    3    |



### granite3.28b-instruct-q4_K_M   => 17.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    4.5  |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    2.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    3.5  |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2.5  |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    7    |
| cat04_02_pseudo_bpmn_open_question |    3    |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    2.5  |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    4    |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    4.5  |
| cat05_05_question_gen_nlp          |    9.25 |
| cat05_06_question_pseudo_bpmn      |    9.25 |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    3.5  |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    5.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    3    |



### qwen2.5-7b-instruct-1m   => 17.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    3.5  |
| cat01_05_merge_two_logs            |    1.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    2    |
| cat02_03_anomaly_event_log         |    4    |
| cat02_04_powl_anomaly_detection    |    3.5  |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    2    |
| cat02_08_underfitting_process_tree |    5    |
| cat02_09_fix_process_tree          |    4    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    2.5  |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    3    |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    7.5  |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    3.5  |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    9.25 |
| cat05_06_question_pseudo_bpmn      |    5.5  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    4    |
| cat06_04_bias_two_logs             |    4.5  |
| cat06_05_bias_two_logs_2           |    3.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    3    |



### gemma34b-it-q8_0   => 16.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2.5  |
| cat01_02_activity_context          |    3    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    2    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    2.5  |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    8.5  |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    1    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    1.5  |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    7.9  |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    7.25 |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    3.5  |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    1    |
| cat07_01_ocdfg                     |    3.5  |
| cat07_02_bpmn_orders               |    3    |
| cat07_03_bpmn_dispatch             |    2.5  |
| cat07_04_causal_net                |    4.5  |
| cat07_05_proclets                  |    4    |
| cat07_06_perf_spectrum             |    2.5  |



### command-r7b7b-12-2024-q4_K_M   => 16.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2.5  |
| cat01_02_activity_context          |    2.5  |
| cat01_03_high_level_events         |    3.8  |
| cat01_04_sensor_recordings         |    3.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    2.5  |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    4.5  |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    5.5  |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    2.5  |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    1.5  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    6.5  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4    |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    2    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    2.5  |
| cat05_01_hyp_generation_log        |    2    |
| cat05_02_hyp_gen_powl              |    4    |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.25 |
| cat05_06_question_pseudo_bpmn      |    7    |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    6.8  |
| cat06_02_bias_event_log            |    4.5  |
| cat06_03_bias_powl                 |    5.5  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    1.5  |



### meta-llamaMeta-Llama-3.1-8B-Instruct   => 16.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1.5  |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    2.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    1.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    2.5  |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    2.5  |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    3.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    2    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    7    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    7.9  |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    7.5  |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    5.5  |
| cat06_04_bias_two_logs             |    3    |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    2.5  |



### falcon33b-instruct-q8_0   => 15.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    2    |
| cat02_04_powl_anomaly_detection    |    6.8  |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    2    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    6.5  |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    2.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3.5  |
| cat04_05_sql_filt_num_events       |    6.5  |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    2    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    2    |
| cat05_04_hyp_gen_temp_profile      |    2    |
| cat05_05_question_gen_nlp          |    6.5  |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    7    |
| cat06_01_bias_text                 |    7.4  |
| cat06_02_bias_event_log            |    3    |
| cat06_03_bias_powl                 |    4.5  |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    2.5  |



### DeepSeek-R1-Distill-Qwen-7B   => 15.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     7.4 |
| cat01_04_sensor_recordings         |     3.1 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1.4 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     4.2 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3.1 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1.4 |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     7.4 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     2.5 |
| cat04_02_pseudo_bpmn_open_question |     4.2 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     6.8 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1.4 |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     3.1 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     5.4 |
| cat05_07_question_interview        |     7.4 |
| cat06_01_bias_text                 |     3.1 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     1.4 |
| cat06_04_bias_two_logs             |     5.4 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     1.4 |
| cat06_07_fair_unfair_powl          |     1.4 |



### microsoftPhi-4-multimodal-instruct   => 14.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    2.5  |
| cat01_03_high_level_events         |    3.2  |
| cat01_04_sensor_recordings         |    2.5  |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    2    |
| cat01_08_tables_to_log             |    2.5  |
| cat02_01_conformance_textual       |    2    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    5.5  |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    6    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    1.5  |
| cat03_03_log_skeleton_generation   |    1.5  |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    1    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    5    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    6.5  |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    1.5  |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    3.5  |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    9.25 |
| cat05_06_question_pseudo_bpmn      |    6    |
| cat05_07_question_interview        |    6    |
| cat06_01_bias_text                 |    6.8  |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    5.5  |
| cat06_04_bias_two_logs             |    3    |
| cat06_05_bias_two_logs_2           |    5.5  |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    2    |
| cat07_01_ocdfg                     |    6.5  |
| cat07_02_bpmn_orders               |    4    |
| cat07_03_bpmn_dispatch             |    2    |
| cat07_04_causal_net                |    3    |
| cat07_05_proclets                  |    8    |
| cat07_06_perf_spectrum             |    3.5  |



### meta-llamaLlama-3.2-11B-Vision-Instruct   => 14.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    2.5  |
| cat01_03_high_level_events         |    3    |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    2.5  |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    5    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    3.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    2.5  |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    2.5  |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    1    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    6    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    1    |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    1    |
| cat05_03_hyp_gen_declare           |    2.5  |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    5    |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    3    |
| cat06_03_bias_powl                 |    1.5  |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    1.5  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    2    |
| cat07_01_ocdfg                     |    2    |
| cat07_02_bpmn_orders               |    3.5  |
| cat07_03_bpmn_dispatch             |    3.5  |
| cat07_04_causal_net                |    5    |
| cat07_05_proclets                  |    3    |
| cat07_06_perf_spectrum             |    4    |



### olmo27b-1124-instruct-q8_0   => 14.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2.5  |
| cat01_02_activity_context          |    3    |
| cat01_03_high_level_events         |    3    |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    1.5  |
| cat02_01_conformance_textual       |    2    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    2.5  |
| cat02_07_root_cause_2              |    3.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    3    |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    1.5  |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    2    |
| cat04_06_sql_filt_three_df         |    1.5  |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    2    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    1    |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    7.4  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    3    |
| cat06_05_bias_two_logs_2           |    3.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    1.5  |



### meta-llamaLlama-3.2-3B-Instruct   => 14.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    3.5  |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    4    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    2    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    3    |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    1.5  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    1    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    4    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    1.5  |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    2    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    8.75 |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    5    |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    2.5  |
| cat06_04_bias_two_logs             |    2.5  |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    1.5  |



### qwen2.53b-instruct-q8_0   => 14.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    2    |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    1.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    2.5  |
| cat02_01_conformance_textual       |    1.5  |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    2    |
| cat02_04_powl_anomaly_detection    |    4    |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    2.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    2    |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    1.5  |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    2.5  |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    2    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    2.5  |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    8    |
| cat05_06_question_pseudo_bpmn      |    7.5  |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    6.8  |
| cat06_02_bias_event_log            |    5.5  |
| cat06_03_bias_powl                 |    3.5  |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    3    |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    2    |



### qwen2.51.5b-instruct-q6_K   => 11.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1.5 |
| cat01_02_activity_context          |     2   |
| cat01_03_high_level_events         |     2   |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     2.5 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     2   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1.5 |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     2   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     6   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     4   |
| cat06_02_bias_event_log            |     2.5 |
| cat06_03_bias_powl                 |     3   |
| cat06_04_bias_two_logs             |     2   |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     1.5 |



### gemma31b-it-q8_0   => 10.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    1    |
| cat01_03_high_level_events         |    2    |
| cat01_04_sensor_recordings         |    1    |
| cat01_05_merge_two_logs            |    1    |
| cat01_06_system_logs               |    1.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    1    |
| cat02_01_conformance_textual       |    1    |
| cat02_02_conf_desiderata           |    1.5  |
| cat02_03_anomaly_event_log         |    1.5  |
| cat02_04_powl_anomaly_detection    |    3    |
| cat02_05_two_powls_anomalies       |    1.5  |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    2    |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    5.5  |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    1    |
| cat03_03_log_skeleton_generation   |    1.5  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    1    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    2    |
| cat04_03_declare_open_question     |    2.5  |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    2    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    1    |
| cat05_01_hyp_generation_log        |    6.4  |
| cat05_02_hyp_gen_powl              |    2.5  |
| cat05_03_hyp_gen_declare           |    2.5  |
| cat05_04_hyp_gen_temp_profile      |    2    |
| cat05_05_question_gen_nlp          |    6    |
| cat05_06_question_pseudo_bpmn      |    5.5  |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    6.5  |
| cat06_02_bias_event_log            |    3    |
| cat06_03_bias_powl                 |    3    |
| cat06_04_bias_two_logs             |    2    |
| cat06_05_bias_two_logs_2           |    3    |
| cat06_06_bias_mitigation_declare   |    1    |
| cat06_07_fair_unfair_powl          |    1.5  |



### DeepSeek-R1-Distill-Qwen-1.5B   => 9.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     3.1 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     1   |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     1   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     2   |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     7.7 |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     3.1 |
| cat06_01_bias_text                 |     5.4 |
| cat06_02_bias_event_log            |     2   |
| cat06_03_bias_powl                 |     3.1 |
| cat06_04_bias_two_logs             |     1   |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |



### meta-llamaLlama-3.2-1B-Instruct   => 8.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     1.5 |
| cat01_03_high_level_events         |     2.5 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1.5 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     1.5 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     3   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     1.5 |
| cat02_07_root_cause_2              |     1.5 |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     1.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     2.5 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     1.5 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     6.5 |
| cat05_06_question_pseudo_bpmn      |     4   |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     4   |
| cat06_02_bias_event_log            |     1.5 |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     2   |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |

