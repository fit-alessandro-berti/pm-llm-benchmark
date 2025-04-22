A score in the range **24-29** is considered **sufficient**; a score in the range **29-34** is considered **fair**; a score in the range **34-40** is considered **good**; and a score **>40** is considered **excellent**.

**Update**: Since **19-04-2025**, a normalization step is applied to the score.

## LLAMA Leaderboard (1-shot; gemini-2.5-pro-preview-03-25 used as a judge)

| Model                            | Score    | OS                 | LRM                | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       | OPT                  |
|:---------------------------------|:---------|:-------------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| nemotron-ultra-253b-v1-thinkenab | **37.0** | :white_check_mark: | :white_check_mark: | :mage_woman: **6.0** | 6.8                  | 5.3                  | **4.5**              | :mage_woman: **5.1** | :mage_woman: **5.6** | 0.0                  | **3.7**              |
| nemotron-super-49b-v1-thinkenab  | **36.4** | :white_check_mark: | :white_check_mark: | 5.0                  | :mage_woman: **7.3** | :mage_woman: **6.0** | :mage_woman: **4.8** | 4.4                  | 5.0                  | 0.0                  | :mage_woman: **3.9** |
| nemotron-70b-instruct            | **29.8** | :white_check_mark: | :x:                | 4.4                  | 5.5                  | 3.5                  | 4.3                  | 4.4                  | 4.8                  | 0.0                  | 3.0                  |
| DeepSeek-R1-Distill-Llama-70B    | **26.3** | :white_check_mark: | :white_check_mark: | 4.7                  | 6.1                  | 2.7                  | 4.3                  | 4.0                  | 4.5                  | 0.0                  | 0.0                  |
| Llama-3.3-70B-Instruct           | **25.6** | :white_check_mark: | :x:                | 4.6                  | 5.4                  | 2.7                  | 4.3                  | 4.2                  | 4.4                  | 0.0                  | 0.0                  |
| llama-4-maverick                 | **24.5** | :white_check_mark: | :x:                | 4.3                  | 5.3                  | 2.9                  | 3.6                  | **4.9**              | 3.6                  | :mage_woman: **3.7** | 0.0                  |
| Llama-3.2-90B-Vision-Instruct    | **21.4** | :white_check_mark: | :x:                | 3.9                  | 4.2                  | 2.5                  | 3.5                  | 4.2                  | 3.0                  | 2.5                  | 0.0                  |
| llama-4-scout                    | **20.9** | :white_check_mark: | :x:                | 3.0                  | 3.9                  | 2.8                  | 3.6                  | 4.3                  | 3.3                  | 3.2                  | 0.0                  |
| Llama-3.1-8B-Instruct            | **16.1** | :white_check_mark: | :x:                | 2.4                  | 2.8                  | 1.6                  | 2.3                  | 4.3                  | 2.8                  | 0.0                  | 0.0                  |
| Llama-3.2-11B-Vision-Instruct    | **14.8** | :white_check_mark: | :x:                | 2.8                  | 3.0                  | 1.9                  | 2.0                  | 3.0                  | 2.0                  | 2.1                  | 0.0                  |
| Llama-3.2-3B-Instruct            | **14.1** | :white_check_mark: | :x:                | 2.4                  | 2.7                  | 1.3                  | 2.1                  | 3.4                  | 2.1                  | 0.0                  | 0.0                  |
| Llama-3.2-1B-Instruct            | **8.9**  | :white_check_mark: | :x:                | 1.3                  | 1.7                  | 0.8                  | 1.1                  | 2.4                  | 1.6                  | 0.0                  | 0.0                  |

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



### nvidiaLlama-3.1-Nemotron-70B-Instruct   => 29.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    5    |
| cat01_03_high_level_events         |    7.75 |
| cat01_04_sensor_recordings         |    7    |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    7.25 |
| cat02_03_anomaly_event_log         |    8    |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    6.5  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    9.25 |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    7.4  |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2.5  |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    6    |
| cat04_04_declare_description       |    4.5  |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    9.25 |
| cat05_01_hyp_generation_log        |    4.5  |
| cat05_02_hyp_gen_powl              |    6.5  |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    7.9  |
| cat05_06_question_pseudo_bpmn      |    8.5  |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    5.5  |
| cat06_03_bias_powl                 |    8.5  |
| cat06_04_bias_two_logs             |    7.25 |
| cat06_05_bias_two_logs_2           |    7.6  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    7    |
| cat08_01_queue_mining              |    5    |
| cat08_02_instance_spanning         |    5    |
| cat08_03_transport_opt             |    7.25 |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    6    |



### deepseek-aiDeepSeek-R1-Distill-Llama-70B   => 26.3 points

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



### meta-llamaLlama-3.3-70B-Instruct   => 25.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.9  |
| cat01_02_activity_context          |    7.25 |
| cat01_03_high_level_events         |    4.5  |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    6    |
| cat01_07_interv_to_pseudo_bpmn     |    5.5  |
| cat01_08_tables_to_log             |    3.5  |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    7.5  |
| cat02_03_anomaly_event_log         |    7.65 |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    5.5  |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    5.5  |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    5    |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    7.5  |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    7.75 |
| cat04_06_sql_filt_three_df         |    7.75 |
| cat04_07_sql_filt_top_k_vars       |    7.25 |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    4    |
| cat05_03_hyp_gen_declare           |    7    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.5  |
| cat05_06_question_pseudo_bpmn      |    8    |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    9.25 |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    5    |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    7.25 |
| cat06_06_bias_mitigation_declare   |    4.5  |
| cat06_07_fair_unfair_powl          |    7.25 |



### meta-llamallama-4-maverick   => 24.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    6.5  |
| cat01_02_activity_context          |    5.5  |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    7.25 |
| cat02_01_conformance_textual       |    7.75 |
| cat02_02_conf_desiderata           |    7.25 |
| cat02_03_anomaly_event_log         |    8    |
| cat02_04_powl_anomaly_detection    |    4.5  |
| cat02_05_two_powls_anomalies       |    5.5  |
| cat02_06_root_cause_1              |    5.5  |
| cat02_07_root_cause_2              |    6.5  |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    5    |
| cat03_01_process_tree_generation   |    5    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3.5  |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    6    |
| cat04_01_pseudo_bpmn_description   |    3.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    8    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    7.75 |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    5.5  |
| cat06_03_bias_powl                 |    3    |
| cat06_04_bias_two_logs             |    6.8  |
| cat06_05_bias_two_logs_2           |    6.5  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    4    |
| cat07_01_ocdfg                     |    5    |
| cat07_02_bpmn_orders               |    7.75 |
| cat07_03_bpmn_dispatch             |    4    |
| cat07_04_causal_net                |    7.75 |
| cat07_05_proclets                  |    5    |
| cat07_06_perf_spectrum             |    7.75 |



### meta-llamaLlama-3.2-90B-Vision-Instruct   => 21.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.25 |
| cat01_02_activity_context          |    5    |
| cat01_03_high_level_events         |    4.5  |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    5    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    6    |
| cat03_03_log_skeleton_generation   |    2.5  |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3.5  |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    5    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.25 |
| cat04_06_sql_filt_three_df         |    7.5  |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    7.6  |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    5.5  |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    4.5  |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    5.5  |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    2.5  |
| cat07_01_ocdfg                     |    5    |
| cat07_02_bpmn_orders               |    6.5  |
| cat07_03_bpmn_dispatch             |    4    |
| cat07_04_causal_net                |    3    |
| cat07_05_proclets                  |    3    |
| cat07_06_perf_spectrum             |    3.5  |



### meta-llamallama-4-scout   => 20.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    3    |
| cat01_04_sensor_recordings         |    5    |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    7.75 |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    5.5  |
| cat03_01_process_tree_generation   |    6.5  |
| cat03_02_powl_generation           |    7    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    6.5  |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    7.25 |
| cat04_06_sql_filt_three_df         |    7.5  |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    5    |
| cat05_02_hyp_gen_powl              |    7    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    9.25 |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    7.75 |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    3    |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    4.5  |
| cat07_01_ocdfg                     |    4.5  |
| cat07_02_bpmn_orders               |    6.5  |
| cat07_03_bpmn_dispatch             |    3.5  |
| cat07_04_causal_net                |    4.5  |
| cat07_05_proclets                  |    6    |
| cat07_06_perf_spectrum             |    7.25 |



### meta-llamaMeta-Llama-3.1-8B-Instruct   => 16.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1.5  |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    2.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    1.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    2.5  |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    2.5  |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    3.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    2    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    7    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    7.9  |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    7.5  |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    5.5  |
| cat06_04_bias_two_logs             |    3    |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    2.5  |



### meta-llamaLlama-3.2-11B-Vision-Instruct   => 14.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    2.5  |
| cat01_03_high_level_events         |    3    |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    2.5  |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    5    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    3.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    2.5  |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    2.5  |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    1    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    6    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    1    |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    1    |
| cat05_03_hyp_gen_declare           |    2.5  |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    5    |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    3    |
| cat06_03_bias_powl                 |    1.5  |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    1.5  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    2    |
| cat07_01_ocdfg                     |    2    |
| cat07_02_bpmn_orders               |    3.5  |
| cat07_03_bpmn_dispatch             |    3.5  |
| cat07_04_causal_net                |    5    |
| cat07_05_proclets                  |    3    |
| cat07_06_perf_spectrum             |    4    |



### meta-llamaLlama-3.2-3B-Instruct   => 14.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    3.5  |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    4    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    2    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    3    |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    1.5  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    1    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    4    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    1.5  |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    2    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    8.75 |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    5    |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    2.5  |
| cat06_04_bias_two_logs             |    2.5  |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    1.5  |



### meta-llamaLlama-3.2-1B-Instruct   => 8.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     1.5 |
| cat01_03_high_level_events         |     2.5 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1.5 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     1.5 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     3   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     1.5 |
| cat02_07_root_cause_2              |     1.5 |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     1.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     2.5 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     1.5 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     6.5 |
| cat05_06_question_pseudo_bpmn      |     4   |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     4   |
| cat06_02_bias_event_log            |     1.5 |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     2   |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |

