A score in the range **24-29** is considered **sufficient**; a score in the range **29-34** is considered **fair**; a score in the range **34-40** is considered **good**; and a score **>40** is considered **excellent**.

## QWEN Leaderboard (1-shot; gemini-2.5-pro-preview-06-05 used as a judge)

| Model                          | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | OPT                  | :nerd_face: VI       |
|:-------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| qwen-qwq-32b-nostepbystep      | **36.7** | :white_check_mark: | :white_check_mark: | 5.7                  | 6.4                  | :mage_woman: **5.9** | **4.5**              | **4.8**              | :mage_woman: **5.6** | **3.7**              | 0.0                  |
| qwen-qwq-32b-stepbystep        | **35.6** | :white_check_mark: | :white_check_mark: | 5.6                  | **6.7**              | 4.3                  | :mage_woman: **4.6** | :mage_woman: **5.0** | **5.5**              | :mage_woman: **3.9** | 0.0                  |
| Qwen3-235B-A22B                | **34.2** | :white_check_mark: | :white_check_mark: | 5.7                  | 5.8                  | 4.2                  | :mage_woman: **4.6** | 4.4                  | :mage_woman: **5.6** | :mage_woman: **3.9** | 0.0                  |
| Qwen3-32B                      | **33.4** | :white_check_mark: | :white_check_mark: | 5.5                  | 6.0                  | 4.0                  | 4.1                  | :mage_woman: **5.0** | 5.2                  | **3.6**              | 0.0                  |
| Qwen3-30B-A3B                  | **32.1** | :white_check_mark: | :white_check_mark: | 5.3                  | 6.2                  | 2.8                  | **4.3**              | 4.5                  | **5.4**              | **3.7**              | 0.0                  |
| Qwen3-14B                      | **32.0** | :white_check_mark: | :white_check_mark: | :mage_woman: **6.2** | 5.6                  | 3.5                  | 3.8                  | 4.4                  | 5.0                  | 3.5                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-32B   | **31.5** | :white_check_mark: | :white_check_mark: | 5.1                  | :mage_woman: **6.9** | 3.7                  | 3.8                  | 4.5                  | 4.9                  | 2.6                  | 0.0                  |
| qwen-turbo-2025-04-28          | **30.6** | :x:                | :white_check_mark: | 4.2                  | 5.4                  | 3.2                  | **4.3**              | **4.8**              | 5.1                  | **3.6**              | 0.0                  |
| Qwen-3-235B-A22B-nothink       | **30.4** | :white_check_mark: | :x:                | 5.0                  | 5.5                  | 2.9                  | 3.6                  | **4.8**              | 5.0                  | **3.6**              | 0.0                  |
| Qwen-3-32B-nothink             | **30.0** | :white_check_mark: | :x:                | 4.6                  | 5.3                  | 3.0                  | 3.7                  | 4.5                  | 5.0                  | :mage_woman: **3.9** | 0.0                  |
| QwQ-32B-Preview                | **29.8** | :white_check_mark: | :white_check_mark: | 4.9                  | 6.3                  | 3.3                  | 3.5                  | **4.9**              | 3.9                  | 2.8                  | 0.0                  |
| qwen-max-2025-01-25            | **29.2** | :x:                | :x:                | 4.6                  | 5.2                  | 3.0                  | 3.5                  | **4.7**              | 4.7                  | 3.4                  | :mage_woman: **3.7** |
| deepseek-r1-distill-qwen-14b   | **28.7** | :white_check_mark: | :white_check_mark: | 4.6                  | :mage_woman: **6.9** | 3.9                  | 3.2                  | 3.9                  | 4.1                  | 2.0                  | 0.0                  |
| Qwen-3-30B-A3B-nothink         | **28.6** | :white_check_mark: | :x:                | 3.5                  | 5.4                  | 2.9                  | 3.9                  | **4.9**              | 4.3                  | **3.8**              | 0.0                  |
| Qwen-3-14B-nothink             | **28.5** | :white_check_mark: | :x:                | 4.6                  | 5.4                  | 2.2                  | 4.2                  | 4.2                  | 4.4                  | 3.4                  | 0.0                  |
| qwen2.5-72b-instruct           | **28.2** | :white_check_mark: | :x:                | 4.5                  | 5.7                  | 2.9                  | 4.1                  | 3.7                  | 4.7                  | 2.9                  | 0.0                  |
| qwen38b                        | **28.2** | :white_check_mark: | :white_check_mark: | 4.4                  | 5.1                  | 3.5                  | 3.9                  | 4.4                  | 4.1                  | 2.8                  | 0.0                  |
| qwen34b                        | **27.2** | :white_check_mark: | :white_check_mark: | 4.8                  | 5.5                  | 1.7                  | 3.7                  | **4.7**              | 3.7                  | 3.2                  | 0.0                  |
| cogito14b-v1-preview-qwen-fp16 | **26.2** | :white_check_mark: | :white_check_mark: | 4.6                  | 4.3                  | 2.9                  | 3.5                  | 3.8                  | 4.6                  | 2.4                  | 0.0                  |
| Qwen2.5-Coder-32B-Instruct     | **26.1** | :white_check_mark: | :x:                | 3.8                  | 4.4                  | 3.0                  | 3.7                  | 4.0                  | 4.0                  | 3.1                  | 0.0                  |
| qwen2.5-32b-instruct           | **25.7** | :white_check_mark: | :x:                | 4.1                  | 5.0                  | 2.0                  | 3.3                  | 4.4                  | 4.1                  | 2.9                  | 0.0                  |
| qwen2.5-14b-instruct-1m        | **24.0** | :white_check_mark: | :x:                | 3.6                  | 4.5                  | 1.7                  | 3.5                  | 4.3                  | 3.7                  | 2.7                  | 0.0                  |
| qwen-plus-2025-04-28           | **23.1** | :x:                | :white_check_mark: | 2.9                  | 4.2                  | 2.1                  | 2.8                  | 4.3                  | 3.4                  | 3.4                  | 0.0                  |
| qwen31.7b                      | **21.3** | :white_check_mark: | :white_check_mark: | 3.1                  | 4.1                  | 2.0                  | 2.0                  | 4.0                  | 3.5                  | 2.7                  | 0.0                  |
| qwen2.5-omni-7b                | **21.1** | :white_check_mark: | :x:                | 3.2                  | 3.5                  | 1.9                  | 3.0                  | 3.8                  | 3.1                  | 2.4                  | 2.2                  |
| qwen2.5-7b-instruct-1m         | **19.7** | :white_check_mark: | :x:                | 3.0                  | 3.0                  | 1.9                  | 2.5                  | 3.5                  | 3.0                  | 2.8                  | 0.0                  |
| deepseek-r1-distill-qwen-7b    | **18.3** | :white_check_mark: | :white_check_mark: | 2.1                  | 3.2                  | 2.6                  | 2.4                  | 3.3                  | 3.0                  | 1.8                  | 0.0                  |
| qwen30.6b                      | **13.9** | :white_check_mark: | :white_check_mark: | 1.3                  | 2.7                  | 1.6                  | 1.3                  | 2.8                  | 2.5                  | 1.6                  | 0.0                  |
| deepseek-r1-distill-qwen-1.5b  | **11.1** | :white_check_mark: | :white_check_mark: | 1.5                  | 1.9                  | 1.0                  | 1.2                  | 2.8                  | 1.7                  | 0.9                  | 0.0                  |

### qwen-qwq-32b-nostepbystep   => 36.7 points

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
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     7.4 |
| cat03_01_process_tree_generation   |     7.1 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     6.8 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     8.9 |
| cat03_08_powl_discovery            |     7.4 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     1.4 |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     7.4 |
| cat06_07_fair_unfair_powl          |     6.6 |
| cat08_01_queue_mining              |     7.4 |
| cat08_02_instance_spanning         |     6.8 |
| cat08_03_transport_opt             |     7.4 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     7.4 |



### qwen-qwq-32b-stepbystep   => 35.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8.9 |
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
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
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
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.8 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     6.8 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     7.4 |
| cat06_07_fair_unfair_powl          |     7.4 |
| cat08_01_queue_mining              |     7.6 |
| cat08_02_instance_spanning         |     7.7 |
| cat08_03_transport_opt             |     7.6 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     8.2 |



### QwenQwen3-235B-A22B   => 34.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     4.5 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     6.7 |
| cat01_05_merge_two_logs            |     7.8 |
| cat01_06_system_logs               |     7.8 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     5.6 |
| cat02_04_powl_anomaly_detection    |     7.8 |
| cat02_05_two_powls_anomalies       |     7.8 |
| cat02_06_root_cause_1              |     4.3 |
| cat02_07_root_cause_2              |     5.6 |
| cat02_08_underfitting_process_tree |     6.7 |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     7.3 |
| cat03_02_powl_generation           |     7.5 |
| cat03_03_log_skeleton_generation   |     7.3 |
| cat03_04_declare_generation        |     1.3 |
| cat03_05_temp_profile_generation   |     5.6 |
| cat03_06_petri_net_generation      |     7.5 |
| cat03_07_process_tree_discovery    |     3.5 |
| cat03_08_powl_discovery            |     1.8 |
| cat04_01_pseudo_bpmn_description   |     5.6 |
| cat04_02_pseudo_bpmn_open_question |     7.3 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     5.6 |
| cat04_05_sql_filt_num_events       |     6.7 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     7.8 |
| cat05_01_hyp_generation_log        |     7.3 |
| cat05_02_hyp_gen_powl              |     6.2 |
| cat05_03_hyp_gen_declare           |     7.5 |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     7.3 |
| cat05_06_question_pseudo_bpmn      |     7.3 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     8.3 |
| cat06_03_bias_powl                 |     7.8 |
| cat06_04_bias_two_logs             |     6.7 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     9.6 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     8.3 |
| cat08_02_instance_spanning         |     7.8 |
| cat08_03_transport_opt             |     7.3 |
| cat08_04_resource_assign           |     9.3 |
| cat08_05_task_schedul              |     6.7 |



