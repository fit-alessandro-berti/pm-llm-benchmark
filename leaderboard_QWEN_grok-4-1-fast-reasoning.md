A score in the range **27-34** is considered **sufficient**; a score in the range **34-38** is considered **fair**; a score in the range **38-44** is considered **good**; and a score **>44** is considered **excellent**.

## QWEN Leaderboard (1-shot; grok-4-1-fast-reasoning used as a judge)

| Model                         | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | OPT                  | :nerd_face: VI       |
|:------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| Qwen3-235B-A22B-Thinking-2507 | **43.9** | :white_check_mark: | :white_check_mark: | :mage_woman: **6.8** | 7.5                  | :mage_woman: **6.9** | 5.7                  | 5.8                  | :mage_woman: **6.3** | :mage_woman: **4.8** | :mage_woman: **0.0** |
| qwen3-next-80b-a3b-thinking   | **41.8** | :white_check_mark: | :white_check_mark: | **6.7**              | 7.6                  | 5.1                  | 6.1                  | **6.2**              | 5.7                  | 4.3                  | :mage_woman: **0.0** |
| qwen3-235b-a22b-07-25         | **41.4** | :white_check_mark: | :white_check_mark: | **6.6**              | :mage_woman: **8.0** | 3.6                  | :mage_woman: **6.4** | **6.1**              | **6.0**              | **4.7**              | :mage_woman: **0.0** |
| qwen3-max                     | **39.0** | :x:                | :x:                | **6.7**              | 6.8                  | 4.8                  | 5.9                  | 5.5                  | 5.3                  | 3.8                  | :mage_woman: **0.0** |
| qwen34b-thinking-2507-q8_0    | **38.8** | :white_check_mark: | :white_check_mark: | 6.0                  | **7.7**              | 5.7                  | 4.5                  | **6.0**              | 5.3                  | 3.5                  | :mage_woman: **0.0** |
| qwen3-next-80b-a3b-instruct   | **38.7** | :white_check_mark: | :x:                | 6.1                  | 6.9                  | 4.1                  | 5.4                  | :mage_woman: **6.3** | 5.5                  | 4.4                  | :mage_woman: **0.0** |
| Qwen3-32B                     | **37.9** | :white_check_mark: | :white_check_mark: | **6.6**              | 6.8                  | 3.2                  | 5.9                  | 5.3                  | **6.0**              | 4.1                  | :mage_woman: **0.0** |
| Qwen3-30B-A3B-2507-Thinking   | **37.6** | :white_check_mark: | :white_check_mark: | 5.7                  | 6.2                  | 5.8                  | 4.6                  | 5.5                  | **6.0**              | 4.0                  | :mage_woman: **0.0** |
| qwen38b                       | **37.3** | :white_check_mark: | :white_check_mark: | 5.8                  | 7.4                  | 3.4                  | 5.2                  | 5.9                  | 5.1                  | **4.5**              | :mage_woman: **0.0** |
| Qwen3-14B                     | **37.1** | :white_check_mark: | :white_check_mark: | 6.3                  | 5.6                  | 4.0                  | 5.7                  | 5.9                  | **6.1**              | 3.6                  | :mage_woman: **0.0** |
| QwQ-32B-Preview               | **34.9** | :white_check_mark: | :white_check_mark: | 5.9                  | 7.3                  | 4.2                  | 4.8                  | 4.4                  | 5.2                  | 3.2                  | :mage_woman: **0.0** |
| qwen3-coder                   | **34.3** | :white_check_mark: | :x:                | 5.8                  | 5.3                  | 3.5                  | 5.2                  | 5.9                  | 4.5                  | 4.1                  | :mage_woman: **0.0** |
| qwen3-30b-a3b-instruct-2507   | **34.2** | :white_check_mark: | :x:                | 5.7                  | 6.4                  | 3.3                  | 4.2                  | 5.9                  | 5.1                  | 3.6                  | :mage_woman: **0.0** |
| qwen2.5-72b-instruct          | **34.0** | :white_check_mark: | :x:                | 6.1                  | 6.1                  | 3.8                  | 4.8                  | 4.9                  | 5.2                  | 3.1                  | :mage_woman: **0.0** |
| Qwen-3-14B-nothink            | **32.3** | :white_check_mark: | :x:                | 6.0                  | 6.4                  | 2.2                  | 4.4                  | 5.3                  | 4.9                  | 3.0                  | :mage_woman: **0.0** |
| qwen2.5-32b-instruct          | **31.7** | :white_check_mark: | :x:                | 6.3                  | 5.6                  | 2.0                  | 4.5                  | 5.4                  | 5.0                  | 3.0                  | :mage_woman: **0.0** |
| qwen34b-instruct-2507-q8_0    | **31.6** | :white_check_mark: | :x:                | 4.8                  | 5.9                  | 3.1                  | 4.1                  | 5.3                  | 4.8                  | 3.5                  | :mage_woman: **0.0** |
| Qwen-3-32B-nothink            | **31.1** | :white_check_mark: | :x:                | 5.8                  | 6.2                  | 2.2                  | 3.6                  | 5.5                  | 5.1                  | 2.7                  | :mage_woman: **0.0** |
| qwen34b                       | **30.7** | :white_check_mark: | :white_check_mark: | 5.1                  | 6.6                  | 1.8                  | 5.5                  | 4.0                  | 4.6                  | 3.0                  | :mage_woman: **0.0** |
| qwen-qwq-32b-nostepbystep     | **30.3** | :white_check_mark: | :white_check_mark: | 3.9                  | 5.5                  | 1.5                  | 4.7                  | 5.5                  | 5.4                  | 3.9                  | :mage_woman: **0.0** |
| qwen-qwq-32b-stepbystep       | **29.3** | :white_check_mark: | :white_check_mark: | 2.8                  | 6.0                  | 0.9                  | 5.5                  | 5.1                  | 5.2                  | 3.9                  | :mage_woman: **0.0** |
| qwen31.7b                     | **20.6** | :white_check_mark: | :white_check_mark: | 3.1                  | 3.4                  | 1.1                  | 2.7                  | 3.5                  | 3.9                  | 2.9                  | :mage_woman: **0.0** |
| qwen30.6b                     | **11.6** | :white_check_mark: | :white_check_mark: | 1.1                  | 2.9                  | 0.9                  | 1.4                  | 2.3                  | 2.0                  | 1.0                  | :mage_woman: **0.0** |

