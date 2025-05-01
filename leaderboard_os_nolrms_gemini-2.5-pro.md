A score in the range **24-29** is considered **sufficient**; a score in the range **29-34** is considered **fair**; a score in the range **34-40** is considered **good**; and a score **>40** is considered **excellent**.

**Update**: Since **19-04-2025**, a normalization step is applied to the score.

## Base Open-Source LLMs Leaderboard (1-shot; gemini-2.5-pro-preview-03-25 used as a judge)

| Model                      | Score    | OS                 | LRM   | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       | OPT                  |
|:---------------------------|:---------|:-------------------|:------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| Qwen-3-235B-A22B-nothink   | **34.6** | :white_check_mark: | :x:   | 5.0                  | :mage_woman: **6.5** | 3.4                  | :mage_woman: **4.8** | :mage_woman: **5.4** | :mage_woman: **5.4** | 0.0                  | :mage_woman: **4.0** |
| DeepSeek-V3-0324           | **32.2** | :white_check_mark: | :x:   | :mage_woman: **5.5** | **6.2**              | :mage_woman: **3.7** | **4.5**              | 4.5                  | 4.4                  | 0.0                  | 3.3                  |
| Qwen-3-32B-nothink         | **30.0** | :white_check_mark: | :x:   | 4.6                  | 5.3                  | 3.0                  | 3.7                  | 4.5                  | 5.0                  | 0.0                  | **3.9**              |
| nemotron-70b-instruct      | **29.7** | :white_check_mark: | :x:   | 4.4                  | 5.4                  | **3.5**              | 4.2                  | 4.4                  | 4.8                  | 0.0                  | 3.0                  |
| DeepSeek-V3                | **29.5** | :white_check_mark: | :x:   | 4.3                  | 5.5                  | 2.8                  | 4.2                  | 4.9                  | 4.5                  | 0.0                  | 3.2                  |
| Qwen-3-30B-A3B-nothink     | **28.6** | :white_check_mark: | :x:   | 3.5                  | 5.4                  | 2.9                  | 3.9                  | 4.9                  | 4.3                  | 0.0                  | **3.8**              |
| Qwen-3-14B-nothink         | **28.5** | :white_check_mark: | :x:   | 4.6                  | 5.4                  | 2.2                  | 4.2                  | 4.2                  | 4.4                  | 0.0                  | 3.4                  |
| Llama-3.3-70B-Instruct     | **28.3** | :white_check_mark: | :x:   | 4.6                  | 5.4                  | 2.7                  | 4.3                  | 4.2                  | 4.3                  | 0.0                  | 2.8                  |
| qwen2.5-72b-instruct       | **28.2** | :white_check_mark: | :x:   | 4.5                  | 5.7                  | 2.9                  | 4.1                  | 3.7                  | 4.7                  | 0.0                  | 2.9                  |
| pixtral-large-2411         | **27.9** | :white_check_mark: | :x:   | 5.0                  | 5.0                  | 3.1                  | 3.8                  | 4.2                  | 4.0                  | :mage_woman: **4.5** | 2.7                  |
| gemma327b-it-q8_0          | **27.6** | :white_check_mark: | :x:   | 4.1                  | 4.4                  | 2.5                  | 3.4                  | 4.7                  | 4.7                  | 2.1                  | **3.8**              |
| llama-4-maverick           | **27.1** | :white_check_mark: | :x:   | 4.3                  | 5.3                  | 2.9                  | 3.5                  | 4.8                  | 3.6                  | 3.7                  | 2.7                  |
| mistral-large-2411         | **27.0** | :white_check_mark: | :x:   | 4.0                  | 5.1                  | 2.8                  | 3.6                  | 4.2                  | 4.4                  | 0.0                  | 3.0                  |
| mistral-small-2503         | **26.4** | :white_check_mark: | :x:   | 3.1                  | 4.9                  | 2.4                  | 4.2                  | 4.5                  | 4.7                  | 3.6                  | 2.6                  |
| WizardLM-2-8x22B           | **26.4** | :white_check_mark: | :x:   | 3.8                  | 4.7                  | 2.5                  | 3.8                  | 4.7                  | 4.3                  | 0.0                  | 2.7                  |
| mistral-small-2501         | **26.4** | :white_check_mark: | :x:   | 3.9                  | 4.8                  | 3.2                  | 3.2                  | 4.3                  | 4.1                  | 0.0                  | 2.9                  |
| phi-4                      | **26.3** | :white_check_mark: | :x:   | 4.0                  | 5.0                  | 3.1                  | 3.2                  | 4.0                  | 4.0                  | 0.0                  | 2.9                  |
| Qwen2.5-Coder-32B-Instruct | **26.1** | :white_check_mark: | :x:   | 3.8                  | 4.4                  | 3.0                  | 3.7                  | 4.0                  | 4.0                  | 0.0                  | 3.1                  |
| qwen2.5-32b-instruct       | **25.7** | :white_check_mark: | :x:   | 4.1                  | 5.0                  | 2.0                  | 3.3                  | 4.4                  | 4.1                  | 0.0                  | 2.9                  |
| open-mixtral-8x22b         | **25.3** | :white_check_mark: | :x:   | 4.3                  | 4.8                  | 1.9                  | 3.8                  | 4.2                  | 4.2                  | 0.0                  | 2.0                  |
| gemma312b-it-q8_0          | **25.1** | :white_check_mark: | :x:   | 3.8                  | 3.6                  | 1.9                  | 3.3                  | 4.4                  | 4.6                  | 2.8                  | 3.5                  |
| qwen2.5-14b-instruct-1m    | **24.0** | :white_check_mark: | :x:   | 3.6                  | 4.5                  | 1.7                  | 3.5                  | 4.3                  | 3.7                  | 0.0                  | 2.7                  |
| codestral-2501             | **23.9** | :white_check_mark: | :x:   | 4.0                  | 4.5                  | 2.2                  | 3.4                  | 4.0                  | 3.6                  | 0.0                  | 2.2                  |
| falcon310b-instruct-q8_0   | **23.5** | :white_check_mark: | :x:   | 3.5                  | 4.7                  | 1.9                  | 3.1                  | 4.1                  | 3.8                  | 0.0                  | 2.4                  |
| falcon37b-instruct-q8_0    | **22.8** | :white_check_mark: | :x:   | 3.0                  | 4.0                  | 2.6                  | 3.0                  | 4.2                  | 3.1                  | 0.0                  | 2.9                  |
| pixtral-12b-2409           | **22.6** | :white_check_mark: | :x:   | 2.8                  | 4.3                  | 2.5                  | 3.1                  | 4.0                  | 3.6                  | 4.0                  | 2.2                  |
| llama-4-scout              | **22.5** | :white_check_mark: | :x:   | 3.0                  | 3.9                  | 2.8                  | 3.6                  | 4.3                  | 3.3                  | 3.2                  | 1.6                  |
| granite3.3                 | **21.9** | :white_check_mark: | :x:   | 3.4                  | 3.5                  | 1.6                  | 2.6                  | 4.3                  | 3.1                  | 0.0                  | 3.5                  |
| qwen2.5-omni-7b            | **21.1** | :white_check_mark: | :x:   | 3.2                  | 3.5                  | 1.9                  | 3.0                  | 3.8                  | 3.1                  | 2.2                  | 2.4                  |
| gemma34b-it-q8_0           | **19.8** | :white_check_mark: | :x:   | 2.2                  | 3.3                  | 1.3                  | 2.7                  | 4.1                  | 3.1                  | 2.0                  | 3.1                  |
| qwen2.5-7b-instruct-1m     | **19.7** | :white_check_mark: | :x:   | 3.0                  | 3.0                  | 1.9                  | 2.5                  | 3.5                  | 3.0                  | 0.0                  | 2.8                  |
| falcon33b-instruct-q8_0    | **18.1** | :white_check_mark: | :x:   | 2.5                  | 3.2                  | 1.6                  | 2.2                  | 3.0                  | 2.8                  | 0.0                  | 2.7                  |
| Phi-4-multimodal-instruct  | **17.7** | :white_check_mark: | :x:   | 2.1                  | 3.0                  | 1.2                  | 2.5                  | 3.3                  | 2.9                  | 2.7                  | 2.8                  |
| olmo27b-1124-instruct-q8_0 | **16.4** | :white_check_mark: | :x:   | 2.2                  | 3.0                  | 1.4                  | 2.0                  | 3.0                  | 2.8                  | 0.0                  | 1.9                  |
| gemma31b-it-q8_0           | **12.6** | :white_check_mark: | :x:   | 1.1                  | 1.9                  | 1.0                  | 1.4                  | 3.2                  | 2.0                  | 0.0                  | 1.9                  |