### QwenQwen3-32B   => 33.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.8 |
| cat01_02_activity_context          |     6.2 |
| cat01_03_high_level_events         |     7.3 |
| cat01_04_sensor_recordings         |     6.2 |
| cat01_05_merge_two_logs            |     7.8 |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     7.3 |
| cat01_08_tables_to_log             |     5.1 |
| cat02_01_conformance_textual       |     7.5 |
| cat02_02_conf_desiderata           |     5.1 |
| cat02_03_anomaly_event_log         |     5.6 |
| cat02_04_powl_anomaly_detection    |     7.8 |
| cat02_05_two_powls_anomalies       |     7.3 |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     5.6 |
| cat02_08_underfitting_process_tree |     7.5 |
| cat02_09_fix_process_tree          |     9.6 |
| cat03_01_process_tree_generation   |     1.8 |
| cat03_02_powl_generation           |     5.1 |
| cat03_03_log_skeleton_generation   |     5.6 |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     7.8 |
| cat03_06_petri_net_generation      |     9.6 |
| cat03_07_process_tree_discovery    |     3.5 |
| cat03_08_powl_discovery            |     2.4 |
| cat04_01_pseudo_bpmn_description   |     5.6 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     1.8 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     7.8 |
| cat04_06_sql_filt_three_df         |     9.6 |
| cat04_07_sql_filt_top_k_vars       |     6.7 |
| cat05_01_hyp_generation_log        |     8.9 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     6.2 |
| cat05_04_hyp_gen_temp_profile      |     3.5 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.3 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     5.6 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     6.7 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     7.2 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     7.3 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     7.7 |



### QwenQwen3-30B-A3B   => 32.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.2 |
| cat01_02_activity_context          |     5.6 |
| cat01_03_high_level_events         |     7.3 |
| cat01_04_sensor_recordings         |     5.6 |
| cat01_05_merge_two_logs            |     7.5 |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6.2 |
| cat01_08_tables_to_log             |     7.3 |
| cat02_01_conformance_textual       |     7.3 |
| cat02_02_conf_desiderata           |     5.1 |
| cat02_03_anomaly_event_log         |     6.7 |
| cat02_04_powl_anomaly_detection    |     7.3 |
| cat02_05_two_powls_anomalies       |     5.6 |
| cat02_06_root_cause_1              |     5.6 |
| cat02_07_root_cause_2              |     5.1 |
| cat02_08_underfitting_process_tree |     9.6 |
| cat02_09_fix_process_tree          |     9.6 |
| cat03_01_process_tree_generation   |     4.5 |
| cat03_02_powl_generation           |     2.4 |
| cat03_03_log_skeleton_generation   |     2.4 |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     7   |
| cat03_07_process_tree_discovery    |     1.8 |
| cat03_08_powl_discovery            |     2.4 |
| cat04_01_pseudo_bpmn_description   |     5.1 |
| cat04_02_pseudo_bpmn_open_question |     7   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     7.8 |
| cat04_06_sql_filt_three_df         |     7.8 |
| cat04_07_sql_filt_top_k_vars       |     9.6 |
| cat05_01_hyp_generation_log        |     4.5 |
| cat05_02_hyp_gen_powl              |     6.2 |
| cat05_03_hyp_gen_declare           |     6.2 |
| cat05_04_hyp_gen_temp_profile      |     5.1 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     7.3 |
| cat06_01_bias_text                 |     6.2 |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     7.3 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     7.2 |
| cat06_06_bias_mitigation_declare   |    10   |
| cat06_07_fair_unfair_powl          |     7.8 |
| cat08_01_queue_mining              |     7.5 |
| cat08_02_instance_spanning         |     7   |
| cat08_03_transport_opt             |     7.5 |
| cat08_04_resource_assign           |     7.5 |
| cat08_05_task_schedul              |     7.2 |



### QwenQwen3-14B   => 32.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     7.8 |
| cat01_03_high_level_events         |     7.8 |
| cat01_04_sensor_recordings         |     6.7 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     8.3 |
| cat01_08_tables_to_log             |     5.6 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     5.6 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     6.2 |
| cat02_07_root_cause_2              |     3.5 |
| cat02_08_underfitting_process_tree |     7.5 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     3.5 |
| cat03_02_powl_generation           |     4.5 |
| cat03_03_log_skeleton_generation   |     5.6 |
| cat03_04_declare_generation        |     2.9 |
| cat03_05_temp_profile_generation   |     2.4 |
| cat03_06_petri_net_generation      |    10   |
| cat03_07_process_tree_discovery    |     1.8 |
| cat03_08_powl_discovery            |     4.5 |
| cat04_01_pseudo_bpmn_description   |     7.3 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     2.4 |
| cat04_04_declare_description       |     1.8 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     6.2 |
| cat04_07_sql_filt_top_k_vars       |     4.9 |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     6.2 |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     7.8 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     7.3 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     7   |
| cat08_01_queue_mining              |     7.3 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     6.7 |
| cat08_05_task_schedul              |     6.7 |



### deepseek-aiDeepSeek-R1-Distill-Qwen-32B   => 31.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     7.8 |
| cat01_04_sensor_recordings         |     7.5 |
| cat01_05_merge_two_logs            |     5.6 |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.8 |
| cat02_03_anomaly_event_log         |     7.3 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     7.3 |
| cat02_06_root_cause_1              |     5.6 |
| cat02_07_root_cause_2              |     5.6 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1.3 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     3.5 |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     7.8 |
| cat03_07_process_tree_discovery    |     1.3 |
| cat03_08_powl_discovery            |     7.5 |
| cat04_01_pseudo_bpmn_description   |     5.6 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     7.3 |
| cat04_06_sql_filt_three_df         |     5.6 |
| cat04_07_sql_filt_top_k_vars       |     7.5 |
| cat05_01_hyp_generation_log        |     3.5 |
| cat05_02_hyp_gen_powl              |     5.6 |
| cat05_03_hyp_gen_declare           |     6.2 |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.8 |
| cat06_02_bias_event_log            |     7.3 |
| cat06_03_bias_powl                 |     5.6 |
| cat06_04_bias_two_logs             |     7.3 |
| cat06_05_bias_two_logs_2           |     6.2 |
| cat06_06_bias_mitigation_declare   |     7   |
| cat06_07_fair_unfair_powl          |     7.5 |
| cat08_01_queue_mining              |     4.5 |
| cat08_02_instance_spanning         |     2.9 |
| cat08_03_transport_opt             |     5.1 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     6.2 |



