A score in the range **25-30** is considered **sufficient**; a score in the range **30-35** is considered **good**; and a score **>35** is considered **excellent**.


**As of 2025-01-26, the chain of thought of Large Reasoning Models, if provided, is considered in the assessment of answers.**

## Overall Leaderboard (1-shot; gemini-2.5-pro-exp-03-25 used as a judge)

| Model                         | Avg     | Score    | OS                 | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:------------------------------|:--------|:---------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| gemini-2.5-pro-exp-03-25      | **8.2** | **37.9** | :x:                | :mage_woman: **6.4** | :mage_woman: **8.0** | :mage_woman: **5.7** | :mage_woman: **5.9** | :mage_woman: **6.2** | :mage_woman: **5.8** | :mage_woman: **5.8** |
| o3-mini-20250131-HIGH         | **7.3** | **33.8** | :x:                | 5.9                  | 7.6                  | 4.3                  | 4.9                  | 5.4                  | **5.6**              | 3.5                  |
| o1-pro-2024-12-17             | **7.3** | **33.7** | :x:                | 5.9                  | **7.7**              | 4.5                  | 5.0                  | 5.5                  | 5.2                  | 4.8                  |
| gpt-4.5-preview               | **7.1** | **32.6** | :x:                | 5.7                  | 7.4                  | 4.2                  | 4.9                  | 5.2                  | 5.3                  | 4.2                  |
| DeepSeek-R1-671B-DS           | **6.7** | **30.6** | :white_check_mark: | 5.3                  | 7.1                  | 4.0                  | 4.8                  | 4.6                  | 4.8                  | 0.0                  |
| DeepSeek-V3-0324              | **6.6** | **30.4** | :white_check_mark: | 5.8                  | 6.5                  | 3.8                  | 4.8                  | 4.8                  | 4.6                  | 0.0                  |
| o3-mini-20250131-LOW          | **6.5** | **29.9** | :x:                | 4.9                  | 6.3                  | 3.5                  | 4.6                  | 5.5                  | 4.9                  | 3.8                  |
| gpt-4o-2024-11-20             | **5.9** | **27.1** | :x:                | 4.5                  | 5.8                  | 3.0                  | 3.6                  | 5.1                  | 5.1                  | 4.5                  |
| gemini-2.0-flash              | **5.8** | **26.8** | :x:                | 4.6                  | 6.1                  | 3.4                  | 3.0                  | 4.5                  | 5.2                  | 3.8                  |
| DeepSeek-R1-Distill-Qwen-32B  | **5.6** | **25.8** | :white_check_mark: | 5.1                  | 6.2                  | 3.5                  | 3.2                  | 3.8                  | 4.0                  | 0.0                  |
| mistral-small-2503            | **5.3** | **24.3** | :white_check_mark: | 3.1                  | 5.0                  | 2.4                  | 4.3                  | 4.7                  | 4.8                  | 3.6                  |
| DeepSeek-R1-Distill-Llama-70B | **5.3** | **24.3** | :white_check_mark: | 4.1                  | 5.7                  | 2.2                  | 3.6                  | 4.4                  | 4.4                  | 0.0                  |
| ministral-3b-2410             | **4.1** | **18.6** | :x:                | 2.9                  | 3.4                  | 2.0                  | 3.3                  | 3.7                  | 3.4                  | 0.0                  |

### gemini-2.5-pro-exp-03-25   => 37.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     6.5 |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     7.5 |
| cat01_08_tables_to_log             |     8.5 |
| cat02_01_conformance_textual       |     9.8 |
| cat02_02_conf_desiderata           |     9.2 |
| cat02_03_anomaly_event_log         |     9.2 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     9   |
| cat02_06_root_cause_1              |     9.5 |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     9.5 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     8   |
| cat03_06_petri_net_generation      |     8   |
| cat03_07_process_tree_discovery    |     9.8 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     9.1 |
| cat04_03_declare_open_question     |     9   |
| cat04_04_declare_description       |     8.2 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.5 |
| cat04_07_sql_filt_top_k_vars       |     5.5 |
| cat05_01_hyp_generation_log        |     8.5 |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     9   |
| cat05_04_hyp_gen_temp_profile      |     8.7 |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     9   |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8.5 |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |     9.5 |
| cat07_03_bpmn_dispatch             |     9.5 |
| cat07_04_causal_net                |    10   |
| cat07_05_proclets                  |     9   |
| cat07_06_perf_spectrum             |     9.8 |



### o3-mini-20250131-HIGH   => 33.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     9   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     8.8 |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     9.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     9.6 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     8.5 |
| cat02_08_underfitting_process_tree |     9.8 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     5.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     5   |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     8.8 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     8.5 |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     7.8 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8.8 |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     8.8 |
| cat06_04_bias_two_logs             |     8.5 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     7   |
| cat06_07_fair_unfair_powl          |     7   |
| cat07_01_ocdfg                     |     6   |
| cat07_02_bpmn_orders               |     3.5 |
| cat07_03_bpmn_dispatch             |     4.5 |
| cat07_04_causal_net                |     5.5 |
| cat07_05_proclets                  |     7.5 |
| cat07_06_perf_spectrum             |     8   |



