A score in the range **27-34** is considered **sufficient**; a score in the range **34-38** is considered **fair**; a score in the range **38-44** is considered **good**; and a score **>44** is considered **excellent**.

## Large Reasoning Models Leaderboard (Models with CoT) (1-shot; grok-4-1-fast-reasoning used as a judge)

| Model                            | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | OPT                  | :nerd_face: VI       |
|:---------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| Qwen3-235B-A22B-Thinking-2507    | **43.9** | :white_check_mark: | :white_check_mark: | 6.8                  | 7.5                  | :mage_woman: **6.9** | 5.7                  | 5.8                  | **6.3**              | **4.8**              | :mage_woman: **0.0** |
| moonshotaikimi-k2-thinking       | **43.7** | :white_check_mark: | :white_check_mark: | :mage_woman: **7.3** | **8.5**              | 6.4                  | **6.2**              | 5.8                  | 5.5                  | 4.0                  | :mage_woman: **0.0** |
| grok-code-fast-1                 | **42.5** | :x:                | :white_check_mark: | 6.7                  | 7.5                  | 5.3                  | **6.2**              | **6.5**              | 5.6                  | **4.8**              | :mage_woman: **0.0** |
| nemotron-ultra-253b-v1-thinkenab | **42.3** | :white_check_mark: | :white_check_mark: | 6.8                  | 7.8                  | 6.1                  | 5.6                  | 6.0                  | 5.7                  | 4.2                  | :mage_woman: **0.0** |
| qwen3-next-80b-a3b-thinking      | **41.8** | :white_check_mark: | :white_check_mark: | 6.7                  | 7.6                  | 5.1                  | 6.1                  | 6.2                  | 5.7                  | 4.3                  | :mage_woman: **0.0** |
| DeepSeek-V3.1-Reasoner           | **41.7** | :white_check_mark: | :white_check_mark: | 6.6                  | :mage_woman: **8.6** | 5.1                  | 5.9                  | 5.7                  | 5.8                  | 4.1                  | :mage_woman: **0.0** |
| nemotron-super-49b-v1-thinkenab  | **41.5** | :white_check_mark: | :white_check_mark: | 6.7                  | 8.2                  | 5.5                  | 5.5                  | 5.0                  | **6.4**              | 4.2                  | :mage_woman: **0.0** |
| qwen3-235b-a22b-07-25            | **41.4** | :white_check_mark: | :white_check_mark: | 6.6                  | 8.0                  | 3.6                  | :mage_woman: **6.4** | 6.1                  | 6.0                  | **4.7**              | :mage_woman: **0.0** |
| nousresearchhermes-4-70b         | **41.3** | :white_check_mark: | :white_check_mark: | 6.0                  | 8.1                  | 5.4                  | 6.0                  | 4.9                  | 6.2                  | **4.7**              | :mage_woman: **0.0** |
| phi4-reasoningplus               | **41.2** | :white_check_mark: | :white_check_mark: | 6.5                  | 7.4                  | 3.8                  | 5.8                  | :mage_woman: **6.8** | **6.3**              | 4.6                  | :mage_woman: **0.0** |
| DeepSeek-R1-0528                 | **40.7** | :white_check_mark: | :white_check_mark: | 5.8                  | 7.6                  | 5.3                  | 4.9                  | 6.2                  | :mage_woman: **6.6** | 4.4                  | :mage_woman: **0.0** |
| phi4-reasoning                   | **40.6** | :white_check_mark: | :white_check_mark: | **7.1**              | 7.4                  | 4.6                  | 6.0                  | 5.8                  | 5.9                  | 3.8                  | :mage_woman: **0.0** |
| allenaiolmo-3-32b-think          | **40.4** | :white_check_mark: | :white_check_mark: | 6.9                  | 6.5                  | 4.9                  | 5.6                  | 5.7                  | 6.2                  | 4.5                  | :mage_woman: **0.0** |
| nemotron-super-49b-v1.5-thinking | **40.0** | :white_check_mark: | :white_check_mark: | 6.2                  | 7.1                  | 4.9                  | 5.7                  | 5.8                  | **6.4**              | 4.1                  | :mage_woman: **0.0** |
| gpt-oss-120b                     | **39.6** | :white_check_mark: | :white_check_mark: | 5.1                  | 7.5                  | 4.9                  | 5.6                  | 6.1                  | 5.5                  | :mage_woman: **4.9** | :mage_woman: **0.0** |
| qwen34b-thinking-2507-q8_0       | **38.8** | :white_check_mark: | :white_check_mark: | 6.0                  | 7.7                  | 5.7                  | 4.5                  | 6.0                  | 5.3                  | 3.5                  | :mage_woman: **0.0** |
| DeepSeek-R1                      | **38.5** | :white_check_mark: | :white_check_mark: | 6.9                  | 7.0                  | 4.3                  | 5.1                  | 5.0                  | 5.6                  | 4.5                  | :mage_woman: **0.0** |
| magistral-medium-2506            | **37.9** | :x:                | :white_check_mark: | 6.7                  | 7.1                  | 4.0                  | 5.0                  | 5.7                  | 5.7                  | 3.7                  | :mage_woman: **0.0** |
| Qwen3-32B                        | **37.9** | :white_check_mark: | :white_check_mark: | 6.6                  | 6.8                  | 3.2                  | 5.9                  | 5.3                  | 6.0                  | 4.1                  | :mage_woman: **0.0** |
| Qwen3-30B-A3B-2507-Thinking      | **37.6** | :white_check_mark: | :white_check_mark: | 5.7                  | 6.2                  | 5.8                  | 4.6                  | 5.5                  | 6.0                  | 4.0                  | :mage_woman: **0.0** |
| qwen38b                          | **37.3** | :white_check_mark: | :white_check_mark: | 5.8                  | 7.4                  | 3.4                  | 5.2                  | 5.9                  | 5.1                  | 4.5                  | :mage_woman: **0.0** |
| Qwen3-14B                        | **37.1** | :white_check_mark: | :white_check_mark: | 6.3                  | 5.6                  | 4.0                  | 5.7                  | 5.9                  | 6.1                  | 3.6                  | :mage_woman: **0.0** |
| exaone-deep32b-fp16              | **36.9** | :white_check_mark: | :white_check_mark: | 5.8                  | 7.1                  | 4.2                  | 5.4                  | 4.6                  | **6.3**              | 3.6                  | :mage_woman: **0.0** |
| deepseek-r1-zero                 | **35.8** | :white_check_mark: | :white_check_mark: | 6.8                  | 6.1                  | 5.5                  | 3.7                  | 6.2                  | 4.8                  | 2.7                  | :mage_woman: **0.0** |
| r1-1776                          | **35.1** | :white_check_mark: | :white_check_mark: | 3.9                  | 7.6                  | 2.8                  | 5.6                  | 5.9                  | 5.0                  | 4.2                  | :mage_woman: **0.0** |
| QwQ-32B-Preview                  | **34.9** | :white_check_mark: | :white_check_mark: | 5.9                  | 7.3                  | 4.2                  | 4.8                  | 4.4                  | 5.2                  | 3.2                  | :mage_woman: **0.0** |
| magistral-small-2506             | **33.9** | :white_check_mark: | :white_check_mark: | 6.4                  | 6.5                  | 2.7                  | 4.2                  | 4.4                  | 5.6                  | 4.2                  | :mage_woman: **0.0** |
| nemotron-nano-9b-v2-thinking     | **33.5** | :white_check_mark: | :white_check_mark: | 5.5                  | 5.5                  | 3.4                  | 5.5                  | 5.0                  | 4.6                  | 4.0                  | :mage_woman: **0.0** |
| allenaiolmo-3-7b-think           | **32.5** | :white_check_mark: | :white_check_mark: | 6.0                  | 6.2                  | 3.8                  | 4.0                  | 4.4                  | 4.7                  | 3.4                  | :mage_woman: **0.0** |
| sonar-reasoning-pro              | **32.0** | :x:                | :white_check_mark: | 4.9                  | 7.3                  | 2.9                  | 4.3                  | 5.6                  | 4.1                  | 2.8                  | :mage_woman: **0.0** |
| exaone-deep7.8b-fp16             | **31.6** | :white_check_mark: | :white_check_mark: | 4.9                  | 6.2                  | 2.7                  | 5.6                  | 4.7                  | 4.1                  | 3.4                  | :mage_woman: **0.0** |
| qwen34b                          | **30.7** | :white_check_mark: | :white_check_mark: | 5.1                  | 6.6                  | 1.8                  | 5.5                  | 4.0                  | 4.6                  | 3.0                  | :mage_woman: **0.0** |
| qwen-qwq-32b-nostepbystep        | **30.3** | :white_check_mark: | :white_check_mark: | 3.9                  | 5.5                  | 1.5                  | 4.7                  | 5.5                  | 5.4                  | 3.9                  | :mage_woman: **0.0** |
| qwen-qwq-32b-stepbystep          | **29.3** | :white_check_mark: | :white_check_mark: | 2.8                  | 6.0                  | 0.9                  | 5.5                  | 5.1                  | 5.2                  | 3.9                  | :mage_woman: **0.0** |
| gpt-oss-20b                      | **27.7** | :white_check_mark: | :white_check_mark: | 3.4                  | 6.5                  | 1.6                  | 4.5                  | 3.1                  | 4.3                  | 4.3                  | :mage_woman: **0.0** |
| exaone-deep2.4b-fp16             | **23.8** | :white_check_mark: | :white_check_mark: | 4.3                  | 4.9                  | 1.5                  | 3.3                  | 3.4                  | 3.3                  | 3.1                  | :mage_woman: **0.0** |
| phi4-mini-reasoning              | **22.0** | :white_check_mark: | :white_check_mark: | 3.5                  | 2.9                  | 1.2                  | 3.6                  | 3.4                  | 3.9                  | 3.5                  | :mage_woman: **0.0** |
| qwen31.7b                        | **20.6** | :white_check_mark: | :white_check_mark: | 3.1                  | 3.4                  | 1.1                  | 2.7                  | 3.5                  | 3.9                  | 2.9                  | :mage_woman: **0.0** |
| qwen30.6b                        | **11.6** | :white_check_mark: | :white_check_mark: | 1.1                  | 2.9                  | 0.9                  | 1.4                  | 2.3                  | 2.0                  | 1.0                  | :mage_woman: **0.0** |

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



### moonshotaikimi-k2-thinking   => 43.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     9.3 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     9.5 |
| cat02_06_root_cause_1              |     9.8 |
| cat02_07_root_cause_2              |    10   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.2 |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6.7 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |    10   |
| cat03_07_process_tree_discovery    |     8.2 |
| cat03_08_powl_discovery            |     8.2 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     9.5 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     5.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     8.2 |
| cat05_02_hyp_gen_powl              |     1   |
| cat05_03_hyp_gen_declare           |     9.8 |
| cat05_04_hyp_gen_temp_profile      |     8.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     9.5 |
| cat08_03_transport_opt             |     9.5 |
| cat08_04_resource_assign           |     2.2 |
| cat08_05_task_schedul              |     9.5 |



### grok-code-fast-1   => 42.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     7.4 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     8.6 |
| cat02_05_two_powls_anomalies       |     1.4 |
| cat02_06_root_cause_1              |    10   |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     4.2 |
| cat03_05_temp_profile_generation   |     6.7 |
| cat03_06_petri_net_generation      |    10   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     8.6 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.6 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     7.2 |
| cat05_04_hyp_gen_temp_profile      |    10   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     6.7 |
| cat06_07_fair_unfair_powl          |     4.2 |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     9.5 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |    10   |



### nvidiallama-3.1-nemotron-ultra-253b-v1-thinkenab   => 42.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     6.7 |
| cat01_05_merge_two_logs            |     9.5 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.6 |
| cat01_08_tables_to_log             |     7.1 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     8.2 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     7.2 |
| cat02_07_root_cause_2              |     9.3 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.2 |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     6.7 |
| cat04_01_pseudo_bpmn_description   |    10   |
| cat04_02_pseudo_bpmn_open_question |     7.4 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.2 |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     9.5 |
| cat05_03_hyp_gen_declare           |     9.5 |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.6 |
| cat08_02_instance_spanning         |     9.5 |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



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



### DeepSeek-V3.1-Reasoner   => 41.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.3 |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |    10   |
| cat02_07_root_cause_2              |     9.3 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     2.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     8.2 |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     9.3 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     8.2 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     9.5 |
| cat08_03_transport_opt             |     9.5 |
| cat08_04_resource_assign           |     3.3 |
| cat08_05_task_schedul              |     9.5 |



### nvidiallama-3.3-nemotron-super-49b-v1-thinkenab   => 41.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     8.6 |
| cat01_08_tables_to_log             |     8.2 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     8.2 |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     8.2 |
| cat03_06_petri_net_generation      |     6.6 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     2.2 |
| cat04_01_pseudo_bpmn_description   |     8.6 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     7.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     6.8 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     8.2 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     6.7 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     9.5 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.3 |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     7.3 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



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



### nousresearchhermes-4-70b   => 41.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |    10   |
| cat01_05_merge_two_logs            |     7.4 |
| cat01_06_system_logs               |     6.8 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     6   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     8.2 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.3 |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |    10   |
| cat02_07_root_cause_2              |     6.6 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     2.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     5.4 |
| cat03_05_temp_profile_generation   |     8.2 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     8.4 |
| cat04_03_declare_open_question     |     7.4 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |     7.9 |
| cat05_03_hyp_gen_declare           |     6.7 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     4.2 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     8.6 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |     6.6 |
| cat06_06_bias_mitigation_declare   |    10   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     9.3 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     8.9 |



### phi4-reasoningplus   => 41.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     9.3 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     9.3 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     4.2 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     1.7 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     8.2 |
| cat04_01_pseudo_bpmn_description   |    10   |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     7.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     9.5 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     9.5 |
| cat05_04_hyp_gen_temp_profile      |     8.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     8.6 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     8.2 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     9.3 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     9.3 |



### deepseek-aiDeepSeek-R1-0528   => 40.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     6.6 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.3 |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     7.4 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     3.3 |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |    10   |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     7.4 |
| cat04_03_declare_open_question     |     3.3 |
| cat04_04_declare_description       |     2.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.2 |
| cat05_01_hyp_generation_log        |     5.6 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     8.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     9.3 |
| cat06_03_bias_powl                 |     9.3 |
| cat06_04_bias_two_logs             |     9.3 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     8.9 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |    10   |
| cat08_05_task_schedul              |     9.5 |



### phi4-reasoning   => 40.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     7.2 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.6 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     9.5 |
| cat02_07_root_cause_2              |     6.7 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     5.4 |
| cat03_05_temp_profile_generation   |     7.2 |
| cat03_06_petri_net_generation      |     4.2 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     3.7 |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     6.7 |
| cat05_04_hyp_gen_temp_profile      |     7.2 |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |     9.3 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     7.2 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     7.2 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     8.2 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     9.5 |
| cat08_03_transport_opt             |     9.3 |
| cat08_04_resource_assign           |     9.3 |
| cat08_05_task_schedul              |     1.4 |



### allenaiolmo-3-32b-think   => 40.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     9.5 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     7.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.4 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |     4.2 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     7.2 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     9.5 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.2 |
| cat03_01_process_tree_generation   |     2.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     8.2 |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     8.2 |
| cat04_01_pseudo_bpmn_description   |     7.2 |
| cat04_02_pseudo_bpmn_open_question |     8.6 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     4.5 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.2 |
| cat05_01_hyp_generation_log        |     7.2 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     7.4 |
| cat05_04_hyp_gen_temp_profile      |     7.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     9.5 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     8.6 |



### nvidiallama-3.3-nemotron-super-49b-v1.5-thinking   => 40.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     3.7 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.4 |
| cat01_08_tables_to_log             |     8.6 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     7.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     6.6 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.9 |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     6.7 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     8.6 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     5.6 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.2 |
| cat05_01_hyp_generation_log        |     7.2 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     9.3 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     9.3 |
| cat08_02_instance_spanning         |     8.6 |
| cat08_03_transport_opt             |     8.4 |
| cat08_04_resource_assign           |     6   |
| cat08_05_task_schedul              |     8.6 |



### gpt-oss-120b   => 39.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2.2 |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |     8.6 |
| cat01_04_sensor_recordings         |    10   |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.2 |
| cat02_03_anomaly_event_log         |     8.6 |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     7.2 |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |    10   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     6.6 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     8.2 |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     7.7 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     7.7 |
| cat04_01_pseudo_bpmn_description   |     8.6 |
| cat04_02_pseudo_bpmn_open_question |     8.6 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     6.6 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     8.2 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     7.2 |
| cat05_04_hyp_gen_temp_profile      |     7.2 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     5.4 |
| cat06_03_bias_powl                 |     9.3 |
| cat06_04_bias_two_logs             |     6.7 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |    10   |
| cat08_03_transport_opt             |     9.8 |
| cat08_04_resource_assign           |    10   |
| cat08_05_task_schedul              |     9.5 |



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



### deepseek-aiDeepSeek-R1   => 38.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.6 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     6.7 |
| cat02_06_root_cause_1              |     9.5 |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.2 |
| cat03_01_process_tree_generation   |     8.9 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     4.5 |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     9.3 |
| cat04_03_declare_open_question     |     5.6 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     6.7 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |    10   |
| cat06_03_bias_powl                 |     9.3 |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     7.4 |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     9.3 |



### magistral-medium-2506   => 37.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |    10   |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     7.4 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     6.7 |
| cat02_03_anomaly_event_log         |     7.2 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.2 |
| cat02_06_root_cause_1              |    10   |
| cat02_07_root_cause_2              |     9.3 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.3 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6.7 |
| cat03_04_declare_generation        |     6.6 |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     8.6 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     4.5 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     8.2 |
| cat05_02_hyp_gen_powl              |     5.6 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     8.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     7.2 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     3.2 |



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



### exaone-deep32b-fp16   => 36.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     3.3 |
| cat01_05_merge_two_logs            |     3.3 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     6.7 |
| cat02_04_powl_anomaly_detection    |     8.6 |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |     6.7 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     8.4 |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     2.2 |
| cat03_05_temp_profile_generation   |     2.2 |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     6.7 |
| cat04_01_pseudo_bpmn_description   |     9.3 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     5.6 |
| cat04_05_sql_filt_num_events       |     8.2 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     4.2 |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     5.6 |
| cat05_05_question_gen_nlp          |     9.3 |
| cat05_06_question_pseudo_bpmn      |     3.3 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |    10   |
| cat06_07_fair_unfair_powl          |     6.6 |
| cat08_01_queue_mining              |     7   |
| cat08_02_instance_spanning         |     7.3 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     6   |
| cat08_05_task_schedul              |     8.2 |



### deepseekdeepseek-r1-zerofree   => 35.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     8.6 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     3.3 |
| cat02_05_two_powls_anomalies       |     1   |
| cat02_06_root_cause_1              |     8.2 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     8.2 |
| cat03_05_temp_profile_generation   |     7.2 |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |     6.7 |
| cat04_02_pseudo_bpmn_open_question |     1   |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     8.2 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     9.5 |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     7.2 |
| cat06_03_bias_powl                 |     1   |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     6.6 |
| cat08_01_queue_mining              |     6.7 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     1   |
| cat08_05_task_schedul              |     5.6 |



### r1-1776   => 35.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.2 |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     3.3 |
| cat01_06_system_logs               |     2.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     2.2 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     2.2 |
| cat03_07_process_tree_discovery    |     9.5 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.2 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     6.7 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     7.2 |
| cat08_01_queue_mining              |     8.6 |
| cat08_02_instance_spanning         |     9.3 |
| cat08_03_transport_opt             |     7.9 |
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



### magistral-small-2506   => 33.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     7.2 |
| cat01_08_tables_to_log             |     6.6 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     4.2 |
| cat02_06_root_cause_1              |     6.7 |
| cat02_07_root_cause_2              |     6.6 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1.1 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     6.7 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     7.4 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     8.2 |
| cat05_03_hyp_gen_declare           |     2.2 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     6.7 |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     7.2 |
| cat06_03_bias_powl                 |     9.3 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     3.1 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.6 |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



### nvidianemotron-nano-9b-v2-thinking   => 33.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.2 |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     6.7 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     5.4 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |    10   |
| cat03_05_temp_profile_generation   |     8.2 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.2 |
| cat04_01_pseudo_bpmn_description   |     7.2 |
| cat04_02_pseudo_bpmn_open_question |     7.9 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     5.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     6.8 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     7.2 |
| cat08_05_task_schedul              |     9.5 |



### allenaiolmo-3-7b-think   => 32.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |    10   |
| cat01_03_high_level_events         |     9.3 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     2.2 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     5.4 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     6.6 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     6.7 |
| cat02_06_root_cause_1              |     3.1 |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     5.6 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     3.1 |
| cat04_07_sql_filt_top_k_vars       |     7.4 |
| cat05_01_hyp_generation_log        |     2.2 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     3.3 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     3.3 |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.2 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     1.1 |
| cat08_05_task_schedul              |     8.4 |



### sonar-reasoning-pro   => 32.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     7.2 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     2.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     8.6 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     7.2 |
| cat02_07_root_cause_2              |     6.7 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.2 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     2.2 |
| cat03_05_temp_profile_generation   |     8.2 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     7.2 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     3.3 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     5.4 |
| cat05_01_hyp_generation_log        |     8.2 |
| cat05_02_hyp_gen_powl              |     8.2 |
| cat05_03_hyp_gen_declare           |     6.7 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.3 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     1.7 |
| cat06_03_bias_powl                 |     8.6 |
| cat06_04_bias_two_logs             |     9.3 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     3.1 |
| cat08_01_queue_mining              |     7.2 |
| cat08_02_instance_spanning         |     5.6 |
| cat08_03_transport_opt             |     5.6 |
| cat08_04_resource_assign           |     3.3 |
| cat08_05_task_schedul              |     6.6 |



### exaone-deep7.8b-fp16   => 31.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     2.2 |
| cat01_07_interv_to_pseudo_bpmn     |     7.2 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     4.2 |
| cat02_04_powl_anomaly_detection    |     7.2 |
| cat02_05_two_powls_anomalies       |     5.4 |
| cat02_06_root_cause_1              |     6.7 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     5.4 |
| cat03_03_log_skeleton_generation   |     2.2 |
| cat03_04_declare_generation        |     8.9 |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     5.6 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     9.5 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     3.3 |
| cat05_04_hyp_gen_temp_profile      |     5.6 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     9.3 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     9.3 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     6.7 |
| cat08_02_instance_spanning         |     5.6 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     5.7 |



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



### gpt-oss-20b   => 27.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     3.1 |
| cat01_03_high_level_events         |     6.7 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     3.3 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     8.2 |
| cat02_02_conf_desiderata           |     7.1 |
| cat02_03_anomaly_event_log         |     7.2 |
| cat02_04_powl_anomaly_detection    |     7.2 |
| cat02_05_two_powls_anomalies       |     8.2 |
| cat02_06_root_cause_1              |     7.2 |
| cat02_07_root_cause_2              |     4.5 |
| cat02_08_underfitting_process_tree |     8.2 |
| cat02_09_fix_process_tree          |     6.7 |
| cat03_01_process_tree_generation   |     1.4 |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2.2 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.3 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     9.3 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     1.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     5.4 |
| cat05_03_hyp_gen_declare           |     2.2 |
| cat05_04_hyp_gen_temp_profile      |     3.3 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     3.3 |
| cat06_01_bias_text                 |     7.2 |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     9.3 |
| cat06_04_bias_two_logs             |     6.7 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     2.2 |
| cat08_01_queue_mining              |     9.3 |
| cat08_02_instance_spanning         |     8.6 |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     9.3 |
| cat08_05_task_schedul              |     8.2 |



### exaone-deep2.4b-fp16   => 23.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1.4 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     7.2 |
| cat01_05_merge_two_logs            |     8.2 |
| cat01_06_system_logs               |     3.3 |
| cat01_07_interv_to_pseudo_bpmn     |     7.2 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     6.6 |
| cat02_06_root_cause_1              |     3.3 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     5.4 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2.2 |
| cat04_01_pseudo_bpmn_description   |     6.6 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     5.6 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     3.3 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     3.3 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     5.6 |
| cat05_07_question_interview        |     7.2 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     2.2 |
| cat06_03_bias_powl                 |     2.5 |
| cat06_04_bias_two_logs             |     8.6 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     2.5 |
| cat08_01_queue_mining              |     6.3 |
| cat08_02_instance_spanning         |     6   |
| cat08_03_transport_opt             |     5.6 |
| cat08_04_resource_assign           |     6.7 |
| cat08_05_task_schedul              |     6.7 |



### phi4-mini-reasoning   => 22.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     6.7 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     5.4 |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     6.7 |
| cat02_06_root_cause_1              |     3.3 |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     2.2 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     2.2 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     7.2 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     5.6 |
| cat04_04_declare_description       |     2.2 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     2.5 |
| cat04_07_sql_filt_top_k_vars       |     4.2 |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     2.5 |
| cat05_03_hyp_gen_declare           |     1.4 |
| cat05_04_hyp_gen_temp_profile      |     3.3 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     5.4 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     3.1 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     1.4 |
| cat06_07_fair_unfair_powl          |     1.4 |
| cat08_01_queue_mining              |     6.6 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     6   |
| cat08_04_resource_assign           |     7.9 |
| cat08_05_task_schedul              |     6.3 |



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

