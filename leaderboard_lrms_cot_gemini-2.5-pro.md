A score in the range **25-30** is considered **sufficient**; a score in the range **30-35** is considered **good**; and a score **>35** is considered **excellent**.


**As of 2025-01-26, the chain of thought of Large Reasoning Models, if provided, is considered in the assessment of answers.**

## Large Reasoning Models Leaderboard (Models with CoT) (1-shot; gemini-2.5-pro-exp-03-25 used as a judge)

| Model                         | Avg     | Score    | OS                 | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:------------------------------|:--------|:---------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| Grok-3-beta-thinking-20250221 | **8.4** | **38.8** | :x:                | :mage_woman: **6.4** | :mage_woman: **8.1** | :mage_woman: **6.3** | :mage_woman: **5.8** | :mage_woman: **5.9** | :mage_woman: **6.4** | :mage_woman: **0.0** |
| DeepSeek-R1-671B-HB           | **7.6** | **34.8** | :white_check_mark: | **6.2**              | :mage_woman: **8.1** | 4.8                  | **5.6**              | 4.7                  | 5.4                  | :mage_woman: **0.0** |
| DeepSeek-R1-Dynamic-Quant     | **6.6** | **30.4** | :white_check_mark: | 5.4                  | 7.4                  | 3.5                  | 4.6                  | 5.3                  | 4.2                  | :mage_woman: **0.0** |
| Perplexity-R1-1776            | **6.5** | **30.0** | :white_check_mark: | 4.7                  | 7.7                  | 2.6                  | 4.9                  | 5.0                  | 5.0                  | :mage_woman: **0.0** |
| QwQ-32B                       | **6.4** | **29.5** | :white_check_mark: | 4.7                  | 6.6                  | 3.9                  | 4.2                  | 5.2                  | 4.9                  | :mage_woman: **0.0** |
| exaone-deep32b-fp16           | **6.4** | **29.5** | :white_check_mark: | 5.7                  | 6.3                  | 3.6                  | 4.5                  | 4.3                  | 5.2                  | :mage_woman: **0.0** |
| DeepSeek-R1-Zero              | **6.1** | **28.0** | :white_check_mark: | 5.3                  | 5.1                  | 3.6                  | 4.2                  | 5.5                  | 4.3                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-32B  | **5.6** | **25.8** | :white_check_mark: | 5.1                  | 6.2                  | 3.5                  | 3.2                  | 3.8                  | 4.0                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Llama-70B | **5.3** | **24.3** | :white_check_mark: | 4.1                  | 5.7                  | 2.2                  | 3.6                  | 4.4                  | 4.4                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-14B  | **5.0** | **22.9** | :white_check_mark: | 3.3                  | 6.1                  | 3.4                  | 2.4                  | 4.0                  | 3.8                  | :mage_woman: **0.0** |
| Perplexity-Sonar-Reasoning    | **4.7** | **21.5** | :x:                | 3.4                  | 5.6                  | 2.1                  | 2.4                  | 4.8                  | 3.2                  | :mage_woman: **0.0** |
| DeepSeek-R1-Distill-Qwen-7B   | **2.9** | **13.1** | :white_check_mark: | 1.7                  | 2.6                  | 1.5                  | 2.2                  | 3.1                  | 2.0                  | :mage_woman: **0.0** |

### Grok-3-beta-thinking-20250221   => 38.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     9.7 |
| cat01_05_merge_two_logs            |     8.6 |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     8.6 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     9.4 |
| cat02_05_two_powls_anomalies       |     9.4 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     9.4 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     9.7 |
| cat03_03_log_skeleton_generation   |     7.7 |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     9.3 |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     8.3 |
| cat03_08_powl_discovery            |     7.7 |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     8.3 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     8.9 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |     8.3 |
| cat05_01_hyp_generation_log        |     9.1 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     9.4 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     9.2 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     8.9 |
| cat06_07_fair_unfair_powl          |     9.4 |



### DeepSeek-R1-671B-HB   => 34.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     9.4 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     8.9 |
| cat01_08_tables_to_log             |     9.4 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     9.4 |
| cat02_03_anomaly_event_log         |     9.4 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     8.6 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     8.6 |
| cat03_07_process_tree_discovery    |     6.6 |
| cat03_08_powl_discovery            |     4.8 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.9 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     8.3 |
| cat05_01_hyp_generation_log        |     4.9 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.3 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     8.3 |



### DeepSeek-R1-Dynamic-Quant   => 30.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     8.3 |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     9.8 |
| cat02_03_anomaly_event_log         |     5.4 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     4.8 |
| cat03_04_declare_generation        |     4.2 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     4.2 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     6.3 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     8.3 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     8.3 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     3.1 |
| cat06_06_bias_mitigation_declare   |     4.8 |
| cat06_07_fair_unfair_powl          |     6   |



### Perplexity-R1-1776   => 30.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.6 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     9.8 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     8.9 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     3.7 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     9.4 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     4.8 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.3 |



### QwenQwQ-32B   => 29.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.6 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     8.6 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.7 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     6.6 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     9.1 |
| cat02_07_root_cause_2              |     4.8 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     8.3 |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     4.8 |
| cat03_07_process_tree_discovery    |     5.4 |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     6.3 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     8.9 |
| cat04_07_sql_filt_top_k_vars       |     3.1 |
| cat05_01_hyp_generation_log        |     4.8 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.3 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     7.1 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     8.3 |



### exaone-deep32b-fp16   => 29.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     9.4 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.3 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     9.8 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     6   |
| cat03_03_log_skeleton_generation   |     8.3 |
| cat03_04_declare_generation        |     1.4 |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     8.6 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     4.8 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     8.3 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.3 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     3.7 |



### DeepSeek-R1-Zero   => 28.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.1 |
| cat01_02_activity_context          |     7.7 |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     9.4 |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |     3.3 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     2   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     3.1 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     9.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     8.9 |
| cat04_01_pseudo_bpmn_description   |     4.8 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |     8.3 |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     6.9 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     8.3 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     2   |



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



### DeepSeek-R1-Distill-Qwen-14B   => 22.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.4 |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |     2   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     6.6 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     3.1 |
| cat02_07_root_cause_2              |     4.2 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     5.4 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     8.3 |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     4.2 |
| cat06_04_bias_two_logs             |     3.1 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     2.5 |



### Perplexity-Sonar-Reasoning-Pro   => 21.5 points

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
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     4.8 |
| cat02_06_root_cause_1              |     8.9 |
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
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     4.2 |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     4.8 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     4.2 |
| cat06_04_bias_two_logs             |     6.6 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     3.1 |



### DeepSeek-R1-Distill-Qwen-7B   => 13.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     3.1 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     2.5 |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |     2.5 |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     1.4 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     1.4 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     6.6 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     4.8 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     6   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     2.5 |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.3 |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     3.7 |
| cat06_02_bias_event_log            |     4.8 |
| cat06_03_bias_powl                 |     1.4 |
| cat06_04_bias_two_logs             |     3.1 |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     1   |