### Qwen3-235B-A22B-Thinking-2507   => 43.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     6.7 |
| cat01_04_sensor_recordings         |     9.5 |
| cat01_05_merge_two_logs            |     9.5 |
| cat01_06_system_logs               |    10   |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     7.4 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     6.7 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     9.3 |
| cat02_06_root_cause_1              |     3.1 |
| cat02_07_root_cause_2              |     6.7 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |    10   |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |    10   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     8.2 |
| cat04_01_pseudo_bpmn_description   |    10   |
| cat04_02_pseudo_bpmn_open_question |     8.6 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     1.4 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     8.6 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     9.5 |
| cat08_03_transport_opt             |    10   |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |    10   |



### qwenqwen3-next-80b-a3b-thinking   => 41.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     8.4 |
| cat01_07_interv_to_pseudo_bpmn     |     9.3 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     9.5 |
| cat02_06_root_cause_1              |     1.4 |
| cat02_07_root_cause_2              |    10   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     7.1 |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |    10   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     8.6 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     9.3 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |    10   |
| cat05_02_hyp_gen_powl              |     8.6 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     9.3 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |    10   |
| cat06_07_fair_unfair_powl          |     2.2 |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     9.5 |
| cat08_03_transport_opt             |     5.5 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     9.5 |



### qwenqwen3-235b-a22b-07-25   => 41.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     7.2 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     7.2 |
| cat01_07_interv_to_pseudo_bpmn     |     9.5 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     8.2 |
| cat02_07_root_cause_2              |     8.6 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.2 |
| cat03_01_process_tree_generation   |     8.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |    10   |
| cat04_02_pseudo_bpmn_open_question |     9.3 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.7 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     9.5 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     8.4 |
| cat08_03_transport_opt             |     9.3 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |    10   |



