A score in the range **20-25** is considered **sufficient**; a score in the range **25-30** is considered **fair**; a score in the range **30-37** is considered **good**; and a score **>37** is considered **excellent**.

## Small Models (<5B) Leaderboard (1-shot; gpt-5.4 used as a judge)

| Model             | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | OPT                  | :nerd_face: VI       |
| ----------------- | -------- | ------------------ | ------------------ | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| qwen3.54b         | **25.7** | :white_check_mark: | :white_check_mark: | :mage_woman: **4.6** | :mage_woman: **4.9** | :mage_woman: **2.1** | :mage_woman: **3.8** | :mage_woman: **3.2** | :mage_woman: **4.2** | :mage_woman: **2.9** | 0.0                  |
| ministral-3b-2512 | **19.1** | :x:                | :x:                | 3.7                  | 2.3                  | **1.9**              | 2.9                  | 2.9                  | 3.2                  | 2.2                  | :mage_woman: **3.5** |

### qwen3.54b   => 25.7 points

| Question                           | Score |
| ---------------------------------- | ----- |
| cat01_01_case_id_inference         | 8.7   |
| cat01_02_activity_context          | 5.9   |
| cat01_03_high_level_events         | 5.3   |
| cat01_04_sensor_recordings         | 6.2   |
| cat01_05_merge_two_logs            | 4.7   |
| cat01_06_system_logs               | 3.3   |
| cat01_07_interv_to_pseudo_bpmn     | 6.2   |
| cat01_08_tables_to_log             | 5.3   |
| cat02_01_conformance_textual       | 7.2   |
| cat02_02_conf_desiderata           | 5.6   |
| cat02_03_anomaly_event_log         | 5.2   |
| cat02_04_powl_anomaly_detection    | 3.9   |
| cat02_05_two_powls_anomalies       | 5.0   |
| cat02_06_root_cause_1              | 5.3   |
| cat02_07_root_cause_2              | 5.3   |
| cat02_08_underfitting_process_tree | 7.8   |
| cat02_09_fix_process_tree          | 3.3   |
| cat03_01_process_tree_generation   | 1.0   |
| cat03_02_powl_generation           | 8.7   |
| cat03_03_log_skeleton_generation   | 2.2   |
| cat03_04_declare_generation        | 1.0   |
| cat03_05_temp_profile_generation   | 4.4   |
| cat03_06_petri_net_generation      | 1.0   |
| cat03_07_process_tree_discovery    | 1.0   |
| cat03_08_powl_discovery            | 2.2   |
| cat04_01_pseudo_bpmn_description   | 6.8   |
| cat04_02_pseudo_bpmn_open_question | 6.3   |
| cat04_03_declare_open_question     | 1.7   |
| cat04_04_declare_description       | 1.1   |
| cat04_05_sql_filt_num_events       | 8.2   |
| cat04_06_sql_filt_three_df         | 7.5   |
| cat04_07_sql_filt_top_k_vars       | 6.8   |
| cat05_01_hyp_generation_log        | 2.8   |
| cat05_02_hyp_gen_powl              | 2.2   |
| cat05_03_hyp_gen_declare           | 2.2   |
| cat05_04_hyp_gen_temp_profile      | 1.7   |
| cat05_05_question_gen_nlp          | 9.1   |
| cat05_06_question_pseudo_bpmn      | 7.6   |
| cat05_07_question_interview        | 6.9   |
| cat06_01_bias_text                 | 6.7   |
| cat06_02_bias_event_log            | 5.9   |
| cat06_03_bias_powl                 | 7.1   |
| cat06_04_bias_two_logs             | 6.2   |
| cat06_05_bias_two_logs_2           | 6.1   |
| cat06_06_bias_mitigation_declare   | 2.8   |
| cat06_07_fair_unfair_powl          | 6.7   |
| cat08_01_queue_mining              | 5.7   |
| cat08_02_instance_spanning         | 6.2   |
| cat08_03_transport_opt             | 5.3   |
| cat08_04_resource_assign           | 6.0   |
| cat08_05_task_schedul              | 5.3   |

### ministral-3b-2512   => 19.1 points

| Question                           | Score |
| ---------------------------------- | ----- |
| cat01_01_case_id_inference         | 7.7   |
| cat01_02_activity_context          | 4.0   |
| cat01_03_high_level_events         | 5.3   |
| cat01_04_sensor_recordings         | 5.8   |
| cat01_05_merge_two_logs            | 3.0   |
| cat01_06_system_logs               | 3.0   |
| cat01_07_interv_to_pseudo_bpmn     | 3.7   |
| cat01_08_tables_to_log             | 4.3   |
| cat02_01_conformance_textual       | 2.0   |
| cat02_02_conf_desiderata           | 2.5   |
| cat02_03_anomaly_event_log         | 4.0   |
| cat02_04_powl_anomaly_detection    | 3.8   |
| cat02_05_two_powls_anomalies       | 2.5   |
| cat02_06_root_cause_1              | 2.5   |
| cat02_07_root_cause_2              | 3.0   |
| cat02_08_underfitting_process_tree | 1.0   |
| cat02_09_fix_process_tree          | 1.5   |
| cat03_01_process_tree_generation   | 1.0   |
| cat03_02_powl_generation           | 7.0   |
| cat03_03_log_skeleton_generation   | 1.5   |
| cat03_04_declare_generation        | 1.3   |
| cat03_05_temp_profile_generation   | 2.5   |
| cat03_06_petri_net_generation      | 1.2   |
| cat03_07_process_tree_discovery    | 2.0   |
| cat03_08_powl_discovery            | 2.0   |
| cat04_01_pseudo_bpmn_description   | 5.5   |
| cat04_02_pseudo_bpmn_open_question | 6.1   |
| cat04_03_declare_open_question     | 2.0   |
| cat04_04_declare_description       | 2.5   |
| cat04_05_sql_filt_num_events       | 9.4   |
| cat04_06_sql_filt_three_df         | 1.0   |
| cat04_07_sql_filt_top_k_vars       | 2.0   |
| cat05_01_hyp_generation_log        | 2.3   |
| cat05_02_hyp_gen_powl              | 2.7   |
| cat05_03_hyp_gen_declare           | 2.3   |
| cat05_04_hyp_gen_temp_profile      | 3.0   |
| cat05_05_question_gen_nlp          | 7.2   |
| cat05_06_question_pseudo_bpmn      | 6.2   |
| cat05_07_question_interview        | 5.8   |
| cat06_01_bias_text                 | 5.9   |
| cat06_02_bias_event_log            | 3.2   |
| cat06_03_bias_powl                 | 4.5   |
| cat06_04_bias_two_logs             | 4.0   |
| cat06_05_bias_two_logs_2           | 6.0   |
| cat06_06_bias_mitigation_declare   | 2.0   |
| cat06_07_fair_unfair_powl          | 6.8   |
| cat07_01_ocdfg                     | 4.5   |
| cat07_02_bpmn_orders               | 7.2   |
| cat07_03_bpmn_dispatch             | 6.5   |
| cat07_04_causal_net                | 6.5   |
| cat07_05_proclets                  | 7.5   |
| cat07_06_perf_spectrum             | 3.0   |
| cat08_01_queue_mining              | 4.5   |
| cat08_02_instance_spanning         | 4.3   |
| cat08_03_transport_opt             | 5.3   |
| cat08_04_resource_assign           | 4.6   |
| cat08_05_task_schedul              | 3.8   |