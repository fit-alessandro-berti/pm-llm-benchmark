A score in the range **25-30** is considered **sufficient**; a score in the range **30-35** is considered **good**; and a score **>35** is considered **excellent**.


**As of 2025-01-26, the chain of thought of Large Reasoning Models, if provided, is considered in the assessment of answers.**

## QWEN Leaderboard (1-shot; gpt-4o-2024-11-20 used as a judge)

| Model                        | Avg     | Score    | OS                 | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:-----------------------------|:--------|:---------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| QwenQwen2.5-72B-Instruct     | **7.1** | **32.5** | :white_check_mark: | **5.8**              | **7.1**              | :mage_woman: **4.5** | **5.1**              | 4.9                  | **5.0**              | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-32B | **7.0** | **32.1** | :white_check_mark: | :mage_woman: **5.9** | **7.0**              | 3.3                  | 4.8                  | :mage_woman: **5.8** | :mage_woman: **5.2** | :mage_woman: **0.0** |
| Qwen-2.5-Plus                | **6.8** | **31.2** | :x:                | 4.8                  | 6.8                  | :mage_woman: **4.5** | :mage_woman: **5.2** | 5.0                  | **5.1**              | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-14B | **6.7** | **30.9** | :white_check_mark: | **5.7**              | :mage_woman: **7.2** | 3.8                  | 4.1                  | 5.0                  | **5.1**              | :mage_woman: **0.0** |
| QwenQwen2.5-14B-Instruct     | **6.7** | **30.6** | :white_check_mark: | 5.5                  | 6.5                  | **4.2**              | 4.3                  | 4.8                  | :mage_woman: **5.2** | :mage_woman: **0.0** |
| QwenQwQ-32B-Preview          | **6.3** | **28.8** | :white_check_mark: | 5.3                  | **6.9**              | 3.4                  | 3.7                  | 4.8                  | 4.7                  | :mage_woman: **0.0** |
| QwenQwen2.5-14B-Instruct-1M  | **6.2** | **28.5** | :white_check_mark: | 5.0                  | 6.2                  | 3.8                  | 4.6                  | 4.7                  | 4.2                  | :mage_woman: **0.0** |
| QwenQwen2.5-7B-Instruct-1M   | **5.5** | **25.5** | :white_check_mark: | 3.9                  | 5.4                  | 3.1                  | 4.2                  | 4.2                  | 4.7                  | :mage_woman: **0.0** |
| QwenQwen2.5-7B-Instruct      | **5.3** | **24.2** | :white_check_mark: | 3.5                  | 5.8                  | 2.6                  | 3.9                  | 4.5                  | 3.9                  | :mage_woman: **0.0** |
| qwen2.53b-instruct-q8_0      | **4.7** | **21.5** | :white_check_mark: | 3.4                  | 5.0                  | 2.9                  | 3.3                  | 3.4                  | 3.6                  | :mage_woman: **0.0** |

### QwenQwen2.5-72B-Instruct   => 32.5 points

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



### Qwen-2.5-Plus   => 31.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     5.5 |
| cat01_05_merge_two_logs            |     7   |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     6.5 |
| cat02_01_conformance_textual       |     8.7 |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     5   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     7.5 |
| cat02_06_root_cause_1              |     8   |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     5   |
| cat03_02_powl_generation           |     5   |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     8   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     8.5 |
| cat04_02_pseudo_bpmn_open_question |     9   |
| cat04_03_declare_open_question     |     8.7 |
| cat04_04_declare_description       |     8.5 |
| cat04_05_sql_filt_num_events       |     7   |
| cat04_06_sql_filt_three_df         |     6.5 |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     8   |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     6.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8.6 |
| cat06_02_bias_event_log            |     5.5 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     9   |
| cat06_05_bias_two_logs_2           |     8.5 |
| cat06_06_bias_mitigation_declare   |     8   |
| cat06_07_fair_unfair_powl          |     4   |



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



### QwenQwen2.5-14B-Instruct   => 30.6 points

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



### QwenQwen2.5-14B-Instruct-1M   => 28.5 points

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



### QwenQwen2.5-7B-Instruct-1M   => 25.5 points

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



### QwenQwen2.5-7B-Instruct   => 24.2 points

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

