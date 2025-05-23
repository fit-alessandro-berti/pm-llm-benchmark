A score in the range **24-29** is considered **sufficient**; a score in the range **29-34** is considered **fair**; a score in the range **34-40** is considered **good**; and a score **>40** is considered **excellent**.

**Update**: Since **19-04-2025**, a normalization step is applied to the score.

## Large Reasoning Models Leaderboard (Models with CoT) (1-shot; gemini-2.5-pro-preview-05-06 used as a judge)

| Model                            | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | OPT                  | :nerd_face: VI       |
|:---------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| grok-3-mini-beta-high            | **41.2** | :x:                | :white_check_mark: | :mage_woman: **6.2** | **7.3**              | :mage_woman: **6.2** | :mage_woman: **5.8** | :mage_woman: **5.7** | :mage_woman: **5.8** | **4.2**              | :mage_woman: **0.0** |
| Grok-3-beta-thinking-20250221    | **39.3** | :x:                | :white_check_mark: | **5.9**              | :mage_woman: **7.4** | **5.9**              | 5.4                  | **5.4**              | **5.7**              | 3.7                  | :mage_woman: **0.0** |
| phi4-reasoningplus               | **38.3** | :white_check_mark: | :white_check_mark: | 5.3                  | **7.2**              | 5.6                  | 5.4                  | **5.4**              | 5.2                  | 4.1                  | :mage_woman: **0.0** |
| Qwen3-235B-A22B                  | **37.6** | :white_check_mark: | :white_check_mark: | **5.9**              | 6.9                  | 4.3                  | **5.5**              | 5.3                  | **5.7**              | 4.0                  | :mage_woman: **0.0** |
| phi4-reasoning                   | **37.2** | :white_check_mark: | :white_check_mark: | :mage_woman: **6.2** | 6.1                  | 5.5                  | 4.8                  | **5.4**              | 5.0                  | 4.1                  | :mage_woman: **0.0** |
| nemotron-ultra-253b-v1-thinkenab | **36.7** | :white_check_mark: | :white_check_mark: | **6.0**              | 6.7                  | 5.2                  | 4.5                  | 5.0                  | **5.6**              | 3.7                  | :mage_woman: **0.0** |
| qwen-qwq-32b-nostepbystep        | **36.7** | :white_check_mark: | :white_check_mark: | 5.7                  | 6.4                  | **5.9**              | 4.5                  | 4.8                  | **5.6**              | 3.7                  | :mage_woman: **0.0** |
| DeepSeek-R1                      | **36.4** | :white_check_mark: | :white_check_mark: | 5.8                  | **7.3**              | 4.7                  | 5.1                  | 4.6                  | 5.1                  | 3.8                  | :mage_woman: **0.0** |
| nemotron-super-49b-v1-thinkenab  | **36.0** | :white_check_mark: | :white_check_mark: | 4.9                  | **7.2**              | **5.9**              | 4.7                  | 4.4                  | 5.0                  | 3.9                  | :mage_woman: **0.0** |
| grok-3-mini-beta-low             | **36.0** | :x:                | :white_check_mark: | 5.7                  | 6.9                  | 4.0                  | 5.0                  | 4.9                  | 5.4                  | **4.2**              | :mage_woman: **0.0** |
| Qwen3-14B                        | **35.9** | :white_check_mark: | :white_check_mark: | 5.7                  | 6.8                  | 4.2                  | 5.1                  | 4.7                  | 5.3                  | 4.0                  | :mage_woman: **0.0** |
| Qwen3-30B-A3B                    | **35.7** | :white_check_mark: | :white_check_mark: | 5.6                  | 6.7                  | 3.6                  | 4.8                  | 5.3                  | 5.4                  | :mage_woman: **4.4** | :mage_woman: **0.0** |
| qwen-qwq-32b-stepbystep          | **35.6** | :white_check_mark: | :white_check_mark: | 5.6                  | 6.7                  | 4.3                  | 4.6                  | 5.0                  | **5.5**              | 3.9                  | :mage_woman: **0.0** |
| Qwen3-32B                        | **35.3** | :white_check_mark: | :white_check_mark: | **6.0**              | 6.4                  | 4.6                  | 4.7                  | 4.7                  | 5.2                  | 3.9                  | :mage_woman: **0.0** |
| qwen-turbo-2025-04-28            | **33.3** | :x:                | :white_check_mark: | 4.5                  | 6.5                  | 3.4                  | 5.1                  | 4.8                  | 4.8                  | 4.1                  | :mage_woman: **0.0** |
| qwen38b                          | **33.0** | :white_check_mark: | :white_check_mark: | 4.6                  | 7.1                  | 3.3                  | 4.9                  | 5.0                  | 4.4                  | 3.8                  | :mage_woman: **0.0** |
| r1-1776                          | **31.8** | :white_check_mark: | :white_check_mark: | 4.4                  | 7.1                  | 2.4                  | 4.7                  | 4.8                  | 4.6                  | 3.9                  | :mage_woman: **0.0** |
| exaone-deep32b-fp16              | **31.4** | :white_check_mark: | :white_check_mark: | 5.4                  | 6.0                  | 3.5                  | 4.2                  | 4.0                  | 4.8                  | 3.5                  | :mage_woman: **0.0** |
| qwen34b                          | **30.6** | :white_check_mark: | :white_check_mark: | 5.3                  | 6.3                  | 2.3                  | 4.5                  | 4.5                  | 4.2                  | 3.5                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-32B     | **30.5** | :white_check_mark: | :white_check_mark: | 5.0                  | 6.8                  | 3.5                  | 3.6                  | 4.4                  | 4.8                  | 2.5                  | :mage_woman: **0.0** |
| exaone-deep7.8b-fp16             | **30.1** | :white_check_mark: | :white_check_mark: | 4.8                  | 6.4                  | 2.6                  | 3.6                  | 4.3                  | 4.8                  | 3.6                  | :mage_woman: **0.0** |
| deepseek-r1-zero                 | **29.8** | :white_check_mark: | :white_check_mark: | 5.0                  | 4.7                  | 3.5                  | 4.0                  | 5.0                  | 4.1                  | 3.6                  | :mage_woman: **0.0** |
| QwQ-32B-Preview                  | **28.7** | :white_check_mark: | :white_check_mark: | 4.8                  | 6.2                  | 3.1                  | 3.4                  | 4.8                  | 3.8                  | 2.8                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Llama-70B    | **28.5** | :white_check_mark: | :white_check_mark: | 4.7                  | 6.1                  | 2.7                  | 4.2                  | 4.0                  | 4.5                  | 2.3                  | :mage_woman: **0.0** |
| deepseek-r1-distill-qwen-14b     | **27.6** | :white_check_mark: | :white_check_mark: | 4.5                  | 6.8                  | 3.8                  | 3.0                  | 3.8                  | 3.9                  | 1.9                  | :mage_woman: **0.0** |
| cogito14b-v1-preview-qwen-fp16   | **25.0** | :white_check_mark: | :white_check_mark: | 4.4                  | 4.1                  | 2.7                  | 3.3                  | 3.7                  | 4.5                  | 2.3                  | :mage_woman: **0.0** |
| sonar-reasoning-pro              | **24.5** | :x:                | :white_check_mark: | 3.4                  | 5.4                  | 2.1                  | 2.3                  | 4.5                  | 3.2                  | 3.7                  | :mage_woman: **0.0** |
| exaone-deep2.4b-fp16             | **23.4** | :white_check_mark: | :white_check_mark: | 3.7                  | 5.3                  | 1.8                  | 2.9                  | 3.2                  | 3.2                  | 3.4                  | :mage_woman: **0.0** |
| phi4-mini-reasoning              | **22.6** | :white_check_mark: | :white_check_mark: | 3.6                  | 4.1                  | 1.7                  | 2.8                  | 3.5                  | 3.2                  | 3.7                  | :mage_woman: **0.0** |
| qwen-plus-2025-04-28             | **21.8** | :x:                | :white_check_mark: | 2.6                  | 4.0                  | 1.9                  | 2.6                  | 4.2                  | 3.2                  | 3.2                  | :mage_woman: **0.0** |
| deepseek-r1-distill-llama-8b     | **20.6** | :white_check_mark: | :white_check_mark: | 2.6                  | 4.1                  | 1.9                  | 2.5                  | 4.1                  | 4.0                  | 1.5                  | :mage_woman: **0.0** |
| qwen31.7b                        | **19.9** | :white_check_mark: | :white_check_mark: | 2.8                  | 4.0                  | 1.7                  | 1.8                  | 3.8                  | 3.2                  | 2.6                  | :mage_woman: **0.0** |
| deepseek-r1-distill-qwen-7b      | **16.8** | :white_check_mark: | :white_check_mark: | 1.8                  | 2.9                  | 2.4                  | 2.2                  | 3.1                  | 2.8                  | 1.6                  | :mage_woman: **0.0** |
| qwen30.6b                        | **12.7** | :white_check_mark: | :white_check_mark: | 1.1                  | 2.5                  | 1.6                  | 1.2                  | 2.6                  | 2.4                  | 1.4                  | :mage_woman: **0.0** |
| deepseek-r1-distill-qwen-1.5b    | **9.9**  | :white_check_mark: | :white_check_mark: | 1.3                  | 1.6                  | 0.9                  | 1.0                  | 2.7                  | 1.6                  | 0.8                  | :mage_woman: **0.0** |

### grok-3-mini-beta-high   => 41.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     8.4 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     6.8 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |     7.6 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     9.5 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     6.6 |
| cat03_04_declare_generation        |     7.4 |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     8.9 |
| cat03_08_powl_discovery            |     6.8 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     6.8 |
| cat04_03_declare_open_question     |     7.7 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     9.5 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     6.8 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     9.5 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     8.9 |
| cat06_07_fair_unfair_powl          |     7.4 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     8.2 |



### Grok-3-beta-thinking-20250221   => 39.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.1 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     9.3 |
| cat01_05_merge_two_logs            |     7.6 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6.8 |
| cat01_08_tables_to_log             |     7.6 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     8.2 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |     7.4 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     9.3 |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |     7.1 |
| cat03_05_temp_profile_generation   |     8.6 |
| cat03_06_petri_net_generation      |     6.8 |
| cat03_07_process_tree_discovery    |     7.4 |
| cat03_08_powl_discovery            |     7.1 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.4 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     7.4 |
| cat05_01_hyp_generation_log        |     8.2 |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     6   |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     7.7 |



### phi4-reasoningplus   => 38.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     7.6 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     7.4 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     6.6 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     7.6 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     8.9 |
| cat04_01_pseudo_bpmn_description   |     7.4 |
| cat04_02_pseudo_bpmn_open_question |     7.4 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     7.4 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     7.4 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.4 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     7.4 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     6.8 |
| cat06_07_fair_unfair_powl          |     7.4 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     8.2 |



### QwenQwen3-235B-A22B   => 37.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     6.6 |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     7.6 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     6.8 |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6.8 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     7.4 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     7.7 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     7.4 |
| cat03_06_petri_net_generation      |     6   |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.4 |
| cat04_03_declare_open_question     |     7.1 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     7.4 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     7.7 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     4.8 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.4 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     7.4 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     7.4 |



### phi4-reasoning   => 37.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7.6 |
| cat01_05_merge_two_logs            |     4.2 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     7.4 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     7.4 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6.8 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |     1.4 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     7.7 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     7.4 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     7.1 |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     7.4 |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     7.6 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     7.7 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     7.4 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.6 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     5.4 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     7.6 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



### nvidiallama-3.1-nemotron-ultra-253b-v1-thinkenab   => 36.7 points

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
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     7.4 |
| cat02_08_underfitting_process_tree |     7.1 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     9.5 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     7.4 |
| cat03_06_petri_net_generation      |     4.8 |
| cat03_07_process_tree_discovery    |     9.5 |
| cat03_08_powl_discovery            |     7.4 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     4.8 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     9.5 |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     7.4 |
| cat08_02_instance_spanning         |     6.6 |
| cat08_03_transport_opt             |     7.6 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     7.4 |



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



### deepseek-aiDeepSeek-R1   => 36.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.4 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     6.8 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     7.6 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |    10   |
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
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     7.4 |
| cat05_01_hyp_generation_log        |     4.9 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     8.9 |
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



### nvidiallama-3.3-nemotron-super-49b-v1-thinkenab   => 36.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     4.8 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     3.7 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     9.5 |
| cat03_02_powl_generation           |     6.6 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     6.8 |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     8.9 |
| cat03_08_powl_discovery            |     8.9 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     7.7 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.4 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     6.6 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     7.7 |
| cat08_03_transport_opt             |     7.6 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     7.7 |



### grok-3-mini-beta-low   => 36.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.5 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     7.4 |
| cat02_02_conf_desiderata           |     7.4 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     6.8 |
| cat02_07_root_cause_2              |     6.8 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     8.9 |
| cat03_02_powl_generation           |     8.9 |
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
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     7.1 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     7.6 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     7.4 |
| cat06_07_fair_unfair_powl          |     7.7 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     8.9 |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     8.9 |



### QwenQwen3-14B   => 35.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.1 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     7.6 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     7   |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     7.4 |
| cat02_09_fix_process_tree          |     7.4 |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |     4.8 |
| cat03_03_log_skeleton_generation   |     7.4 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     5.4 |
| cat03_06_petri_net_generation      |     7.7 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     7.4 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6.8 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     7.4 |
| cat06_01_bias_text                 |     7.4 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     8.9 |
| cat08_03_transport_opt             |     7.4 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



### QwenQwen3-30B-A3B   => 35.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.5 |
| cat01_02_activity_context          |     3.1 |
| cat01_03_high_level_events         |     7.4 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6.8 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.4 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     6.8 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     7.4 |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     7.4 |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     7.4 |
| cat03_07_process_tree_discovery    |     1.4 |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     6.6 |
| cat04_02_pseudo_bpmn_open_question |     7.6 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     3.7 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     7.4 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     7.4 |
| cat06_03_bias_powl                 |     6.8 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.4 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     8.9 |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     9.5 |
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



### QwenQwen3-32B   => 35.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     6.8 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6.8 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     4.8 |
| cat02_03_anomaly_event_log         |     6.6 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     5.4 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     4.2 |
| cat03_04_declare_generation        |     6.6 |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     6.6 |
| cat04_02_pseudo_bpmn_open_question |     6.6 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     7.4 |
| cat04_07_sql_filt_top_k_vars       |     5.4 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     5.4 |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     8.4 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     7.4 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     4.8 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     7.4 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     6.6 |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     7.6 |



### qwen-turbo-2025-04-28   => 33.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     4.8 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     6.8 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     4.8 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     6.8 |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     7.9 |
| cat08_03_transport_opt             |     7.6 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     7.4 |



### qwen38b   => 33.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     4.2 |
| cat01_04_sensor_recordings         |     2.5 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     6.8 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     6.8 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     8.9 |
| cat03_02_powl_generation           |     7.4 |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     4.2 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     7.6 |
| cat04_03_declare_open_question     |     4.8 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     4.2 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     3.1 |
| cat08_01_queue_mining              |     7.1 |
| cat08_02_instance_spanning         |     7.4 |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     7.6 |
| cat08_05_task_schedul              |     7.7 |



### r1-1776   => 31.8 points

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
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
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
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     7.1 |
| cat05_01_hyp_generation_log        |     3.7 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     4.8 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     7.4 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     7.4 |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     8.9 |



### exaone-deep32b-fp16   => 31.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     7.4 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     7.4 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     7.1 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
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
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     4.8 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     7.1 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.4 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     7.1 |
| cat06_07_fair_unfair_powl          |     3.7 |
| cat08_01_queue_mining              |     7.1 |
| cat08_02_instance_spanning         |     6.8 |
| cat08_03_transport_opt             |     6.8 |
| cat08_04_resource_assign           |     6.8 |
| cat08_05_task_schedul              |     7.7 |



### qwen34b   => 30.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     7.4 |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     7.4 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     7.4 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     5.4 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     5.4 |
| cat08_01_queue_mining              |     5.4 |
| cat08_02_instance_spanning         |     5.4 |
| cat08_03_transport_opt             |     8.4 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     8.2 |



### deepseek-aiDeepSeek-R1-Distill-Qwen-32B   => 30.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     7.4 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.9 |
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
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     8.9 |
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



### exaone-deep7.8b-fp16   => 30.1 points

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
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
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
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     6.6 |
| cat08_01_queue_mining              |     7.1 |
| cat08_02_instance_spanning         |     7.1 |
| cat08_03_transport_opt             |     7.4 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     6.6 |



### deepseekdeepseek-r1-zerofree   => 29.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.8 |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     8.9 |
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
| cat03_02_powl_generation           |     8.9 |
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
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     7.6 |
| cat06_01_bias_text                 |     6.7 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     2   |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     7.2 |
| cat08_05_task_schedul              |     6.8 |



### QwenQwQ-32B-Preview   => 28.7 points

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
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     7.4 |
| cat02_04_powl_anomaly_detection    |     4.2 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     7.4 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     9.5 |
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
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     6.8 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     2   |
| cat08_01_queue_mining              |     6.4 |
| cat08_02_instance_spanning         |     6.8 |
| cat08_03_transport_opt             |     7.4 |
| cat08_04_resource_assign           |     6   |
| cat08_05_task_schedul              |     1   |



