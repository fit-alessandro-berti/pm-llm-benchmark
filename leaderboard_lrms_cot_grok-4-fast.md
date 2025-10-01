A score in the range **27-34** is considered **sufficient**; a score in the range **34-38** is considered **fair**; a score in the range **38-44** is considered **good**; and a score **>44** is considered **excellent**.

## Large Reasoning Models Leaderboard (Models with CoT) (1-shot; x-ai/grok-4-fast:free used as a judge)

| Model                            | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | OPT                  | :nerd_face: VI       |
|:---------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| Grok-3-beta-thinking-20250221    | **45.7** | :x:                | :white_check_mark: | **6.9**              | :mage_woman: **8.5** | :mage_woman: **6.9** | **6.2**              | **6.3**              | :mage_woman: **6.7** | 4.3                  | :mage_woman: **0.0** |
| grok-3-mini-high                 | **44.6** | :x:                | :white_check_mark: | **6.8**              | 8.1                  | 6.3                  | **6.2**              | 5.7                  | :mage_woman: **6.7** | **4.7**              | :mage_woman: **0.0** |
| Qwen3-235B-A22B-Thinking-2507    | **43.3** | :white_check_mark: | :white_check_mark: | 6.4                  | 7.5                  | 6.6                  | 5.7                  | **6.3**              | 6.0                  | :mage_woman: **4.8** | :mage_woman: **0.0** |
| grok-code-fast-1                 | **42.2** | :x:                | :white_check_mark: | 6.5                  | **8.3**              | 4.9                  | 6.0                  | :mage_woman: **6.6** | 5.2                  | **4.6**              | :mage_woman: **0.0** |
| DeepSeek-V3.1-Reasoner           | **42.1** | :white_check_mark: | :white_check_mark: | 6.6                  | 7.8                  | 5.4                  | 6.0                  | 5.8                  | 5.6                  | :mage_woman: **4.8** | :mage_woman: **0.0** |
| phi4-reasoningplus               | **41.5** | :white_check_mark: | :white_check_mark: | 6.5                  | 8.1                  | 4.8                  | 5.6                  | **6.4**              | 5.9                  | 4.2                  | :mage_woman: **0.0** |
| grok-3-mini-low                  | **41.4** | :x:                | :white_check_mark: | 6.2                  | 7.8                  | 4.5                  | :mage_woman: **6.5** | 5.6                  | 6.3                  | **4.5**              | :mage_woman: **0.0** |
| nemotron-ultra-253b-v1-thinkenab | **41.4** | :white_check_mark: | :white_check_mark: | **6.8**              | 7.9                  | 5.6                  | 5.3                  | 5.7                  | 5.8                  | 4.2                  | :mage_woman: **0.0** |
| qwen3-next-80b-a3b-thinking      | **41.3** | :white_check_mark: | :white_check_mark: | 6.2                  | 7.0                  | 4.5                  | **6.4**              | **6.4**              | 6.1                  | **4.5**              | :mage_woman: **0.0** |
| DeepSeek-R1-0528                 | **41.0** | :white_check_mark: | :white_check_mark: | 6.0                  | 8.1                  | 5.2                  | 5.6                  | 5.8                  | 6.3                  | 4.1                  | :mage_woman: **0.0** |
| Qwen3-235B-A22B                  | **40.7** | :white_check_mark: | :white_check_mark: | 6.2                  | 7.4                  | 4.7                  | **6.2**              | 6.1                  | 6.3                  | 3.9                  | :mage_woman: **0.0** |
| nemotron-super-49b-v1-thinkenab  | **40.0** | :white_check_mark: | :white_check_mark: | 6.2                  | 8.1                  | 5.7                  | 4.7                  | 5.0                  | 6.2                  | 4.2                  | :mage_woman: **0.0** |
| DeepSeek-R1                      | **39.6** | :white_check_mark: | :white_check_mark: | 6.4                  | 6.9                  | 5.4                  | 5.9                  | 5.2                  | 5.5                  | 4.2                  | :mage_woman: **0.0** |
| qwen3-235b-a22b-07-25            | **39.5** | :white_check_mark: | :white_check_mark: | 6.0                  | 7.0                  | 3.5                  | **6.4**              | 6.1                  | 6.1                  | **4.5**              | :mage_woman: **0.0** |
| magistral-medium-2506            | **39.0** | :x:                | :white_check_mark: | 6.5                  | 7.0                  | 4.4                  | 5.2                  | 5.9                  | 6.2                  | 3.9                  | :mage_woman: **0.0** |
| Qwen3-14B                        | **38.9** | :white_check_mark: | :white_check_mark: | 6.0                  | 7.6                  | 3.8                  | 5.9                  | 5.6                  | 5.9                  | 4.0                  | :mage_woman: **0.0** |
| phi4-reasoning                   | **38.7** | :white_check_mark: | :white_check_mark: | :mage_woman: **7.0** | 6.6                  | 4.2                  | 5.9                  | 5.6                  | 4.7                  | **4.7**              | :mage_woman: **0.0** |
| nousresearchhermes-4-70b         | **38.3** | :white_check_mark: | :white_check_mark: | 5.3                  | 7.9                  | 4.6                  | 5.1                  | 4.8                  | 6.0                  | **4.5**              | :mage_woman: **0.0** |
| Qwen3-32B                        | **38.0** | :white_check_mark: | :white_check_mark: | **6.9**              | 6.6                  | 3.9                  | 5.5                  | 5.6                  | 5.1                  | 4.3                  | :mage_woman: **0.0** |
| gpt-oss-120b                     | **37.8** | :white_check_mark: | :white_check_mark: | 5.6                  | 6.7                  | 4.3                  | 5.5                  | 5.9                  | 5.3                  | **4.7**              | :mage_woman: **0.0** |
| exaone-deep32b-fp16              | **37.4** | :white_check_mark: | :white_check_mark: | 6.0                  | 7.7                  | 4.2                  | 5.0                  | 5.1                  | 5.3                  | 4.2                  | :mage_woman: **0.0** |
| qwen34b-thinking-2507-q8_0       | **37.4** | :white_check_mark: | :white_check_mark: | 6.0                  | 7.9                  | 4.9                  | 4.4                  | 5.4                  | 5.0                  | 3.8                  | :mage_woman: **0.0** |
| Qwen3-30B-A3B                    | **37.1** | :white_check_mark: | :white_check_mark: | 5.5                  | 7.1                  | 3.1                  | 5.9                  | 5.8                  | 6.0                  | 3.9                  | :mage_woman: **0.0** |
| Qwen3-30B-A3B-2507-Thinking      | **35.7** | :white_check_mark: | :white_check_mark: | 4.5                  | 6.5                  | 5.1                  | 5.1                  | 5.4                  | 4.9                  | 4.3                  | :mage_woman: **0.0** |
| QwQ-32B-Preview                  | **35.6** | :white_check_mark: | :white_check_mark: | 5.8                  | 7.0                  | 5.0                  | 5.1                  | 4.2                  | 5.5                  | 3.1                  | :mage_woman: **0.0** |
| qwen38b                          | **35.2** | :white_check_mark: | :white_check_mark: | 5.1                  | 6.5                  | 3.8                  | 5.2                  | 5.7                  | 5.1                  | 3.9                  | :mage_woman: **0.0** |
| r1-1776                          | **34.8** | :white_check_mark: | :white_check_mark: | 4.4                  | 7.8                  | 2.4                  | 5.8                  | 5.2                  | 4.9                  | 4.2                  | :mage_woman: **0.0** |
| deepseek-r1-zero                 | **34.2** | :white_check_mark: | :white_check_mark: | 5.9                  | 5.8                  | 5.4                  | 4.9                  | 5.9                  | 3.6                  | 2.8                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-32B     | **34.1** | :white_check_mark: | :white_check_mark: | 5.9                  | 7.0                  | 4.4                  | 4.4                  | 4.6                  | 5.3                  | 2.5                  | :mage_woman: **0.0** |
| nemotron-nano-9b-v2-thinking     | **33.2** | :white_check_mark: | :white_check_mark: | 5.3                  | 5.2                  | 3.6                  | 5.4                  | 5.2                  | 4.9                  | 3.6                  | :mage_woman: **0.0** |
| magistral-small-2506             | **33.0** | :white_check_mark: | :white_check_mark: | 6.0                  | 5.9                  | 3.4                  | 4.5                  | 4.1                  | 5.3                  | 3.7                  | :mage_woman: **0.0** |
| sonar-reasoning-pro              | **32.3** | :x:                | :white_check_mark: | 4.5                  | 7.0                  | 2.6                  | 4.5                  | 5.5                  | 5.0                  | 3.1                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Llama-70B    | **31.6** | :white_check_mark: | :white_check_mark: | 5.1                  | 5.4                  | 3.3                  | 5.7                  | 5.3                  | 5.0                  | 1.9                  | :mage_woman: **0.0** |
| qwen-qwq-32b-nostepbystep        | **31.0** | :white_check_mark: | :white_check_mark: | 4.6                  | 5.3                  | 1.1                  | 5.2                  | 5.4                  | 5.4                  | 4.1                  | :mage_woman: **0.0** |
| exaone-deep7.8b-fp16             | **31.0** | :white_check_mark: | :white_check_mark: | 4.7                  | 5.6                  | 2.9                  | 4.7                  | 5.3                  | 4.3                  | 3.5                  | :mage_woman: **0.0** |
| qwen34b                          | **30.6** | :white_check_mark: | :white_check_mark: | 4.7                  | 6.2                  | 1.9                  | 4.7                  | 4.9                  | 4.4                  | 3.7                  | :mage_woman: **0.0** |
| cogito14b-v1-preview-qwen-fp16   | **29.3** | :white_check_mark: | :white_check_mark: | 4.4                  | 5.3                  | 2.8                  | 3.7                  | 5.0                  | 4.9                  | 3.2                  | :mage_woman: **0.0** |
| deepseek-r1-distill-qwen-14b     | **29.1** | :white_check_mark: | :white_check_mark: | 4.5                  | 6.3                  | 3.3                  | 4.0                  | 4.3                  | 4.8                  | 2.0                  | :mage_woman: **0.0** |
| qwen-qwq-32b-stepbystep          | **29.1** | :white_check_mark: | :white_check_mark: | 3.8                  | 6.0                  | 1.6                  | 5.3                  | 4.3                  | 4.5                  | 3.6                  | :mage_woman: **0.0** |
| gpt-oss-20b                      | **27.7** | :white_check_mark: | :white_check_mark: | 3.2                  | 7.1                  | 1.7                  | 4.3                  | 3.3                  | 4.1                  | 4.1                  | :mage_woman: **0.0** |
| exaone-deep2.4b-fp16             | **26.2** | :white_check_mark: | :white_check_mark: | 4.4                  | 6.1                  | 2.1                  | 3.2                  | 3.9                  | 3.7                  | 2.9                  | :mage_woman: **0.0** |
| deepseek-r1-distill-llama-8b     | **24.0** | :white_check_mark: | :white_check_mark: | 3.4                  | 5.3                  | 1.9                  | 2.9                  | 3.7                  | 4.5                  | 2.3                  | :mage_woman: **0.0** |
| phi4-mini-reasoning              | **22.0** | :white_check_mark: | :white_check_mark: | 3.7                  | 2.8                  | 1.6                  | 3.6                  | 3.9                  | 3.3                  | 3.1                  | :mage_woman: **0.0** |
| qwen31.7b                        | **21.3** | :white_check_mark: | :white_check_mark: | 2.6                  | 3.7                  | 1.4                  | 2.9                  | 3.8                  | 3.9                  | 3.1                  | :mage_woman: **0.0** |
| deepseek-r1-distill-qwen-7b      | **15.8** | :white_check_mark: | :white_check_mark: | 2.1                  | 2.9                  | 1.8                  | 2.3                  | 3.3                  | 1.9                  | 1.6                  | :mage_woman: **0.0** |
| qwen30.6b                        | **14.2** | :white_check_mark: | :white_check_mark: | 1.6                  | 3.3                  | 1.1                  | 1.8                  | 3.0                  | 2.2                  | 1.3                  | :mage_woman: **0.0** |
| deepseek-r1-distill-qwen-1.5b    | **9.6**  | :white_check_mark: | :white_check_mark: | 1.5                  | 2.1                  | 0.9                  | 1.0                  | 2.0                  | 1.6                  | 0.6                  | :mage_woman: **0.0** |

### Grok-3-beta-thinking-20250221   => 45.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     7.4 |
| cat01_06_system_logs               |     8.9 |
| cat01_07_interv_to_pseudo_bpmn     |     7.4 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     9.5 |
| cat02_06_root_cause_1              |    10   |
| cat02_07_root_cause_2              |    10   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |    10   |
| cat03_05_temp_profile_generation   |     8.2 |
| cat03_06_petri_net_generation      |     6.8 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     6.8 |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     9.5 |
| cat04_03_declare_open_question     |     7.1 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |    10   |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |    10   |
| cat05_04_hyp_gen_temp_profile      |     7.4 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |    10   |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |     7.2 |
| cat08_03_transport_opt             |     7.7 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     8.2 |



### grok-3-mini-high   => 44.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     7.7 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |    10   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     9.5 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6.8 |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     7.1 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     8.9 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     7.4 |
| cat05_04_hyp_gen_temp_profile      |     6.8 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     9.5 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |     9.5 |
| cat08_03_transport_opt             |     9.5 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     9.5 |



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



### grok-code-fast-1   => 42.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     6.7 |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     8.9 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |     8.2 |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     9.5 |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |    10   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     4.2 |
| cat03_04_declare_generation        |     3.7 |
| cat03_05_temp_profile_generation   |     8.2 |
| cat03_06_petri_net_generation      |     6   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |    10   |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     5.6 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     9.5 |
| cat05_01_hyp_generation_log        |     9.5 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |    10   |
| cat05_04_hyp_gen_temp_profile      |     9.5 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     3.7 |
| cat06_07_fair_unfair_powl          |     2.5 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     8.9 |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |    10   |



### DeepSeek-V3.1-Reasoner   => 42.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |    10   |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     8.2 |
| cat02_05_two_powls_anomalies       |     4.8 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |    10   |
| cat02_08_underfitting_process_tree |     7.4 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     9.5 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     7.1 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     7.2 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     6.8 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     3.3 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |    10   |
| cat08_03_transport_opt             |     9.5 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     9.5 |



### phi4-reasoningplus   => 41.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.7 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     7.4 |
| cat01_06_system_logs               |     7.7 |
| cat01_07_interv_to_pseudo_bpmn     |     8.9 |
| cat01_08_tables_to_log             |     6.8 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     6.6 |
| cat03_05_temp_profile_generation   |     9.5 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     4.2 |
| cat04_01_pseudo_bpmn_description   |    10   |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |    10   |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     7.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     7.2 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     7.2 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     9.3 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.2 |



### grok-3-mini-low   => 41.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     4.2 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     6.8 |
| cat02_06_root_cause_1              |     7.4 |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |     9.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.3 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.7 |
| cat04_01_pseudo_bpmn_description   |    10   |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     8.2 |
| cat04_04_declare_description       |     8.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     8.9 |
| cat06_07_fair_unfair_powl          |     9.5 |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     9.5 |



### nvidiallama-3.1-nemotron-ultra-253b-v1-thinkenab   => 41.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     7.4 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |    10   |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |    10   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     8.9 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     6.8 |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     7.4 |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |     7.1 |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     7.1 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     8.9 |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     9.5 |



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



### deepseek-aiDeepSeek-R1-0528   => 41.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     8.2 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     4.8 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     5.4 |
| cat03_08_powl_discovery            |     8.9 |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.8 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     8.9 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     9.5 |
| cat06_07_fair_unfair_powl          |     7.7 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     6.7 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     8.2 |



### QwenQwen3-235B-A22B   => 40.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     7.4 |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     8.2 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     7.2 |
| cat02_04_powl_anomaly_detection    |     8.2 |
| cat02_05_two_powls_anomalies       |     9.5 |
| cat02_06_root_cause_1              |     6.7 |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     6.8 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |    10   |
| cat03_06_petri_net_generation      |     3.7 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     9.5 |
| cat05_01_hyp_generation_log        |     8.2 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     9.5 |
| cat05_04_hyp_gen_temp_profile      |     8.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.9 |
| cat08_03_transport_opt             |     5.5 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     8.2 |



### nvidiallama-3.3-nemotron-super-49b-v1-thinkenab   => 40.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     8.2 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     6.6 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     6.6 |
| cat03_03_log_skeleton_generation   |    10   |
| cat03_04_declare_generation        |    10   |
| cat03_05_temp_profile_generation   |     6.6 |
| cat03_06_petri_net_generation      |     3.7 |
| cat03_07_process_tree_discovery    |     8.9 |
| cat03_08_powl_discovery            |     6.8 |
| cat04_01_pseudo_bpmn_description   |     7.2 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     2.5 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     6.7 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     9.5 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     7.7 |



### deepseek-aiDeepSeek-R1   => 39.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     9.3 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     7.2 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     6.8 |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     7.1 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     6.8 |
| cat03_05_temp_profile_generation   |     7.2 |
| cat03_06_petri_net_generation      |    10   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     8.9 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.2 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     8.2 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     8.9 |



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



### magistral-medium-2506   => 39.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     7.2 |
| cat01_08_tables_to_log             |     7.1 |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     7.4 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.2 |
| cat02_06_root_cause_1              |    10   |
| cat02_07_root_cause_2              |     7.2 |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.3 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     4.2 |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     6.7 |
| cat04_01_pseudo_bpmn_description   |     6.6 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     4.2 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     7.4 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     7.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |    10   |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     8.2 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     6.8 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     6   |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     9.3 |



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



### phi4-reasoning   => 38.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     9.5 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     7.2 |
| cat01_05_merge_two_logs            |     7.4 |
| cat01_06_system_logs               |     8.9 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |     9.5 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |     8.2 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |     6.8 |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     3.7 |
| cat03_03_log_skeleton_generation   |     8.2 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     9.5 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     4.5 |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     8.2 |
| cat05_03_hyp_gen_declare           |     7.2 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     7.4 |
| cat06_04_bias_two_logs             |     6.8 |
| cat06_05_bias_two_logs_2           |     6.8 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.9 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |    10   |
| cat08_03_transport_opt             |     9.5 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     9.3 |



### nousresearchhermes-4-70b   => 38.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     4.5 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     9.5 |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     8.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6.8 |
| cat02_06_root_cause_1              |     9.5 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     6.6 |
| cat03_05_temp_profile_generation   |     3.7 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |    10   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     3.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     7.4 |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     3.7 |
| cat05_07_question_interview        |     8.2 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |    10   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     7.2 |
| cat08_03_transport_opt             |    10   |
| cat08_04_resource_assign           |    10   |
| cat08_05_task_schedul              |     8.9 |



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



### gpt-oss-120b   => 37.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |    10   |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     7.2 |
| cat01_07_interv_to_pseudo_bpmn     |     7.4 |
| cat01_08_tables_to_log             |     8.2 |
| cat02_01_conformance_textual       |     6.6 |
| cat02_02_conf_desiderata           |     6.8 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     6.7 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     7.1 |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     7.7 |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     7.1 |
| cat03_05_temp_profile_generation   |     8.2 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     6.8 |
| cat04_01_pseudo_bpmn_description   |     7.4 |
| cat04_02_pseudo_bpmn_open_question |     9.5 |
| cat04_03_declare_open_question     |     6.7 |
| cat04_04_declare_description       |     4.8 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     6.6 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     8.9 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     6.7 |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |     7.4 |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |    10   |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     9.5 |
| cat06_06_bias_mitigation_declare   |     3.7 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |    10   |
| cat08_03_transport_opt             |     8.9 |
| cat08_04_resource_assign           |     9.5 |
| cat08_05_task_schedul              |     8.2 |



### exaone-deep32b-fp16   => 37.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.8 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     3.7 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     8.2 |
| cat01_08_tables_to_log             |    10   |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     9.5 |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |     6.8 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.7 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     6.6 |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     4.2 |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |    10   |
| cat04_01_pseudo_bpmn_description   |    10   |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     7.1 |
| cat04_04_declare_description       |     4.8 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |    10   |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     4.2 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     7.1 |
| cat06_07_fair_unfair_powl          |     3.7 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.9 |
| cat08_03_transport_opt             |     7.2 |
| cat08_04_resource_assign           |     8.9 |
| cat08_05_task_schedul              |     8.9 |



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



### QwenQwen3-30B-A3B   => 37.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.8 |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     6.7 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     7.2 |
| cat02_02_conf_desiderata           |     6.8 |
| cat02_03_anomaly_event_log         |     8.2 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     7.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3.1 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     3.7 |
| cat03_05_temp_profile_generation   |     6.8 |
| cat03_06_petri_net_generation      |     6.6 |
| cat03_07_process_tree_discovery    |     1.4 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     8.9 |
| cat05_02_hyp_gen_powl              |     4.8 |
| cat05_03_hyp_gen_declare           |     7.2 |
| cat05_04_hyp_gen_temp_profile      |     8.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     7.4 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     9.5 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     6.7 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     7.2 |



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



### r1-1776   => 34.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.2 |
| cat01_02_activity_context          |     4.8 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     9.5 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     7.2 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |    10   |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     1   |
| cat02_07_root_cause_2              |    10   |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     8.2 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     4.8 |
| cat04_04_declare_description       |     8.9 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     1.7 |
| cat05_03_hyp_gen_declare           |     9.5 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     8.2 |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     6.8 |
| cat06_06_bias_mitigation_declare   |     1.4 |
| cat06_07_fair_unfair_powl          |     7.4 |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |    10   |
| cat08_03_transport_opt             |     6.7 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     8.2 |



### deepseekdeepseek-r1-zerofree   => 34.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     7.4 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     3.1 |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     1.4 |
| cat02_05_two_powls_anomalies       |     7.4 |
| cat02_06_root_cause_1              |     8.2 |
| cat02_07_root_cause_2              |     3.7 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     6.6 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     7.4 |
| cat03_06_petri_net_generation      |     6.6 |
| cat03_07_process_tree_discovery    |     3.3 |
| cat03_08_powl_discovery            |     6.6 |
| cat04_01_pseudo_bpmn_description   |     6.8 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     6.8 |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     7.7 |
| cat05_02_hyp_gen_powl              |     8.2 |
| cat05_03_hyp_gen_declare           |     8.2 |
| cat05_04_hyp_gen_temp_profile      |     7.7 |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     1   |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     5.4 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     1   |
| cat08_03_transport_opt             |     6   |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     5.6 |



### deepseek-aiDeepSeek-R1-Distill-Qwen-32B   => 34.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     6.8 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     6.7 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     1.4 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     6.8 |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     8.2 |
| cat03_07_process_tree_discovery    |     1.4 |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     4.8 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     4.8 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     6.8 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     3.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     6.8 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     3.3 |
| cat08_02_instance_spanning         |     2   |
| cat08_03_transport_opt             |     6.6 |
| cat08_04_resource_assign           |     7.4 |
| cat08_05_task_schedul              |     5.6 |



### nvidianemotron-nano-9b-v2-thinking   => 33.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.4 |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     6.6 |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |    10   |
| cat03_05_temp_profile_generation   |     6.6 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.3 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     7.2 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     6.8 |
| cat05_02_hyp_gen_powl              |     5.4 |
| cat05_03_hyp_gen_declare           |     6.7 |
| cat05_04_hyp_gen_temp_profile      |     5.6 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     7.1 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     3.1 |
| cat06_07_fair_unfair_powl          |     7.7 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     6.6 |
| cat08_03_transport_opt             |     6.7 |
| cat08_04_resource_assign           |     7.7 |
| cat08_05_task_schedul              |     7   |



### magistral-small-2506   => 33.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     6.7 |
| cat01_06_system_logs               |     3.7 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     6.8 |
| cat02_01_conformance_textual       |     6.8 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |    10   |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     7.7 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     3.7 |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     6.7 |
| cat05_03_hyp_gen_declare           |     3.1 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     6.8 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     7.4 |
| cat06_06_bias_mitigation_declare   |     3.1 |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     7.7 |
| cat08_02_instance_spanning         |     7.7 |
| cat08_03_transport_opt             |     6.6 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     7.2 |



### sonar-reasoning-pro   => 32.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.5 |
| cat01_02_activity_context          |     5.6 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     7.2 |
| cat01_05_merge_two_logs            |     6.6 |
| cat01_06_system_logs               |     1.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     6.7 |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     7.7 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     2.5 |
| cat03_03_log_skeleton_generation   |     6.8 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     6.7 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     6.6 |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6.7 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     4.8 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     6   |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     7.1 |
| cat08_03_transport_opt             |     5.6 |
| cat08_04_resource_assign           |     2.5 |
| cat08_05_task_schedul              |     7.2 |



### deepseek-aiDeepSeek-R1-Distill-Llama-70B   => 31.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6.7 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     7.4 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     6.7 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     4.8 |
| cat02_04_powl_anomaly_detection    |     2.5 |
| cat02_05_two_powls_anomalies       |     6.6 |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     6.8 |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     6.8 |
| cat03_03_log_skeleton_generation   |     3.7 |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     6.8 |
| cat03_08_powl_discovery            |     3.7 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     6.6 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     5.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     6.8 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     6.7 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     6.8 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     7.4 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.1 |
| cat06_07_fair_unfair_powl          |     4.2 |
| cat08_01_queue_mining              |     8.9 |
| cat08_02_instance_spanning         |     1   |
| cat08_03_transport_opt             |     1   |
| cat08_04_resource_assign           |     6.7 |
| cat08_05_task_schedul              |     1   |



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



### exaone-deep7.8b-fp16   => 31.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     6.8 |
| cat01_03_high_level_events         |     8.2 |
| cat01_04_sensor_recordings         |     4.2 |
| cat01_05_merge_two_logs            |     6.8 |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     4.2 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     3.7 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     6.8 |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     6.8 |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     4.2 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     6.8 |
| cat04_04_declare_description       |     6.6 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     2.5 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     5.4 |
| cat05_03_hyp_gen_declare           |     6.8 |
| cat05_04_hyp_gen_temp_profile      |     6.6 |
| cat05_05_question_gen_nlp          |     7.7 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     2.5 |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     5.4 |
| cat08_03_transport_opt             |     6.6 |
| cat08_04_resource_assign           |     9.3 |
| cat08_05_task_schedul              |     5.4 |



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



### deepseekdeepseek-r1-distill-qwen-14b   => 29.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.2 |
| cat01_03_high_level_events         |     6.8 |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     4.2 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     6.6 |
| cat02_02_conf_desiderata           |     4.8 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     3.7 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |    10   |
| cat02_09_fix_process_tree          |     6.8 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     7.1 |
| cat03_03_log_skeleton_generation   |     8.9 |
| cat03_04_declare_generation        |     5.4 |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     4.2 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     4.5 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1.4 |
| cat04_07_sql_filt_top_k_vars       |     3.7 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     4.8 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     6.6 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     2.5 |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |    10   |
| cat06_06_bias_mitigation_declare   |     9.5 |
| cat06_07_fair_unfair_powl          |     2   |
| cat08_01_queue_mining              |     4.8 |
| cat08_02_instance_spanning         |     2.5 |
| cat08_03_transport_opt             |     2   |
| cat08_04_resource_assign           |     6.6 |
| cat08_05_task_schedul              |     3.7 |



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



### gpt-oss-20b   => 27.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.7 |
| cat01_02_activity_context          |     3.7 |
| cat01_03_high_level_events         |     6.6 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     1.4 |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     7.4 |
| cat02_03_anomaly_event_log         |     7.4 |
| cat02_04_powl_anomaly_detection    |    10   |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     6.6 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |     6.8 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     6   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.7 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     9.3 |
| cat04_03_declare_open_question     |     6.6 |
| cat04_04_declare_description       |     6.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     2.5 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     3.7 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     3.7 |
| cat05_07_question_interview        |     2.5 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     6.7 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     8.2 |
| cat08_02_instance_spanning         |     8.2 |
| cat08_03_transport_opt             |     9.3 |
| cat08_04_resource_assign           |     8.2 |
| cat08_05_task_schedul              |     6.7 |



### exaone-deep2.4b-fp16   => 26.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2.5 |
| cat01_02_activity_context          |     1.4 |
| cat01_03_high_level_events         |    10   |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     8.9 |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |    10   |
| cat02_02_conf_desiderata           |     4.2 |
| cat02_03_anomaly_event_log         |     2.5 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     4.8 |
| cat02_07_root_cause_2              |     3.7 |
| cat02_08_underfitting_process_tree |     7.7 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     1.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.4 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     6.7 |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     3.1 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3.7 |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     6.8 |
| cat05_07_question_interview        |     7.2 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     3.1 |
| cat06_03_bias_powl                 |     3.3 |
| cat06_04_bias_two_logs             |     9.5 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     2.5 |
| cat08_01_queue_mining              |     6.3 |
| cat08_02_instance_spanning         |     6.6 |
| cat08_03_transport_opt             |     5.6 |
| cat08_04_resource_assign           |     4.2 |
| cat08_05_task_schedul              |     6.7 |



### deepseekdeepseek-r1-distill-llama-8b   => 24.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.6 |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |     5.6 |
| cat01_04_sensor_recordings         |     3.7 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |     5.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     6.8 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3.7 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     1.4 |
| cat03_02_powl_generation           |     5.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     2.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     3.7 |
| cat05_02_hyp_gen_powl              |     4.8 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     2.5 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     2.5 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     6.7 |
| cat06_03_bias_powl                 |     6.7 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     4.8 |
| cat06_07_fair_unfair_powl          |     2   |
| cat08_01_queue_mining              |     6.1 |
| cat08_02_instance_spanning         |     3.7 |
| cat08_03_transport_opt             |     3.1 |
| cat08_04_resource_assign           |     6   |
| cat08_05_task_schedul              |     4.2 |



### phi4-mini-reasoning   => 22.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     1.4 |
| cat01_07_interv_to_pseudo_bpmn     |     6.7 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     4.2 |
| cat02_02_conf_desiderata           |     3.7 |
| cat02_03_anomaly_event_log         |     2.5 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     3.7 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     2.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     8.2 |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     6   |
| cat04_06_sql_filt_three_df         |     3.1 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     5.4 |
| cat05_03_hyp_gen_declare           |     3.7 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     2   |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     1.4 |
| cat08_01_queue_mining              |     6.7 |
| cat08_02_instance_spanning         |     7.2 |
| cat08_03_transport_opt             |     6.7 |
| cat08_04_resource_assign           |     6.7 |
| cat08_05_task_schedul              |     3.7 |



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



### deepseekdeepseek-r1-distill-qwen-7b   => 15.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     5.4 |
| cat01_04_sensor_recordings         |     4.2 |
| cat01_05_merge_two_logs            |     1.4 |
| cat01_06_system_logs               |     1.4 |
| cat01_07_interv_to_pseudo_bpmn     |     5.6 |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |     2.5 |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     3.7 |
| cat02_04_powl_anomaly_detection    |     7.2 |
| cat02_05_two_powls_anomalies       |     3.7 |
| cat02_06_root_cause_1              |     3.1 |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     2.5 |
| cat03_01_process_tree_generation   |     3.3 |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     1.4 |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     3.3 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2.5 |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     2.5 |
| cat05_03_hyp_gen_declare           |     3.1 |
| cat05_04_hyp_gen_temp_profile      |     2.5 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     6.8 |
| cat05_07_question_interview        |     6.7 |
| cat06_01_bias_text                 |     2   |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     3.1 |
| cat06_04_bias_two_logs             |     4.2 |
| cat06_05_bias_two_logs_2           |     1.4 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     2.5 |
| cat08_01_queue_mining              |     3.7 |
| cat08_02_instance_spanning         |     2   |
| cat08_03_transport_opt             |     3.7 |
| cat08_04_resource_assign           |     3.1 |
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



### deepseekdeepseek-r1-distill-qwen-1.5b   => 9.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     3.7 |
| cat01_04_sensor_recordings         |     3.1 |
| cat01_05_merge_two_logs            |     1.4 |
| cat01_06_system_logs               |     1.4 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1.4 |
| cat02_09_fix_process_tree          |     2   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     1.4 |
| cat04_02_pseudo_bpmn_open_question |     1   |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     2.5 |
| cat05_03_hyp_gen_declare           |     1.4 |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     3.3 |
| cat05_07_question_interview        |     2.2 |
| cat06_01_bias_text                 |     3.3 |
| cat06_02_bias_event_log            |     2.5 |
| cat06_03_bias_powl                 |     2.5 |
| cat06_04_bias_two_logs             |     1   |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     2   |
| cat08_02_instance_spanning         |     1   |
| cat08_03_transport_opt             |     1   |
| cat08_04_resource_assign           |     1   |
| cat08_05_task_schedul              |     1   |

