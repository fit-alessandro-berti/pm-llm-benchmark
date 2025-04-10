A score in the range **22-26** is considered **sufficient**; a score in the range **26-30** is considered **fair**; a score in the range **30-34** is considered **good**; and a score **>34** is considered **excellent**.

## Large Reasoning Models Leaderboard (Models with CoT) (1-shot; gemini-2.5-pro-preview-03-25 used as a judge)

| Model                            | Avg     | Score    | OS                 | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:---------------------------------|:--------|:---------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| grok-3-mini-beta-high            | **8.6** | **39.6** | :x:                | **6.7**              | **7.9**              | :mage_woman: **6.5** | :mage_woman: **6.1** | :mage_woman: **6.0** | :mage_woman: **6.4** | :mage_woman: **0.0** |
| Grok-3-beta-thinking-20250221    | **8.4** | **38.8** | :x:                | 6.4                  | :mage_woman: **8.1** | **6.3**              | **5.8**              | **5.9**              | :mage_woman: **6.4** | :mage_woman: **0.0** |
| nemotron-ultra-253b-v1-thinkenab | **7.8** | **35.8** | :white_check_mark: | :mage_woman: **6.8** | 7.5                  | 5.5                  | 4.6                  | 5.4                  | 6.0                  | :mage_woman: **0.0** |
| qwen-qwq-32b-nostepbystep        | **7.7** | **35.3** | :white_check_mark: | 6.2                  | 7.0                  | **6.3**              | 4.7                  | 5.0                  | 6.1                  | :mage_woman: **0.0** |
| DeepSeek-R1                      | **7.6** | **34.8** | :white_check_mark: | 6.2                  | :mage_woman: **8.1** | 4.8                  | 5.6                  | 4.7                  | 5.4                  | :mage_woman: **0.0** |
| qwen-qwq-32b-stepbystep          | **7.5** | **34.4** | :white_check_mark: | 5.9                  | 7.3                  | 4.6                  | 4.9                  | 5.5                  | **6.2**              | :mage_woman: **0.0** |
| nemotron-super-49b-v1-thinkenab  | **7.4** | **33.9** | :white_check_mark: | 5.1                  | 7.7                  | 6.1                  | 4.9                  | 4.6                  | 5.5                  | :mage_woman: **0.0** |
| DeepSeek-R1-Dynamic-Quant        | **6.6** | **30.4** | :white_check_mark: | 5.4                  | 7.4                  | 3.5                  | 4.6                  | 5.3                  | 4.2                  | :mage_woman: **0.0** |
| r1-1776                          | **6.5** | **30.0** | :white_check_mark: | 4.7                  | 7.7                  | 2.6                  | 4.9                  | 5.0                  | 5.0                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-32B     | **6.5** | **29.8** | :white_check_mark: | 5.3                  | 7.3                  | 3.8                  | 3.7                  | 4.6                  | 5.1                  | :mage_woman: **0.0** |
| exaone-deep32b-fp16              | **6.4** | **29.5** | :white_check_mark: | 5.7                  | 6.3                  | 3.6                  | 4.5                  | 4.3                  | 5.2                  | :mage_woman: **0.0** |
| exaone-deep7.8b-fp16             | **6.1** | **28.1** | :white_check_mark: | 5.2                  | 6.8                  | 2.7                  | 3.8                  | 4.5                  | 5.1                  | :mage_woman: **0.0** |
| DeepSeek-R1-Zero                 | **6.1** | **28.0** | :white_check_mark: | 5.3                  | 5.1                  | 3.6                  | 4.2                  | 5.5                  | 4.3                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Llama-70B    | **6.0** | **27.6** | :white_check_mark: | 4.9                  | 6.5                  | 2.7                  | 4.5                  | 4.3                  | 4.7                  | :mage_woman: **0.0** |
| QwQ-32B-Preview                  | **6.0** | **27.4** | :white_check_mark: | 5.1                  | 6.7                  | 3.1                  | 3.4                  | 5.1                  | 4.0                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-14B     | **5.9** | **27.1** | :white_check_mark: | 4.5                  | 7.5                  | 3.9                  | 3.1                  | 4.0                  | 4.1                  | :mage_woman: **0.0** |
| sonar-reasoning-pro              | **4.7** | **21.5** | :x:                | 3.4                  | 5.6                  | 2.1                  | 2.4                  | 4.8                  | 3.2                  | :mage_woman: **0.0** |
| exaone-deep2.4b-fp16             | **4.6** | **21.1** | :white_check_mark: | 3.8                  | 5.8                  | 1.8                  | 2.9                  | 3.4                  | 3.3                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Llama-8B     | **4.3** | **19.8** | :white_check_mark: | 2.6                  | 4.2                  | 2.0                  | 2.5                  | 4.3                  | 4.2                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-7B      | **3.4** | **15.8** | :white_check_mark: | 1.9                  | 3.0                  | 2.5                  | 2.2                  | 3.3                  | 2.9                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-1.5B    | **2.0** | **9.4**  | :white_check_mark: | 1.3                  | 1.7                  | 0.9                  | 1.0                  | 2.9                  | 1.6                  | :mage_woman: **0.0** |

