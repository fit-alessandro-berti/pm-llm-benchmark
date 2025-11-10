A score in the range **27-34** is considered **sufficient**; a score in the range **34-38** is considered **fair**; a score in the range **38-44** is considered **good**; and a score **>44** is considered **excellent**.

## QWEN Leaderboard (1-shot; x-ai/grok-4-fast used as a judge)

| Model                          | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | OPT                  | :nerd_face: VI       |
|:-------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| Qwen3-235B-A22B-Thinking-2507  | **43.3** | :white_check_mark: | :white_check_mark: | 6.4                  | 7.5                  | :mage_woman: **6.6** | 5.7                  | **6.3**              | **6.0**              | :mage_woman: **4.8** | 0.0                  |
| qwen3-next-80b-a3b-thinking    | **41.3** | :white_check_mark: | :white_check_mark: | 6.2                  | 7.0                  | 4.5                  | :mage_woman: **6.4** | :mage_woman: **6.4** | :mage_woman: **6.1** | **4.5**              | 0.0                  |
| qwen3-max                      | **41.2** | :x:                | :x:                | 6.6                  | 6.8                  | 5.6                  | 6.0                  | 6.0                  | **5.9**              | 4.3                  | 0.0                  |
| qwen3-235b-a22b-07-25          | **39.5** | :white_check_mark: | :white_check_mark: | 6.0                  | 7.0                  | 3.5                  | :mage_woman: **6.4** | 6.1                  | :mage_woman: **6.1** | **4.5**              | 0.0                  |
| Qwen3-14B                      | **38.9** | :white_check_mark: | :white_check_mark: | 6.0                  | 7.6                  | 3.8                  | 5.9                  | 5.6                  | **5.9**              | 4.0                  | 0.0                  |
| Qwen3-32B                      | **38.0** | :white_check_mark: | :white_check_mark: | :mage_woman: **6.9** | 6.6                  | 3.9                  | 5.5                  | 5.6                  | 5.1                  | 4.3                  | 0.0                  |
| qwen34b-thinking-2507-q8_0     | **37.4** | :white_check_mark: | :white_check_mark: | 6.0                  | :mage_woman: **7.9** | 4.9                  | 4.4                  | 5.4                  | 5.0                  | 3.8                  | 0.0                  |
| qwen3-next-80b-a3b-instruct    | **36.8** | :white_check_mark: | :x:                | 6.2                  | 6.0                  | 3.6                  | 5.4                  | 6.1                  | **5.9**              | 3.6                  | 0.0                  |
| Qwen3-30B-A3B-2507-Thinking    | **35.7** | :white_check_mark: | :white_check_mark: | 4.5                  | 6.5                  | 5.1                  | 5.1                  | 5.4                  | 4.9                  | 4.3                  | 0.0                  |
| qwen3-coder                    | **35.6** | :white_check_mark: | :x:                | 5.6                  | 6.2                  | 3.2                  | 5.7                  | 5.6                  | 5.4                  | 3.9                  | 0.0                  |
| QwQ-32B-Preview                | **35.6** | :white_check_mark: | :white_check_mark: | 5.8                  | 7.0                  | 5.0                  | 5.1                  | 4.2                  | 5.5                  | 3.1                  | 0.0                  |
| qwen2.5-72b-instruct           | **35.4** | :white_check_mark: | :x:                | 6.3                  | 6.3                  | 4.2                  | 4.9                  | 4.9                  | 5.0                  | 3.8                  | 0.0                  |
| qwen38b                        | **35.2** | :white_check_mark: | :white_check_mark: | 5.1                  | 6.5                  | 3.8                  | 5.2                  | 5.7                  | 5.1                  | 3.9                  | 0.0                  |
| qwen34b-instruct-2507-q8_0     | **33.9** | :white_check_mark: | :x:                | 5.4                  | 5.9                  | 3.1                  | 4.7                  | 5.3                  | 5.1                  | 4.3                  | 0.0                  |
| qwen3-30b-a3b-instruct-2507    | **33.8** | :white_check_mark: | :x:                | 5.2                  | 5.6                  | 4.0                  | 4.6                  | 5.3                  | 5.3                  | 3.9                  | 0.0                  |
| Qwen-3-14B-nothink             | **33.5** | :white_check_mark: | :x:                | 5.7                  | 5.9                  | 2.5                  | 5.5                  | 4.9                  | **5.8**              | 3.3                  | 0.0                  |
| qwen2.5-32b-instruct           | **33.5** | :white_check_mark: | :x:                | 5.9                  | 5.7                  | 3.2                  | 4.7                  | 5.4                  | 5.3                  | 3.2                  | 0.0                  |
| Qwen-3-32B-nothink             | **33.1** | :white_check_mark: | :x:                | 5.7                  | 6.3                  | 3.5                  | 3.3                  | 5.4                  | 5.3                  | 3.6                  | 0.0                  |
| Qwen2.5-Coder-32B-Instruct     | **31.9** | :white_check_mark: | :x:                | 5.2                  | 5.1                  | 3.4                  | 5.0                  | 4.6                  | 5.0                  | 3.6                  | 0.0                  |
| qwen-qwq-32b-nostepbystep      | **31.0** | :white_check_mark: | :white_check_mark: | 4.6                  | 5.3                  | 1.1                  | 5.2                  | 5.4                  | 5.4                  | 4.1                  | 0.0                  |
| qwen34b                        | **30.6** | :white_check_mark: | :white_check_mark: | 4.7                  | 6.2                  | 1.9                  | 4.7                  | 4.9                  | 4.4                  | 3.7                  | 0.0                  |
| cogito14b-v1-preview-qwen-fp16 | **29.3** | :white_check_mark: | :white_check_mark: | 4.4                  | 5.3                  | 2.8                  | 3.7                  | 5.0                  | 4.9                  | 3.2                  | 0.0                  |
| qwen-qwq-32b-stepbystep        | **29.1** | :white_check_mark: | :white_check_mark: | 3.8                  | 6.0                  | 1.6                  | 5.3                  | 4.3                  | 4.5                  | 3.6                  | 0.0                  |
| qwen2.5-14b-instruct-1m        | **28.1** | :white_check_mark: | :x:                | 4.7                  | 5.1                  | 2.5                  | 3.9                  | 5.1                  | 4.0                  | 2.7                  | 0.0                  |
| qwen2.5-omni-7b                | **25.3** | :white_check_mark: | :x:                | 4.1                  | 4.7                  | 2.1                  | 4.1                  | 3.9                  | 4.3                  | 2.1                  | :mage_woman: **4.8** |
| qwen2.5-7b-instruct-1m         | **25.0** | :white_check_mark: | :x:                | 3.8                  | 4.4                  | 2.3                  | 3.1                  | 4.3                  | 3.8                  | 3.2                  | 0.0                  |
| qwen31.7b                      | **21.3** | :white_check_mark: | :white_check_mark: | 2.6                  | 3.7                  | 1.4                  | 2.9                  | 3.8                  | 3.9                  | 3.1                  | 0.0                  |
| qwen30.6b                      | **14.2** | :white_check_mark: | :white_check_mark: | 1.6                  | 3.3                  | 1.1                  | 1.8                  | 3.0                  | 2.2                  | 1.3                  | 0.0                  |

