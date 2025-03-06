A score in the range **25-30** is considered **sufficient**; a score in the range **30-35** is considered **good**; and a score **>35** is considered **excellent**.


**As of 2025-01-26, the chain of thought of Large Reasoning Models, if provided, is considered in the assessment of answers.**

## QWEN Leaderboard (1-shot; gpt-4o-2024-11-20 used as a judge)

| Model                         | Avg     | Score    | OS                 | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:------------------------------|:--------|:---------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| qwen-max-2025-01-25           | **7.4** | **33.9** | :x:                | **5.8**              | :mage_woman: **7.6** | **4.7**              | 4.8                  | 5.4                  | :mage_woman: **5.8** | :mage_woman: **5.4** |
| qwen-plus-2025-01-25          | **7.3** | **33.5** | :x:                | 4.8                  | **7.4**              | :mage_woman: **5.0** | :mage_woman: **5.4** | **5.6**              | 5.4                  | 4.8                  |
| qwen2.5-72b-instruct          | **7.1** | **32.5** | :white_check_mark: | **5.8**              | 7.1                  | 4.5                  | 5.1                  | 4.9                  | 5.0                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-32B  | **7.0** | **32.1** | :white_check_mark: | :mage_woman: **5.9** | 7.0                  | 3.3                  | 4.8                  | :mage_woman: **5.8** | 5.2                  | 0.0                  |
| qwen2.5-32b-instruct          | **6.8** | **31.4** | :white_check_mark: | **5.7**              | 6.8                  | 3.9                  | 5.0                  | 4.8                  | 5.2                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-14B  | **6.7** | **30.9** | :white_check_mark: | **5.7**              | 7.2                  | 3.8                  | 4.1                  | 5.0                  | 5.1                  | 0.0                  |
| qwen2.5-14b-instruct          | **6.7** | **30.6** | :white_check_mark: | 5.5                  | 6.5                  | 4.2                  | 4.3                  | 4.8                  | 5.2                  | 0.0                  |
| qwen-turbo-2024-11-01         | **6.5** | **29.8** | :x:                | 4.0                  | 6.5                  | 4.3                  | 5.0                  | 5.0                  | 4.8                  | 0.0                  |
| QwenQwQ-32B-Preview           | **6.3** | **28.8** | :white_check_mark: | 5.3                  | 6.9                  | 3.4                  | 3.7                  | 4.8                  | 4.7                  | 0.0                  |
| qwen2.5-14b-instruct-1m       | **6.2** | **28.5** | :white_check_mark: | 5.0                  | 6.2                  | 3.8                  | 4.6                  | 4.7                  | 4.2                  | 0.0                  |
| QwenQwen2.5-Coder-32B         | **5.9** | **27.2** | :white_check_mark: | 4.0                  | 5.8                  | 4.0                  | 4.2                  | 4.8                  | 4.3                  | 0.0                  |
| qwen2.5-7b-instruct-1m        | **5.5** | **25.5** | :white_check_mark: | 3.9                  | 5.4                  | 3.1                  | 4.2                  | 4.2                  | 4.7                  | 0.0                  |
| QwenQwQ-32B                   | **5.5** | **25.2** | :white_check_mark: | 4.7                  | 6.5                  | 1.4                  | 4.2                  | 3.9                  | 4.5                  | 0.0                  |
| qwen2.5-7b-instruct           | **5.3** | **24.2** | :white_check_mark: | 3.5                  | 5.8                  | 2.6                  | 3.9                  | 4.5                  | 3.9                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-7B   | **5.0** | **22.9** | :white_check_mark: | 3.3                  | 5.2                  | 2.7                  | 4.0                  | 4.2                  | 3.6                  | 0.0                  |
| qwen2.53b-instruct-q8_0       | **4.7** | **21.5** | :white_check_mark: | 3.4                  | 5.0                  | 2.9                  | 3.3                  | 3.4                  | 3.6                  | 0.0                  |
| qwen2.51.5b-instruct-q6_K     | **3.9** | **18.1** | :white_check_mark: | 2.2                  | 3.1                  | 2.6                  | 2.9                  | 3.7                  | 3.6                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-1.5B | **3.1** | **14.4** | :white_check_mark: | 2.4                  | 3.6                  | 1.4                  | 2.3                  | 2.4                  | 2.4                  | 0.0                  |