### qwen-turbo-2025-04-28   => 30.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.8 |
| cat01_02_activity_context          |     7.8 |
| cat01_03_high_level_events         |     5.6 |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     1.8 |
| cat01_06_system_logs               |     5.1 |
| cat01_07_interv_to_pseudo_bpmn     |     5.1 |
| cat01_08_tables_to_log             |     4.5 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     3.5 |
| cat02_03_anomaly_event_log         |     6.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     2.4 |
| cat02_06_root_cause_1              |     6.7 |
| cat02_07_root_cause_2              |     2.4 |
| cat02_08_underfitting_process_tree |     7.3 |
| cat02_09_fix_process_tree          |     7.8 |
| cat03_01_process_tree_generation   |     3.5 |
| cat03_02_powl_generation           |     7.3 |
| cat03_03_log_skeleton_generation   |     3.5 |
| cat03_04_declare_generation        |     4.5 |
| cat03_05_temp_profile_generation   |     5.1 |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     1.8 |
| cat03_08_powl_discovery            |     2.9 |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     7.3 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     8.3 |
| cat05_01_hyp_generation_log        |     7.3 |
| cat05_02_hyp_gen_powl              |     5.6 |
| cat05_03_hyp_gen_declare           |     6.7 |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     8.3 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     6.2 |
| cat06_05_bias_two_logs_2           |     7.3 |
| cat06_06_bias_mitigation_declare   |     6.7 |
| cat06_07_fair_unfair_powl          |     7.8 |
| cat08_01_queue_mining              |     7.5 |
| cat08_02_instance_spanning         |     6.5 |
| cat08_03_transport_opt             |     7.3 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     6.8 |



### Qwen-3-235B-A22B-nothink   => 30.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    8    |
| cat01_02_activity_context          |    7.9  |
| cat01_03_high_level_events         |    7.5  |
| cat01_04_sensor_recordings         |    7.25 |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    7.4  |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    6.5  |
| cat02_09_fix_process_tree          |    6.5  |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    4    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    4.5  |
| cat03_06_petri_net_generation      |    5    |
| cat03_07_process_tree_discovery    |    2.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    3.5  |
| cat04_02_pseudo_bpmn_open_question |    6.5  |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    5.5  |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    7.25 |
| cat05_03_hyp_gen_declare           |    5.5  |
| cat05_04_hyp_gen_temp_profile      |    6.5  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    9.6  |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    7.9  |
| cat06_02_bias_event_log            |    5.8  |
| cat06_03_bias_powl                 |    7.6  |
| cat06_04_bias_two_logs             |    7    |
| cat06_05_bias_two_logs_2           |    7.9  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    9.6  |
| cat08_01_queue_mining              |    7.5  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    7.25 |
| cat08_04_resource_assign           |    7.9  |
| cat08_05_task_schedul              |    7.25 |



### Qwen-3-32B-nothink   => 30.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.9  |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    6.5  |
| cat01_04_sensor_recordings         |    7.25 |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    6.5  |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    7.75 |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    6.5  |
| cat02_04_powl_anomaly_detection    |    7.75 |
| cat02_05_two_powls_anomalies       |    4.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    4.5  |
| cat02_09_fix_process_tree          |    9    |
| cat03_01_process_tree_generation   |    6    |
| cat03_02_powl_generation           |    5.5  |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3.5  |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3.5  |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    6.8  |
| cat04_03_declare_open_question     |    6.8  |
| cat04_04_declare_description       |    3.5  |
| cat04_05_sql_filt_num_events       |    1    |
| cat04_06_sql_filt_three_df         |    6    |
| cat04_07_sql_filt_top_k_vars       |    7.5  |
| cat05_01_hyp_generation_log        |    5    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    6.5  |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    9    |
| cat06_02_bias_event_log            |    7    |
| cat06_03_bias_powl                 |    7.75 |
| cat06_04_bias_two_logs             |    6.8  |
| cat06_05_bias_two_logs_2           |    9    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    6    |
| cat08_01_queue_mining              |    7.25 |
| cat08_02_instance_spanning         |    7.9  |
| cat08_03_transport_opt             |    7.25 |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    7.9  |