### Qwen-3-235B-A22B-nothink   => 34.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    8.4  |
| cat01_02_activity_context          |    7.75 |
| cat01_03_high_level_events         |    6.5  |
| cat01_04_sensor_recordings         |    7.25 |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    9    |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    8    |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    5    |
| cat02_06_root_cause_1              |    5.5  |
| cat02_07_root_cause_2              |    6.5  |
| cat02_08_underfitting_process_tree |    7.75 |
| cat02_09_fix_process_tree          |    9    |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    7    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    6    |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    7    |
| cat04_02_pseudo_bpmn_open_question |    7    |
| cat04_03_declare_open_question     |    6    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    9.6  |
| cat04_07_sql_filt_top_k_vars       |    5    |
| cat05_01_hyp_generation_log        |    6.5  |
| cat05_02_hyp_gen_powl              |    8    |
| cat05_03_hyp_gen_declare           |    8    |
| cat05_04_hyp_gen_temp_profile      |    7.05 |
| cat05_05_question_gen_nlp          |    9    |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    9.6  |
| cat06_02_bias_event_log            |    7.5  |
| cat06_03_bias_powl                 |    9    |
| cat06_04_bias_two_logs             |    9    |
| cat06_05_bias_two_logs_2           |    8    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    7    |
| cat08_01_queue_mining              |    8    |
| cat08_02_instance_spanning         |    7.25 |
| cat08_03_transport_opt             |    7.5  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    9    |



### deepseek-aiDeepSeek-V3-0324   => 32.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.5  |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    7.75 |
| cat01_04_sensor_recordings         |    7.75 |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    5.5  |
| cat01_08_tables_to_log             |    7.9  |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    9    |
| cat02_04_powl_anomaly_detection    |    7.25 |
| cat02_05_two_powls_anomalies       |    7    |
| cat02_06_root_cause_1              |    8    |
| cat02_07_root_cause_2              |    7.5  |
| cat02_08_underfitting_process_tree |    3.5  |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    6.5  |
| cat03_02_powl_generation           |    7.75 |
| cat03_03_log_skeleton_generation   |    3.5  |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    6.5  |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    8    |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    7.75 |
| cat04_06_sql_filt_three_df         |    8    |
| cat04_07_sql_filt_top_k_vars       |    8    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    5.5  |
| cat05_05_question_gen_nlp          |    7.5  |
| cat05_06_question_pseudo_bpmn      |    8    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    7.5  |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    6.5  |
| cat08_01_queue_mining              |    6.5  |
| cat08_02_instance_spanning         |    6.5  |
| cat08_03_transport_opt             |    7    |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    6.8  |



### Qwen-3-32B-nothink   => 30.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.9  |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    6.5  |
| cat01_04_sensor_recordings         |    7.25 |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    6.5  |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    7.75 |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    6.5  |
| cat02_04_powl_anomaly_detection    |    7.75 |
| cat02_05_two_powls_anomalies       |    4.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    4.5  |
| cat02_09_fix_process_tree          |    9    |
| cat03_01_process_tree_generation   |    6    |
| cat03_02_powl_generation           |    5.5  |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3.5  |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3.5  |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    6.8  |
| cat04_03_declare_open_question     |    6.8  |
| cat04_04_declare_description       |    3.5  |
| cat04_05_sql_filt_num_events       |    1    |
| cat04_06_sql_filt_three_df         |    6    |
| cat04_07_sql_filt_top_k_vars       |    7.5  |
| cat05_01_hyp_generation_log        |    5    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    6.5  |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    9    |
| cat06_02_bias_event_log            |    7    |
| cat06_03_bias_powl                 |    7.75 |
| cat06_04_bias_two_logs             |    6.8  |
| cat06_05_bias_two_logs_2           |    9    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    6    |
| cat08_01_queue_mining              |    7.25 |
| cat08_02_instance_spanning         |    7.9  |
| cat08_03_transport_opt             |    7.25 |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    7.9  |



### nvidiaLlama-3.1-Nemotron-70B-Instruct   => 29.7 points

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
| cat02_09_fix_process_tree          |    9    |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    9.6  |
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
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    9    |
| cat05_01_hyp_generation_log        |    4.5  |
| cat05_02_hyp_gen_powl              |    6.5  |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    7.9  |
| cat05_06_question_pseudo_bpmn      |    8.4  |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    5.5  |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    7.25 |
| cat06_05_bias_two_logs_2           |    7.6  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    7    |
| cat08_01_queue_mining              |    5    |
| cat08_02_instance_spanning         |    5    |
| cat08_03_transport_opt             |    7.25 |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    6    |



### deepseek-aiDeepSeek-V3   => 29.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7    |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    7.5  |
| cat02_01_conformance_textual       |    7.25 |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    7.75 |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    7.75 |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    7.9  |
| cat03_01_process_tree_generation   |    3.5  |
| cat03_02_powl_generation           |    5    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    4.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    7.25 |
| cat04_02_pseudo_bpmn_open_question |    7    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    9.6  |
| cat04_07_sql_filt_top_k_vars       |    3.5  |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    7.5  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |    9.6  |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    7.5  |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    6.3  |
| cat06_05_bias_two_logs_2           |    7    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    6    |
| cat08_01_queue_mining              |    6.5  |
| cat08_02_instance_spanning         |    6.5  |
| cat08_03_transport_opt             |    6.8  |
| cat08_04_resource_assign           |    4.5  |
| cat08_05_task_schedul              |    7.4  |



### Qwen-3-30B-A3B-nothink   => 28.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    4.5  |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    5    |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    9.6  |
| cat02_03_anomaly_event_log         |    7.25 |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    5    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    3.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    7.5  |
| cat04_02_pseudo_bpmn_open_question |    7.6  |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    7    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    8    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    5.5  |
| cat05_05_question_gen_nlp          |    9    |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    7.5  |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    4    |
| cat08_01_queue_mining              |    7.9  |
| cat08_02_instance_spanning         |    7.75 |
| cat08_03_transport_opt             |    7.5  |
| cat08_04_resource_assign           |    7    |
| cat08_05_task_schedul              |    7.9  |