### qwenqwen3-max   => 39.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.4 |
| cat01_02_activity_context          |     7.6 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     8.4 |
| cat01_06_system_logs               |     8.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.8 |
| cat01_08_tables_to_log             |     8   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     4.2 |
| cat02_03_anomaly_event_log         |     9.6 |
| cat02_04_powl_anomaly_detection    |     7.1 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     7   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     9   |
| cat03_08_powl_discovery            |     7.1 |
| cat04_01_pseudo_bpmn_description   |     8.4 |
| cat04_02_pseudo_bpmn_open_question |     8.4 |
| cat04_03_declare_open_question     |     7   |
| cat04_04_declare_description       |     8.4 |
| cat04_05_sql_filt_num_events       |     8.4 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.4 |
| cat05_01_hyp_generation_log        |     8.4 |
| cat05_02_hyp_gen_powl              |     8.4 |
| cat05_03_hyp_gen_declare           |    10   |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     1.5 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.4 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     7.6 |
| cat06_05_bias_two_logs_2           |     7.6 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     8.4 |
| cat08_01_queue_mining              |     9.6 |
| cat08_02_instance_spanning         |     8.4 |
| cat08_03_transport_opt             |     9   |
| cat08_04_resource_assign           |     2.5 |
| cat08_05_task_schedul              |     8.8 |



### qwen34b-thinking-2507-q8_0   => 38.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |     6.7 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     4.8 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     6.7 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |    10   |
| cat03_05_temp_profile_generation   |     9.5 |
| cat03_06_petri_net_generation      |    10   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |    10   |
| cat04_01_pseudo_bpmn_description   |     9.3 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     1.4 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     9.3 |
| cat05_04_hyp_gen_temp_profile      |     9.3 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     3.3 |
| cat06_07_fair_unfair_powl          |     8.2 |
| cat08_01_queue_mining              |     5.5 |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     8.6 |
| cat08_04_resource_assign           |     2.2 |
| cat08_05_task_schedul              |     9.3 |



### qwenqwen3-next-80b-a3b-instruct   => 38.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.4 |
| cat01_02_activity_context          |     7.6 |
| cat01_03_high_level_events         |     8.8 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     7.6 |
| cat01_07_interv_to_pseudo_bpmn     |     8.4 |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     9.6 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9   |
| cat02_05_two_powls_anomalies       |     8.4 |
| cat02_06_root_cause_1              |     8.4 |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     8.4 |
| cat03_03_log_skeleton_generation   |     7.6 |
| cat03_04_declare_generation        |     3.2 |
| cat03_05_temp_profile_generation   |     9   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     4   |
| cat03_08_powl_discovery            |     4.2 |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     9   |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     6.5 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.4 |
| cat05_01_hyp_generation_log        |     8.8 |
| cat05_02_hyp_gen_powl              |     8.4 |
| cat05_03_hyp_gen_declare           |     8.4 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.8 |
| cat06_02_bias_event_log            |     9   |
| cat06_03_bias_powl                 |     9.4 |
| cat06_04_bias_two_logs             |     7.6 |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.4 |
| cat08_02_instance_spanning         |     8.4 |
| cat08_03_transport_opt             |     9.4 |
| cat08_04_resource_assign           |     8.4 |
| cat08_05_task_schedul              |     9   |



### QwenQwen3-32B   => 37.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.6 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     8.6 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     7.1 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     8.2 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.2 |
| cat03_03_log_skeleton_generation   |     6.6 |
| cat03_04_declare_generation        |     8.2 |
| cat03_05_temp_profile_generation   |     1.1 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.9 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     7.2 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     7.2 |
| cat05_04_hyp_gen_temp_profile      |     3.3 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     8.6 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     9.5 |
| cat06_07_fair_unfair_powl          |     7.1 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     7.1 |
| cat08_03_transport_opt             |     9.3 |
| cat08_04_resource_assign           |     8.6 |
| cat08_05_task_schedul              |     8.2 |



### Qwen3-30B-A3B-2507-Thinking   => 37.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     6.7 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     6.7 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     7.7 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.9 |
| cat03_04_declare_generation        |     7.1 |
| cat03_05_temp_profile_generation   |     7.2 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     3.3 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |    10   |
| cat05_04_hyp_gen_temp_profile      |     1.4 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     9.3 |
| cat06_01_bias_text                 |     8.6 |
| cat06_02_bias_event_log            |    10   |
| cat06_03_bias_powl                 |     7.2 |
| cat06_04_bias_two_logs             |     6.7 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     8.9 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     7.2 |
| cat08_03_transport_opt             |     3.9 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     9.5 |



### qwen38b   => 37.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     6.7 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     7.2 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     9.3 |
| cat02_04_powl_anomaly_detection    |     8.2 |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |     7.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     7.2 |
| cat03_06_petri_net_generation      |     2.9 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     7.2 |
| cat04_02_pseudo_bpmn_open_question |     8.6 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.2 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     6.7 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     9.3 |
| cat08_02_instance_spanning         |     8.9 |
| cat08_03_transport_opt             |     9.5 |
| cat08_04_resource_assign           |     8.6 |
| cat08_05_task_schedul              |     8.6 |



### QwenQwen3-14B   => 37.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     9.5 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     8.6 |
| cat01_08_tables_to_log             |     7.1 |
| cat02_01_conformance_textual       |     8.6 |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     8.4 |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     6.6 |
| cat03_02_powl_generation           |     3.1 |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     5.4 |
| cat03_06_petri_net_generation      |    10   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     9.3 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.2 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     1   |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



### QwenQwQ-32B-Preview   => 34.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7.9 |
| cat01_05_merge_two_logs            |     6.7 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     6.7 |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     7.2 |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6.6 |
| cat03_04_declare_generation        |     5.4 |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     7.2 |
| cat03_07_process_tree_discovery    |     2.2 |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |     7.2 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     5.6 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |     5.4 |
| cat05_03_hyp_gen_declare           |     7.2 |
| cat05_04_hyp_gen_temp_profile      |     3.3 |
| cat05_05_question_gen_nlp          |     1   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     5.6 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     1.4 |
| cat08_05_task_schedul              |     8.2 |



### qwenqwen3-coder   => 34.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     8.4 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     8.4 |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     8.4 |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     8.4 |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     7.1 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     7.1 |
| cat03_03_log_skeleton_generation   |     1.5 |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     7.1 |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     7.6 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     7.6 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     8   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     9   |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     7   |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     1.6 |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     3.2 |
| cat06_07_fair_unfair_powl          |     9   |
| cat08_01_queue_mining              |     8.4 |
| cat08_02_instance_spanning         |     8.4 |
| cat08_03_transport_opt             |     8.4 |
| cat08_04_resource_assign           |     8.4 |
| cat08_05_task_schedul              |     7.1 |



### qwenqwen3-30b-a3b-instruct-2507   => 34.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     7.6 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     9   |
| cat01_07_interv_to_pseudo_bpmn     |     8.8 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     8.6 |
| cat02_02_conf_desiderata           |     7.6 |
| cat02_03_anomaly_event_log         |     7.6 |
| cat02_04_powl_anomaly_detection    |     8.4 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     9.4 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     3.5 |
| cat03_02_powl_generation           |     7   |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     3.2 |
| cat03_08_powl_discovery            |     4.2 |
| cat04_01_pseudo_bpmn_description   |     8.8 |
| cat04_02_pseudo_bpmn_open_question |     7.6 |
| cat04_03_declare_open_question     |     7.1 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     6.2 |
| cat05_02_hyp_gen_powl              |     8.4 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     7.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     7.6 |
| cat06_03_bias_powl                 |     8.8 |
| cat06_04_bias_two_logs             |     8.4 |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8.4 |
| cat08_01_queue_mining              |     9.2 |
| cat08_02_instance_spanning         |     6.5 |
| cat08_03_transport_opt             |     2.3 |
| cat08_04_resource_assign           |     8.4 |
| cat08_05_task_schedul              |     9.4 |



### qwen2.5-72b-instruct   => 34.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    7.6  |
| cat01_03_high_level_events         |    7.1  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    7.5  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    7.75 |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |    7.25 |
| cat02_04_powl_anomaly_detection    |    8.6  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    1    |
| cat02_07_root_cause_2              |    7.6  |
| cat02_08_underfitting_process_tree |    8.4  |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    3.2  |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    7    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    7    |
| cat04_01_pseudo_bpmn_description   |    8    |
| cat04_02_pseudo_bpmn_open_question |    7.1  |
| cat04_03_declare_open_question     |    4.2  |
| cat04_04_declare_description       |    1    |
| cat04_05_sql_filt_num_events       |    8.4  |
| cat04_06_sql_filt_three_df         |   10    |
| cat04_07_sql_filt_top_k_vars       |    9    |
| cat05_01_hyp_generation_log        |    4.2  |
| cat05_02_hyp_gen_powl              |    8.4  |
| cat05_03_hyp_gen_declare           |    7.5  |
| cat05_04_hyp_gen_temp_profile      |    7.1  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    5    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    9.4  |
| cat06_02_bias_event_log            |    7.1  |
| cat06_03_bias_powl                 |    7.6  |
| cat06_04_bias_two_logs             |    7.6  |
| cat06_05_bias_two_logs_2           |    8    |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |   10    |
| cat08_01_queue_mining              |    5.2  |
| cat08_02_instance_spanning         |    5.8  |
| cat08_03_transport_opt             |    7.1  |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    6.2  |



### Qwen-3-14B-nothink   => 32.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.8 |
| cat01_03_high_level_events         |     9   |
| cat01_04_sensor_recordings         |     7.6 |
| cat01_05_merge_two_logs            |     7   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |     7.1 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.4 |
| cat02_05_two_powls_anomalies       |     8.4 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.2 |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.2 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2.1 |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     7.6 |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     1.5 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     8.4 |
| cat04_07_sql_filt_top_k_vars       |     8.4 |
| cat05_01_hyp_generation_log        |     8.4 |
| cat05_02_hyp_gen_powl              |     7.6 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     8.4 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     8.8 |
| cat06_02_bias_event_log            |     7.6 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     8.4 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.4 |
| cat08_01_queue_mining              |     6.5 |
| cat08_02_instance_spanning         |     6.8 |
| cat08_03_transport_opt             |     1.3 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     8.4 |



### qwen2.5-32b-instruct   => 31.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8.6  |
| cat01_03_high_level_events         |    7.1  |
| cat01_04_sensor_recordings         |   10    |
| cat01_05_merge_two_logs            |    7.1  |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    5.2  |
| cat01_08_tables_to_log             |   10    |
| cat02_01_conformance_textual       |    8.4  |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |    8.4  |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    6    |
| cat02_06_root_cause_1              |    1.5  |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    1.12 |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    1.2  |
| cat03_08_powl_discovery            |    3.2  |
| cat04_01_pseudo_bpmn_description   |    8    |
| cat04_02_pseudo_bpmn_open_question |    7.05 |
| cat04_03_declare_open_question     |    6    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    4    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    7.1  |
| cat05_03_hyp_gen_declare           |    7.1  |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    7.6  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    3.2  |
| cat06_07_fair_unfair_powl          |    8.4  |
| cat08_01_queue_mining              |    6.2  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    6.2  |
| cat08_04_resource_assign           |    5    |
| cat08_05_task_schedul              |    6.2  |



### qwen34b-instruct-2507-q8_0   => 31.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     4   |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     8.4 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     3.2 |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     7   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     8.4 |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     7   |
| cat02_04_powl_anomaly_detection    |     8.4 |
| cat02_05_two_powls_anomalies       |     7.6 |
| cat02_06_root_cause_1              |     5   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     7.6 |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     7.1 |
| cat03_02_powl_generation           |     7   |
| cat03_03_log_skeleton_generation   |     3.2 |
| cat03_04_declare_generation        |     1.5 |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     1.2 |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     7.6 |
| cat04_03_declare_open_question     |     7.5 |
| cat04_04_declare_description       |     5.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     7.5 |
| cat05_02_hyp_gen_powl              |     7.6 |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     8.4 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     7.6 |
| cat06_03_bias_powl                 |     8.4 |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     4.5 |
| cat08_01_queue_mining              |     8.4 |
| cat08_02_instance_spanning         |     1.8 |
| cat08_03_transport_opt             |     8.4 |
| cat08_04_resource_assign           |     8.4 |
| cat08_05_task_schedul              |     8.4 |



### Qwen-3-32B-nothink   => 31.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     8.4 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     8.4 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     3.2 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.2 |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     7.1 |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     8.4 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     7.6 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     8.6 |
| cat06_04_bias_two_logs             |     4.2 |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     7.5 |
| cat08_01_queue_mining              |     8.4 |
| cat08_02_instance_spanning         |     7.1 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     1.3 |
| cat08_05_task_schedul              |     2.4 |



### qwen34b   => 30.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     6.7 |
| cat01_04_sensor_recordings         |     6.6 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     7.4 |
| cat02_04_powl_anomaly_detection    |     9.3 |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     6.7 |
| cat02_07_root_cause_2              |     4.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     6.7 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2.2 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     7.2 |
| cat04_02_pseudo_bpmn_open_question |     8.4 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     9.5 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     2.2 |
| cat05_05_question_gen_nlp          |     5.6 |
| cat05_06_question_pseudo_bpmn      |     7.2 |
| cat05_07_question_interview        |     1   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     4.2 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     7.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     7.2 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     6   |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     1   |
| cat08_05_task_schedul              |     7.9 |



### qwen-qwq-32b-nostepbystep   => 30.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     1   |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     8.6 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |     8.2 |
| cat02_03_anomaly_event_log         |     8.2 |
| cat02_04_powl_anomaly_detection    |     6.7 |
| cat02_05_two_powls_anomalies       |     7.2 |
| cat02_06_root_cause_1              |     4.2 |
| cat02_07_root_cause_2              |     1.4 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     1   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     7.7 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     5.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     7.2 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     5.6 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.2 |
| cat08_01_queue_mining              |     9.8 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     6.7 |
| cat08_05_task_schedul              |     7.5 |



### qwen-qwq-32b-stepbystep   => 29.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.3 |
| cat01_02_activity_context          |     7.2 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     9.3 |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     3.3 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     1   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.2 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     7.9 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.2 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     3.1 |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     9.3 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     8.6 |
| cat06_04_bias_two_logs             |     7.2 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     7.7 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     8.6 |
| cat08_05_task_schedul              |     8.2 |



### qwen31.7b   => 20.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     8.6 |
| cat01_04_sensor_recordings         |     2.2 |
| cat01_05_merge_two_logs            |     2.2 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     2.2 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     6.7 |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     9.3 |
| cat02_05_two_powls_anomalies       |     1   |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.3 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.2 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     2.2 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     2.2 |
| cat05_04_hyp_gen_temp_profile      |     2.5 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     3.3 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.2 |
| cat06_03_bias_powl                 |     3.3 |
| cat06_04_bias_two_logs             |     5.4 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     3.1 |
| cat08_01_queue_mining              |     6.7 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     6.7 |
| cat08_04_resource_assign           |     5.6 |
| cat08_05_task_schedul              |     3.3 |



### qwen30.6b   => 11.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     2.2 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     3.3 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     8.2 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2.2 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     3.3 |
| cat04_03_declare_open_question     |     3.3 |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     1   |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     2.2 |
| cat05_05_question_gen_nlp          |     7.2 |
| cat05_06_question_pseudo_bpmn      |     9.3 |
| cat05_07_question_interview        |     1   |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     5.4 |
| cat06_03_bias_powl                 |     1   |
| cat06_04_bias_two_logs             |     2   |
| cat06_05_bias_two_logs_2           |     1   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     2.2 |
| cat08_02_instance_spanning         |     1   |
| cat08_03_transport_opt             |     3.3 |
| cat08_04_resource_assign           |     2.2 |
| cat08_05_task_schedul              |     1   |