### QwenQwQ-32B-Preview   => 29.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.8 |
| cat01_02_activity_context          |     7.8 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     6.2 |
| cat01_05_merge_two_logs            |     5.1 |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     4.5 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.3 |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     4.5 |
| cat02_05_two_powls_anomalies       |     7.5 |
| cat02_06_root_cause_1              |     6.7 |
| cat02_07_root_cause_2              |     5.6 |
| cat02_08_underfitting_process_tree |     7.5 |
| cat02_09_fix_process_tree          |     7.8 |
| cat03_01_process_tree_generation   |     4.5 |
| cat03_02_powl_generation           |     9.6 |
| cat03_03_log_skeleton_generation   |     2.4 |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     2.4 |
| cat03_06_petri_net_generation      |     2.4 |
| cat03_07_process_tree_discovery    |     2.4 |
| cat03_08_powl_discovery            |     6.2 |
| cat04_01_pseudo_bpmn_description   |     6.7 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     7   |
| cat04_06_sql_filt_three_df         |     6.2 |
| cat04_07_sql_filt_top_k_vars       |     2.4 |
| cat05_01_hyp_generation_log        |     7.5 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     4.5 |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     9.6 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     6.2 |
| cat06_02_bias_event_log            |     7.3 |
| cat06_03_bias_powl                 |     7.8 |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     7.3 |
| cat06_06_bias_mitigation_declare   |     1.3 |
| cat06_07_fair_unfair_powl          |     2.4 |
| cat08_01_queue_mining              |     6.6 |
| cat08_02_instance_spanning         |     7   |
| cat08_03_transport_opt             |     7.5 |
| cat08_04_resource_assign           |     6.2 |
| cat08_05_task_schedul              |     1   |



### qwen-max-2025-01-25   => 29.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.9  |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    5    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    7.4  |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    4.5  |
| cat02_05_two_powls_anomalies       |    6    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    4.5  |
| cat02_08_underfitting_process_tree |    6.5  |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    7    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    4    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    6.5  |
| cat04_03_declare_open_question     |    4.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    4    |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    4.5  |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    7.4  |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    7.9  |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    7.9  |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    7.5  |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    8    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    7.25 |
| cat07_01_ocdfg                     |    6    |
| cat07_02_bpmn_orders               |    5    |
| cat07_03_bpmn_dispatch             |    6    |
| cat07_04_causal_net                |    6.5  |
| cat07_05_proclets                  |    6.5  |
| cat07_06_perf_spectrum             |    7.25 |
| cat08_01_queue_mining              |    6.5  |
| cat08_02_instance_spanning         |    7.25 |
| cat08_03_transport_opt             |    6    |
| cat08_04_resource_assign           |    7.5  |
| cat08_05_task_schedul              |    6.5  |



### deepseekdeepseek-r1-distill-qwen-14b   => 28.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     5.6 |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     2.9 |
| cat01_06_system_logs               |     5.6 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     4.5 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.3 |
| cat02_04_powl_anomaly_detection    |     7.8 |
| cat02_05_two_powls_anomalies       |     7.5 |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     7.8 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     7.5 |
| cat03_03_log_skeleton_generation   |     8.9 |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     1.3 |
| cat03_08_powl_discovery            |     1.8 |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     6.2 |
| cat04_03_declare_open_question     |     5.6 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     1.3 |
| cat04_07_sql_filt_top_k_vars       |     3.5 |
| cat05_01_hyp_generation_log        |     4.5 |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     5.6 |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     7.3 |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     7.3 |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     2.4 |
| cat06_04_bias_two_logs             |     7.3 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     6.7 |
| cat06_07_fair_unfair_powl          |     2.4 |
| cat08_01_queue_mining              |     4.5 |
| cat08_02_instance_spanning         |     2.9 |
| cat08_03_transport_opt             |     2.4 |
| cat08_04_resource_assign           |     7   |
| cat08_05_task_schedul              |     3.5 |



### Qwen-3-30B-A3B-nothink   => 28.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    4.5  |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    5    |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    9.6  |
| cat02_03_anomaly_event_log         |    7.25 |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    5    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    3.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    7.5  |
| cat04_02_pseudo_bpmn_open_question |    7.6  |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    7    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    8    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    5.5  |
| cat05_05_question_gen_nlp          |    9    |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    7.5  |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    4    |
| cat08_01_queue_mining              |    7.9  |
| cat08_02_instance_spanning         |    7.75 |
| cat08_03_transport_opt             |    7.5  |
| cat08_04_resource_assign           |    7    |
| cat08_05_task_schedul              |    7.9  |



### Qwen-3-14B-nothink   => 28.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7    |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    8    |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    7    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    9    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    7.75 |
| cat02_06_root_cause_1              |    5    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    6    |
| cat04_07_sql_filt_top_k_vars       |    7.25 |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    4    |
| cat05_03_hyp_gen_declare           |    5.5  |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |    9    |
| cat05_06_question_pseudo_bpmn      |    7    |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    8.4  |
| cat06_03_bias_powl                 |    3.5  |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    6    |
| cat08_01_queue_mining              |    7.5  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    5.5  |
| cat08_04_resource_assign           |    7.4  |
| cat08_05_task_schedul              |    7.75 |



### qwen2.5-72b-instruct   => 28.2 points

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
| cat02_09_fix_process_tree          |    9    |
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
| cat06_07_fair_unfair_powl          |    9    |
| cat08_01_queue_mining              |    5.5  |
| cat08_02_instance_spanning         |    5    |
| cat08_03_transport_opt             |    5    |
| cat08_04_resource_assign           |    7.5  |
| cat08_05_task_schedul              |    5.5  |



### qwen38b   => 28.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7   |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     3.5 |
| cat01_05_merge_two_logs            |     3.5 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     5.1 |
| cat01_08_tables_to_log             |     7.8 |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     5.6 |
| cat02_03_anomaly_event_log         |     4.5 |
| cat02_04_powl_anomaly_detection    |     6.7 |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     5.1 |
| cat02_08_underfitting_process_tree |     7.3 |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     5.6 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     5.6 |
| cat03_04_declare_generation        |     2.9 |
| cat03_05_temp_profile_generation   |     2.4 |
| cat03_06_petri_net_generation      |     6.2 |
| cat03_07_process_tree_discovery    |     2.4 |
| cat03_08_powl_discovery            |     1.3 |
| cat04_01_pseudo_bpmn_description   |     5.6 |
| cat04_02_pseudo_bpmn_open_question |     6.2 |
| cat04_03_declare_open_question     |     5.6 |
| cat04_04_declare_description       |     1.8 |
| cat04_05_sql_filt_num_events       |     7.5 |
| cat04_06_sql_filt_three_df         |     7   |
| cat04_07_sql_filt_top_k_vars       |     5.6 |
| cat05_01_hyp_generation_log        |     2.9 |
| cat05_02_hyp_gen_powl              |     7.5 |
| cat05_03_hyp_gen_declare           |     5.6 |
| cat05_04_hyp_gen_temp_profile      |     5.1 |
| cat05_05_question_gen_nlp          |     7.3 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     7.8 |
| cat06_02_bias_event_log            |     5.6 |
| cat06_03_bias_powl                 |     5.6 |
| cat06_04_bias_two_logs             |     6.7 |
| cat06_05_bias_two_logs_2           |     5.1 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     1.2 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     7.5 |
| cat08_04_resource_assign           |     6.7 |
| cat08_05_task_schedul              |     5.4 |



### qwen34b   => 27.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.6 |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |     3.5 |
| cat01_04_sensor_recordings         |     7.3 |
| cat01_05_merge_two_logs            |     5.6 |
| cat01_06_system_logs               |     7.8 |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     6.7 |
| cat02_02_conf_desiderata           |     7.3 |
| cat02_03_anomaly_event_log         |     5.1 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     5.6 |
| cat02_07_root_cause_2              |     1.8 |
| cat02_08_underfitting_process_tree |     9.6 |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     1.8 |
| cat03_02_powl_generation           |     2.4 |
| cat03_03_log_skeleton_generation   |     2.9 |
| cat03_04_declare_generation        |     2.9 |
| cat03_05_temp_profile_generation   |     1.8 |
| cat03_06_petri_net_generation      |     2.4 |
| cat03_07_process_tree_discovery    |     1.3 |
| cat03_08_powl_discovery            |     1.8 |
| cat04_01_pseudo_bpmn_description   |     2.9 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     4.5 |
| cat04_04_declare_description       |     2.9 |
| cat04_05_sql_filt_num_events       |     7.8 |
| cat04_06_sql_filt_three_df         |     6.2 |
| cat04_07_sql_filt_top_k_vars       |     6.7 |
| cat05_01_hyp_generation_log        |     7.5 |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     6.2 |
| cat05_04_hyp_gen_temp_profile      |     4.3 |
| cat05_05_question_gen_nlp          |     6.7 |
| cat05_06_question_pseudo_bpmn      |     6.7 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.5 |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     6.7 |
| cat06_04_bias_two_logs             |     5.6 |
| cat06_05_bias_two_logs_2           |     5.6 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     4.5 |
| cat08_01_queue_mining              |     6.2 |
| cat08_02_instance_spanning         |     4.5 |
| cat08_03_transport_opt             |     6.5 |
| cat08_04_resource_assign           |     7.3 |
| cat08_05_task_schedul              |     7.3 |



### cogito14b-v1-preview-qwen-fp16   => 26.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.6 |
| cat01_02_activity_context          |     5.6 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     5.6 |
| cat01_06_system_logs               |     5.6 |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     5.6 |
| cat02_02_conf_desiderata           |     7.8 |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     5.6 |
| cat02_05_two_powls_anomalies       |     2.4 |
| cat02_06_root_cause_1              |     2.9 |
| cat02_07_root_cause_2              |     2.4 |
| cat02_08_underfitting_process_tree |     1.3 |
| cat02_09_fix_process_tree          |     7.8 |
| cat03_01_process_tree_generation   |     2.4 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     2.4 |
| cat03_04_declare_generation        |     2.4 |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     1.3 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     7.3 |
| cat04_01_pseudo_bpmn_description   |     5.6 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     2.4 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     9.6 |
| cat04_06_sql_filt_three_df         |     1.3 |
| cat04_07_sql_filt_top_k_vars       |     7.8 |
| cat05_01_hyp_generation_log        |     2.9 |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     5.1 |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     7.8 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     7.8 |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     7.8 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     3.5 |
| cat08_01_queue_mining              |     5.1 |
| cat08_02_instance_spanning         |     5.6 |
| cat08_03_transport_opt             |     5.6 |
| cat08_04_resource_assign           |     4   |
| cat08_05_task_schedul              |     4   |



### QwenQwen2.5-Coder-32B-Instruct   => 26.1 points

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
| cat02_09_fix_process_tree          |    9.6  |
| cat03_01_process_tree_generation   |    5    |
| cat03_02_powl_generation           |    9    |
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
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    6.5  |
| cat04_07_sql_filt_top_k_vars       |    7.35 |
| cat05_01_hyp_generation_log        |    3.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    6    |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    5    |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    7    |
| cat08_01_queue_mining              |    6.5  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    3.7  |
| cat08_04_resource_assign           |    7.5  |
| cat08_05_task_schedul              |    7.4  |



### qwen2.5-32b-instruct   => 25.7 points

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
| cat02_09_fix_process_tree          |    9    |
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
| cat05_05_question_gen_nlp          |    9.6  |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    7.25 |
| cat06_04_bias_two_logs             |    7.75 |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    5    |
| cat08_01_queue_mining              |    4.5  |
| cat08_02_instance_spanning         |    6.5  |
| cat08_03_transport_opt             |    5    |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    6    |



### qwen2.5-14b-instruct-1m   => 24.0 points

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
| cat04_05_sql_filt_num_events       |    9.6  |
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
| cat08_01_queue_mining              |    7.25 |
| cat08_02_instance_spanning         |    5.5  |
| cat08_03_transport_opt             |    3.5  |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    4    |



### qwen-plus-2025-04-28   => 23.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     4.5 |
| cat01_02_activity_context          |     3.5 |
| cat01_03_high_level_events         |     5.6 |
| cat01_04_sensor_recordings         |     3.5 |
| cat01_05_merge_two_logs            |     2.4 |
| cat01_06_system_logs               |     2.4 |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     5.6 |
| cat02_02_conf_desiderata           |     3.5 |
| cat02_03_anomaly_event_log         |     2.4 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     1.8 |
| cat02_06_root_cause_1              |     2.4 |
| cat02_07_root_cause_2              |     4.5 |
| cat02_08_underfitting_process_tree |     5.6 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     5.6 |
| cat03_03_log_skeleton_generation   |     2.4 |
| cat03_04_declare_generation        |     2.4 |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1.3 |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     3.5 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1.8 |
| cat04_07_sql_filt_top_k_vars       |     1.3 |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     2.4 |
| cat05_04_hyp_gen_temp_profile      |     2.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.3 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     2.4 |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     3.5 |
| cat08_01_queue_mining              |     6.7 |
| cat08_02_instance_spanning         |     7.2 |
| cat08_03_transport_opt             |     5.1 |
| cat08_04_resource_assign           |     7.3 |
| cat08_05_task_schedul              |     7.2 |



### qwen31.7b   => 21.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1.3 |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     6.2 |
| cat01_04_sensor_recordings         |     2.4 |
| cat01_05_merge_two_logs            |     2.4 |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     2.9 |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     2.9 |
| cat02_03_anomaly_event_log         |     1.3 |
| cat02_04_powl_anomaly_detection    |     5.6 |
| cat02_05_two_powls_anomalies       |     5.6 |
| cat02_06_root_cause_1              |     1.3 |
| cat02_07_root_cause_2              |     1.3 |
| cat02_08_underfitting_process_tree |     6.7 |
| cat02_09_fix_process_tree          |     7.8 |
| cat03_01_process_tree_generation   |     1.3 |
| cat03_02_powl_generation           |     2.4 |
| cat03_03_log_skeleton_generation   |     2.4 |
| cat03_04_declare_generation        |     2.4 |
| cat03_05_temp_profile_generation   |     2.4 |
| cat03_06_petri_net_generation      |     5.6 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.4 |
| cat04_01_pseudo_bpmn_description   |     3.5 |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     2.4 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     5.6 |
| cat04_06_sql_filt_three_df         |     1.3 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     4.5 |
| cat05_02_hyp_gen_powl              |     6.2 |
| cat05_03_hyp_gen_declare           |     2.4 |
| cat05_04_hyp_gen_temp_profile      |     2.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7   |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     8.3 |
| cat06_02_bias_event_log            |     4.5 |
| cat06_03_bias_powl                 |     2.9 |
| cat06_04_bias_two_logs             |     5.1 |
| cat06_05_bias_two_logs_2           |     7.3 |
| cat06_06_bias_mitigation_declare   |     2.9 |
| cat06_07_fair_unfair_powl          |     3.5 |
| cat08_01_queue_mining              |     7.5 |
| cat08_02_instance_spanning         |     6.2 |
| cat08_03_transport_opt             |     7.3 |
| cat08_04_resource_assign           |     3.5 |
| cat08_05_task_schedul              |     2.4 |



### qwen2.5-omni-7b   => 21.1 points

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
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    4.5  |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    8.6  |
| cat05_06_question_pseudo_bpmn      |    8.4  |
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
| cat08_01_queue_mining              |    3    |
| cat08_02_instance_spanning         |    5.5  |
| cat08_03_transport_opt             |    5.5  |
| cat08_04_resource_assign           |    4.5  |
| cat08_05_task_schedul              |    5.5  |



### qwen2.5-7b-instruct-1m   => 19.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     3.5 |
| cat01_05_merge_two_logs            |     1.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     4   |
| cat02_04_powl_anomaly_detection    |     3.5 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     5   |
| cat02_09_fix_process_tree          |     4   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     3   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     7.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     5.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     4   |
| cat06_04_bias_two_logs             |     4.5 |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     3   |
| cat08_01_queue_mining              |     6   |
| cat08_02_instance_spanning         |     5   |
| cat08_03_transport_opt             |     5   |
| cat08_04_resource_assign           |     6.5 |
| cat08_05_task_schedul              |     5   |