### Qwen-3-14B-nothink   => 28.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7    |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    8    |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    7    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    9    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    7.75 |
| cat02_06_root_cause_1              |    5    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    6    |
| cat04_07_sql_filt_top_k_vars       |    7.25 |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    4    |
| cat05_03_hyp_gen_declare           |    5.5  |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |    9    |
| cat05_06_question_pseudo_bpmn      |    7    |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    8.4  |
| cat06_03_bias_powl                 |    3.5  |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    6    |
| cat08_01_queue_mining              |    7.5  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    5.5  |
| cat08_04_resource_assign           |    7.4  |
| cat08_05_task_schedul              |    7.75 |



### meta-llamaLlama-3.3-70B-Instruct   => 28.3 points

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
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    8    |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    9    |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    5    |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    7.25 |
| cat06_06_bias_mitigation_declare   |    4.5  |
| cat06_07_fair_unfair_powl          |    7.25 |
| cat08_01_queue_mining              |    6    |
| cat08_02_instance_spanning         |    5.5  |
| cat08_03_transport_opt             |    5.75 |
| cat08_04_resource_assign           |    6    |
| cat08_05_task_schedul              |    4.5  |



### qwen2.5-72b-instruct   => 28.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.5  |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    7.5  |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    4.5  |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    6.5  |
| cat02_08_underfitting_process_tree |    6.5  |
| cat02_09_fix_process_tree          |    9    |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    6.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3.5  |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    7.75 |
| cat04_06_sql_filt_three_df         |    7.25 |
| cat04_07_sql_filt_top_k_vars       |    7.75 |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    5    |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    7.75 |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    7.4  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    9    |
| cat08_01_queue_mining              |    5.5  |
| cat08_02_instance_spanning         |    5    |
| cat08_03_transport_opt             |    5    |
| cat08_04_resource_assign           |    7.5  |
| cat08_05_task_schedul              |    5.5  |



### pixtral-large-2411   => 27.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    9    |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    7.5  |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    4.5  |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    6    |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    4.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    8    |
| cat03_02_powl_generation           |    7    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    4.5  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    2    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    9    |
| cat04_07_sql_filt_top_k_vars       |    6.5  |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    7    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    7.5  |
| cat05_06_question_pseudo_bpmn      |    7.9  |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    7.25 |
| cat06_02_bias_event_log            |    7    |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    5.5  |
| cat06_07_fair_unfair_powl          |    2.5  |
| cat07_01_ocdfg                     |    3.5  |
| cat07_02_bpmn_orders               |   10    |
| cat07_03_bpmn_dispatch             |    8    |
| cat07_04_causal_net                |    7.5  |
| cat07_05_proclets                  |    7    |
| cat07_06_perf_spectrum             |    9    |
| cat08_01_queue_mining              |    6.8  |
| cat08_02_instance_spanning         |    7    |
| cat08_03_transport_opt             |    6    |
| cat08_04_resource_assign           |    1.5  |
| cat08_05_task_schedul              |    6    |



### gemma327b-it-q8_0   => 27.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    5    |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    4.5  |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7.4  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7.25 |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    7.75 |
| cat03_06_petri_net_generation      |    2.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    5.5  |
| cat05_01_hyp_generation_log        |    4.5  |
| cat05_02_hyp_gen_powl              |    6.5  |
| cat05_03_hyp_gen_declare           |    7    |
| cat05_04_hyp_gen_temp_profile      |    4.5  |
| cat05_05_question_gen_nlp          |    8    |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    9.4  |
| cat06_02_bias_event_log            |    7.25 |
| cat06_03_bias_powl                 |    7.25 |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    6    |
| cat07_01_ocdfg                     |    1    |
| cat07_02_bpmn_orders               |    6    |
| cat07_03_bpmn_dispatch             |    1    |
| cat07_04_causal_net                |    4    |
| cat07_05_proclets                  |    5.5  |
| cat07_06_perf_spectrum             |    4    |
| cat08_01_queue_mining              |    7.5  |
| cat08_02_instance_spanning         |    7.75 |
| cat08_03_transport_opt             |    8    |
| cat08_04_resource_assign           |    7.75 |
| cat08_05_task_schedul              |    7.25 |



### meta-llamallama-4-maverick   => 27.1 points

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
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    8    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    7.75 |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    9.6  |
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
| cat08_01_queue_mining              |    5    |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    4    |
| cat08_04_resource_assign           |    5.5  |
| cat08_05_task_schedul              |    6.5  |



### mistral-large-2411   => 27.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    7    |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    7.75 |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    5    |
| cat02_04_powl_anomaly_detection    |    7.9  |
| cat02_05_two_powls_anomalies       |    5    |
| cat02_06_root_cause_1              |    4.5  |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    2.5  |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    6    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    7.5  |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    2.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    6.5  |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    5.5  |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    7.4  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    7    |
| cat08_01_queue_mining              |    6.5  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    4.5  |
| cat08_04_resource_assign           |    6    |
| cat08_05_task_schedul              |    6.8  |



