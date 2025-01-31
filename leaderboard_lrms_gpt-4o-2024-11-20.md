A score in the range **25-30** is considered **sufficient**; a score in the range **30-35** is considered **good**; and a score **>35** is considered **excellent**.


**As of 2025-01-26, the chain of thought of Large Reasoning Models, if provided, is considered in the assessment of answers.**

## Large Reasoning Models Leaderboard (1-shot; gpt-4o-2024-11-20 used as a judge)

| Model                         | Avg     | Score    | OS                 | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:------------------------------|:--------|:---------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| o1-pro-2024-12-17             | **7.7** | **35.6** | :x:                | **6.0**              | :mage_woman: **7.3** | 5.2                  | **5.5**              | **5.9**              | :mage_woman: **5.8** | :mage_woman: **5.8** |
| o3-mini-20250131-LOW          | **7.7** | **35.5** | :white_check_mark: | **6.0**              | 6.8                  | :mage_woman: **6.1** | :mage_woman: **5.6** | **5.7**              | 5.2                  | 0.0                  |
| DeepSeek-R1-671B-DS           | **7.6** | **35.1** | :white_check_mark: | **6.2**              | **7.0**              | 4.8                  | :mage_woman: **5.6** | 5.5                  | :mage_woman: **5.8** | 0.0                  |
| o1-2024-12-17                 | **7.6** | **34.8** | :x:                | :mage_woman: **6.3** | 6.8                  | 5.2                  | 5.0                  | :mage_woman: **6.0** | **5.5**              | **5.7**              |
| o1-preview-2024-09-12         | **7.2** | **33.3** | :x:                | **6.2**              | **7.0**              | 4.0                  | 4.9                  | **5.8**              | 5.3                  | 0.0                  |
| DeepSeek-R1-Distill-Llama-70B | **7.2** | **33.2** | :white_check_mark: | 5.8                  | 6.8                  | 4.4                  | 5.2                  | 5.3                  | **5.5**              | 0.0                  |
| gemini-2.0-flash-thinking-exp | **7.1** | **32.8** | :x:                | 5.2                  | **7.2**              | 4.0                  | **5.3**              | **5.7**              | 5.4                  | **5.5**              |
| DeepSeek-R1-Zero              | **7.0** | **32.1** | :white_check_mark: | 5.3                  | 6.8                  | 4.3                  | 4.6                  | **5.9**              | 5.2                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-32B  | **7.0** | **32.1** | :white_check_mark: | 5.9                  | **7.0**              | 3.3                  | 4.8                  | **5.8**              | 5.2                  | 0.0                  |
| o1-mini-2024-09-12            | **6.9** | **31.5** | :x:                | 5.8                  | 6.2                  | 4.0                  | 5.2                  | 4.8                  | **5.6**              | 0.0                  |
| DeepSeek-R1-Distill-Qwen-14B  | **6.7** | **30.9** | :white_check_mark: | 5.7                  | **7.2**              | 3.8                  | 4.1                  | 5.0                  | 5.1                  | 0.0                  |
| DeepSeek-R1-Distill-Llama-8B  | **6.4** | **29.3** | :white_check_mark: | 5.5                  | 6.9                  | 3.0                  | 3.6                  | 4.5                  | :mage_woman: **5.8** | 0.0                  |
| QwenQwQ-32B-Preview           | **6.3** | **28.8** | :white_check_mark: | 5.3                  | 6.9                  | 3.4                  | 3.7                  | 4.8                  | 4.7                  | 0.0                  |
| Sonus-1-Pro-Reasoning         | **6.1** | **28.1** | :x:                | 4.8                  | 6.7                  | 3.2                  | 4.5                  | 4.2                  | 4.7                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-7B   | **5.0** | **22.9** | :white_check_mark: | 3.3                  | 5.2                  | 2.7                  | 4.0                  | 4.2                  | 3.6                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-1.5B | **3.1** | **14.4** | :white_check_mark: | 2.4                  | 3.6                  | 1.4                  | 2.3                  | 2.4                  | 2.4                  | 0.0                  |

### o1-pro-2024-12-17   => 35.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.5 |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     8.5 |
| cat01_05_merge_two_logs            |     4.5 |
| cat01_06_system_logs               |     8   |
| cat01_07_interv_to_pseudo_bpmn     |     8.5 |
| cat01_08_tables_to_log             |     8.5 |
| cat02_01_conformance_textual       |     8.5 |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     9.3 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     9   |
| cat02_07_root_cause_2              |     9.8 |
| cat02_08_underfitting_process_tree |     6.5 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     6.5 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     7   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     8   |
| cat03_07_process_tree_discovery    |     5   |
| cat03_08_powl_discovery            |     5   |
| cat04_01_pseudo_bpmn_description   |     8.7 |
| cat04_02_pseudo_bpmn_open_question |     9.2 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     8.7 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     5   |
| cat05_01_hyp_generation_log        |     8   |
| cat05_02_hyp_gen_powl              |     8   |
| cat05_03_hyp_gen_declare           |     9.5 |
| cat05_04_hyp_gen_temp_profile      |     9   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     8.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     9.2 |
| cat06_06_bias_mitigation_declare   |     6.5 |
| cat06_07_fair_unfair_powl          |     8.5 |
| cat07_01_ocdfg                     |     9.5 |
| cat07_02_bpmn_orders               |    10   |
| cat07_03_bpmn_dispatch             |     9.5 |
| cat07_04_causal_net                |     9.5 |
| cat07_05_proclets                  |     9.5 |
| cat07_06_perf_spectrum             |     9.5 |