### Qwen3-235B-A22B-Thinking-2507   => 43.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.2 |
| cat01_02_activity_context          |     9.5 |
| cat01_03_high_level_events         |     6.8 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     6.7 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     8.2 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     3.7 |
| cat02_07_root_cause_2              |     7.4 |
| cat02_08_underfitting_process_tree |     9.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.9 |
| cat03_04_declare_generation        |     6.8 |
| cat03_05_temp_profile_generation   |     9.5 |
| cat03_06_petri_net_generation      |     9.5 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |    10   |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     9.5 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     8.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |    10   |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     3.1 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |    10   |
| cat08_03_transport_opt             |    10   |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     8.9 |



### qwenqwen3-next-80b-a3b-thinking   => 41.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     6.7 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     8.9 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |     9.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     8.9 |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     9.5 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     8.9 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     9.3 |
| cat05_04_hyp_gen_temp_profile      |     8.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     9.5 |
| cat06_07_fair_unfair_powl          |     7.4 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     9.5 |
| cat08_04_resource_assign           |     9.3 |
| cat08_05_task_schedul              |     8.9 |



### qwenqwen3-max   => 41.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    8.4  |
| cat01_02_activity_context          |    7.6  |
| cat01_03_high_level_events         |    9    |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    8.4  |
| cat01_06_system_logs               |    7.6  |
| cat01_07_interv_to_pseudo_bpmn     |    8    |
| cat01_08_tables_to_log             |    8.4  |
| cat02_01_conformance_textual       |   10    |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |    8    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    7.1  |
| cat02_06_root_cause_1              |    7.25 |
| cat02_07_root_cause_2              |    7.1  |
| cat02_08_underfitting_process_tree |    3.5  |
| cat02_09_fix_process_tree          |    9.6  |
| cat03_01_process_tree_generation   |    7.25 |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    9    |
| cat03_06_petri_net_generation      |    7.5  |
| cat03_07_process_tree_discovery    |    9.6  |
| cat03_08_powl_discovery            |    7.25 |
| cat04_01_pseudo_bpmn_description   |    9    |
| cat04_02_pseudo_bpmn_open_question |    9.4  |
| cat04_03_declare_open_question     |    7.1  |
| cat04_04_declare_description       |    7    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |   10    |
| cat04_07_sql_filt_top_k_vars       |   10    |
| cat05_01_hyp_generation_log        |    8    |
| cat05_02_hyp_gen_powl              |    6.5  |
| cat05_03_hyp_gen_declare           |    9    |
| cat05_04_hyp_gen_temp_profile      |    6.5  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    9.6  |
| cat06_01_bias_text                 |    9    |
| cat06_02_bias_event_log            |    8.4  |
| cat06_03_bias_powl                 |    9    |
| cat06_04_bias_two_logs             |    7.75 |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    7.5  |
| cat06_07_fair_unfair_powl          |    9.6  |
| cat08_01_queue_mining              |    9.6  |
| cat08_02_instance_spanning         |    7.6  |
| cat08_03_transport_opt             |    9    |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    8.4  |