### qwen-max-2025-01-25   => 33.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.5 |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     9   |
| cat01_04_sensor_recordings         |     7.5 |
| cat01_05_merge_two_logs            |     8   |
| cat01_06_system_logs               |     8   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     4.5 |
| cat02_01_conformance_textual       |     8.5 |
| cat02_02_conf_desiderata           |     9   |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     9   |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     7.8 |
| cat02_07_root_cause_2              |     8.5 |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     5   |
| cat03_02_powl_generation           |     6.5 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     7   |
| cat03_07_process_tree_discovery    |     7.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8.5 |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     8.5 |
| cat04_04_declare_description       |     4.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     7.5 |
| cat05_01_hyp_generation_log        |     9   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     9   |
| cat05_04_hyp_gen_temp_profile      |     8   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     6.5 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     8.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     9   |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     7.5 |
| cat06_07_fair_unfair_powl          |     7   |
| cat07_01_ocdfg                     |     9.5 |
| cat07_02_bpmn_orders               |     9   |
| cat07_03_bpmn_dispatch             |     8.5 |
| cat07_04_causal_net                |     9   |
| cat07_05_proclets                  |     9   |
| cat07_06_perf_spectrum             |     9   |



### qwen-plus-2025-01-25   => 33.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7   |
| cat01_02_activity_context          |     6.5 |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     8   |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     6   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     6.5 |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     6   |
| cat03_07_process_tree_discovery    |     9   |
| cat03_08_powl_discovery            |     7.5 |
| cat04_01_pseudo_bpmn_description   |     8.5 |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     9   |
| cat04_04_declare_description       |     8.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     6.5 |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     8   |
| cat05_02_hyp_gen_powl              |     9   |
| cat05_03_hyp_gen_declare           |     8   |
| cat05_04_hyp_gen_temp_profile      |     7   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     6.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     8.5 |
| cat06_06_bias_mitigation_declare   |     7   |
| cat06_07_fair_unfair_powl          |     6.5 |
| cat07_01_ocdfg                     |     8.5 |
| cat07_02_bpmn_orders               |     9   |
| cat07_03_bpmn_dispatch             |     4   |
| cat07_04_causal_net                |     9   |
| cat07_05_proclets                  |     7.5 |
| cat07_06_perf_spectrum             |    10   |



### qwen2.5-72b-instruct   => 32.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     9   |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     6.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     9   |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     9   |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     6.5 |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     4.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     7   |
| cat03_06_petri_net_generation      |     6.5 |
| cat03_07_process_tree_discovery    |     8.5 |
| cat03_08_powl_discovery            |     7.5 |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     7   |
| cat04_04_declare_description       |     9   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     8.5 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     7   |
| cat06_07_fair_unfair_powl          |     5.5 |



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



### qwen2.5-32b-instruct   => 31.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     8.5 |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     4.5 |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     8.5 |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     5   |
| cat02_05_two_powls_anomalies       |     6.5 |
| cat02_06_root_cause_1              |     8   |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     7   |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     7   |
| cat03_04_declare_generation        |     6.5 |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     6   |
| cat03_07_process_tree_discovery    |     4   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     7.5 |
| cat04_04_declare_description       |     6.5 |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     4   |
| cat04_07_sql_filt_top_k_vars       |     8   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     6.5 |
| cat06_01_bias_text                 |     5.5 |
| cat06_02_bias_event_log            |     8.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     8   |



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



### qwen2.5-14b-instruct   => 30.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     7.5 |
| cat01_05_merge_two_logs            |     7   |
| cat01_06_system_logs               |     5.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     6   |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     6.5 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     8.5 |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     7   |
| cat03_02_powl_generation           |     6.5 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     7   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     8   |
| cat04_03_declare_open_question     |     8.5 |
| cat04_04_declare_description       |     5   |
| cat04_05_sql_filt_num_events       |     6   |
| cat04_06_sql_filt_three_df         |     5   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     7.5 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     5.5 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     7.5 |
| cat06_02_bias_event_log            |     8.5 |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     6   |