### deepseekdeepseek-r1-distill-qwen-7b   => 18.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1.3 |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     3.5 |
| cat01_05_merge_two_logs            |     1.3 |
| cat01_06_system_logs               |     1.8 |
| cat01_07_interv_to_pseudo_bpmn     |     2.4 |
| cat01_08_tables_to_log             |     1.8 |
| cat02_01_conformance_textual       |     2.4 |
| cat02_02_conf_desiderata           |     3.5 |
| cat02_03_anomaly_event_log         |     1.3 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     2.4 |
| cat02_06_root_cause_1              |     2.4 |
| cat02_07_root_cause_2              |     5.6 |
| cat02_08_underfitting_process_tree |     2.4 |
| cat02_09_fix_process_tree          |     4.5 |
| cat03_01_process_tree_generation   |     2.4 |
| cat03_02_powl_generation           |     3.5 |
| cat03_03_log_skeleton_generation   |     2.4 |
| cat03_04_declare_generation        |     1.8 |
| cat03_05_temp_profile_generation   |     6.2 |
| cat03_06_petri_net_generation      |     7.5 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.3 |
| cat04_01_pseudo_bpmn_description   |     2.9 |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     4.5 |
| cat04_04_declare_description       |     2.4 |
| cat04_05_sql_filt_num_events       |     7   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1.3 |
| cat05_01_hyp_generation_log        |     1.8 |
| cat05_02_hyp_gen_powl              |     2.4 |
| cat05_03_hyp_gen_declare           |     3.5 |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     5.6 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     3.5 |
| cat06_02_bias_event_log            |     7.3 |
| cat06_03_bias_powl                 |     1.8 |
| cat06_04_bias_two_logs             |     5.6 |
| cat06_05_bias_two_logs_2           |     7.8 |
| cat06_06_bias_mitigation_declare   |     1.8 |
| cat06_07_fair_unfair_powl          |     1.8 |
| cat08_01_queue_mining              |     2.9 |
| cat08_02_instance_spanning         |     3.5 |
| cat08_03_transport_opt             |     3.5 |
| cat08_04_resource_assign           |     5.6 |
| cat08_05_task_schedul              |     2.4 |



### qwen30.6b   => 13.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     1.8 |
| cat01_04_sensor_recordings         |     1.8 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1.8 |
| cat01_07_interv_to_pseudo_bpmn     |     2.4 |
| cat01_08_tables_to_log             |     2.4 |
| cat02_01_conformance_textual       |     1.3 |
| cat02_02_conf_desiderata           |     2.4 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     7.3 |
| cat02_05_two_powls_anomalies       |     2.4 |
| cat02_06_root_cause_1              |     2.4 |
| cat02_07_root_cause_2              |     1.3 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1.3 |
| cat03_08_powl_discovery            |     6.7 |
| cat04_01_pseudo_bpmn_description   |     1.8 |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     2.9 |
| cat04_04_declare_description       |     1.3 |
| cat04_05_sql_filt_num_events       |     1.3 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     2.4 |
| cat05_03_hyp_gen_declare           |     1.3 |
| cat05_04_hyp_gen_temp_profile      |     1.3 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     7.3 |
| cat05_07_question_interview        |     6.7 |
| cat06_01_bias_text                 |     6.7 |
| cat06_02_bias_event_log            |     7.3 |
| cat06_03_bias_powl                 |     1.3 |
| cat06_04_bias_two_logs             |     6.2 |
| cat06_05_bias_two_logs_2           |     1.3 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1.3 |
| cat08_01_queue_mining              |     3.5 |
| cat08_02_instance_spanning         |     2.9 |
| cat08_03_transport_opt             |     3.5 |
| cat08_04_resource_assign           |     4   |
| cat08_05_task_schedul              |     2.4 |



### deepseekdeepseek-r1-distill-qwen-1.5b   => 11.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1.3 |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     3.5 |
| cat01_04_sensor_recordings         |     1.3 |
| cat01_05_merge_two_logs            |     1.3 |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     2.4 |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     1.3 |
| cat02_02_conf_desiderata           |     1.3 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     1.3 |
| cat02_06_root_cause_1              |     1.3 |
| cat02_07_root_cause_2              |     2.4 |
| cat02_08_underfitting_process_tree |     1.3 |
| cat02_09_fix_process_tree          |     1.3 |
| cat03_01_process_tree_generation   |     1.3 |
| cat03_02_powl_generation           |     1.3 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2.4 |
| cat03_06_petri_net_generation      |     1.3 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     2.4 |
| cat04_02_pseudo_bpmn_open_question |     2.4 |
| cat04_03_declare_open_question     |     2.4 |
| cat04_04_declare_description       |     1.3 |
| cat04_05_sql_filt_num_events       |     1.3 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     7.8 |
| cat05_02_hyp_gen_powl              |     2.4 |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     2.4 |
| cat05_05_question_gen_nlp          |     7.8 |
| cat05_06_question_pseudo_bpmn      |     3.5 |
| cat05_07_question_interview        |     3.5 |
| cat06_01_bias_text                 |     5.6 |
| cat06_02_bias_event_log            |     2.4 |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     1   |
| cat06_05_bias_two_logs_2           |     2.4 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1.3 |
| cat08_01_queue_mining              |     2.9 |
| cat08_02_instance_spanning         |     1   |
| cat08_03_transport_opt             |     1.3 |
| cat08_04_resource_assign           |     1.8 |
| cat08_05_task_schedul              |     2.4 |