### qwenqwen3-235b-a22b-07-25   => 39.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     7.2 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     6.8 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     9.5 |
| cat01_08_tables_to_log             |     7.1 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     6.7 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     7.1 |
| cat03_01_process_tree_generation   |     8.9 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     1.4 |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     3.7 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     9.5 |
| cat04_04_declare_description       |     7.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     8.9 |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     7.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     6.8 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     9.8 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |    10   |
| cat08_05_task_schedul              |     7.1 |



### QwenQwen3-14B   => 38.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     6.8 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     6.6 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     4.8 |
| cat03_02_powl_generation           |     3.7 |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     5.4 |
| cat03_05_temp_profile_generation   |     6.7 |
| cat03_06_petri_net_generation      |     3.7 |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     7.4 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     7.4 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     6.8 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     7.7 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     6.8 |



### QwenQwen3-32B   => 38.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     9.5 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     9.5 |
| cat01_05_merge_two_logs            |    10   |
| cat01_06_system_logs               |     6.8 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     6.7 |
| cat02_01_conformance_textual       |     6.6 |
| cat02_02_conf_desiderata           |     3.7 |
| cat02_03_anomaly_event_log         |     7.4 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     3.7 |
| cat02_07_root_cause_2              |     6.8 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.2 |
| cat03_03_log_skeleton_generation   |     6.6 |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     3.7 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     6.7 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     7.2 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     6   |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     8.2 |



### qwen34b-thinking-2507-q8_0   => 37.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     8.2 |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     6.8 |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     7.4 |
| cat03_04_declare_generation        |     6.7 |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |    10   |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     4.5 |
| cat05_03_hyp_gen_declare           |    10   |
| cat05_04_hyp_gen_temp_profile      |     8.2 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     7.1 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     6.7 |
| cat08_05_task_schedul              |     8.2 |