### o3-mini-20250131-LOW   => 35.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     7   |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     7   |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     9   |
| cat02_08_underfitting_process_tree |     4   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     9   |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     8   |
| cat03_04_declare_generation        |     7.5 |
| cat03_05_temp_profile_generation   |     8   |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     8.5 |
| cat03_08_powl_discovery            |     6.5 |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     8.5 |
| cat04_03_declare_open_question     |     8   |
| cat04_04_declare_description       |     9.1 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     8   |
| cat04_07_sql_filt_top_k_vars       |     6.5 |
| cat05_01_hyp_generation_log        |     7   |
| cat05_02_hyp_gen_powl              |     8   |
| cat05_03_hyp_gen_declare           |     8   |
| cat05_04_hyp_gen_temp_profile      |     7.5 |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     7   |
| cat06_02_bias_event_log            |     9.2 |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     9.2 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     7   |



### DeepSeek-R1-671B-DS   => 35.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.5 |
| cat01_02_activity_context          |     9.2 |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     7.5 |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     8   |
| cat01_08_tables_to_log             |     8   |
| cat02_01_conformance_textual       |     6.5 |
| cat02_02_conf_desiderata           |     8.5 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     6.5 |
| cat02_07_root_cause_2              |     7   |
| cat02_08_underfitting_process_tree |     9   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     7.5 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     6.5 |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     9   |
| cat03_07_process_tree_discovery    |     6.5 |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     9   |
| cat04_03_declare_open_question     |     9.5 |
| cat04_04_declare_description       |     9.4 |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     8   |
| cat05_02_hyp_gen_powl              |     8   |
| cat05_03_hyp_gen_declare           |     8   |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     9   |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     9   |
| cat06_05_bias_two_logs_2           |     8.5 |
| cat06_06_bias_mitigation_declare   |     6.5 |
| cat06_07_fair_unfair_powl          |     8.5 |



### o1-2024-12-17   => 34.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     8   |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     8.5 |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     6.5 |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     6.5 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     9.2 |
| cat02_07_root_cause_2              |     9.1 |
| cat02_08_underfitting_process_tree |     8.5 |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     6.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     7   |
| cat03_05_temp_profile_generation   |     8   |
| cat03_06_petri_net_generation      |     5.5 |
| cat03_07_process_tree_discovery    |     8   |
| cat03_08_powl_discovery            |     9.5 |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     9.3 |
| cat04_03_declare_open_question     |     6.5 |
| cat04_04_declare_description       |     8.5 |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     5   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     7.5 |
| cat05_02_hyp_gen_powl              |     9.5 |
| cat05_03_hyp_gen_declare           |     9   |
| cat05_04_hyp_gen_temp_profile      |     9.2 |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     7.5 |
| cat06_07_fair_unfair_powl          |     8   |
| cat07_01_ocdfg                     |     9.5 |
| cat07_02_bpmn_orders               |    10   |
| cat07_03_bpmn_dispatch             |     9.5 |
| cat07_04_causal_net                |     9   |
| cat07_05_proclets                  |     9   |
| cat07_06_perf_spectrum             |     9.5 |



### o1-preview-2024-09-12   => 33.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     9   |
| cat01_03_high_level_events         |     9   |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     9   |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     7.5 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     8.7 |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     7   |
| cat03_02_powl_generation           |     8   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     5   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8.5 |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     7.8 |
| cat04_04_declare_description       |     8.5 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     9.5 |
| cat05_02_hyp_gen_powl              |     8   |
| cat05_03_hyp_gen_declare           |     8.5 |
| cat05_04_hyp_gen_temp_profile      |     7   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     9   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     5   |
| cat06_07_fair_unfair_powl          |     6   |



### DeepSeek-R1-Distill-Llama-70B   => 33.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     7.7 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     6.6 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     8.9 |
| cat03_04_declare_generation        |     5.4 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     3.7 |
| cat03_08_powl_discovery            |     7.1 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     8.9 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     5.4 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     8.3 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     8.3 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     6.6 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.1 |
| cat06_07_fair_unfair_powl          |     8.9 |