### mistral-small-2503   => 26.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    8.6  |
| cat02_03_anomaly_event_log         |    4.5  |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    5    |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    8    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4.5  |
| cat05_05_question_gen_nlp          |    7.9  |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    9.2  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    7.25 |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    7.75 |
| cat07_01_ocdfg                     |    7    |
| cat07_02_bpmn_orders               |    6    |
| cat07_03_bpmn_dispatch             |    5    |
| cat07_04_causal_net                |    7    |
| cat07_05_proclets                  |    6.5  |
| cat07_06_perf_spectrum             |    4.5  |
| cat08_01_queue_mining              |    7    |
| cat08_02_instance_spanning         |    3    |
| cat08_03_transport_opt             |    4.5  |
| cat08_04_resource_assign           |    6    |
| cat08_05_task_schedul              |    5.5  |



### microsoftWizardLM-2-8x22B   => 26.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.5  |
| cat01_02_activity_context          |    4.5  |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    5    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    8    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    7    |
| cat02_07_root_cause_2              |    4.5  |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    5.5  |
| cat03_06_petri_net_generation      |    3.5  |
| cat03_07_process_tree_discovery    |    2.5  |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    7.25 |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    5.5  |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    8    |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    7.5  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    9    |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    4    |
| cat06_04_bias_two_logs             |    7    |
| cat06_05_bias_two_logs_2           |    4.8  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    8    |
| cat08_01_queue_mining              |    4    |
| cat08_02_instance_spanning         |    5    |
| cat08_03_transport_opt             |    5    |
| cat08_04_resource_assign           |    6    |
| cat08_05_task_schedul              |    7.25 |



### mistral-small-2501   => 26.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    9    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    3.5  |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    3.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4.5  |
| cat01_08_tables_to_log             |    4.5  |
| cat02_01_conformance_textual       |    6.5  |
| cat02_02_conf_desiderata           |    5.5  |
| cat02_03_anomaly_event_log         |    7.75 |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    4.5  |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    7.25 |
| cat03_01_process_tree_generation   |    8.6  |
| cat03_02_powl_generation           |    7.75 |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    5    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    7.25 |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    9.4  |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    5.5  |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    6    |
| cat08_01_queue_mining              |    7.6  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    5.5  |
| cat08_04_resource_assign           |    5    |
| cat08_05_task_schedul              |    5    |



### microsoftphi-4   => 26.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    7.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    3.5  |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    7.65 |
| cat02_03_anomaly_event_log         |    6.5  |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    6.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7.75 |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    8    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3.5  |
| cat03_05_temp_profile_generation   |    6    |
| cat03_06_petri_net_generation      |    4    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    5.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    5.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.6  |
| cat05_06_question_pseudo_bpmn      |    7.4  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    7.75 |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    7    |
| cat06_04_bias_two_logs             |    4.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    6    |
| cat08_01_queue_mining              |    6.5  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    6    |
| cat08_04_resource_assign           |    5.5  |
| cat08_05_task_schedul              |    5    |



### QwenQwen2.5-Coder-32B-Instruct   => 26.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    5    |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    5.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    5.5  |
| cat02_04_powl_anomaly_detection    |    7.25 |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    2.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    9.6  |
| cat03_01_process_tree_generation   |    5    |
| cat03_02_powl_generation           |    9    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3.5  |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    6.5  |
| cat04_07_sql_filt_top_k_vars       |    7.35 |
| cat05_01_hyp_generation_log        |    3.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    6    |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    5    |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    7    |
| cat08_01_queue_mining              |    6.5  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    3.7  |
| cat08_04_resource_assign           |    7.5  |
| cat08_05_task_schedul              |    7.4  |



### qwen2.5-32b-instruct   => 25.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    6    |
| cat01_02_activity_context          |    7.25 |
| cat01_03_high_level_events         |    4.5  |
| cat01_04_sensor_recordings         |    6.8  |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    5.5  |
| cat01_08_tables_to_log             |    3.5  |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    2.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    9    |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    2.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3.5  |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    3.5  |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    6.5  |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    9.6  |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    6    |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    7.25 |
| cat06_04_bias_two_logs             |    7.75 |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    5    |
| cat08_01_queue_mining              |    4.5  |
| cat08_02_instance_spanning         |    6.5  |
| cat08_03_transport_opt             |    5    |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    6    |



### open-mixtral-8x22b   => 25.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.25 |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    4    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    9    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    2.5  |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    7.75 |
| cat03_01_process_tree_generation   |    2.5  |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    4.5  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4    |
| cat04_02_pseudo_bpmn_open_question |    6.5  |
| cat04_03_declare_open_question     |    2.5  |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    7.5  |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    2    |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    7.75 |
| cat06_01_bias_text                 |    7    |
| cat06_02_bias_event_log            |    6.8  |
| cat06_03_bias_powl                 |    7    |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    3.5  |
| cat08_01_queue_mining              |    3.5  |
| cat08_02_instance_spanning         |    4.5  |
| cat08_03_transport_opt             |    3.5  |
| cat08_04_resource_assign           |    4.5  |
| cat08_05_task_schedul              |    4.5  |



### gemma312b-it-q8_0   => 25.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    7.25 |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    5.5  |
| cat01_07_interv_to_pseudo_bpmn     |    5.5  |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    2    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    3.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    6    |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    4    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    6.5  |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    4.5  |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    6    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    3.5  |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    8    |
| cat05_06_question_pseudo_bpmn      |    9    |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    7.9  |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    9    |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    8    |
| cat07_01_ocdfg                     |    3.5  |
| cat07_02_bpmn_orders               |    4.5  |
| cat07_03_bpmn_dispatch             |    4.5  |
| cat07_04_causal_net                |    4.5  |
| cat07_05_proclets                  |    7.4  |
| cat07_06_perf_spectrum             |    4    |
| cat08_01_queue_mining              |    7.4  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    6.5  |
| cat08_04_resource_assign           |    7.75 |
| cat08_05_task_schedul              |    7.75 |



### qwen2.5-14b-instruct-1m   => 24.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    7.5  |
| cat01_03_high_level_events         |    5    |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    5.5  |
| cat02_04_powl_anomaly_detection    |    7.75 |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    4    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    7.25 |
| cat04_02_pseudo_bpmn_open_question |    5.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    4    |
| cat05_01_hyp_generation_log        |    3    |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    6.5  |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    8    |
| cat05_07_question_interview        |    7.4  |
| cat06_01_bias_text                 |    8    |
| cat06_02_bias_event_log            |    5    |
| cat06_03_bias_powl                 |    7.5  |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    5.5  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    3.5  |
| cat08_01_queue_mining              |    7.25 |
| cat08_02_instance_spanning         |    5.5  |
| cat08_03_transport_opt             |    3.5  |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    4    |



### codestral-2501   => 23.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.75 |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    8    |
| cat02_01_conformance_textual       |    5    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    4.5  |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    2.5  |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    2.5  |
| cat03_02_powl_generation           |    3    |
| cat03_03_log_skeleton_generation   |    4    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    4.5  |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5.5  |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    6.5  |
| cat06_01_bias_text                 |    4.5  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    3.5  |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    6    |
| cat08_01_queue_mining              |    4    |
| cat08_02_instance_spanning         |    5    |
| cat08_03_transport_opt             |    5.5  |
| cat08_04_resource_assign           |    4    |
| cat08_05_task_schedul              |    4    |



### falcon310b-instruct-q8_0   => 23.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    5    |
| cat01_02_activity_context          |    7.25 |
| cat01_03_high_level_events         |    3.5  |
| cat01_04_sensor_recordings         |    6.5  |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    9    |
| cat02_02_conf_desiderata           |    5    |
| cat02_03_anomaly_event_log         |    5    |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    7.75 |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    2.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3.5  |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    5    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    5    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    7.25 |
| cat05_06_question_pseudo_bpmn      |    9.4  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    2    |
| cat06_04_bias_two_logs             |    6.5  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    5    |
| cat06_07_fair_unfair_powl          |    6.5  |
| cat08_01_queue_mining              |    5.5  |
| cat08_02_instance_spanning         |    4    |
| cat08_03_transport_opt             |    5    |
| cat08_04_resource_assign           |    5    |
| cat08_05_task_schedul              |    4.5  |



### falcon37b-instruct-q8_0   => 22.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    6.5  |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    2.5  |
| cat02_01_conformance_textual       |    5    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    7.75 |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    5    |
| cat02_08_underfitting_process_tree |    3    |
| cat02_09_fix_process_tree          |    7    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    9.6  |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3    |
| cat04_01_pseudo_bpmn_description   |    4.5  |
| cat04_02_pseudo_bpmn_open_question |    5.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    7.75 |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    7.25 |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    7.5  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    2    |
| cat06_04_bias_two_logs             |    5.5  |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    5    |
| cat08_01_queue_mining              |    6.5  |
| cat08_02_instance_spanning         |    5.5  |
| cat08_03_transport_opt             |    6    |
| cat08_04_resource_assign           |    6    |
| cat08_05_task_schedul              |    4.5  |



### pixtral-12b-2409   => 22.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    3.5  |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    4.5  |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4.5  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    7    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    5    |
| cat02_04_powl_anomaly_detection    |    6.5  |
| cat02_05_two_powls_anomalies       |    4.5  |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |    6.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    2.5  |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    3.5  |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    5.5  |
| cat05_05_question_gen_nlp          |    7    |
| cat05_06_question_pseudo_bpmn      |    7.25 |
| cat05_07_question_interview        |    7    |
| cat06_01_bias_text                 |    7.6  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    6.8  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    6.5  |
| cat06_06_bias_mitigation_declare   |    2.5  |
| cat06_07_fair_unfair_powl          |    3    |
| cat07_01_ocdfg                     |    7.75 |
| cat07_02_bpmn_orders               |    6.5  |
| cat07_03_bpmn_dispatch             |    3.5  |
| cat07_04_causal_net                |    6    |
| cat07_05_proclets                  |   10    |
| cat07_06_perf_spectrum             |    6    |
| cat08_01_queue_mining              |    4.5  |
| cat08_02_instance_spanning         |    5.5  |
| cat08_03_transport_opt             |    4    |
| cat08_04_resource_assign           |    4    |
| cat08_05_task_schedul              |    4.5  |



### meta-llamallama-4-scout   => 22.5 points

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
| cat05_05_question_gen_nlp          |    9    |
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
| cat08_01_queue_mining              |    2.5  |
| cat08_02_instance_spanning         |    4    |
| cat08_03_transport_opt             |    3.5  |
| cat08_04_resource_assign           |    4    |
| cat08_05_task_schedul              |    2.5  |



### granite3.3   => 21.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    3    |
| cat01_02_activity_context          |    6.5  |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    6    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    2.5  |
| cat02_03_anomaly_event_log         |    3.5  |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    5    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    1.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2.5  |
| cat03_05_temp_profile_generation   |    2.5  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    5    |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3.5  |
| cat04_05_sql_filt_num_events       |    6.5  |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    3    |
| cat05_01_hyp_generation_log        |    5    |
| cat05_02_hyp_gen_powl              |    4    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    9.6  |
| cat05_06_question_pseudo_bpmn      |    8    |
| cat05_07_question_interview        |    9    |
| cat06_01_bias_text                 |    7.75 |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    3    |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    3    |
| cat08_01_queue_mining              |    7.5  |
| cat08_02_instance_spanning         |    6    |
| cat08_03_transport_opt             |    7    |
| cat08_04_resource_assign           |    7.4  |
| cat08_05_task_schedul              |    7    |



### qwen2.5-omni-7b   => 21.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2.5  |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    3    |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    2.5  |
| cat02_03_anomaly_event_log         |    4    |
| cat02_04_powl_anomaly_detection    |    7.25 |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    3    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    7    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    4    |
| cat04_01_pseudo_bpmn_description   |    4    |
| cat04_02_pseudo_bpmn_open_question |    4    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    7    |
| cat05_01_hyp_generation_log        |    2.5  |
| cat05_02_hyp_gen_powl              |    4.5  |
| cat05_03_hyp_gen_declare           |    3    |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |    8.6  |
| cat05_06_question_pseudo_bpmn      |    8.4  |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    6.5  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    4    |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    3.5  |
| cat07_01_ocdfg                     |    3.5  |
| cat07_02_bpmn_orders               |    1    |
| cat07_03_bpmn_dispatch             |    3.5  |
| cat07_04_causal_net                |    3.5  |
| cat07_05_proclets                  |    3.5  |
| cat07_06_perf_spectrum             |    7.25 |
| cat08_01_queue_mining              |    3    |
| cat08_02_instance_spanning         |    5.5  |
| cat08_03_transport_opt             |    5.5  |
| cat08_04_resource_assign           |    4.5  |
| cat08_05_task_schedul              |    5.5  |



### gemma34b-it-q8_0   => 19.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2.5  |
| cat01_02_activity_context          |    3    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    2.5  |
| cat01_06_system_logs               |    2    |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    2.5  |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    1    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    1.5  |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    6    |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    9.6  |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    1.5  |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    5    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    7.9  |
| cat05_07_question_interview        |    7.9  |
| cat06_01_bias_text                 |    7.25 |
| cat06_02_bias_event_log            |    3.5  |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    3.5  |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    1    |
| cat07_01_ocdfg                     |    3.5  |
| cat07_02_bpmn_orders               |    3    |
| cat07_03_bpmn_dispatch             |    2.5  |
| cat07_04_causal_net                |    4.5  |
| cat07_05_proclets                  |    4    |
| cat07_06_perf_spectrum             |    2.5  |
| cat08_01_queue_mining              |    7    |
| cat08_02_instance_spanning         |    7    |
| cat08_03_transport_opt             |    6.5  |
| cat08_04_resource_assign           |    4.4  |
| cat08_05_task_schedul              |    6.5  |



### qwen2.5-7b-instruct-1m   => 19.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     3.5 |
| cat01_05_merge_two_logs            |     1.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     4   |
| cat02_04_powl_anomaly_detection    |     3.5 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     5   |
| cat02_09_fix_process_tree          |     4   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     3   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     7.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     5.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     4   |
| cat06_04_bias_two_logs             |     4.5 |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     3   |
| cat08_01_queue_mining              |     6   |
| cat08_02_instance_spanning         |     5   |
| cat08_03_transport_opt             |     5   |
| cat08_04_resource_assign           |     6.5 |
| cat08_05_task_schedul              |     5   |



### falcon33b-instruct-q8_0   => 18.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    4    |
| cat01_04_sensor_recordings         |    4    |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3.5  |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    3    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    2    |
| cat02_04_powl_anomaly_detection    |    6.8  |
| cat02_05_two_powls_anomalies       |    2.5  |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    2    |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    6.5  |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    2.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    3.5  |
| cat04_03_declare_open_question     |    3    |
| cat04_04_declare_description       |    3.5  |
| cat04_05_sql_filt_num_events       |    6.5  |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    2    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    2    |
| cat05_04_hyp_gen_temp_profile      |    2    |
| cat05_05_question_gen_nlp          |    6.5  |
| cat05_06_question_pseudo_bpmn      |    7.75 |
| cat05_07_question_interview        |    7    |
| cat06_01_bias_text                 |    7.4  |
| cat06_02_bias_event_log            |    3    |
| cat06_03_bias_powl                 |    4.5  |
| cat06_04_bias_two_logs             |    4    |
| cat06_05_bias_two_logs_2           |    4    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    2.5  |
| cat08_01_queue_mining              |    5    |
| cat08_02_instance_spanning         |    3.5  |
| cat08_03_transport_opt             |    5.5  |
| cat08_04_resource_assign           |    7    |
| cat08_05_task_schedul              |    6    |



### microsoftPhi-4-multimodal-instruct   => 17.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     2.5 |
| cat01_03_high_level_events         |     3.2 |
| cat01_04_sensor_recordings         |     2.5 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     5.5 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     1.5 |
| cat03_03_log_skeleton_generation   |     1.5 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     6.5 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     1.5 |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     3.5 |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     6.8 |
| cat06_02_bias_event_log            |     3.5 |
| cat06_03_bias_powl                 |     5.5 |
| cat06_04_bias_two_logs             |     3   |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     2   |
| cat07_01_ocdfg                     |     6.5 |
| cat07_02_bpmn_orders               |     4   |
| cat07_03_bpmn_dispatch             |     2   |
| cat07_04_causal_net                |     3   |
| cat07_05_proclets                  |     8   |
| cat07_06_perf_spectrum             |     3.5 |
| cat08_01_queue_mining              |     6   |
| cat08_02_instance_spanning         |     5.5 |
| cat08_03_transport_opt             |     6.5 |
| cat08_04_resource_assign           |     6   |
| cat08_05_task_schedul              |     4   |



### olmo27b-1124-instruct-q8_0   => 16.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    2.5  |
| cat01_02_activity_context          |    3    |
| cat01_03_high_level_events         |    3    |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    3    |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    1.5  |
| cat02_01_conformance_textual       |    2    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    3    |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3    |
| cat02_06_root_cause_1              |    2.5  |
| cat02_07_root_cause_2              |    3.5  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    3    |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    1.5  |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    4.5  |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    3    |
| cat04_05_sql_filt_num_events       |    2    |
| cat04_06_sql_filt_three_df         |    1.5  |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    3    |
| cat05_03_hyp_gen_declare           |    2    |
| cat05_04_hyp_gen_temp_profile      |    3    |
| cat05_05_question_gen_nlp          |    7.75 |
| cat05_06_question_pseudo_bpmn      |    1    |
| cat05_07_question_interview        |    7.5  |
| cat06_01_bias_text                 |    7.4  |
| cat06_02_bias_event_log            |    4    |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    3    |
| cat06_05_bias_two_logs_2           |    3.5  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    1.5  |
| cat08_01_queue_mining              |    2.5  |
| cat08_02_instance_spanning         |    3.5  |
| cat08_03_transport_opt             |    4    |
| cat08_04_resource_assign           |    5.5  |
| cat08_05_task_schedul              |    4    |



### gemma31b-it-q8_0   => 12.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    1    |
| cat01_03_high_level_events         |    2    |
| cat01_04_sensor_recordings         |    1    |
| cat01_05_merge_two_logs            |    1    |
| cat01_06_system_logs               |    1.5  |
| cat01_07_interv_to_pseudo_bpmn     |    3    |
| cat01_08_tables_to_log             |    1    |
| cat02_01_conformance_textual       |    1    |
| cat02_02_conf_desiderata           |    1.5  |
| cat02_03_anomaly_event_log         |    1.5  |
| cat02_04_powl_anomaly_detection    |    3    |
| cat02_05_two_powls_anomalies       |    1.5  |
| cat02_06_root_cause_1              |    2    |
| cat02_07_root_cause_2              |    2    |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |    5.5  |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    1    |
| cat03_03_log_skeleton_generation   |    1.5  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    1    |
| cat04_01_pseudo_bpmn_description   |    3    |
| cat04_02_pseudo_bpmn_open_question |    2    |
| cat04_03_declare_open_question     |    2.5  |
| cat04_04_declare_description       |    2    |
| cat04_05_sql_filt_num_events       |    2    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    1    |
| cat05_01_hyp_generation_log        |    6.4  |
| cat05_02_hyp_gen_powl              |    2.5  |
| cat05_03_hyp_gen_declare           |    2.5  |
| cat05_04_hyp_gen_temp_profile      |    2    |
| cat05_05_question_gen_nlp          |    6    |
| cat05_06_question_pseudo_bpmn      |    5.5  |
| cat05_07_question_interview        |    7.25 |
| cat06_01_bias_text                 |    6.5  |
| cat06_02_bias_event_log            |    3    |
| cat06_03_bias_powl                 |    3    |
| cat06_04_bias_two_logs             |    2    |
| cat06_05_bias_two_logs_2           |    3    |
| cat06_06_bias_mitigation_declare   |    1    |
| cat06_07_fair_unfair_powl          |    1.5  |
| cat08_01_queue_mining              |    3.5  |
| cat08_02_instance_spanning         |    3    |
| cat08_03_transport_opt             |    4    |
| cat08_04_resource_assign           |    3    |
| cat08_05_task_schedul              |    6    |