### qwenqwen3-next-80b-a3b-instruct   => 36.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    7.1  |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    7    |
| cat01_06_system_logs               |    8    |
| cat01_07_interv_to_pseudo_bpmn     |    8    |
| cat01_08_tables_to_log             |    5.5  |
| cat02_01_conformance_textual       |    9.6  |
| cat02_02_conf_desiderata           |    1    |
| cat02_03_anomaly_event_log         |   10    |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    9    |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    7.1  |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    8.4  |
| cat03_01_process_tree_generation   |    4.2  |
| cat03_02_powl_generation           |    8.4  |
| cat03_03_log_skeleton_generation   |    7.1  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    7.25 |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    4    |
| cat03_08_powl_discovery            |    3.5  |
| cat04_01_pseudo_bpmn_description   |    9    |
| cat04_02_pseudo_bpmn_open_question |    8.4  |
| cat04_03_declare_open_question     |    1    |
| cat04_04_declare_description       |    7.6  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    9.6  |
| cat04_07_sql_filt_top_k_vars       |    8    |
| cat05_01_hyp_generation_log        |    8.4  |
| cat05_02_hyp_gen_powl              |    8.2  |
| cat05_03_hyp_gen_declare           |    8.4  |
| cat05_04_hyp_gen_temp_profile      |    7.1  |
| cat05_05_question_gen_nlp          |    9    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    9.6  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    7.6  |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    8.4  |
| cat06_05_bias_two_logs_2           |    7.75 |
| cat06_06_bias_mitigation_declare   |    8    |
| cat06_07_fair_unfair_powl          |   10    |
| cat08_01_queue_mining              |    7.25 |
| cat08_02_instance_spanning         |    8.2  |
| cat08_03_transport_opt             |    8.4  |
| cat08_04_resource_assign           |    4.2  |
| cat08_05_task_schedul              |    8.4  |



### Qwen3-30B-A3B-2507-Thinking   => 35.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     3.7 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.8 |
| cat01_08_tables_to_log             |     3.7 |
| cat02_01_conformance_textual       |     6.7 |
| cat02_02_conf_desiderata           |     4.8 |
| cat02_03_anomaly_event_log         |     6.6 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     4.2 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     7.4 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     6.8 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |    10   |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     6.6 |
| cat08_03_transport_opt             |     9.3 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     8.9 |



### qwenqwen3-coder   => 35.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.25 |
| cat01_02_activity_context          |    8    |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    6.5  |
| cat01_06_system_logs               |    5.2  |
| cat01_07_interv_to_pseudo_bpmn     |    8.4  |
| cat01_08_tables_to_log             |    3.5  |
| cat02_01_conformance_textual       |    7    |
| cat02_02_conf_desiderata           |    7.25 |
| cat02_03_anomaly_event_log         |    8    |
| cat02_04_powl_anomaly_detection    |    8    |
| cat02_05_two_powls_anomalies       |    7.25 |
| cat02_06_root_cause_1              |    5    |
| cat02_07_root_cause_2              |    7.1  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    7.5  |
| cat03_03_log_skeleton_generation   |    5    |
| cat03_04_declare_generation        |    6.5  |
| cat03_05_temp_profile_generation   |    5    |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    3.5  |
| cat04_01_pseudo_bpmn_description   |    8.4  |
| cat04_02_pseudo_bpmn_open_question |    8.4  |
| cat04_03_declare_open_question     |    7.6  |
| cat04_04_declare_description       |    5    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    8.4  |
| cat04_07_sql_filt_top_k_vars       |    9.6  |
| cat05_01_hyp_generation_log        |    6.2  |
| cat05_02_hyp_gen_powl              |    7.6  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    7.25 |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |   10    |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    7.25 |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    7.25 |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    4.5  |
| cat06_07_fair_unfair_powl          |   10    |
| cat08_01_queue_mining              |    8.4  |
| cat08_02_instance_spanning         |    7.6  |
| cat08_03_transport_opt             |    7.6  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    7.1  |



### QwenQwQ-32B-Preview   => 35.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.7 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     7.4 |
| cat01_06_system_logs               |     7.7 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |     7.1 |
| cat02_02_conf_desiderata           |     6.8 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     8.2 |
| cat02_05_two_powls_anomalies       |     5.4 |
| cat02_06_root_cause_1              |     9.5 |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |     6.8 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     6.7 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     6.6 |
| cat03_05_temp_profile_generation   |     7.1 |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     6.8 |
| cat04_03_declare_open_question     |     6.8 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     1   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     6.6 |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     1.4 |
| cat08_05_task_schedul              |     2.8 |