### gemini-2.0-flash-thinking-exp-01-21   => 32.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     8   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     9   |
| cat02_03_anomaly_event_log         |     4.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     9   |
| cat02_06_root_cause_1              |     9   |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     7   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     8   |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     7.5 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     8.5 |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     9   |
| cat04_04_declare_description       |     9.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     8.5 |
| cat05_02_hyp_gen_powl              |     7.5 |
| cat05_03_hyp_gen_declare           |     8   |
| cat05_04_hyp_gen_temp_profile      |     7.5 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     9.2 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     7.5 |
| cat06_07_fair_unfair_powl          |     3   |
| cat07_01_ocdfg                     |     9   |
| cat07_02_bpmn_orders               |     8.5 |
| cat07_03_bpmn_dispatch             |     9.5 |
| cat07_04_causal_net                |     9.5 |
| cat07_05_proclets                  |     9   |
| cat07_06_perf_spectrum             |     9.5 |



### DeepSeek-R1-Zero   => 32.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.1 |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     8.3 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     7.1 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     6.6 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.3 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     5.4 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     6.6 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     6.6 |
| cat03_03_log_skeleton_generation   |     4.2 |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     8.3 |
| cat03_06_petri_net_generation      |     4.2 |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |     8.3 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     4.2 |
| cat05_01_hyp_generation_log        |     8.9 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     8.3 |
| cat05_04_hyp_gen_temp_profile      |     8.9 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     6.6 |



### DeepSeek-R1-Distill-Qwen-32B   => 32.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     6.6 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     6.6 |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1.4 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     4.8 |
| cat03_05_temp_profile_generation   |     4.8 |
| cat03_06_petri_net_generation      |     7.7 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     8.3 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     8.3 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     9.4 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     8.3 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     8.3 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.3 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     3.7 |
| cat06_07_fair_unfair_powl          |     5.4 |



### o1-mini-2024-09-12   => 31.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     8.5 |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     7.5 |
| cat01_08_tables_to_log             |     5.5 |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     5   |
| cat02_03_anomaly_event_log         |     5   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     8.5 |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     5   |
| cat03_03_log_skeleton_generation   |     5   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     7   |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     9.4 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     8   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     9   |
| cat05_04_hyp_gen_temp_profile      |     8   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     5   |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     8.5 |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     7   |
| cat06_07_fair_unfair_powl          |     6   |



### DeepSeek-R1-Distill-Qwen-14B   => 30.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     3.7 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     8.3 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     4.2 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     8.3 |
| cat03_05_temp_profile_generation   |     6.6 |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     1.4 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     8.3 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     8.3 |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     3.7 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     7.1 |
| cat06_01_bias_text                 |     6.6 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     7.1 |



### DeepSeek-R1-Distill-Llama-8B   => 29.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     9.4 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.3 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     5.4 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     6.6 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     4.2 |
| cat03_08_powl_discovery            |     7.7 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     8.3 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     8.3 |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     2.5 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     8.3 |
| cat06_02_bias_event_log            |     8.3 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     9.4 |



### QwenQwQ-32B-Preview   => 28.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     9.2 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     8.3 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     7.1 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     4.2 |
| cat03_04_declare_generation        |     5.4 |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     7.7 |
| cat03_08_powl_discovery            |     4.2 |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     9.2 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     8.3 |
| cat04_05_sql_filt_num_events       |     3.1 |
| cat04_06_sql_filt_three_df         |     4.2 |
| cat04_07_sql_filt_top_k_vars       |     4.2 |
| cat05_01_hyp_generation_log        |     7.7 |
| cat05_02_hyp_gen_powl              |     8.3 |
| cat05_03_hyp_gen_declare           |     8.3 |
| cat05_04_hyp_gen_temp_profile      |     8.9 |
| cat05_05_question_gen_nlp          |     1   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     8.3 |
| cat06_04_bias_two_logs             |     9.4 |
| cat06_05_bias_two_logs_2           |     8.3 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     2   |



### Sonus-1-Pro-Reasoning   => 28.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     8.5 |
| cat01_04_sensor_recordings         |     7.5 |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     5   |
| cat01_07_interv_to_pseudo_bpmn     |     6.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     9   |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     6.5 |
| cat02_06_root_cause_1              |     6.5 |
| cat02_07_root_cause_2              |     7   |
| cat02_08_underfitting_process_tree |     7.5 |
| cat02_09_fix_process_tree          |     6.5 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     2.5 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     6   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     8.5 |
| cat04_03_declare_open_question     |     8   |
| cat04_04_declare_description       |     9   |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     7.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     6.5 |
| cat05_06_question_pseudo_bpmn      |     6.5 |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     5   |
| cat06_07_fair_unfair_powl          |     2   |



### DeepSeek-R1-Distill-Qwen-7B   => 22.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     6.6 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     4.2 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     4.8 |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     4.8 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     8.3 |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     1.4 |
| cat03_05_temp_profile_generation   |     4.8 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     8.3 |
| cat04_03_declare_open_question     |     7.1 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |     6.6 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     2.5 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     1   |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     1   |



### DeepSeek-R1-Distill-Qwen-1.5B   => 14.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1.4 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     3.1 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     3.1 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     3.1 |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     5.4 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     4.8 |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     1   |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     4.2 |
| cat05_07_question_interview        |     2.5 |
| cat06_01_bias_text                 |     2   |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     3.1 |
| cat06_05_bias_two_logs_2           |     5.4 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |

