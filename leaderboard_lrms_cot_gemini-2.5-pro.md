A score in the range **24-29** is considered **sufficient**; a score in the range **29-34** is considered **fair**; a score in the range **34-40** is considered **good**; and a score **>40** is considered **excellent**.

**Update**: Since **19-04-2025**, a normalization step is applied to the score.

## Large Reasoning Models Leaderboard (Models with CoT) (1-shot; gemini-2.5-pro-preview-03-25 used as a judge)

| Model                            | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       | OPT                  |
|:---------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| grok-3-mini-beta-high            | **42.0** | :x:                | :white_check_mark: | :mage_woman: **6.3** | **7.4**              | :mage_woman: **6.3** | :mage_woman: **5.9** | :mage_woman: **5.9** | :mage_woman: **5.9** | :mage_woman: **0.0** | :mage_woman: **4.2** |
| Grok-3-beta-thinking-20250221    | **39.8** | :x:                | :white_check_mark: | 5.9                  | :mage_woman: **7.5** | 5.9                  | 5.5                  | 5.5                  | **5.8**              | :mage_woman: **0.0** | 3.7                  |
| nemotron-ultra-253b-v1-thinkenab | **37.0** | :white_check_mark: | :white_check_mark: | **6.0**              | 6.8                  | 5.3                  | 4.5                  | 5.1                  | 5.6                  | :mage_woman: **0.0** | 3.7                  |
| qwen-qwq-32b-nostepbystep        | **36.9** | :white_check_mark: | :white_check_mark: | 5.7                  | 6.4                  | **6.0**              | 4.5                  | 4.9                  | **5.7**              | :mage_woman: **0.0** | 3.7                  |
| DeepSeek-R1                      | **36.8** | :white_check_mark: | :white_check_mark: | 5.9                  | **7.4**              | 4.7                  | 5.2                  | 4.7                  | 5.1                  | :mage_woman: **0.0** | 3.8                  |
| nemotron-super-49b-v1-thinkenab  | **36.4** | :white_check_mark: | :white_check_mark: | 5.0                  | **7.3**              | **6.0**              | 4.8                  | 4.4                  | 5.0                  | :mage_woman: **0.0** | 3.9                  |
| grok-3-mini-beta-low             | **36.3** | :x:                | :white_check_mark: | 5.7                  | 6.9                  | 4.0                  | 5.1                  | 4.9                  | 5.4                  | :mage_woman: **0.0** | :mage_woman: **4.2** |
| qwen-qwq-32b-stepbystep          | **35.8** | :white_check_mark: | :white_check_mark: | 5.6                  | 6.7                  | 4.3                  | 4.6                  | 5.1                  | 5.6                  | :mage_woman: **0.0** | 3.9                  |
| r1-1776                          | **32.1** | :white_check_mark: | :white_check_mark: | 4.4                  | **7.2**              | 2.4                  | 4.8                  | 4.8                  | 4.6                  | :mage_woman: **0.0** | 3.9                  |
| DeepSeek-R1-Distill-Qwen-32B     | **30.7** | :white_check_mark: | :white_check_mark: | 5.0                  | 6.9                  | 3.5                  | 3.6                  | 4.5                  | 4.8                  | :mage_woman: **0.0** | 2.5                  |
| exaone-deep7.8b-fp16             | **30.2** | :white_check_mark: | :white_check_mark: | 4.8                  | 6.4                  | 2.6                  | 3.6                  | 4.3                  | 4.8                  | :mage_woman: **0.0** | 3.6                  |
| deepseek-r1-zero                 | **29.9** | :white_check_mark: | :white_check_mark: | 5.0                  | 4.7                  | 3.5                  | 4.0                  | 5.0                  | 4.1                  | :mage_woman: **0.0** | 3.6                  |
| DeepSeek-R1-Distill-Llama-70B    | **28.6** | :white_check_mark: | :white_check_mark: | 4.7                  | 6.1                  | 2.7                  | 4.3                  | 4.0                  | 4.5                  | :mage_woman: **0.0** | 2.3                  |
| exaone-deep32b-fp16              | **28.1** | :white_check_mark: | :white_check_mark: | 5.4                  | 6.1                  | 3.5                  | 4.3                  | 4.0                  | 4.8                  | :mage_woman: **0.0** | 0.0                  |
| deepseek-r1-distill-qwen-14b     | **27.8** | :white_check_mark: | :white_check_mark: | 4.5                  | 6.9                  | 3.8                  | 3.0                  | 3.8                  | 3.9                  | :mage_woman: **0.0** | 1.9                  |
| sonar-reasoning-pro              | **24.5** | :x:                | :white_check_mark: | 3.4                  | 5.4                  | 2.1                  | 2.3                  | 4.5                  | 3.2                  | :mage_woman: **0.0** | 3.7                  |
| exaone-deep2.4b-fp16             | **23.5** | :white_check_mark: | :white_check_mark: | 3.7                  | 5.3                  | 1.8                  | 2.9                  | 3.2                  | 3.2                  | :mage_woman: **0.0** | 3.4                  |
| cogito14b-v1-preview-qwen-fp16   | **22.8** | :white_check_mark: | :white_check_mark: | 4.4                  | 4.1                  | 2.7                  | 3.4                  | 3.7                  | 4.5                  | :mage_woman: **0.0** | 0.0                  |
| deepseek-r1-distill-llama-8b     | **20.6** | :white_check_mark: | :white_check_mark: | 2.6                  | 4.1                  | 1.9                  | 2.5                  | 4.1                  | 4.0                  | :mage_woman: **0.0** | 1.5                  |
| deepseek-r1-distill-qwen-1.5b    | **9.9**  | :white_check_mark: | :white_check_mark: | 1.3                  | 1.6                  | 0.9                  | 1.0                  | 2.7                  | 1.6                  | :mage_woman: **0.0** | 0.8                  |