### qwen2.5-72b-instruct   => 35.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    7.1  |
| cat01_03_high_level_events         |    7.1  |
| cat01_04_sensor_recordings         |    9    |
| cat01_05_merge_two_logs            |    6.5  |
| cat01_06_system_logs               |    7.5  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    8.4  |
| cat02_01_conformance_textual       |    6.5  |
| cat02_02_conf_desiderata           |    6.5  |
| cat02_03_anomaly_event_log         |    8.4  |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    4.2  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    7    |
| cat02_08_underfitting_process_tree |    7.75 |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    8    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    6.5  |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    6.5  |
| cat04_01_pseudo_bpmn_description   |    8    |
| cat04_02_pseudo_bpmn_open_question |    7.1  |
| cat04_03_declare_open_question     |    6    |
| cat04_04_declare_description       |    1    |
| cat04_05_sql_filt_num_events       |    7.25 |
| cat04_06_sql_filt_three_df         |   10    |
| cat04_07_sql_filt_top_k_vars       |   10    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |   10    |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    6.5  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    4.2  |
| cat05_07_question_interview        |   10    |
| cat06_01_bias_text                 |    9    |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    7.1  |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |   10    |
| cat08_01_queue_mining              |    7.6  |
| cat08_02_instance_spanning         |    7.1  |
| cat08_03_transport_opt             |    7.1  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    7.5  |



### qwen38b   => 35.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     7.2 |
| cat01_04_sensor_recordings         |     3.7 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     7.1 |
| cat02_02_conf_desiderata           |     3.7 |
| cat02_03_anomaly_event_log         |     6.8 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     6.6 |
| cat02_06_root_cause_1              |     4.2 |
| cat02_07_root_cause_2              |     6.8 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     7.7 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3.7 |
| cat03_06_petri_net_generation      |     3.7 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     7.4 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     6.8 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     7.4 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     8.2 |



### qwen34b-instruct-2507-q8_0   => 33.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    4.2  |
| cat01_02_activity_context          |    8.4  |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    9.6  |
| cat01_05_merge_two_logs            |    4.5  |
| cat01_06_system_logs               |    7.75 |
| cat01_07_interv_to_pseudo_bpmn     |    8.4  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    7.6  |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    7.1  |
| cat02_06_root_cause_1              |    4.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    7    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    5    |
| cat03_02_powl_generation           |    5    |
| cat03_03_log_skeleton_generation   |    4    |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    5    |
| cat03_06_petri_net_generation      |    2.5  |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    4.5  |
| cat04_01_pseudo_bpmn_description   |    7.75 |
| cat04_02_pseudo_bpmn_open_question |    8.4  |
| cat04_03_declare_open_question     |    7.1  |
| cat04_04_declare_description       |    5.5  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    7.25 |
| cat05_01_hyp_generation_log        |    7    |
| cat05_02_hyp_gen_powl              |    7.1  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    7.1  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    9.6  |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    7.1  |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    7.25 |
| cat06_05_bias_two_logs_2           |    8    |
| cat06_06_bias_mitigation_declare   |    6.5  |
| cat06_07_fair_unfair_powl          |    5.5  |
| cat08_01_queue_mining              |    9    |
| cat08_02_instance_spanning         |    8.4  |
| cat08_03_transport_opt             |    9    |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    8    |