### o1-pro-2024-12-17   => 33.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     9.2 |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     9   |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     6   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     8.8 |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     9   |
| cat02_06_root_cause_1              |     9.2 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     6.5 |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     9   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     8.7 |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     5   |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     8.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     8.8 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     9.5 |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |    10   |
| cat07_03_bpmn_dispatch             |     1   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     9.8 |
| cat07_06_perf_spectrum             |     9.8 |



### gpt-4.5-preview   => 32.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     9.1 |
| cat01_05_merge_two_logs            |     7.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     8   |
| cat01_08_tables_to_log             |     6.5 |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     8.5 |
| cat02_07_root_cause_2              |     8.5 |
| cat02_08_underfitting_process_tree |     9   |
| cat02_09_fix_process_tree          |     9.2 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     8.5 |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     7.5 |
| cat05_03_hyp_gen_declare           |     4.5 |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     4.5 |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     9.2 |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8   |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |     6.5 |
| cat07_03_bpmn_dispatch             |     1   |
| cat07_04_causal_net                |     6.5 |
| cat07_05_proclets                  |     9.5 |
| cat07_06_perf_spectrum             |     8.8 |



### DeepSeek-R1-671B-DS   => 30.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.8 |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     9.4 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     5.5 |
| cat01_07_interv_to_pseudo_bpmn     |     4.5 |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     6.5 |
| cat02_03_anomaly_event_log         |     6.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     9.2 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     9.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     9   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     5.5 |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     8.5 |
| cat04_01_pseudo_bpmn_description   |     7   |
| cat04_02_pseudo_bpmn_open_question |     7.4 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     8   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     5   |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     5.5 |
| cat06_07_fair_unfair_powl          |     7   |



### deepseek-aiDeepSeek-V3-0324   => 30.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     8.5 |
| cat01_04_sensor_recordings         |     8.5 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     5   |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     8.8 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     9   |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     3.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     6.5 |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     3.5 |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     9   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     5.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     9.2 |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     6.5 |



### o3-mini-20250131-LOW   => 29.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     6.8 |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     7.5 |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     9   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     6.5 |
| cat02_07_root_cause_2              |     4   |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     5   |
| cat03_02_powl_generation           |     8   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     5.5 |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     6.8 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.6 |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     5.5 |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     7.5 |
| cat05_04_hyp_gen_temp_profile      |     8   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     8.8 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     3.5 |
| cat07_01_ocdfg                     |     6   |
| cat07_02_bpmn_orders               |     4   |
| cat07_03_bpmn_dispatch             |     4   |
| cat07_04_causal_net                |     8.5 |
| cat07_05_proclets                  |     7   |
| cat07_06_perf_spectrum             |     8.5 |



### gpt-4o-2024-11-20   => 27.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     5.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     4.5 |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     5.5 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     3.5 |
| cat03_02_powl_generation           |     9   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8.5 |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     5   |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     6.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     9.2 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8   |
| cat07_01_ocdfg                     |     9.5 |
| cat07_02_bpmn_orders               |     6   |
| cat07_03_bpmn_dispatch             |     5   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     7   |
| cat07_06_perf_spectrum             |     9.5 |



### gemini-2.0-flash   => 26.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.8 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     9.8 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     8.5 |
| cat02_07_root_cause_2              |     5.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     1.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     8   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8.8 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     9   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     6   |
| cat07_01_ocdfg                     |     8.5 |
| cat07_02_bpmn_orders               |     9.2 |
| cat07_03_bpmn_dispatch             |     1   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     9.8 |
| cat07_06_perf_spectrum             |     1   |



### DeepSeek-R1-Distill-Qwen-32B   => 25.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     9.1 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     4.8 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     7.1 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     4.2 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     9.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     1.4 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     3.7 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     3.1 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     2.5 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     7.1 |



### mistral-small-2503   => 24.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     9.3 |
| cat02_03_anomaly_event_log         |     4.5 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |     5   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     5.5 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     8.8 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     9.6 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8.5 |
| cat07_01_ocdfg                     |     7   |
| cat07_02_bpmn_orders               |     6   |
| cat07_03_bpmn_dispatch             |     5   |
| cat07_04_causal_net                |     7   |
| cat07_05_proclets                  |     6.5 |
| cat07_06_perf_spectrum             |     4.5 |



### DeepSeek-R1-Distill-Llama-70B   => 24.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     3.1 |
| cat01_03_high_level_events         |     4.8 |
| cat01_04_sensor_recordings         |     6.3 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     1   |
| cat02_05_two_powls_anomalies       |     5.4 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     5.4 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     4.8 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4.2 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     8.3 |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     4.8 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     5.4 |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     3.7 |



### ministral-3b-2410   => 18.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     2   |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     5.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8.7 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     7   |
| cat06_02_bias_event_log            |     3   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     3   |