### deepseek-aiDeepSeek-R1-Distill-Llama-70B   => 28.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     7.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     8.9 |
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
| cat04_07_sql_filt_top_k_vars       |     9.5 |
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



### deepseekdeepseek-r1-distill-qwen-14b   => 27.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     4.2 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.2 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     3.1 |
| cat02_07_root_cause_2              |     7.4 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     3.7 |
| cat03_02_powl_generation           |     7.4 |
| cat03_03_log_skeleton_generation   |     8.9 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     3.7 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     8.9 |
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



### cogito14b-v1-preview-qwen-fp16   => 25.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8.9 |
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
| cat03_02_powl_generation           |     8.9 |
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
| cat04_05_sql_filt_num_events       |     9.5 |
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
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     3.1 |
| cat06_07_fair_unfair_powl          |     3.1 |
| cat08_01_queue_mining              |     4.8 |
| cat08_02_instance_spanning         |     5.4 |
| cat08_03_transport_opt             |     5.4 |
| cat08_04_resource_assign           |     3.7 |
| cat08_05_task_schedul              |     3.7 |



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
| cat02_03_anomaly_event_log         |     8.2 |
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



### exaone-deep2.4b-fp16   => 23.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     1.4 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     7.6 |
| cat01_06_system_logs               |     4.8 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     8.9 |
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
| cat04_01_pseudo_bpmn_description   |     8.9 |
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



### phi4-mini-reasoning   => 22.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     7.4 |
| cat01_04_sensor_recordings         |     6.8 |
| cat01_05_merge_two_logs            |     4.2 |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     5.4 |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     3.1 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |     6.8 |
| cat02_09_fix_process_tree          |     2   |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     7.4 |
| cat04_02_pseudo_bpmn_open_question |     6.6 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |     4.2 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     2.5 |
| cat05_05_question_gen_nlp          |     6.8 |
| cat05_06_question_pseudo_bpmn      |     7.4 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.4 |
| cat06_02_bias_event_log            |     3.1 |
| cat06_03_bias_powl                 |     6.8 |
| cat06_04_bias_two_logs             |     3.1 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |
| cat08_01_queue_mining              |     6.6 |
| cat08_02_instance_spanning         |     7.7 |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     7.4 |



### qwen-plus-2025-04-28   => 21.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     4.2 |
| cat01_02_activity_context          |     3.1 |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     3.1 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     3.1 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     5.4 |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     7.4 |
| cat02_05_two_powls_anomalies       |     1.4 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     4.2 |
| cat02_08_underfitting_process_tree |     5.4 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     5.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1.4 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.4 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     3.1 |
| cat06_06_bias_mitigation_declare   |     3.1 |
| cat06_07_fair_unfair_powl          |     3.1 |
| cat08_01_queue_mining              |     6.6 |
| cat08_02_instance_spanning         |     7   |
| cat08_03_transport_opt             |     4.8 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     7   |



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
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.2 |
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



### qwen31.7b   => 19.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     7.4 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     2.5 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     5.4 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     6.6 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     5.4 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     6.8 |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     4.2 |
| cat06_03_bias_powl                 |     2.5 |
| cat06_04_bias_two_logs             |     4.8 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     3.1 |
| cat08_01_queue_mining              |     7.4 |
| cat08_02_instance_spanning         |     6   |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     3.1 |
| cat08_05_task_schedul              |     2   |



### deepseekdeepseek-r1-distill-qwen-7b   => 16.8 points

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
| cat08_01_queue_mining              |     2.5 |
| cat08_02_instance_spanning         |     3.1 |
| cat08_03_transport_opt             |     3.1 |
| cat08_04_resource_assign           |     5.4 |
| cat08_05_task_schedul              |     2   |



### qwen30.6b   => 12.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     1.4 |
| cat01_04_sensor_recordings         |     1.4 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1.4 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     7.1 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     7.4 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |     1.4 |
| cat04_02_pseudo_bpmn_open_question |     3.7 |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     7.6 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     6.6 |
| cat06_01_bias_text                 |     6.6 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     1   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     1   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     3.1 |
| cat08_02_instance_spanning         |     2.5 |
| cat08_03_transport_opt             |     3.1 |
| cat08_04_resource_assign           |     3.7 |
| cat08_05_task_schedul              |     2   |



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