### qwenqwen3-30b-a3b-instruct-2507   => 33.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    6.5  |
| cat01_03_high_level_events         |    7    |
| cat01_04_sensor_recordings         |    5    |
| cat01_05_merge_two_logs            |    5    |
| cat01_06_system_logs               |    8    |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    3.5  |
| cat02_01_conformance_textual       |    7.1  |
| cat02_02_conf_desiderata           |    7.6  |
| cat02_03_anomaly_event_log         |    7    |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    7    |
| cat02_06_root_cause_1              |    7.1  |
| cat02_07_root_cause_2              |    1.5  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    8.4  |
| cat03_01_process_tree_generation   |    4.5  |
| cat03_02_powl_generation           |    7    |
| cat03_03_log_skeleton_generation   |    6.5  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    7.25 |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    4    |
| cat03_08_powl_discovery            |    7.5  |
| cat04_01_pseudo_bpmn_description   |    8.4  |
| cat04_02_pseudo_bpmn_open_question |    8.4  |
| cat04_03_declare_open_question     |    8    |
| cat04_04_declare_description       |    3.2  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    4    |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    1    |
| cat05_02_hyp_gen_powl              |    7.1  |
| cat05_03_hyp_gen_declare           |    7.75 |
| cat05_04_hyp_gen_temp_profile      |    7.1  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |   10    |
| cat06_01_bias_text                 |    9    |
| cat06_02_bias_event_log            |    9    |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |   10    |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    1    |
| cat06_07_fair_unfair_powl          |    8.4  |
| cat08_01_queue_mining              |   10    |
| cat08_02_instance_spanning         |    8.4  |
| cat08_03_transport_opt             |    1    |
| cat08_04_resource_assign           |    9.6  |
| cat08_05_task_schedul              |    9.6  |



### Qwen-3-14B-nothink   => 33.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8.4  |
| cat01_03_high_level_events         |    9    |
| cat01_04_sensor_recordings         |    7    |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    8.4  |
| cat01_08_tables_to_log             |    7.5  |
| cat02_01_conformance_textual       |    7.25 |
| cat02_02_conf_desiderata           |    4.5  |
| cat02_03_anomaly_event_log         |    9    |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    7.1  |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    6.5  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    9    |
| cat03_01_process_tree_generation   |    3.5  |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    3.5  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    6.5  |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    7.6  |
| cat04_02_pseudo_bpmn_open_question |    7.75 |
| cat04_03_declare_open_question     |    7.1  |
| cat04_04_declare_description       |    5.2  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    7.25 |
| cat04_07_sql_filt_top_k_vars       |    9.6  |
| cat05_01_hyp_generation_log        |    7.5  |
| cat05_02_hyp_gen_powl              |    6.5  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    7.1  |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    7.75 |
| cat06_02_bias_event_log            |    9    |
| cat06_03_bias_powl                 |    7    |
| cat06_04_bias_two_logs             |    8    |
| cat06_05_bias_two_logs_2           |   10    |
| cat06_06_bias_mitigation_declare   |    6.2  |
| cat06_07_fair_unfair_powl          |    9.6  |
| cat08_01_queue_mining              |    7.5  |
| cat08_02_instance_spanning         |    7.5  |
| cat08_03_transport_opt             |    7.6  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    1.8  |



### qwen2.5-32b-instruct   => 33.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8.4  |
| cat01_03_high_level_events         |    7.75 |
| cat01_04_sensor_recordings         |    9    |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    7    |
| cat02_01_conformance_textual       |    9    |
| cat02_02_conf_desiderata           |    3.5  |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    6.5  |
| cat02_06_root_cause_1              |    6.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    2.5  |
| cat03_02_powl_generation           |    7    |
| cat03_03_log_skeleton_generation   |    2.5  |
| cat03_04_declare_generation        |    5    |
| cat03_05_temp_profile_generation   |    7.25 |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    3.5  |
| cat04_01_pseudo_bpmn_description   |    8    |
| cat04_02_pseudo_bpmn_open_question |    7    |
| cat04_03_declare_open_question     |    5    |
| cat04_04_declare_description       |    4.2  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    4    |
| cat04_07_sql_filt_top_k_vars       |    9    |
| cat05_01_hyp_generation_log        |    7.1  |
| cat05_02_hyp_gen_powl              |    7.75 |
| cat05_03_hyp_gen_declare           |    7.25 |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    7    |
| cat06_02_bias_event_log            |    7    |
| cat06_03_bias_powl                 |    8    |
| cat06_04_bias_two_logs             |    8    |
| cat06_05_bias_two_logs_2           |    9    |
| cat06_06_bias_mitigation_declare   |    4.2  |
| cat06_07_fair_unfair_powl          |   10    |
| cat08_01_queue_mining              |    7.1  |
| cat08_02_instance_spanning         |    6.2  |
| cat08_03_transport_opt             |    4.5  |
| cat08_04_resource_assign           |    7.25 |
| cat08_05_task_schedul              |    7.1  |