### grok-3-mini-beta-high   => 39.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.4 |
| cat01_02_activity_context          |     9.4 |
| cat01_03_high_level_events         |     9.2 |
| cat01_04_sensor_recordings         |     9.1 |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     9.4 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     8.6 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     6.6 |
| cat03_04_declare_generation        |     8.3 |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     9.4 |
| cat03_08_powl_discovery            |     7.1 |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     8.9 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     9.4 |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     9.4 |
| cat05_03_hyp_gen_declare           |     9.8 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     9.4 |
| cat06_07_fair_unfair_powl          |     8.3 |



### Grok-3-beta-thinking-20250221   => 38.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     9.7 |
| cat01_05_merge_two_logs            |     8.6 |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     8.6 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     9.4 |
| cat02_05_two_powls_anomalies       |     9.4 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     9.4 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     9.7 |
| cat03_03_log_skeleton_generation   |     7.7 |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     9.3 |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     8.3 |
| cat03_08_powl_discovery            |     7.7 |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     8.3 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     8.9 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |     8.3 |
| cat05_01_hyp_generation_log        |     9.1 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     9.4 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     9.2 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     8.9 |
| cat06_07_fair_unfair_powl          |     9.4 |



### nvidiallama-3.1-nemotron-ultra-253b-v1-thinkenab   => 35.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     8.3 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     8.9 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     9.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     8.3 |
| cat03_06_petri_net_generation      |     4.8 |
| cat03_07_process_tree_discovery    |     9.8 |
| cat03_08_powl_discovery            |     8.3 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     4.8 |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     9.4 |



### qwen-qwq-32b-nostepbystep   => 35.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     8.9 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     8.3 |
| cat02_01_conformance_textual       |     8.3 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     5.4 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     8.3 |
| cat03_01_process_tree_generation   |     7.7 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     9.4 |
| cat03_08_powl_discovery            |     8.3 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     1.4 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     9.4 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     9.4 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     8.3 |
| cat06_07_fair_unfair_powl          |     6.6 |



### deepseek-aiDeepSeek-R1   => 34.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     9.4 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     8.9 |
| cat01_08_tables_to_log             |     9.4 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     9.4 |
| cat02_03_anomaly_event_log         |     9.4 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     8.6 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     8.6 |
| cat03_07_process_tree_discovery    |     6.6 |
| cat03_08_powl_discovery            |     4.8 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.9 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     8.3 |
| cat05_01_hyp_generation_log        |     4.9 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.3 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     8.3 |



### qwen-qwq-32b-stepbystep   => 34.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     8.9 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     8.6 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     7.7 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     6.6 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     8.3 |
| cat06_07_fair_unfair_powl          |     8.3 |



### nvidiallama-3.3-nemotron-super-49b-v1-thinkenab   => 33.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     4.8 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     9.4 |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     3.7 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     9.4 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     9.4 |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     6.6 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     7.1 |
| cat03_06_petri_net_generation      |     9.4 |
| cat03_07_process_tree_discovery    |     9.4 |
| cat03_08_powl_discovery            |     9.4 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     8.9 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     8.3 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.3 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     8.3 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     6.6 |



### DeepSeek-R1-Dynamic-Quant   => 30.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     8.3 |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     9.8 |
| cat02_03_anomaly_event_log         |     5.4 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     4.8 |
| cat03_04_declare_generation        |     4.2 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     4.2 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     6.3 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     8.3 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     8.3 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     3.1 |
| cat06_06_bias_mitigation_declare   |     4.8 |
| cat06_07_fair_unfair_powl          |     6   |