### qwen-turbo-2024-11-01   => 29.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     7.5 |
| cat01_05_merge_two_logs            |     6.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     2.5 |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     7   |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7   |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     6.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     6.5 |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     7   |
| cat04_03_declare_open_question     |     8   |
| cat04_04_declare_description       |     7.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     5   |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     7   |
| cat05_02_hyp_gen_powl              |     7.5 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     7.5 |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     5.5 |
| cat06_04_bias_two_logs             |     9   |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     7.5 |
| cat06_07_fair_unfair_powl          |     4.5 |



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



### qwen2.5-14b-instruct-1m   => 28.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     4   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     7.5 |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     8   |
| cat01_08_tables_to_log             |     5.5 |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     7   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     6.5 |
| cat02_07_root_cause_2              |     7   |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     4.5 |
| cat03_03_log_skeleton_generation   |     5.5 |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     7   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     8.5 |
| cat04_04_declare_description       |     8.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     7   |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     9.8 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     6.5 |
| cat06_01_bias_text                 |     7.5 |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     1   |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     4.5 |



### QwenQwen2.5-Coder-32B-Instruct   => 27.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     6.5 |
| cat01_03_high_level_events         |     5   |
| cat01_04_sensor_recordings         |     5.5 |
| cat01_05_merge_two_logs            |     3.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     6.5 |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     4.5 |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     5   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     6.5 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     4.5 |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     7.5 |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     6.5 |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     8.5 |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     4.5 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     8   |



### qwen2.5-7b-instruct-1m   => 25.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     7.5 |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     6.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     6.5 |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     4.5 |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     6.5 |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     8.5 |
| cat04_04_declare_description       |     6.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     4   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     7   |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     6.5 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     8.5 |
| cat06_05_bias_two_logs_2           |     6.5 |
| cat06_06_bias_mitigation_declare   |     5   |
| cat06_07_fair_unfair_powl          |     3   |



### QwenQwQ-32B   => 25.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.6 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     1   |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     2.5 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     9.4 |
| cat02_07_root_cause_2              |     3.7 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     3.7 |
| cat04_01_pseudo_bpmn_description   |     9.2 |
| cat04_02_pseudo_bpmn_open_question |     8.3 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     4.8 |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     5.4 |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     8.3 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     8.3 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     3.1 |



### qwen2.5-7b-instruct   => 24.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     3   |
| cat01_03_high_level_events         |     8.5 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     7.5 |
| cat02_02_conf_desiderata           |     5   |
| cat02_03_anomaly_event_log         |     5   |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     6.5 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     4   |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     7   |
| cat04_05_sql_filt_num_events       |     6   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     9.2 |
| cat05_03_hyp_gen_declare           |     7.5 |
| cat05_04_hyp_gen_temp_profile      |     7.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     6.5 |
| cat05_07_question_interview        |     5   |
| cat06_01_bias_text                 |     5   |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     8.8 |
| cat06_06_bias_mitigation_declare   |     6.5 |
| cat06_07_fair_unfair_powl          |     1   |



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



### qwen2.53b-instruct-q8_0   => 21.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1.5 |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     4.5 |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     5   |
| cat02_03_anomaly_event_log         |     4   |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     7   |
| cat02_09_fix_process_tree          |     6.5 |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     3.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     4.5 |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     7   |
| cat04_05_sql_filt_num_events       |     3   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     2.5 |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     5.8 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     5   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     6.5 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |



### qwen2.51.5b-instruct-q6_K   => 18.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     2   |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     4.3 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     4.5 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     4.5 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     4   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     7   |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     7.5 |
| cat06_02_bias_event_log            |     5.5 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     3.5 |
| cat06_05_bias_two_logs_2           |     6.8 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     2   |



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