### grok-3-mini-beta-high   => 42.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.1 |
| cat01_02_activity_context          |     9.1 |
| cat01_03_high_level_events         |     8.6 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     9.1 |
| cat02_03_anomaly_event_log         |     6.8 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |     7.6 |
| cat02_08_underfitting_process_tree |    10.6 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6.6 |
| cat03_04_declare_generation        |     7.4 |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     9.1 |
| cat03_08_powl_discovery            |     6.8 |
| cat04_01_pseudo_bpmn_description   |     9.1 |
| cat04_02_pseudo_bpmn_open_question |     6.8 |
| cat04_03_declare_open_question     |     7.7 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     9.1 |
| cat05_01_hyp_generation_log        |     6.8 |
| cat05_02_hyp_gen_powl              |     9.1 |
| cat05_03_hyp_gen_declare           |    10   |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     9.1 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     9.1 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     9.1 |
| cat06_06_bias_mitigation_declare   |     9.1 |
| cat06_07_fair_unfair_powl          |     7.4 |
| cat08_01_queue_mining              |     8.3 |
| cat08_02_instance_spanning         |     8.3 |
| cat08_03_transport_opt             |     8.3 |
| cat08_04_resource_assign           |     9.1 |
| cat08_05_task_schedul              |     8.3 |



### Grok-3-beta-thinking-20250221   => 39.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.1 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     9.7 |
| cat01_05_merge_two_logs            |     7.6 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6.8 |
| cat01_08_tables_to_log             |     7.6 |
| cat02_01_conformance_textual       |     9.1 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     8.3 |
| cat02_04_powl_anomaly_detection    |     9.1 |
| cat02_05_two_powls_anomalies       |     9.1 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     9.1 |
| cat02_08_underfitting_process_tree |     7.4 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     9.7 |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |     7.1 |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     6.8 |
| cat03_07_process_tree_discovery    |     7.4 |
| cat03_08_powl_discovery            |     7.1 |
| cat04_01_pseudo_bpmn_description   |     9.1 |
| cat04_02_pseudo_bpmn_open_question |     7.4 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |    10.6 |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     7.4 |
| cat05_01_hyp_generation_log        |     8.3 |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     9.1 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     9.1 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     8.6 |
| cat06_02_bias_event_log            |     9.1 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     9.1 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     6   |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     7.7 |



### nvidiallama-3.1-nemotron-ultra-253b-v1-thinkenab   => 37.0 points

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
| cat08_01_queue_mining              |     7.4 |
| cat08_02_instance_spanning         |     6.6 |
| cat08_03_transport_opt             |     7.6 |
| cat08_04_resource_assign           |     8.3 |
| cat08_05_task_schedul              |     7.4 |



### qwen-qwq-32b-nostepbystep   => 36.9 points

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
| cat08_01_queue_mining              |     7.4 |
| cat08_02_instance_spanning         |     6.8 |
| cat08_03_transport_opt             |     7.4 |
| cat08_04_resource_assign           |     8.3 |
| cat08_05_task_schedul              |     7.4 |