### r1-1776   => 30.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.6 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     9.8 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     8.9 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     3.7 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     9.4 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     4.8 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.3 |



### deepseek-aiDeepSeek-R1-Distill-Qwen-32B   => 29.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.4 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     9.4 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     9.4 |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     8.3 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     5.4 |
| cat04_07_sql_filt_top_k_vars       |     8.3 |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     5.4 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     5.4 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     7.1 |
| cat06_07_fair_unfair_powl          |     8.3 |



### exaone-deep32b-fp16   => 29.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     9.4 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.3 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     9.8 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     6   |
| cat03_03_log_skeleton_generation   |     8.3 |
| cat03_04_declare_generation        |     1.4 |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     8.6 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     4.8 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     8.3 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.3 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     3.7 |



### exaone-deep7.8b-fp16   => 28.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     1.4 |
| cat03_02_powl_generation           |     3.1 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     4.2 |
| cat03_08_powl_discovery            |     4.8 |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     3.1 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     4.8 |
| cat05_05_question_gen_nlp          |     7.1 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     4.2 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     6.6 |



### DeepSeek-R1-Zero   => 28.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.1 |
| cat01_02_activity_context          |     7.7 |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     9.4 |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |     3.3 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     2   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     3.1 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     9.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     8.9 |
| cat04_01_pseudo_bpmn_description   |     4.8 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |     8.3 |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     6.9 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     8.3 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     2   |



### deepseek-aiDeepSeek-R1-Distill-Llama-70B   => 27.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.4 |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     9.4 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     1.4 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     6.6 |
| cat02_08_underfitting_process_tree |     6.6 |
| cat02_09_fix_process_tree          |     8.3 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     5.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     9.8 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     6.6 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     5.4 |



### QwenQwQ-32B-Preview   => 27.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     8.6 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     8.3 |
| cat02_04_powl_anomaly_detection    |     4.2 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     9.8 |
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
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     8.3 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9.8 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     2   |



### DeepSeek-R1-Distill-Qwen-14B   => 27.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     4.2 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     9.4 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     3.1 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     3.7 |
| cat03_02_powl_generation           |     8.3 |
| cat03_03_log_skeleton_generation   |     9.4 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     9.4 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     3.7 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     7.1 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.3 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     2   |



### sonar-reasoning-pro   => 21.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     4.2 |
| cat01_02_activity_context          |     4.8 |
| cat01_03_high_level_events         |     3.1 |
| cat01_04_sensor_recordings         |     6.6 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     5.4 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     4.8 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     3.7 |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     6.6 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     2.5 |
| cat03_03_log_skeleton_generation   |     3.7 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     4.2 |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     4.8 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     4.2 |
| cat06_04_bias_two_logs             |     6.6 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     3.1 |



### exaone-deep2.4b-fp16   => 21.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     1.4 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     8.6 |
| cat01_06_system_logs               |     4.8 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     4.8 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |     3.1 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     3.7 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     3.7 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     3.1 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     4.8 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     5.4 |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |



### DeepSeek-R1-Distill-Llama-8B   => 19.8 points

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
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |     3.1 |
| cat02_09_fix_process_tree          |     8.3 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.9 |
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
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     6.6 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.3 |
| cat06_04_bias_two_logs             |     5.4 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     2   |



### DeepSeek-R1-Distill-Qwen-7B   => 15.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     8.3 |
| cat01_04_sensor_recordings         |     3.1 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1.4 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     8.3 |
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
| cat03_06_petri_net_generation      |     8.3 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     2.5 |
| cat04_02_pseudo_bpmn_open_question |     4.2 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1.4 |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     3.1 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     5.4 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     3.1 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     1.4 |
| cat06_04_bias_two_logs             |     5.4 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     1.4 |
| cat06_07_fair_unfair_powl          |     1.4 |



### DeepSeek-R1-Distill-Qwen-1.5B   => 9.4 points

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
| cat02_04_powl_anomaly_detection    |     8.3 |
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
| cat05_01_hyp_generation_log        |     8.9 |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     3.1 |
| cat06_01_bias_text                 |     5.4 |
| cat06_02_bias_event_log            |     2   |
| cat06_03_bias_powl                 |     3.1 |
| cat06_04_bias_two_logs             |     1   |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |

