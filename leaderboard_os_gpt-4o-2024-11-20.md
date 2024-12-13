A score in the range **25-30** is considered **sufficient**; a score in the range **30-35** is considered **good**; a score **>35** is considered **excellent**.

## Open-Source Leaderboard (1-shot; gpt-4o-2024-11-20 used as a judge)

| Model                       | Score    | OS                 | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:----------------------------|:---------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| meta-llamaLlama-3.3-70B     | **31.2** | :white_check_mark: | :mage_woman: **5.2** | :mage_woman: **6.5** | :mage_woman: **4.0** | :mage_woman: **5.3** | :mage_woman: **4.9** | :mage_woman: **5.3** | 0.0                  |
| meta-llamaLlama-3.2-90B     | **25.8** | :white_check_mark: | 4.7                  | 5.0                  | 3.3                  | 4.7                  | 4.3                  | 3.9                  | :mage_woman: **5.0** |
| meta-llamaMeta-Llama-3.1-8B | **21.8** | :white_check_mark: | 3.6                  | 4.7                  | 2.4                  | 3.5                  | 3.8                  | 3.8                  | 0.0                  |
| meta-llamaLlama-3.2-3B      | **21.1** | :white_check_mark: | 4.0                  | 4.8                  | 2.1                  | 3.6                  | 3.1                  | 3.3                  | 0.0                  |
| meta-llamaLlama-3.2-11B     | **19.9** | :white_check_mark: | 2.8                  | 5.4                  | 2.6                  | 2.8                  | 3.4                  | 3.0                  | 4.2                  |
| meta-llamaLlama-3.2-1B      | **12.8** | :white_check_mark: | 1.9                  | 2.6                  | 1.2                  | 1.7                  | 2.6                  | 2.7                  | 0.0                  |

### meta-llamaLlama-3.3-70B-Instruct   => 31.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5   |
| cat01_02_activity_context          |     5   |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     8   |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     7   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     8.5 |
| cat02_02_conf_desiderata           |     7.5 |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     8.5 |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     5.5 |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     7   |
| cat03_07_process_tree_discovery    |     5   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     8.5 |
| cat04_03_declare_open_question     |     8   |
| cat04_04_declare_description       |     8   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     6.5 |
| cat05_04_hyp_gen_temp_profile      |     7.5 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     6.5 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     8   |



### meta-llamaLlama-3.2-90B-Vision-Instruct   => 30.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.5 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     1   |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     4.5 |
| cat01_06_system_logs               |     7.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     6.5 |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     4.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     6.5 |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     3.5 |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     3.5 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     7.5 |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     4.5 |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     8.5 |
| cat04_03_declare_open_question     |     8.5 |
| cat04_04_declare_description       |     8.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     4   |
| cat04_07_sql_filt_top_k_vars       |     1.5 |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     6.5 |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     6   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     7   |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     5   |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     7.2 |
| cat06_06_bias_mitigation_declare   |     5   |
| cat06_07_fair_unfair_powl          |     3   |
| cat07_01_ocdfg                     |     7   |
| cat07_02_bpmn_orders               |     9   |
| cat07_03_bpmn_dispatch             |     9   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     8   |
| cat07_06_perf_spectrum             |     8.5 |



### meta-llamaMeta-Llama-3.1-8B-Instruct   => 21.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.5 |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     3.5 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     7   |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     5   |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     5   |
| cat02_06_root_cause_1              |     5   |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     5   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     4   |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     6.5 |
| cat06_07_fair_unfair_powl          |     4   |



### meta-llamaLlama-3.2-3B-Instruct   => 21.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     5   |
| cat01_03_high_level_events         |     5   |
| cat01_04_sensor_recordings         |     5   |
| cat01_05_merge_two_logs            |     6.5 |
| cat01_06_system_logs               |     5.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6.5 |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     5   |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     2.5 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     3.5 |
| cat02_08_underfitting_process_tree |     8.8 |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     2.5 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     4   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     7   |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     7.5 |
| cat04_04_declare_description       |     5   |
| cat04_05_sql_filt_num_events       |     7   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     4.5 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     6   |
| cat05_06_question_pseudo_bpmn      |     3   |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     6.5 |
| cat06_02_bias_event_log            |     3.5 |
| cat06_03_bias_powl                 |     4   |
| cat06_04_bias_two_logs             |     3   |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     7.5 |
| cat06_07_fair_unfair_powl          |     1   |



### meta-llamaLlama-3.2-11B-Vision-Instruct   => 24.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     3   |
| cat01_03_high_level_events         |     5   |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     6.5 |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     5   |
| cat02_06_root_cause_1              |     7   |
| cat02_07_root_cause_2              |     8.2 |
| cat02_08_underfitting_process_tree |     3.5 |
| cat02_09_fix_process_tree          |     5   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     1.5 |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     5   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     3.5 |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     5.5 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     3   |
| cat06_03_bias_powl                 |     1   |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     5   |
| cat06_06_bias_mitigation_declare   |     5   |
| cat06_07_fair_unfair_powl          |     3   |
| cat07_01_ocdfg                     |     4   |
| cat07_02_bpmn_orders               |     6   |
| cat07_03_bpmn_dispatch             |     8.5 |
| cat07_04_causal_net                |     9   |
| cat07_05_proclets                  |     6   |
| cat07_06_perf_spectrum             |     9   |



### meta-llamaLlama-3.2-1B-Instruct   => 12.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     3   |
| cat01_03_high_level_events         |     3.5 |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     3   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     3   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     5   |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     1.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     2.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     4   |
| cat06_02_bias_event_log            |     3   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     3.5 |
| cat06_05_bias_two_logs_2           |     6.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     1   |