### deepseek-aiDeepSeek-R1   => 36.8 points

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
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     7.1 |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     7.7 |



### nvidiallama-3.3-nemotron-super-49b-v1-thinkenab   => 36.4 points

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
| cat08_01_queue_mining              |     9.1 |
| cat08_02_instance_spanning         |     7.7 |
| cat08_03_transport_opt             |     7.6 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     7.7 |



### grok-3-mini-beta-low   => 36.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     9.1 |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     7.4 |
| cat02_02_conf_desiderata           |     7.4 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     9.1 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     6.8 |
| cat02_07_root_cause_2              |     6.8 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     9.1 |
| cat03_01_process_tree_generation   |     9.1 |
| cat03_02_powl_generation           |     9.1 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     4.2 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     7.6 |
| cat04_02_pseudo_bpmn_open_question |     7.6 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |    10.6 |
| cat04_06_sql_filt_three_df         |     9.1 |
| cat04_07_sql_filt_top_k_vars       |     7.1 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     9.1 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     7.6 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     7.4 |
| cat06_07_fair_unfair_powl          |     7.7 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     9.1 |
| cat08_03_transport_opt             |     9.1 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     9.1 |



### qwen-qwq-32b-stepbystep   => 35.8 points

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
| cat08_01_queue_mining              |     7.6 |
| cat08_02_instance_spanning         |     7.7 |
| cat08_03_transport_opt             |     7.6 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     8.3 |



### r1-1776   => 32.1 points

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
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     7.4 |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     9.1 |



### deepseek-aiDeepSeek-R1-Distill-Qwen-32B   => 30.7 points

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
| cat08_01_queue_mining              |     4.2 |
| cat08_02_instance_spanning         |     2.5 |
| cat08_03_transport_opt             |     4.8 |
| cat08_04_resource_assign           |     7.2 |
| cat08_05_task_schedul              |     6   |



### exaone-deep7.8b-fp16   => 30.2 points

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
| cat08_01_queue_mining              |     7.1 |
| cat08_02_instance_spanning         |     7.1 |
| cat08_03_transport_opt             |     7.4 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     6.6 |



### deepseekdeepseek-r1-zerofree   => 29.9 points

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
| cat08_01_queue_mining              |     8.3 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     7.2 |
| cat08_05_task_schedul              |     6.8 |



### deepseek-aiDeepSeek-R1-Distill-Llama-70B   => 28.6 points

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
| cat08_01_queue_mining              |     7.4 |
| cat08_02_instance_spanning         |     3.1 |
| cat08_03_transport_opt             |     2.5 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     2.5 |



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



### deepseekdeepseek-r1-distill-qwen-14b   => 27.8 points

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
| cat08_01_queue_mining              |     4.2 |
| cat08_02_instance_spanning         |     2.5 |
| cat08_03_transport_opt             |     2   |
| cat08_04_resource_assign           |     6.8 |
| cat08_05_task_schedul              |     3.1 |



### sonar-reasoning-pro   => 24.5 points

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
| cat02_03_anomaly_event_log         |     8.3 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     4.8 |
| cat02_06_root_cause_1              |     7.7 |
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
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     4.2 |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     6.9 |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     7   |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     4.8 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     4.2 |
| cat06_04_bias_two_logs             |     6.6 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     3.1 |
| cat08_01_queue_mining              |     7.4 |
| cat08_02_instance_spanning         |     7.4 |
| cat08_03_transport_opt             |     7.4 |
| cat08_04_resource_assign           |     7.6 |
| cat08_05_task_schedul              |     6.8 |



### exaone-deep2.4b-fp16   => 23.5 points

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
| cat08_01_queue_mining              |     6.8 |
| cat08_02_instance_spanning         |     7.1 |
| cat08_03_transport_opt             |     5.4 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     7.4 |



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



### deepseekdeepseek-r1-distill-llama-8b   => 20.6 points

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
| cat08_01_queue_mining              |     1.4 |
| cat08_02_instance_spanning         |     4.2 |
| cat08_03_transport_opt             |     2.5 |
| cat08_04_resource_assign           |     3.1 |
| cat08_05_task_schedul              |     3.7 |



### deepseekdeepseek-r1-distill-qwen-1.5b   => 9.9 points

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
| cat08_01_queue_mining              |     2.5 |
| cat08_02_instance_spanning         |     1   |
| cat08_03_transport_opt             |     1   |
| cat08_04_resource_assign           |     1.4 |
| cat08_05_task_schedul              |     2   |