### Qwen-3-32B-nothink   => 33.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     8.4 |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     7   |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     8.4 |
| cat02_04_powl_anomaly_detection    |     9.6 |
| cat02_05_two_powls_anomalies       |     7.5 |
| cat02_06_root_cause_1              |     5   |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |     3.5 |
| cat02_09_fix_process_tree          |     9.6 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     6.5 |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     7   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4.5 |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     8   |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     5.2 |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     4.5 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     7   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.6 |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     9.6 |
| cat06_04_bias_two_logs             |     8.4 |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     7.1 |
| cat08_01_queue_mining              |     8.4 |
| cat08_02_instance_spanning         |     7.5 |
| cat08_03_transport_opt             |     7.5 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     5.1 |



### QwenQwen2.5-Coder-32B-Instruct   => 31.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    7.1  |
| cat01_05_merge_two_logs            |    6.2  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    6.2  |
| cat01_08_tables_to_log             |    6.5  |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    4.5  |
| cat02_03_anomaly_event_log         |    7.25 |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    4.5  |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    2.5  |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    4    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    5    |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    2.5  |
| cat03_08_powl_discovery            |    6.5  |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    7.1  |
| cat04_03_declare_open_question     |    7.1  |
| cat04_04_declare_description       |    3.5  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    7    |
| cat04_07_sql_filt_top_k_vars       |    9.6  |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    7.1  |
| cat05_03_hyp_gen_declare           |    4.5  |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    9    |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |   10    |
| cat08_01_queue_mining              |    7.1  |
| cat08_02_instance_spanning         |    7.1  |
| cat08_03_transport_opt             |    7.6  |
| cat08_04_resource_assign           |    7.1  |
| cat08_05_task_schedul              |    7.1  |



### qwen-qwq-32b-nostepbystep   => 31.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.5 |
| cat01_02_activity_context          |     7.2 |
| cat01_03_high_level_events         |     7.2 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     3.7 |
| cat02_01_conformance_textual       |     6.6 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     9.5 |
| cat02_06_root_cause_1              |     1.4 |
| cat02_07_root_cause_2              |     3.7 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     1   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     3.1 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1.4 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     3.7 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     5.4 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     6.8 |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     5.4 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     7.2 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     8.2 |



### qwen34b   => 30.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |     6.7 |
| cat01_04_sensor_recordings         |     6.6 |
| cat01_05_merge_two_logs            |     3.7 |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     7.1 |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     2.2 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     5.4 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     1.4 |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     6.6 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     3.7 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     7.2 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     6.6 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     4.2 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     6.6 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



### cogito14b-v1-preview-qwen-fp16   => 29.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2.5 |
| cat01_02_activity_context          |     3.1 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     7.4 |
| cat01_05_merge_two_logs            |     6.8 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     3.7 |
| cat02_01_conformance_textual       |     6.8 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     3.7 |
| cat02_06_root_cause_1              |     6.8 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |     3.7 |
| cat02_09_fix_process_tree          |     7.4 |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     1.4 |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     6.7 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1.4 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     6.8 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     3.7 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     3.3 |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     7.2 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     3.7 |
| cat06_07_fair_unfair_powl          |     3.7 |
| cat08_01_queue_mining              |     6.7 |
| cat08_02_instance_spanning         |     6.8 |
| cat08_03_transport_opt             |     6.8 |
| cat08_04_resource_assign           |     6   |
| cat08_05_task_schedul              |     5.4 |



### qwen-qwq-32b-stepbystep   => 29.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.1 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     6.8 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     6.6 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     1   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     7.7 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     1   |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |    10   |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     5.4 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     6.7 |
| cat08_02_instance_spanning         |     7.4 |
| cat08_03_transport_opt             |     5.6 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



### qwen2.5-14b-instruct-1m   => 28.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.5 |
| cat01_02_activity_context          |     8.4 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     6.2 |
| cat01_05_merge_two_logs            |     7   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     7.6 |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     6.5 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     4.5 |
| cat02_06_root_cause_1              |     1.8 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     2.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     3.2 |
| cat04_02_pseudo_bpmn_open_question |     9   |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     4   |
| cat04_07_sql_filt_top_k_vars       |     3.5 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     6.2 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.6 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     6.2 |
| cat06_03_bias_powl                 |     1   |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     6   |
| cat08_01_queue_mining              |     5   |
| cat08_02_instance_spanning         |     6   |
| cat08_03_transport_opt             |     3.2 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     6.2 |



### qwen2.5-omni-7b   => 25.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3.5  |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    7.1  |
| cat01_04_sensor_recordings         |    4.2  |
| cat01_05_merge_two_logs            |    4.2  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    4.5  |
| cat02_01_conformance_textual       |    3.5  |
| cat02_02_conf_desiderata           |    5    |
| cat02_03_anomaly_event_log         |    4    |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    6    |
| cat02_09_fix_process_tree          |    8.4  |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    4.2  |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    2.5  |
| cat03_06_petri_net_generation      |    2.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2.5  |
| cat04_01_pseudo_bpmn_description   |    7.5  |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    6.2  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    9.6  |
| cat05_01_hyp_generation_log        |    3.5  |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    4.2  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    7.6  |
| cat05_07_question_interview        |    9.6  |
| cat06_01_bias_text                 |    9.6  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    7    |
| cat06_04_bias_two_logs             |    4.2  |
| cat06_05_bias_two_logs_2           |    9    |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    3.5  |
| cat07_01_ocdfg                     |    7.25 |
| cat07_02_bpmn_orders               |    7.85 |
| cat07_03_bpmn_dispatch             |    8    |
| cat07_04_causal_net                |    8    |
| cat07_05_proclets                  |    9    |
| cat07_06_perf_spectrum             |    7.75 |
| cat08_01_queue_mining              |    4.5  |
| cat08_02_instance_spanning         |    1    |
| cat08_03_transport_opt             |    5.5  |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    3.5  |



### qwen2.5-7b-instruct-1m   => 25.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.5 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     9   |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     6.5 |
| cat02_04_powl_anomaly_detection    |     7.1 |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     5   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     6.2 |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     4.2 |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     4.5 |
| cat05_01_hyp_generation_log        |     3.5 |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     5.2 |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     7.6 |
| cat06_01_bias_text                 |     7.5 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     5.5 |
| cat08_02_instance_spanning         |     6.5 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     7.5 |
| cat08_05_task_schedul              |     5   |



### qwen31.7b   => 21.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     6.7 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3.3 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     2.5 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     1.4 |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     6.6 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     6.8 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1.4 |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     3.1 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     6.8 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     3.7 |
| cat06_04_bias_two_logs             |     6.7 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     3.7 |
| cat08_01_queue_mining              |     6.7 |
| cat08_02_instance_spanning         |     5.6 |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     6.7 |
| cat08_05_task_schedul              |     3.3 |



### qwen30.6b   => 14.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     3.3 |
| cat01_04_sensor_recordings         |     2.5 |
| cat01_05_merge_two_logs            |     3.7 |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     2.5 |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |     2.2 |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     1.4 |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     3.3 |
| cat04_02_pseudo_bpmn_open_question |     3.3 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     2.5 |
| cat05_03_hyp_gen_declare           |     1.4 |
| cat05_04_hyp_gen_temp_profile      |     2.5 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |     6.6 |
| cat06_01_bias_text                 |     6.6 |
| cat06_02_bias_event_log            |     6.8 |
| cat06_03_bias_powl                 |     2.5 |
| cat06_04_bias_two_logs             |     2.5 |
| cat06_05_bias_two_logs_2           |     1   |
| cat06_06_bias_mitigation_declare   |     1.4 |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     2   |
| cat08_02_instance_spanning         |     2.5 |
| cat08_03_transport_opt             |     3.1 |
| cat08_04_resource_assign           |     3.1 |
| cat08_05_task_schedul              |     2.5 |

