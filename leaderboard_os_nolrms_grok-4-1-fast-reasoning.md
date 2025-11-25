A score in the range **27-34** is considered **sufficient**; a score in the range **34-38** is considered **fair**; a score in the range **38-44** is considered **good**; and a score **>44** is considered **excellent**.

## Base Open-Source LLMs Leaderboard (1-shot; grok-4-1-fast-reasoning used as a judge)

| Model                         | Score    | OS                 | LRM   | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | OPT                  | :nerd_face: VI       |
|:------------------------------|:---------|:-------------------|:------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| qwen3-next-80b-a3b-instruct   | **38.7** | :white_check_mark: | :x:   | 6.1                  | 6.9                  | 4.1                  | 5.4                  | **6.3**              | 5.5                  | :mage_woman: **4.4** | 0.0                  |
| deepseek-v3.2-exp             | **38.1** | :white_check_mark: | :x:   | **6.5**              | 5.6                  | 4.5                  | **5.9**              | 5.8                  | :mage_woman: **6.0** | 3.9                  | 0.0                  |
| minimaxminimax-m2             | **37.4** | :white_check_mark: | :x:   | 5.9                  | 6.5                  | :mage_woman: **5.5** | 5.4                  | 5.0                  | 4.7                  | :mage_woman: **4.4** | 0.0                  |
| openrouterbert-nebulon-alpha  | **37.4** | :white_check_mark: | :x:   | 6.3                  | 6.4                  | 4.0                  | 5.3                  | 5.7                  | **5.8**              | 3.8                  | 0.0                  |
| DeepSeek-V3-0324              | **37.0** | :white_check_mark: | :x:   | **6.5**              | 6.1                  | 5.1                  | 4.9                  | 5.2                  | 5.4                  | 3.8                  | 0.0                  |
| DeepSeek-V3.1                 | **36.9** | :white_check_mark: | :x:   | :mage_woman: **6.7** | :mage_woman: **7.4** | 2.8                  | 4.4                  | 5.9                  | 5.6                  | 4.0                  | 0.0                  |
| moonshotaikimi-k2-0905        | **36.8** | :white_check_mark: | :x:   | 6.2                  | 6.2                  | 4.3                  | :mage_woman: **6.2** | :mage_woman: **6.4** | 4.3                  | 3.2                  | 0.0                  |
| mistral-small-2506            | **35.0** | :white_check_mark: | :x:   | 6.1                  | 6.2                  | 4.3                  | 4.9                  | 4.3                  | 5.2                  | 3.9                  | **5.4**              |
| DeepSeek-V3                   | **34.9** | :white_check_mark: | :x:   | 5.5                  | 7.0                  | 2.8                  | 5.1                  | 6.0                  | 5.2                  | 3.3                  | 0.0                  |
| qwen3-coder                   | **34.3** | :white_check_mark: | :x:   | 5.8                  | 5.3                  | 3.5                  | 5.2                  | 5.9                  | 4.5                  | 4.1                  | 0.0                  |
| qwen3-30b-a3b-instruct-2507   | **34.2** | :white_check_mark: | :x:   | 5.7                  | 6.4                  | 3.3                  | 4.2                  | 5.9                  | 5.1                  | 3.6                  | 0.0                  |
| Llama-3.3-70B-Instruct        | **34.1** | :white_check_mark: | :x:   | 6.0                  | 6.2                  | 3.0                  | 5.6                  | 5.2                  | 5.2                  | 2.9                  | 0.0                  |
| baiduernie-4.5-300b-a47b      | **34.0** | :white_check_mark: | :x:   | 5.4                  | 6.1                  | 3.2                  | 4.9                  | 5.5                  | 5.3                  | 3.7                  | 0.0                  |
| qwen2.5-72b-instruct          | **34.0** | :white_check_mark: | :x:   | 6.1                  | 6.1                  | 3.8                  | 4.8                  | 4.9                  | 5.2                  | 3.1                  | 0.0                  |
| nemotron-70b-instruct         | **33.6** | :white_check_mark: | :x:   | 6.0                  | 5.8                  | 4.0                  | 4.5                  | 4.7                  | 5.2                  | 3.5                  | 0.0                  |
| devstral-medium-2507          | **33.3** | :white_check_mark: | :x:   | 5.4                  | 5.5                  | 3.8                  | 5.4                  | 4.9                  | 5.6                  | 2.7                  | 0.0                  |
| WizardLM-2-8x22B              | **32.6** | :white_check_mark: | :x:   | 5.7                  | 5.6                  | 2.9                  | 4.4                  | 5.7                  | 4.9                  | 3.4                  | 0.0                  |
| Qwen-3-14B-nothink            | **32.3** | :white_check_mark: | :x:   | 6.0                  | 6.4                  | 2.2                  | 4.4                  | 5.3                  | 4.9                  | 3.0                  | 0.0                  |
| gemma327b-it-q8_0             | **32.3** | :white_check_mark: | :x:   | 5.5                  | 5.6                  | 1.6                  | 5.0                  | 5.5                  | 5.2                  | 3.9                  | 4.8                  |
| pixtral-large-2411            | **32.0** | :white_check_mark: | :x:   | 6.1                  | 5.8                  | 3.4                  | 4.7                  | 4.6                  | 5.3                  | 2.3                  | :mage_woman: **5.7** |
| qwen2.5-32b-instruct          | **31.7** | :white_check_mark: | :x:   | 6.3                  | 5.6                  | 2.0                  | 4.5                  | 5.4                  | 5.0                  | 3.0                  | 0.0                  |
| qwen34b-instruct-2507-q8_0    | **31.6** | :white_check_mark: | :x:   | 4.8                  | 5.9                  | 3.1                  | 4.1                  | 5.3                  | 4.8                  | 3.5                  | 0.0                  |
| Qwen-3-32B-nothink            | **31.1** | :white_check_mark: | :x:   | 5.8                  | 6.2                  | 2.2                  | 3.6                  | 5.5                  | 5.1                  | 2.7                  | 0.0                  |
| mistral-large-2411            | **30.5** | :white_check_mark: | :x:   | 5.7                  | 5.6                  | 3.2                  | 4.0                  | 4.6                  | 5.2                  | 2.3                  | 0.0                  |
| gemma312b-it-q8_0             | **30.4** | :white_check_mark: | :x:   | 4.9                  | 4.6                  | 2.9                  | 4.9                  | 4.6                  | 5.0                  | 3.4                  | 4.6                  |
| llama-4-maverick              | **30.3** | :white_check_mark: | :x:   | 4.4                  | 6.2                  | 2.3                  | 3.9                  | 5.9                  | 4.9                  | 2.8                  | **5.4**              |
| phi-4                         | **29.9** | :white_check_mark: | :x:   | 6.0                  | 5.3                  | 2.7                  | 3.8                  | 4.2                  | 4.8                  | 3.0                  | 0.0                  |
| mistral-small-2503            | **29.6** | :white_check_mark: | :x:   | 4.7                  | 6.1                  | 1.8                  | 4.7                  | 5.0                  | 5.1                  | 2.3                  | **5.4**              |
| inceptionmercury              | **29.4** | :white_check_mark: | :x:   | 5.2                  | 5.4                  | 2.6                  | 4.5                  | 4.5                  | 5.1                  | 2.1                  | 0.0                  |
| ai21jamba-large-1.7           | **29.1** | :white_check_mark: | :x:   | 4.6                  | 5.2                  | 2.2                  | 4.5                  | 4.2                  | 5.1                  | 3.3                  | 0.0                  |
| granite4small-h               | **28.4** | :white_check_mark: | :x:   | 4.7                  | 5.1                  | 1.6                  | 3.6                  | 5.2                  | 4.5                  | 3.7                  | 0.0                  |
| open-mixtral-8x22b            | **28.0** | :white_check_mark: | :x:   | 5.5                  | 5.3                  | 2.2                  | 4.9                  | 4.8                  | 3.3                  | 1.9                  | 0.0                  |
| falcon310b-instruct-q8_0      | **27.1** | :white_check_mark: | :x:   | 3.7                  | 5.3                  | 2.0                  | 3.6                  | 4.7                  | 4.9                  | 2.8                  | 0.0                  |
| moonshotaikimi-linear-48b-a3b | **26.5** | :white_check_mark: | :x:   | 3.6                  | 5.2                  | 2.0                  | 5.0                  | 4.7                  | 3.6                  | 2.3                  | 0.0                  |
| falcon37b-instruct-q8_0       | **26.0** | :white_check_mark: | :x:   | 3.3                  | 5.3                  | 3.0                  | 3.7                  | 4.6                  | 3.5                  | 2.7                  | 0.0                  |
| pixtral-12b-2409              | **25.9** | :white_check_mark: | :x:   | 3.5                  | 5.2                  | 2.6                  | 3.3                  | 4.0                  | 4.7                  | 2.5                  | **5.4**              |
| llama-4-scout                 | **25.7** | :white_check_mark: | :x:   | 4.1                  | 4.8                  | 2.8                  | 4.7                  | 4.3                  | 3.8                  | 1.2                  | 4.9                  |
| granite3.3                    | **25.1** | :white_check_mark: | :x:   | 3.9                  | 4.3                  | 2.2                  | 3.5                  | 3.9                  | 4.4                  | 2.8                  | 0.0                  |
| gemma-3n-e4b-it               | **24.1** | :white_check_mark: | :x:   | 3.3                  | 3.4                  | 1.6                  | 4.2                  | 4.1                  | 4.2                  | 3.2                  | 0.0                  |
| ai21jamba-mini-1.7            | **23.2** | :white_check_mark: | :x:   | 2.9                  | 4.0                  | 1.9                  | 3.0                  | 3.9                  | 4.1                  | 3.4                  | 0.0                  |
| gemma34b-it-q8_0              | **22.1** | :white_check_mark: | :x:   | 2.2                  | 3.9                  | 1.3                  | 3.7                  | 4.6                  | 3.1                  | 3.3                  | 3.9                  |
| granite4micro-h               | **21.4** | :white_check_mark: | :x:   | 2.7                  | 3.8                  | 1.5                  | 4.0                  | 3.1                  | 3.3                  | 3.0                  | 0.0                  |
| falcon33b-instruct-q8_0       | **21.4** | :white_check_mark: | :x:   | 3.0                  | 3.2                  | 2.4                  | 2.9                  | 3.8                  | 4.0                  | 2.1                  | 0.0                  |
| granite4micro                 | **20.4** | :white_check_mark: | :x:   | 2.9                  | 3.0                  | 1.6                  | 2.9                  | 3.9                  | 3.5                  | 2.6                  | 0.0                  |
| granite4tiny-h                | **19.6** | :white_check_mark: | :x:   | 2.6                  | 4.0                  | 1.5                  | 2.5                  | 3.9                  | 3.0                  | 2.1                  | 0.0                  |
| liquidlfm2-8b-a1b             | **19.4** | :white_check_mark: | :x:   | 2.3                  | 3.2                  | 1.1                  | 3.2                  | 3.9                  | 2.4                  | 3.2                  | 0.0                  |
| olmo27b-1124-instruct-q8_0    | **18.1** | :white_check_mark: | :x:   | 2.8                  | 3.4                  | 1.5                  | 2.0                  | 3.3                  | 3.3                  | 1.9                  | 0.0                  |
| ibmgranite41b-h               | **16.7** | :white_check_mark: | :x:   | 2.3                  | 2.7                  | 1.1                  | 2.0                  | 3.3                  | 2.8                  | 2.4                  | 0.0                  |
| liquidlfm-2.2-6b              | **15.4** | :white_check_mark: | :x:   | 2.3                  | 1.9                  | 1.3                  | 2.4                  | 3.0                  | 2.0                  | 2.5                  | 0.0                  |
| gemma31b-it-q8_0              | **10.7** | :white_check_mark: | :x:   | 1.1                  | 1.6                  | 0.8                  | 1.1                  | 2.7                  | 1.9                  | 1.3                  | 0.0                  |
| ibmgranite4350m-h             | **7.5**  | :white_check_mark: | :x:   | 0.9                  | 1.2                  | 0.9                  | 0.7                  | 1.6                  | 0.8                  | 1.4                  | 0.0                  |

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



### deepseekdeepseek-v3.2-exp   => 38.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     7   |
| cat01_06_system_logs               |     7.6 |
| cat01_07_interv_to_pseudo_bpmn     |     8.4 |
| cat01_08_tables_to_log             |     9   |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     7.5 |
| cat02_03_anomaly_event_log         |     8.4 |
| cat02_04_powl_anomaly_detection    |     1.5 |
| cat02_05_two_powls_anomalies       |     5   |
| cat02_06_root_cause_1              |    10   |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     8.4 |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     8   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     7   |
| cat03_07_process_tree_discovery    |     4   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     8.4 |
| cat04_02_pseudo_bpmn_open_question |     8.8 |
| cat04_03_declare_open_question     |     8.4 |
| cat04_04_declare_description       |     5   |
| cat04_05_sql_filt_num_events       |     8.4 |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.5 |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     7.5 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |     8.4 |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     9.6 |
| cat06_02_bias_event_log            |     8.4 |
| cat06_03_bias_powl                 |     8.4 |
| cat06_04_bias_two_logs             |     8.4 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     7   |
| cat06_07_fair_unfair_powl          |     8.4 |
| cat08_01_queue_mining              |     9.4 |
| cat08_02_instance_spanning         |     9   |
| cat08_03_transport_opt             |     9.4 |
| cat08_04_resource_assign           |     2.1 |
| cat08_05_task_schedul              |     9.4 |



### minimaxminimax-m2free   => 37.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |   10    |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    3    |
| cat01_05_merge_two_logs            |    8.4  |
| cat01_06_system_logs               |    3.5  |
| cat01_07_interv_to_pseudo_bpmn     |    8.4  |
| cat01_08_tables_to_log             |    7.1  |
| cat02_01_conformance_textual       |    9.4  |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |    7.6  |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    3.8  |
| cat02_06_root_cause_1              |    7    |
| cat02_07_root_cause_2              |    1.45 |
| cat02_08_underfitting_process_tree |   10    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    8.4  |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |   10    |
| cat03_05_temp_profile_generation   |   10    |
| cat03_06_petri_net_generation      |   10    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    8.4  |
| cat04_02_pseudo_bpmn_open_question |    8.4  |
| cat04_03_declare_open_question     |    7    |
| cat04_04_declare_description       |    4.2  |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    8.4  |
| cat04_07_sql_filt_top_k_vars       |   10    |
| cat05_01_hyp_generation_log        |    7    |
| cat05_02_hyp_gen_powl              |    8.8  |
| cat05_03_hyp_gen_declare           |    9.4  |
| cat05_04_hyp_gen_temp_profile      |    1    |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    7.05 |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    7.1  |
| cat06_03_bias_powl                 |    8.6  |
| cat06_04_bias_two_logs             |    8.4  |
| cat06_05_bias_two_logs_2           |   10    |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    2.5  |
| cat08_01_queue_mining              |    8.8  |
| cat08_02_instance_spanning         |    9.4  |
| cat08_03_transport_opt             |    8.8  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    8.4  |



### openrouterbert-nebulon-alpha   => 37.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     8.4 |
| cat01_04_sensor_recordings         |     7.6 |
| cat01_05_merge_two_logs            |     4.2 |
| cat01_06_system_logs               |     8.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.8 |
| cat01_08_tables_to_log             |     8   |
| cat02_01_conformance_textual       |     9.6 |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     9.6 |
| cat02_04_powl_anomaly_detection    |     8.4 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     3.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     4.2 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     7.6 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     7   |
| cat04_01_pseudo_bpmn_description   |     7.6 |
| cat04_02_pseudo_bpmn_open_question |     8.4 |
| cat04_03_declare_open_question     |     7.6 |
| cat04_04_declare_description       |     5   |
| cat04_05_sql_filt_num_events       |     8.4 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     8.4 |
| cat05_02_hyp_gen_powl              |     6.2 |
| cat05_03_hyp_gen_declare           |     7.6 |
| cat05_04_hyp_gen_temp_profile      |     8.4 |
| cat05_05_question_gen_nlp          |     8.4 |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     8.4 |
| cat06_03_bias_powl                 |     9.4 |
| cat06_04_bias_two_logs             |     7.6 |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     8.4 |
| cat06_07_fair_unfair_powl          |     7   |
| cat08_01_queue_mining              |    10   |
| cat08_02_instance_spanning         |     8.4 |
| cat08_03_transport_opt             |     8.4 |
| cat08_04_resource_assign           |     3.1 |
| cat08_05_task_schedul              |     8.4 |



### deepseek-aiDeepSeek-V3-0324   => 37.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8.4  |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    7    |
| cat01_06_system_logs               |    5    |
| cat01_07_interv_to_pseudo_bpmn     |    7.6  |
| cat01_08_tables_to_log             |   10    |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |   10    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    7.5  |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    8.4  |
| cat02_08_underfitting_process_tree |    3.2  |
| cat02_09_fix_process_tree          |    8.4  |
| cat03_01_process_tree_generation   |    4    |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    7    |
| cat03_04_declare_generation        |    4    |
| cat03_05_temp_profile_generation   |    7    |
| cat03_06_petri_net_generation      |    7    |
| cat03_07_process_tree_discovery    |    5    |
| cat03_08_powl_discovery            |    7    |
| cat04_01_pseudo_bpmn_description   |    7.6  |
| cat04_02_pseudo_bpmn_open_question |    1.8  |
| cat04_03_declare_open_question     |    7.6  |
| cat04_04_declare_description       |    6    |
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    7    |
| cat04_07_sql_filt_top_k_vars       |   10    |
| cat05_01_hyp_generation_log        |    7.5  |
| cat05_02_hyp_gen_powl              |    9    |
| cat05_03_hyp_gen_declare           |    4.2  |
| cat05_04_hyp_gen_temp_profile      |    5.5  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    8.4  |
| cat05_07_question_interview        |    8.8  |
| cat06_01_bias_text                 |    9.4  |
| cat06_02_bias_event_log            |    8.4  |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    7.5  |
| cat06_06_bias_mitigation_declare   |    4.5  |
| cat06_07_fair_unfair_powl          |    8.4  |
| cat08_01_queue_mining              |    8.4  |
| cat08_02_instance_spanning         |    7.1  |
| cat08_03_transport_opt             |    7.1  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    7.05 |



### deepseek-aiDeepSeek-V3.1   => 36.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    7.6  |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    9    |
| cat01_06_system_logs               |    6    |
| cat01_07_interv_to_pseudo_bpmn     |    9    |
| cat01_08_tables_to_log             |    8.4  |
| cat02_01_conformance_textual       |   10    |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |   10    |
| cat02_04_powl_anomaly_detection    |   10    |
| cat02_05_two_powls_anomalies       |    7    |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    8.4  |
| cat02_08_underfitting_process_tree |   10    |
| cat02_09_fix_process_tree          |    8.4  |
| cat03_01_process_tree_generation   |    5    |
| cat03_02_powl_generation           |    7    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    1.5  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    3.2  |
| cat03_08_powl_discovery            |    6    |
| cat04_01_pseudo_bpmn_description   |    8.4  |
| cat04_02_pseudo_bpmn_open_question |    8.4  |
| cat04_03_declare_open_question     |    7.6  |
| cat04_04_declare_description       |    1    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |   10    |
| cat04_07_sql_filt_top_k_vars       |    1    |
| cat05_01_hyp_generation_log        |    7.75 |
| cat05_02_hyp_gen_powl              |    8    |
| cat05_03_hyp_gen_declare           |    7    |
| cat05_04_hyp_gen_temp_profile      |    8.8  |
| cat05_05_question_gen_nlp          |    9.4  |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    8.4  |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    8.4  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    4.2  |
| cat06_07_fair_unfair_powl          |   10    |
| cat08_01_queue_mining              |    8.4  |
| cat08_02_instance_spanning         |    9    |
| cat08_03_transport_opt             |    9.6  |
| cat08_04_resource_assign           |    4.5  |
| cat08_05_task_schedul              |    8.4  |



### moonshotaikimi-k2-0905   => 36.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.6 |
| cat01_03_high_level_events         |     8.4 |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     8.4 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     8.4 |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     8.4 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     8.4 |
| cat02_04_powl_anomaly_detection    |     4.2 |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     7.6 |
| cat02_08_underfitting_process_tree |     3.2 |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     8.4 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8.8 |
| cat04_02_pseudo_bpmn_open_question |     8.8 |
| cat04_03_declare_open_question     |     6.2 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     8.4 |
| cat05_02_hyp_gen_powl              |     8.4 |
| cat05_03_hyp_gen_declare           |     8.4 |
| cat05_04_hyp_gen_temp_profile      |    10   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     7.6 |
| cat06_03_bias_powl                 |     1.8 |
| cat06_04_bias_two_logs             |     7.6 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     7   |
| cat08_01_queue_mining              |     8.8 |
| cat08_02_instance_spanning         |     4.2 |
| cat08_03_transport_opt             |     8.4 |
| cat08_04_resource_assign           |     1.2 |
| cat08_05_task_schedul              |     9.4 |



### mistral-small-2506   => 35.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    7.6  |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    8.4  |
| cat01_06_system_logs               |    6.2  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    5    |
| cat02_01_conformance_textual       |    9    |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    7.1  |
| cat02_05_two_powls_anomalies       |    7    |
| cat02_06_root_cause_1              |    7    |
| cat02_07_root_cause_2              |    8.4  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    5    |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    7.6  |
| cat03_05_temp_profile_generation   |    6    |
| cat03_06_petri_net_generation      |    8.4  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    8.4  |
| cat04_02_pseudo_bpmn_open_question |    7.6  |
| cat04_03_declare_open_question     |    7.6  |
| cat04_04_declare_description       |    3.2  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |   10    |
| cat05_01_hyp_generation_log        |    8.4  |
| cat05_02_hyp_gen_powl              |    7.15 |
| cat05_03_hyp_gen_declare           |    1    |
| cat05_04_hyp_gen_temp_profile      |    8.4  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    2    |
| cat05_07_question_interview        |    7.65 |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    8.4  |
| cat06_03_bias_powl                 |    6    |
| cat06_04_bias_two_logs             |    7.1  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    4.2  |
| cat06_07_fair_unfair_powl          |   10    |
| cat07_01_ocdfg                     |    8.4  |
| cat07_02_bpmn_orders               |    9.6  |
| cat07_03_bpmn_dispatch             |    8.4  |
| cat07_04_causal_net                |   10    |
| cat07_05_proclets                  |    8.4  |
| cat07_06_perf_spectrum             |    9    |
| cat08_01_queue_mining              |    8.4  |
| cat08_02_instance_spanning         |    8.4  |
| cat08_03_transport_opt             |    7.1  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    7.1  |



### deepseek-aiDeepSeek-V3   => 34.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |  10     |
| cat01_02_activity_context          |   7.7   |
| cat01_03_high_level_events         |   4     |
| cat01_04_sensor_recordings         |   7.1   |
| cat01_05_merge_two_logs            |   3.2   |
| cat01_06_system_logs               |   6     |
| cat01_07_interv_to_pseudo_bpmn     |   7.1   |
| cat01_08_tables_to_log             |  10     |
| cat02_01_conformance_textual       |   8.4   |
| cat02_02_conf_desiderata           |   6     |
| cat02_03_anomaly_event_log         |   9     |
| cat02_04_powl_anomaly_detection    |  10     |
| cat02_05_two_powls_anomalies       |   6     |
| cat02_06_root_cause_1              |   9.6   |
| cat02_07_root_cause_2              |   7.1   |
| cat02_08_underfitting_process_tree |   4     |
| cat02_09_fix_process_tree          |  10     |
| cat03_01_process_tree_generation   |   3     |
| cat03_02_powl_generation           |   7     |
| cat03_03_log_skeleton_generation   |   2     |
| cat03_04_declare_generation        |   3.2   |
| cat03_05_temp_profile_generation   |   7.1   |
| cat03_06_petri_net_generation      |   1     |
| cat03_07_process_tree_discovery    |   1.5   |
| cat03_08_powl_discovery            |   3.2   |
| cat04_01_pseudo_bpmn_description   |   8.4   |
| cat04_02_pseudo_bpmn_open_question |   9     |
| cat04_03_declare_open_question     |   5     |
| cat04_04_declare_description       |   4     |
| cat04_05_sql_filt_num_events       |  10     |
| cat04_06_sql_filt_three_df         |   5.999 |
| cat04_07_sql_filt_top_k_vars       |   8.4   |
| cat05_01_hyp_generation_log        |   9     |
| cat05_02_hyp_gen_powl              |   7     |
| cat05_03_hyp_gen_declare           |   7.1   |
| cat05_04_hyp_gen_temp_profile      |   8.4   |
| cat05_05_question_gen_nlp          |  10     |
| cat05_06_question_pseudo_bpmn      |  10     |
| cat05_07_question_interview        |   8.4   |
| cat06_01_bias_text                 |   9.4   |
| cat06_02_bias_event_log            |   7.7   |
| cat06_03_bias_powl                 |   8     |
| cat06_04_bias_two_logs             |   8.4   |
| cat06_05_bias_two_logs_2           |   8.4   |
| cat06_06_bias_mitigation_declare   |   2     |
| cat06_07_fair_unfair_powl          |   8.4   |
| cat08_01_queue_mining              |   6.2   |
| cat08_02_instance_spanning         |   7.1   |
| cat08_03_transport_opt             |   6.5   |
| cat08_04_resource_assign           |   6.2   |
| cat08_05_task_schedul              |   7.05  |



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



### meta-llamaLlama-3.3-70B-Instruct   => 34.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8    |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    8.4  |
| cat01_06_system_logs               |    6.2  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    3.2  |
| cat02_01_conformance_textual       |    9    |
| cat02_02_conf_desiderata           |    7    |
| cat02_03_anomaly_event_log         |    8.4  |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    7.6  |
| cat02_06_root_cause_1              |    6.5  |
| cat02_07_root_cause_2              |    4    |
| cat02_08_underfitting_process_tree |    1.5  |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    3.2  |
| cat03_02_powl_generation           |    9    |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    6.2  |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    3.2  |
| cat04_01_pseudo_bpmn_description   |    8.4  |
| cat04_02_pseudo_bpmn_open_question |    7.1  |
| cat04_03_declare_open_question     |    6.2  |
| cat04_04_declare_description       |    7.6  |
| cat04_05_sql_filt_num_events       |    9    |
| cat04_06_sql_filt_three_df         |    9    |
| cat04_07_sql_filt_top_k_vars       |    8.4  |
| cat05_01_hyp_generation_log        |    7.1  |
| cat05_02_hyp_gen_powl              |    7    |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |    9.6  |
| cat05_06_question_pseudo_bpmn      |    9.6  |
| cat05_07_question_interview        |    7    |
| cat06_01_bias_text                 |    9.6  |
| cat06_02_bias_event_log            |    7    |
| cat06_03_bias_powl                 |    7.65 |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |   10    |
| cat08_01_queue_mining              |    8.4  |
| cat08_02_instance_spanning         |    6.5  |
| cat08_03_transport_opt             |    5.8  |
| cat08_04_resource_assign           |    6.2  |
| cat08_05_task_schedul              |    2.5  |



### baiduernie-4.5-300b-a47b   => 34.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8.4  |
| cat01_03_high_level_events         |    7.6  |
| cat01_04_sensor_recordings         |    7.6  |
| cat01_05_merge_two_logs            |    7.1  |
| cat01_06_system_logs               |    4.2  |
| cat01_07_interv_to_pseudo_bpmn     |    1.8  |
| cat01_08_tables_to_log             |    7.5  |
| cat02_01_conformance_textual       |    7.25 |
| cat02_02_conf_desiderata           |    8    |
| cat02_03_anomaly_event_log         |    8    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    5    |
| cat02_06_root_cause_1              |    7.1  |
| cat02_07_root_cause_2              |    8.8  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    6    |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    7.1  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    7.6  |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    2.5  |
| cat03_08_powl_discovery            |    6    |
| cat04_01_pseudo_bpmn_description   |    7.6  |
| cat04_02_pseudo_bpmn_open_question |    7.6  |
| cat04_03_declare_open_question     |    4.2  |
| cat04_04_declare_description       |    7    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    4.2  |
| cat04_07_sql_filt_top_k_vars       |    8.4  |
| cat05_01_hyp_generation_log        |    8.4  |
| cat05_02_hyp_gen_powl              |    8.4  |
| cat05_03_hyp_gen_declare           |    7.5  |
| cat05_04_hyp_gen_temp_profile      |    5    |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    7.1  |
| cat05_07_question_interview        |   10    |
| cat06_01_bias_text                 |    9.6  |
| cat06_02_bias_event_log            |    7.6  |
| cat06_03_bias_powl                 |    9.6  |
| cat06_04_bias_two_logs             |    1    |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    7.1  |
| cat06_07_fair_unfair_powl          |    9.6  |
| cat08_01_queue_mining              |    7.6  |
| cat08_02_instance_spanning         |    6.2  |
| cat08_03_transport_opt             |    7.1  |
| cat08_04_resource_assign           |    6.5  |
| cat08_05_task_schedul              |    9.4  |



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



### nvidiaLlama-3.1-Nemotron-70B-Instruct   => 33.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    4.2  |
| cat01_06_system_logs               |    8.4  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    7.5  |
| cat02_01_conformance_textual       |    7    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    9.6  |
| cat02_04_powl_anomaly_detection    |    9    |
| cat02_05_two_powls_anomalies       |    7    |
| cat02_06_root_cause_1              |    4.2  |
| cat02_07_root_cause_2              |    6    |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    8.4  |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    5    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    7.4  |
| cat03_06_petri_net_generation      |    7.5  |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    8    |
| cat04_02_pseudo_bpmn_open_question |    7.05 |
| cat04_03_declare_open_question     |    7.65 |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    7.5  |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    8.4  |
| cat05_01_hyp_generation_log        |    7.1  |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    1.2  |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |   10    |
| cat06_01_bias_text                 |    9.6  |
| cat06_02_bias_event_log            |    4.2  |
| cat06_03_bias_powl                 |    8    |
| cat06_04_bias_two_logs             |    8.4  |
| cat06_05_bias_two_logs_2           |   10    |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    8.4  |
| cat08_01_queue_mining              |    8.8  |
| cat08_02_instance_spanning         |    4.2  |
| cat08_03_transport_opt             |    7.05 |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    7.05 |



### devstral-medium-2507   => 33.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.4 |
| cat01_03_high_level_events         |     7.6 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     6.5 |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     8.4 |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     1.5 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |    10   |
| cat03_01_process_tree_generation   |     3.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     7   |
| cat03_05_temp_profile_generation   |     7   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     8.4 |
| cat04_02_pseudo_bpmn_open_question |     6.2 |
| cat04_03_declare_open_question     |     7   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     8.4 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     7.6 |
| cat05_03_hyp_gen_declare           |     3.5 |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     7.6 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     7.6 |
| cat06_04_bias_two_logs             |     8.4 |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     4.5 |
| cat08_02_instance_spanning         |     6.2 |
| cat08_03_transport_opt             |     6.2 |
| cat08_04_resource_assign           |     6.5 |
| cat08_05_task_schedul              |     3.2 |



### microsoftWizardLM-2-8x22B   => 32.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8    |
| cat01_03_high_level_events         |    7    |
| cat01_04_sensor_recordings         |    7.6  |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    5.5  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    6    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    4.2  |
| cat02_03_anomaly_event_log         |    7.5  |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    8.4  |
| cat02_07_root_cause_2              |    7.6  |
| cat02_08_underfitting_process_tree |    3.2  |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    3.2  |
| cat03_02_powl_generation           |    1    |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    5    |
| cat03_05_temp_profile_generation   |    8.4  |
| cat03_06_petri_net_generation      |    6    |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    1.5  |
| cat04_01_pseudo_bpmn_description   |    8.4  |
| cat04_02_pseudo_bpmn_open_question |    7.05 |
| cat04_03_declare_open_question     |    6.2  |
| cat04_04_declare_description       |    3.2  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    3    |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    6    |
| cat05_02_hyp_gen_powl              |    8    |
| cat05_03_hyp_gen_declare           |    7.1  |
| cat05_04_hyp_gen_temp_profile      |    7.1  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    7.1  |
| cat06_03_bias_powl                 |    7    |
| cat06_04_bias_two_logs             |    7.1  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    9    |
| cat08_01_queue_mining              |    6.2  |
| cat08_02_instance_spanning         |    7.1  |
| cat08_03_transport_opt             |    6.2  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    6.5  |



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



### gemma327b-it-q8_0   => 32.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8.4  |
| cat01_03_high_level_events         |    8.2  |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    4.2  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    4    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    7.1  |
| cat02_04_powl_anomaly_detection    |    7.6  |
| cat02_05_two_powls_anomalies       |    6.5  |
| cat02_06_root_cause_1              |    7    |
| cat02_07_root_cause_2              |    7.6  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    9    |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    1.5  |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    4.2  |
| cat03_05_temp_profile_generation   |    1    |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    3.2  |
| cat04_01_pseudo_bpmn_description   |    8.4  |
| cat04_02_pseudo_bpmn_open_question |    8.4  |
| cat04_03_declare_open_question     |    7.1  |
| cat04_04_declare_description       |    7    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    8.4  |
| cat05_01_hyp_generation_log        |    7.1  |
| cat05_02_hyp_gen_powl              |    6.5  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    7.1  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    8    |
| cat06_01_bias_text                 |   10    |
| cat06_02_bias_event_log            |    7.1  |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    8.4  |
| cat07_01_ocdfg                     |    7.1  |
| cat07_02_bpmn_orders               |    7.6  |
| cat07_03_bpmn_dispatch             |    7.85 |
| cat07_04_causal_net                |    8.8  |
| cat07_05_proclets                  |    8.4  |
| cat07_06_perf_spectrum             |    8.4  |
| cat08_01_queue_mining              |    8.4  |
| cat08_02_instance_spanning         |    6.5  |
| cat08_03_transport_opt             |    7.25 |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    8.4  |



### pixtral-large-2411   => 32.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7.6 |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     7.5 |
| cat01_06_system_logs               |     6.2 |
| cat01_07_interv_to_pseudo_bpmn     |     7.7 |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |     8.4 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     9.8 |
| cat02_04_powl_anomaly_detection    |     9.6 |
| cat02_05_two_powls_anomalies       |     5   |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     7   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     5.2 |
| cat03_06_petri_net_generation      |     6.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.2 |
| cat04_01_pseudo_bpmn_description   |     8.4 |
| cat04_02_pseudo_bpmn_open_question |     6.2 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     3.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |    10   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     8.4 |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     3.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     3.5 |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     8.8 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     8.4 |
| cat07_01_ocdfg                     |    10   |
| cat07_02_bpmn_orders               |     9   |
| cat07_03_bpmn_dispatch             |     8.4 |
| cat07_04_causal_net                |     9.6 |
| cat07_05_proclets                  |     9.6 |
| cat07_06_perf_spectrum             |    10   |
| cat08_01_queue_mining              |     6.5 |
| cat08_02_instance_spanning         |     6.2 |
| cat08_03_transport_opt             |     6.5 |
| cat08_04_resource_assign           |     1   |
| cat08_05_task_schedul              |     2.5 |



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



### mistral-large-2411   => 30.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     7   |
| cat01_06_system_logs               |     3.2 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     7.5 |
| cat02_02_conf_desiderata           |     7.5 |
| cat02_03_anomaly_event_log         |     6.5 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     7.5 |
| cat02_06_root_cause_1              |     1.8 |
| cat02_07_root_cause_2              |     7   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     8   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     7.1 |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8.4 |
| cat04_02_pseudo_bpmn_open_question |     5   |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     7.5 |
| cat05_01_hyp_generation_log        |     7.5 |
| cat05_02_hyp_gen_powl              |     6.2 |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     5.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     7.6 |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     8.4 |
| cat06_04_bias_two_logs             |     8.4 |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     5.2 |
| cat08_02_instance_spanning         |     1.7 |
| cat08_03_transport_opt             |     6   |
| cat08_04_resource_assign           |     6   |
| cat08_05_task_schedul              |     4.2 |



### gemma312b-it-q8_0   => 30.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    6    |
| cat01_02_activity_context          |    8.4  |
| cat01_03_high_level_events         |    7.25 |
| cat01_04_sensor_recordings         |    7.6  |
| cat01_05_merge_two_logs            |    3.2  |
| cat01_06_system_logs               |    2.5  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    7    |
| cat02_01_conformance_textual       |    4.2  |
| cat02_02_conf_desiderata           |    3.2  |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    2    |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    7.1  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    7.5  |
| cat03_02_powl_generation           |    5    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    4.2  |
| cat03_06_petri_net_generation      |    1.5  |
| cat03_07_process_tree_discovery    |    3    |
| cat03_08_powl_discovery            |    3.2  |
| cat04_01_pseudo_bpmn_description   |    7.6  |
| cat04_02_pseudo_bpmn_open_question |    8.6  |
| cat04_03_declare_open_question     |    7.6  |
| cat04_04_declare_description       |    7.1  |
| cat04_05_sql_filt_num_events       |    8.4  |
| cat04_06_sql_filt_three_df         |    3.2  |
| cat04_07_sql_filt_top_k_vars       |    6    |
| cat05_01_hyp_generation_log        |    7.1  |
| cat05_02_hyp_gen_powl              |    7.6  |
| cat05_03_hyp_gen_declare           |    1.5  |
| cat05_04_hyp_gen_temp_profile      |    3.2  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    8.4  |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    5.2  |
| cat06_03_bias_powl                 |    6.5  |
| cat06_04_bias_two_logs             |    7.1  |
| cat06_05_bias_two_logs_2           |   10    |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    9    |
| cat07_01_ocdfg                     |    8.4  |
| cat07_02_bpmn_orders               |    7.85 |
| cat07_03_bpmn_dispatch             |    7.6  |
| cat07_04_causal_net                |    7.7  |
| cat07_05_proclets                  |    7.1  |
| cat07_06_perf_spectrum             |    7.1  |
| cat08_01_queue_mining              |    7.6  |
| cat08_02_instance_spanning         |    6.5  |
| cat08_03_transport_opt             |    6.2  |
| cat08_04_resource_assign           |    7.6  |
| cat08_05_task_schedul              |    6.5  |



### meta-llamallama-4-maverick   => 30.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    8.4  |
| cat01_02_activity_context          |    1    |
| cat01_03_high_level_events         |    5.5  |
| cat01_04_sensor_recordings         |    9    |
| cat01_05_merge_two_logs            |    1    |
| cat01_06_system_logs               |    7    |
| cat01_07_interv_to_pseudo_bpmn     |    6.2  |
| cat01_08_tables_to_log             |    6    |
| cat02_01_conformance_textual       |   10    |
| cat02_02_conf_desiderata           |    6.2  |
| cat02_03_anomaly_event_log         |    8.4  |
| cat02_04_powl_anomaly_detection    |    6    |
| cat02_05_two_powls_anomalies       |    8.4  |
| cat02_06_root_cause_1              |    4.2  |
| cat02_07_root_cause_2              |    7.5  |
| cat02_08_underfitting_process_tree |    3.2  |
| cat02_09_fix_process_tree          |    8    |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    1    |
| cat03_03_log_skeleton_generation   |    6    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    3.2  |
| cat03_07_process_tree_discovery    |    1.5  |
| cat03_08_powl_discovery            |    6    |
| cat04_01_pseudo_bpmn_description   |    6.2  |
| cat04_02_pseudo_bpmn_open_question |    6.2  |
| cat04_03_declare_open_question     |    1.2  |
| cat04_04_declare_description       |    3.2  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    4    |
| cat04_07_sql_filt_top_k_vars       |    8.4  |
| cat05_01_hyp_generation_log        |    7.1  |
| cat05_02_hyp_gen_powl              |    8.4  |
| cat05_03_hyp_gen_declare           |    7.6  |
| cat05_04_hyp_gen_temp_profile      |    7.6  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |   10    |
| cat06_01_bias_text                 |    7.6  |
| cat06_02_bias_event_log            |    7    |
| cat06_03_bias_powl                 |    6.2  |
| cat06_04_bias_two_logs             |    8.4  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    7    |
| cat07_01_ocdfg                     |   10    |
| cat07_02_bpmn_orders               |    8.4  |
| cat07_03_bpmn_dispatch             |    9.4  |
| cat07_04_causal_net                |    9    |
| cat07_05_proclets                  |    7.75 |
| cat07_06_perf_spectrum             |    9.6  |
| cat08_01_queue_mining              |    5.5  |
| cat08_02_instance_spanning         |    4.2  |
| cat08_03_transport_opt             |    6.8  |
| cat08_04_resource_assign           |    5.2  |
| cat08_05_task_schedul              |    6.2  |



### microsoftphi-4   => 29.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |    8    |
| cat01_03_high_level_events         |    7.05 |
| cat01_04_sensor_recordings         |    8.4  |
| cat01_05_merge_two_logs            |    7.6  |
| cat01_06_system_logs               |    6    |
| cat01_07_interv_to_pseudo_bpmn     |    6    |
| cat01_08_tables_to_log             |    7.1  |
| cat02_01_conformance_textual       |    7    |
| cat02_02_conf_desiderata           |    3    |
| cat02_03_anomaly_event_log         |    7.1  |
| cat02_04_powl_anomaly_detection    |   10    |
| cat02_05_two_powls_anomalies       |    4    |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    7.1  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    8    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    6    |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    7.1  |
| cat04_02_pseudo_bpmn_open_question |    5.2  |
| cat04_03_declare_open_question     |    5.2  |
| cat04_04_declare_description       |    4.2  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    4.2  |
| cat05_01_hyp_generation_log        |    7.1  |
| cat05_02_hyp_gen_powl              |    9.6  |
| cat05_03_hyp_gen_declare           |    3.2  |
| cat05_04_hyp_gen_temp_profile      |    4.2  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    1.5  |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    7.6  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    6    |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    3    |
| cat06_07_fair_unfair_powl          |    9    |
| cat08_01_queue_mining              |    7.55 |
| cat08_02_instance_spanning         |    3.2  |
| cat08_03_transport_opt             |    7.05 |
| cat08_04_resource_assign           |    6.2  |
| cat08_05_task_schedul              |    6.2  |



### mistral-small-2503   => 29.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    4    |
| cat01_02_activity_context          |    8    |
| cat01_03_high_level_events         |    7.1  |
| cat01_04_sensor_recordings         |    7.6  |
| cat01_05_merge_two_logs            |    3.2  |
| cat01_06_system_logs               |    4    |
| cat01_07_interv_to_pseudo_bpmn     |    4.2  |
| cat01_08_tables_to_log             |    8.4  |
| cat02_01_conformance_textual       |    7.5  |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    7    |
| cat02_04_powl_anomaly_detection    |    9.6  |
| cat02_05_two_powls_anomalies       |    7.1  |
| cat02_06_root_cause_1              |    7.1  |
| cat02_07_root_cause_2              |    4.25 |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    3    |
| cat03_02_powl_generation           |    1    |
| cat03_03_log_skeleton_generation   |    2    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    4    |
| cat03_06_petri_net_generation      |    3    |
| cat03_07_process_tree_discovery    |    2    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    7    |
| cat04_02_pseudo_bpmn_open_question |    6.2  |
| cat04_03_declare_open_question     |    3.2  |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    8.4  |
| cat04_07_sql_filt_top_k_vars       |    8    |
| cat05_01_hyp_generation_log        |    7.6  |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4    |
| cat05_04_hyp_gen_temp_profile      |    4.2  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    7.1  |
| cat06_03_bias_powl                 |    7.6  |
| cat06_04_bias_two_logs             |    7.5  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |   10    |
| cat07_01_ocdfg                     |    9.4  |
| cat07_02_bpmn_orders               |    8.6  |
| cat07_03_bpmn_dispatch             |    9    |
| cat07_04_causal_net                |    9    |
| cat07_05_proclets                  |    9.6  |
| cat07_06_perf_spectrum             |    8.4  |
| cat08_01_queue_mining              |    8    |
| cat08_02_instance_spanning         |    6.2  |
| cat08_03_transport_opt             |    3.5  |
| cat08_04_resource_assign           |    3.2  |
| cat08_05_task_schedul              |    2.5  |



### inceptionmercury   => 29.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     7.6 |
| cat01_03_high_level_events         |     8.4 |
| cat01_04_sensor_recordings         |     7.6 |
| cat01_05_merge_two_logs            |     3.2 |
| cat01_06_system_logs               |     3.2 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |     7.5 |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     8.4 |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4.2 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7   |
| cat04_07_sql_filt_top_k_vars       |     8.4 |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     7.1 |
| cat05_03_hyp_gen_declare           |     3.2 |
| cat05_04_hyp_gen_temp_profile      |     6.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.8 |
| cat06_02_bias_event_log            |     6.2 |
| cat06_03_bias_powl                 |     8.4 |
| cat06_04_bias_two_logs             |     7.6 |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     6   |
| cat08_01_queue_mining              |     6   |
| cat08_02_instance_spanning         |     3.5 |
| cat08_03_transport_opt             |     2.5 |
| cat08_04_resource_assign           |     5.5 |
| cat08_05_task_schedul              |     3.2 |



### ai21jamba-large-1.7   => 29.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.2 |
| cat01_02_activity_context          |     8.6 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     8.4 |
| cat01_05_merge_two_logs            |     4.2 |
| cat01_06_system_logs               |     5.2 |
| cat01_07_interv_to_pseudo_bpmn     |     6.2 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     3.2 |
| cat02_03_anomaly_event_log         |     7.6 |
| cat02_04_powl_anomaly_detection    |     9.6 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     4.2 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     3.2 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1.5 |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     8.4 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     8.4 |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     3.2 |
| cat05_04_hyp_gen_temp_profile      |     5   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     8.4 |
| cat05_07_question_interview        |     7.6 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     8.4 |
| cat06_04_bias_two_logs             |     8.4 |
| cat06_05_bias_two_logs_2           |     8.8 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     9   |
| cat08_01_queue_mining              |     6.5 |
| cat08_02_instance_spanning         |     5.2 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     7   |



### granite4small-h   => 28.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    9    |
| cat01_02_activity_context          |    8.4  |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    7.1  |
| cat01_05_merge_two_logs            |    6    |
| cat01_06_system_logs               |    3.2  |
| cat01_07_interv_to_pseudo_bpmn     |    1.5  |
| cat01_08_tables_to_log             |    3.2  |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    6    |
| cat02_04_powl_anomaly_detection    |    7.6  |
| cat02_05_two_powls_anomalies       |    5.5  |
| cat02_06_root_cause_1              |    6    |
| cat02_07_root_cause_2              |    3.2  |
| cat02_08_underfitting_process_tree |    2    |
| cat02_09_fix_process_tree          |    8.8  |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    1    |
| cat03_03_log_skeleton_generation   |    3.2  |
| cat03_04_declare_generation        |    1.5  |
| cat03_05_temp_profile_generation   |    4.2  |
| cat03_06_petri_net_generation      |    2    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    9    |
| cat04_02_pseudo_bpmn_open_question |    6.2  |
| cat04_03_declare_open_question     |    4.2  |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    2    |
| cat04_07_sql_filt_top_k_vars       |    1    |
| cat05_01_hyp_generation_log        |    7.6  |
| cat05_02_hyp_gen_powl              |    8.4  |
| cat05_03_hyp_gen_declare           |    7.1  |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    7.1  |
| cat05_07_question_interview        |    8.2  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    6.5  |
| cat06_03_bias_powl                 |    7.1  |
| cat06_04_bias_two_logs             |    4.2  |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    6    |
| cat06_07_fair_unfair_powl          |    4    |
| cat08_01_queue_mining              |    7.1  |
| cat08_02_instance_spanning         |    7.05 |
| cat08_03_transport_opt             |    7.1  |
| cat08_04_resource_assign           |    8.4  |
| cat08_05_task_schedul              |    7.55 |



### open-mixtral-8x22b   => 28.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |   10    |
| cat01_02_activity_context          |   10    |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    3.2  |
| cat01_06_system_logs               |    6.2  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    6    |
| cat02_02_conf_desiderata           |    4    |
| cat02_03_anomaly_event_log         |    7.6  |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    6    |
| cat02_06_root_cause_1              |    3    |
| cat02_07_root_cause_2              |    7.5  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |   10    |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    8.4  |
| cat03_03_log_skeleton_generation   |    4    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    2.62 |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    1    |
| cat04_01_pseudo_bpmn_description   |    4.2  |
| cat04_02_pseudo_bpmn_open_question |    7.1  |
| cat04_03_declare_open_question     |    4    |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |   10    |
| cat04_07_sql_filt_top_k_vars       |   10    |
| cat05_01_hyp_generation_log        |    7    |
| cat05_02_hyp_gen_powl              |    7.5  |
| cat05_03_hyp_gen_declare           |    7    |
| cat05_04_hyp_gen_temp_profile      |    4.2  |
| cat05_05_question_gen_nlp          |    7.6  |
| cat05_06_question_pseudo_bpmn      |    7.5  |
| cat05_07_question_interview        |    7.6  |
| cat06_01_bias_text                 |    1.6  |
| cat06_02_bias_event_log            |    4.2  |
| cat06_03_bias_powl                 |    9    |
| cat06_04_bias_two_logs             |    5    |
| cat06_05_bias_two_logs_2           |    8.8  |
| cat06_06_bias_mitigation_declare   |    2    |
| cat06_07_fair_unfair_powl          |    2    |
| cat08_01_queue_mining              |    6.2  |
| cat08_02_instance_spanning         |    2.5  |
| cat08_03_transport_opt             |    2.5  |
| cat08_04_resource_assign           |    4    |
| cat08_05_task_schedul              |    4.2  |



### falcon310b-instruct-q8_0   => 27.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     1.5 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     8.4 |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     7.6 |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     4.5 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.2 |
| cat04_01_pseudo_bpmn_description   |     7.6 |
| cat04_02_pseudo_bpmn_open_question |     6.2 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     5.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     9.6 |
| cat06_01_bias_text                 |     7.6 |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     3   |
| cat06_04_bias_two_logs             |    10   |
| cat06_05_bias_two_logs_2           |     8.4 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |    10   |
| cat08_01_queue_mining              |     7.6 |
| cat08_02_instance_spanning         |     4.2 |
| cat08_03_transport_opt             |     6.2 |
| cat08_04_resource_assign           |     6.2 |
| cat08_05_task_schedul              |     4.2 |



### moonshotaikimi-linear-48b-a3b-instruct   => 26.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    7.6  |
| cat01_02_activity_context          |    2    |
| cat01_03_high_level_events         |    8.4  |
| cat01_04_sensor_recordings         |    6    |
| cat01_05_merge_two_logs            |    1    |
| cat01_06_system_logs               |    2    |
| cat01_07_interv_to_pseudo_bpmn     |    7.05 |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    8.4  |
| cat02_02_conf_desiderata           |    8    |
| cat02_03_anomaly_event_log         |    6.2  |
| cat02_04_powl_anomaly_detection    |    7.5  |
| cat02_05_two_powls_anomalies       |    3.2  |
| cat02_06_root_cause_1              |    3.2  |
| cat02_07_root_cause_2              |    7.1  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    3.2  |
| cat03_03_log_skeleton_generation   |    4.2  |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    7.1  |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    6.2  |
| cat04_02_pseudo_bpmn_open_question |    7.05 |
| cat04_03_declare_open_question     |    7    |
| cat04_04_declare_description       |    6.2  |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    4    |
| cat04_07_sql_filt_top_k_vars       |   10    |
| cat05_01_hyp_generation_log        |    3.2  |
| cat05_02_hyp_gen_powl              |    6    |
| cat05_03_hyp_gen_declare           |    4.2  |
| cat05_04_hyp_gen_temp_profile      |    6    |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    7.1  |
| cat06_01_bias_text                 |    7.1  |
| cat06_02_bias_event_log            |    6    |
| cat06_03_bias_powl                 |    8.8  |
| cat06_04_bias_two_logs             |    2    |
| cat06_05_bias_two_logs_2           |    7.1  |
| cat06_06_bias_mitigation_declare   |    1    |
| cat06_07_fair_unfair_powl          |    4    |
| cat08_01_queue_mining              |    8.2  |
| cat08_02_instance_spanning         |    3.2  |
| cat08_03_transport_opt             |    7.6  |
| cat08_04_resource_assign           |    1.5  |
| cat08_05_task_schedul              |    2.5  |



### falcon37b-instruct-q8_0   => 26.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.2 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     8.4 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     6.2 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     4   |
| cat02_04_powl_anomaly_detection    |     9   |
| cat02_05_two_powls_anomalies       |     3.2 |
| cat02_06_root_cause_1              |     7.1 |
| cat02_07_root_cause_2              |     7   |
| cat02_08_underfitting_process_tree |     4   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3.2 |
| cat03_04_declare_generation        |     4.2 |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.2 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     6.2 |
| cat04_03_declare_open_question     |     7.1 |
| cat04_04_declare_description       |     3.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     3.2 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     6.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     6.5 |
| cat08_01_queue_mining              |     5.2 |
| cat08_02_instance_spanning         |     7.6 |
| cat08_03_transport_opt             |     5.5 |
| cat08_04_resource_assign           |     4.2 |
| cat08_05_task_schedul              |     4.2 |



### pixtral-12b-2409   => 25.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.2 |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     4.2 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     3.2 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     9.6 |
| cat02_05_two_powls_anomalies       |     5   |
| cat02_06_root_cause_1              |     1.8 |
| cat02_07_root_cause_2              |     5.2 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     3.2 |
| cat03_02_powl_generation           |     8.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     5.2 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2.3 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     3.2 |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     8.4 |
| cat05_07_question_interview        |     7.6 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     6.2 |
| cat06_03_bias_powl                 |     7.6 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     8.4 |
| cat07_01_ocdfg                     |     8.4 |
| cat07_02_bpmn_orders               |     8.6 |
| cat07_03_bpmn_dispatch             |     8.8 |
| cat07_04_causal_net                |    10   |
| cat07_05_proclets                  |     8.4 |
| cat07_06_perf_spectrum             |    10   |
| cat08_01_queue_mining              |     7.1 |
| cat08_02_instance_spanning         |     3.2 |
| cat08_03_transport_opt             |     6.1 |
| cat08_04_resource_assign           |     6.5 |
| cat08_05_task_schedul              |     2.5 |



### meta-llamallama-4-scout   => 25.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    7    |
| cat01_03_high_level_events         |    6.2  |
| cat01_04_sensor_recordings         |    5    |
| cat01_05_merge_two_logs            |    7.1  |
| cat01_06_system_logs               |    3.2  |
| cat01_07_interv_to_pseudo_bpmn     |    7.1  |
| cat01_08_tables_to_log             |    4    |
| cat02_01_conformance_textual       |    8    |
| cat02_02_conf_desiderata           |    5    |
| cat02_03_anomaly_event_log         |    5    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    3.2  |
| cat02_06_root_cause_1              |    4.2  |
| cat02_07_root_cause_2              |    5.2  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    8.4  |
| cat03_01_process_tree_generation   |    3.2  |
| cat03_02_powl_generation           |   10    |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    3.2  |
| cat03_05_temp_profile_generation   |    4.2  |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    2.3  |
| cat03_08_powl_discovery            |    3.2  |
| cat04_01_pseudo_bpmn_description   |    7.1  |
| cat04_02_pseudo_bpmn_open_question |    7.6  |
| cat04_03_declare_open_question     |    7.1  |
| cat04_04_declare_description       |    4    |
| cat04_05_sql_filt_num_events       |    8    |
| cat04_06_sql_filt_three_df         |    9    |
| cat04_07_sql_filt_top_k_vars       |    4.2  |
| cat05_01_hyp_generation_log        |    7.1  |
| cat05_02_hyp_gen_powl              |    7.1  |
| cat05_03_hyp_gen_declare           |    6    |
| cat05_04_hyp_gen_temp_profile      |    4    |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    8.4  |
| cat05_07_question_interview        |    1.8  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    6.2  |
| cat06_03_bias_powl                 |    3.2  |
| cat06_04_bias_two_logs             |    7.75 |
| cat06_05_bias_two_logs_2           |    7    |
| cat06_06_bias_mitigation_declare   |    1.5  |
| cat06_07_fair_unfair_powl          |    3.5  |
| cat07_01_ocdfg                     |    8.8  |
| cat07_02_bpmn_orders               |    8.4  |
| cat07_03_bpmn_dispatch             |    6.2  |
| cat07_04_causal_net                |    7.6  |
| cat07_05_proclets                  |    8.8  |
| cat07_06_perf_spectrum             |    9.6  |
| cat08_01_queue_mining              |    1    |
| cat08_02_instance_spanning         |    3.2  |
| cat08_03_transport_opt             |    4.2  |
| cat08_04_resource_assign           |    2    |
| cat08_05_task_schedul              |    2    |



### granite3.3   => 25.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3.2 |
| cat01_02_activity_context          |     7.1 |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     6.2 |
| cat01_05_merge_two_logs            |     3.2 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     6.2 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     4.2 |
| cat02_02_conf_desiderata           |     1.5 |
| cat02_03_anomaly_event_log         |     4.2 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3.2 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     4.2 |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     6.2 |
| cat04_03_declare_open_question     |     7.1 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     2.8 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     6.2 |
| cat06_03_bias_powl                 |     8.8 |
| cat06_04_bias_two_logs             |     5   |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     3.2 |
| cat06_07_fair_unfair_powl          |     5   |
| cat08_01_queue_mining              |     7.1 |
| cat08_02_instance_spanning         |     7.6 |
| cat08_03_transport_opt             |     5.5 |
| cat08_04_resource_assign           |     7.1 |
| cat08_05_task_schedul              |     1   |



### gemma-3n-e4b-it   => 24.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     8.4 |
| cat01_03_high_level_events         |     5.2 |
| cat01_04_sensor_recordings         |     4.2 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     6.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     1.5 |
| cat02_02_conf_desiderata           |     3.2 |
| cat02_03_anomaly_event_log         |     3.2 |
| cat02_04_powl_anomaly_detection    |     8.4 |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     7.1 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     4.2 |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     8.6 |
| cat04_03_declare_open_question     |     7   |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |     8.4 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8.4 |
| cat05_06_question_pseudo_bpmn      |     9.6 |
| cat05_07_question_interview        |    10   |
| cat06_01_bias_text                 |     8.6 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     6.2 |
| cat06_04_bias_two_logs             |     8.4 |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     1.5 |
| cat06_07_fair_unfair_powl          |     6   |
| cat08_01_queue_mining              |     4.2 |
| cat08_02_instance_spanning         |     6.5 |
| cat08_03_transport_opt             |     6.2 |
| cat08_04_resource_assign           |     8.4 |
| cat08_05_task_schedul              |     7.1 |



### ai21jamba-mini-1.7   => 23.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    4    |
| cat01_03_high_level_events         |    7.1  |
| cat01_04_sensor_recordings         |    5.2  |
| cat01_05_merge_two_logs            |    2    |
| cat01_06_system_logs               |    1.5  |
| cat01_07_interv_to_pseudo_bpmn     |    6.2  |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    3.2  |
| cat02_02_conf_desiderata           |    6    |
| cat02_03_anomaly_event_log         |    1    |
| cat02_04_powl_anomaly_detection    |    9.6  |
| cat02_05_two_powls_anomalies       |    4.2  |
| cat02_06_root_cause_1              |    4.2  |
| cat02_07_root_cause_2              |    4.2  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    7.1  |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    1.5  |
| cat03_03_log_skeleton_generation   |    6    |
| cat03_04_declare_generation        |    2    |
| cat03_05_temp_profile_generation   |    3.2  |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    7.1  |
| cat04_02_pseudo_bpmn_open_question |    7.05 |
| cat04_03_declare_open_question     |    1    |
| cat04_04_declare_description       |    1    |
| cat04_05_sql_filt_num_events       |    7.5  |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    5    |
| cat05_01_hyp_generation_log        |    1    |
| cat05_02_hyp_gen_powl              |    4.2  |
| cat05_03_hyp_gen_declare           |    4.2  |
| cat05_04_hyp_gen_temp_profile      |    3.5  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    7.6  |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    7.1  |
| cat06_03_bias_powl                 |    8.4  |
| cat06_04_bias_two_logs             |    5    |
| cat06_05_bias_two_logs_2           |    8.4  |
| cat06_06_bias_mitigation_declare   |    1.5  |
| cat06_07_fair_unfair_powl          |    2    |
| cat08_01_queue_mining              |    7.6  |
| cat08_02_instance_spanning         |    7    |
| cat08_03_transport_opt             |    6.2  |
| cat08_04_resource_assign           |    6.2  |
| cat08_05_task_schedul              |    7.1  |



### gemma34b-it-q8_0   => 22.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |     3.2 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     3.2 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     4   |
| cat02_04_powl_anomaly_detection    |     8.4 |
| cat02_05_two_powls_anomalies       |     1.5 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     3.2 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.2 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     7.6 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     8.4 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     8.4 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     7.6 |
| cat06_02_bias_event_log            |     4.2 |
| cat06_03_bias_powl                 |     5   |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     7.6 |
| cat06_06_bias_mitigation_declare   |     1.5 |
| cat06_07_fair_unfair_powl          |     1.5 |
| cat07_01_ocdfg                     |     8.6 |
| cat07_02_bpmn_orders               |     6.2 |
| cat07_03_bpmn_dispatch             |     7.7 |
| cat07_04_causal_net                |     8.8 |
| cat07_05_proclets                  |     1   |
| cat07_06_perf_spectrum             |     6.2 |
| cat08_01_queue_mining              |     6.5 |
| cat08_02_instance_spanning         |     5.2 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     7.6 |
| cat08_05_task_schedul              |     6.2 |



### granite4micro-h   => 21.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     3.2 |
| cat01_03_high_level_events         |     3   |
| cat01_04_sensor_recordings         |     5   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     3.2 |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     4   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8.4 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     3.2 |
| cat03_08_powl_discovery            |     3.2 |
| cat04_01_pseudo_bpmn_description   |     8.4 |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     7   |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |     8.4 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3.2 |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     2.5 |
| cat05_05_question_gen_nlp          |     8.4 |
| cat05_06_question_pseudo_bpmn      |     1.2 |
| cat05_07_question_interview        |     7.1 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     6.2 |
| cat06_03_bias_powl                 |     6.2 |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     5   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     3.2 |
| cat08_01_queue_mining              |     4.2 |
| cat08_02_instance_spanning         |     6.5 |
| cat08_03_transport_opt             |     7.1 |
| cat08_04_resource_assign           |     7.5 |
| cat08_05_task_schedul              |     5.2 |



### falcon33b-instruct-q8_0   => 21.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    5.2  |
| cat01_03_high_level_events         |    7    |
| cat01_04_sensor_recordings         |    4.2  |
| cat01_05_merge_two_logs            |    4.2  |
| cat01_06_system_logs               |    1    |
| cat01_07_interv_to_pseudo_bpmn     |    5    |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    2    |
| cat02_02_conf_desiderata           |    4.2  |
| cat02_03_anomaly_event_log         |    1.5  |
| cat02_04_powl_anomaly_detection    |    7    |
| cat02_05_two_powls_anomalies       |    3.2  |
| cat02_06_root_cause_1              |    3.2  |
| cat02_07_root_cause_2              |    2    |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    7.5  |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    8    |
| cat03_04_declare_generation        |    3    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    3.2  |
| cat03_08_powl_discovery            |    3.2  |
| cat04_01_pseudo_bpmn_description   |    6    |
| cat04_02_pseudo_bpmn_open_question |    4.2  |
| cat04_03_declare_open_question     |    5.2  |
| cat04_04_declare_description       |    1    |
| cat04_05_sql_filt_num_events       |   10    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    4    |
| cat05_02_hyp_gen_powl              |    3.2  |
| cat05_03_hyp_gen_declare           |    2    |
| cat05_04_hyp_gen_temp_profile      |    3.2  |
| cat05_05_question_gen_nlp          |    8.4  |
| cat05_06_question_pseudo_bpmn      |    8.4  |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    8.4  |
| cat06_02_bias_event_log            |    4.2  |
| cat06_03_bias_powl                 |    7    |
| cat06_04_bias_two_logs             |    3.2  |
| cat06_05_bias_two_logs_2           |    6    |
| cat06_06_bias_mitigation_declare   |    3.5  |
| cat06_07_fair_unfair_powl          |    8    |
| cat08_01_queue_mining              |    4.2  |
| cat08_02_instance_spanning         |    2.5  |
| cat08_03_transport_opt             |    4.2  |
| cat08_04_resource_assign           |    7.05 |
| cat08_05_task_schedul              |    3.2  |



### granite4micro   => 20.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     2   |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     3.2 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5.2 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     1.5 |
| cat02_03_anomaly_event_log         |     4   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3.2 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     2   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     3.2 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.2 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     3.2 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     3.2 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     7   |
| cat04_04_declare_description       |     5   |
| cat04_05_sql_filt_num_events       |     6   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1.2 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     3.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |    10   |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     8.4 |
| cat06_02_bias_event_log            |     6.2 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     4.2 |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     1.5 |
| cat06_07_fair_unfair_powl          |     3.2 |
| cat08_01_queue_mining              |     7.1 |
| cat08_02_instance_spanning         |     6.2 |
| cat08_03_transport_opt             |     1.5 |
| cat08_04_resource_assign           |     8.4 |
| cat08_05_task_schedul              |     3.2 |



### granite4tiny-h   => 19.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     2   |
| cat01_03_high_level_events         |     4.2 |
| cat01_04_sensor_recordings         |     4.2 |
| cat01_05_merge_two_logs            |     4.2 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     3.2 |
| cat02_04_powl_anomaly_detection    |     8.4 |
| cat02_05_two_powls_anomalies       |     3.2 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     3.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     3.2 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     4.2 |
| cat04_02_pseudo_bpmn_open_question |     2   |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     5   |
| cat04_05_sql_filt_num_events       |     8.4 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     3.2 |
| cat05_01_hyp_generation_log        |     4.2 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     3.2 |
| cat05_04_hyp_gen_temp_profile      |     3.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     7   |
| cat05_07_question_interview        |     7.1 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     4.2 |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     1.5 |
| cat06_07_fair_unfair_powl          |     3.2 |
| cat08_01_queue_mining              |     5   |
| cat08_02_instance_spanning         |     1.3 |
| cat08_03_transport_opt             |     6   |
| cat08_04_resource_assign           |     5.8 |
| cat08_05_task_schedul              |     3.2 |



### liquidlfm2-8b-a1b   => 19.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    4.2  |
| cat01_04_sensor_recordings         |    3.2  |
| cat01_05_merge_two_logs            |    1    |
| cat01_06_system_logs               |    1.5  |
| cat01_07_interv_to_pseudo_bpmn     |    4.2  |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    2    |
| cat02_02_conf_desiderata           |    2.5  |
| cat02_03_anomaly_event_log         |    1.5  |
| cat02_04_powl_anomaly_detection    |    7.6  |
| cat02_05_two_powls_anomalies       |    3.5  |
| cat02_06_root_cause_1              |    3.5  |
| cat02_07_root_cause_2              |    3.2  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    7.6  |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    2    |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    3    |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    1    |
| cat04_01_pseudo_bpmn_description   |    2.8  |
| cat04_02_pseudo_bpmn_open_question |    7.55 |
| cat04_03_declare_open_question     |    8.4  |
| cat04_04_declare_description       |    4.2  |
| cat04_05_sql_filt_num_events       |    7    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    1    |
| cat05_01_hyp_generation_log        |    1.5  |
| cat05_02_hyp_gen_powl              |    2    |
| cat05_03_hyp_gen_declare           |    4.2  |
| cat05_04_hyp_gen_temp_profile      |    3.2  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |   10    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    7.05 |
| cat06_02_bias_event_log            |    4.2  |
| cat06_03_bias_powl                 |    4.2  |
| cat06_04_bias_two_logs             |    3.2  |
| cat06_05_bias_two_logs_2           |    3    |
| cat06_06_bias_mitigation_declare   |    1    |
| cat06_07_fair_unfair_powl          |    1.2  |
| cat08_01_queue_mining              |    6.2  |
| cat08_02_instance_spanning         |    6.3  |
| cat08_03_transport_opt             |    7.1  |
| cat08_04_resource_assign           |    5.5  |
| cat08_05_task_schedul              |    7.1  |



### olmo27b-1124-instruct-q8_0   => 18.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    3.2  |
| cat01_03_high_level_events         |    6    |
| cat01_04_sensor_recordings         |    4.2  |
| cat01_05_merge_two_logs            |    3.2  |
| cat01_06_system_logs               |    3.2  |
| cat01_07_interv_to_pseudo_bpmn     |    4    |
| cat01_08_tables_to_log             |    3    |
| cat02_01_conformance_textual       |    2    |
| cat02_02_conf_desiderata           |    2.5  |
| cat02_03_anomaly_event_log         |    4    |
| cat02_04_powl_anomaly_detection    |    8.4  |
| cat02_05_two_powls_anomalies       |    4.2  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    3.2  |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    4.2  |
| cat03_01_process_tree_generation   |    2    |
| cat03_02_powl_generation           |    3.2  |
| cat03_03_log_skeleton_generation   |    3    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    3.2  |
| cat04_02_pseudo_bpmn_open_question |    3.2  |
| cat04_03_declare_open_question     |    5.2  |
| cat04_04_declare_description       |    3.2  |
| cat04_05_sql_filt_num_events       |    3    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    1    |
| cat05_01_hyp_generation_log        |    3.3  |
| cat05_02_hyp_gen_powl              |    4.2  |
| cat05_03_hyp_gen_declare           |    3.2  |
| cat05_04_hyp_gen_temp_profile      |    3.2  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    1    |
| cat05_07_question_interview        |    8.4  |
| cat06_01_bias_text                 |    6.2  |
| cat06_02_bias_event_log            |    5.2  |
| cat06_03_bias_powl                 |    7.1  |
| cat06_04_bias_two_logs             |    2    |
| cat06_05_bias_two_logs_2           |    7.1  |
| cat06_06_bias_mitigation_declare   |    4    |
| cat06_07_fair_unfair_powl          |    1.5  |
| cat08_01_queue_mining              |    1    |
| cat08_02_instance_spanning         |    3.2  |
| cat08_03_transport_opt             |    3.2  |
| cat08_04_resource_assign           |    7.05 |
| cat08_05_task_schedul              |    4.2  |



### ibmgranite41b-h   => 16.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    1    |
| cat01_02_activity_context          |    6    |
| cat01_03_high_level_events         |    3.5  |
| cat01_04_sensor_recordings         |    3.2  |
| cat01_05_merge_two_logs            |    3.2  |
| cat01_06_system_logs               |    1    |
| cat01_07_interv_to_pseudo_bpmn     |    3.2  |
| cat01_08_tables_to_log             |    2    |
| cat02_01_conformance_textual       |    1.5  |
| cat02_02_conf_desiderata           |    3.2  |
| cat02_03_anomaly_event_log         |    2.5  |
| cat02_04_powl_anomaly_detection    |    7.6  |
| cat02_05_two_powls_anomalies       |    3.2  |
| cat02_06_root_cause_1              |    4    |
| cat02_07_root_cause_2              |    1    |
| cat02_08_underfitting_process_tree |    1    |
| cat02_09_fix_process_tree          |    3    |
| cat03_01_process_tree_generation   |    1    |
| cat03_02_powl_generation           |    2.3  |
| cat03_03_log_skeleton_generation   |    1    |
| cat03_04_declare_generation        |    1    |
| cat03_05_temp_profile_generation   |    2    |
| cat03_06_petri_net_generation      |    1    |
| cat03_07_process_tree_discovery    |    1    |
| cat03_08_powl_discovery            |    2    |
| cat04_01_pseudo_bpmn_description   |    4.2  |
| cat04_02_pseudo_bpmn_open_question |    7.05 |
| cat04_03_declare_open_question     |    1    |
| cat04_04_declare_description       |    4.2  |
| cat04_05_sql_filt_num_events       |    1    |
| cat04_06_sql_filt_three_df         |    1    |
| cat04_07_sql_filt_top_k_vars       |    2    |
| cat05_01_hyp_generation_log        |    5    |
| cat05_02_hyp_gen_powl              |    4.2  |
| cat05_03_hyp_gen_declare           |    1.5  |
| cat05_04_hyp_gen_temp_profile      |    3.2  |
| cat05_05_question_gen_nlp          |   10    |
| cat05_06_question_pseudo_bpmn      |    2.8  |
| cat05_07_question_interview        |    6.2  |
| cat06_01_bias_text                 |    4.2  |
| cat06_02_bias_event_log            |    4.2  |
| cat06_03_bias_powl                 |    4.2  |
| cat06_04_bias_two_logs             |    3.2  |
| cat06_05_bias_two_logs_2           |    7.1  |
| cat06_06_bias_mitigation_declare   |    1.5  |
| cat06_07_fair_unfair_powl          |    3.2  |
| cat08_01_queue_mining              |    2.5  |
| cat08_02_instance_spanning         |    5.2  |
| cat08_03_transport_opt             |    4.2  |
| cat08_04_resource_assign           |    6.2  |
| cat08_05_task_schedul              |    6.2  |



### liquidlfm-2.2-6b   => 15.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     3.2 |
| cat01_03_high_level_events         |     7.1 |
| cat01_04_sensor_recordings         |     3.2 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     3.2 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     1.5 |
| cat02_04_powl_anomaly_detection    |     6.2 |
| cat02_05_two_powls_anomalies       |     1   |
| cat02_06_root_cause_1              |     3.2 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     1   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     7.1 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     3.2 |
| cat04_05_sql_filt_num_events       |     3.2 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     1.5 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     1.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     8.4 |
| cat05_07_question_interview        |     7.1 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     3.2 |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     1   |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     2   |
| cat08_01_queue_mining              |     3.2 |
| cat08_02_instance_spanning         |     5.5 |
| cat08_03_transport_opt             |     5.8 |
| cat08_04_resource_assign           |     6.8 |
| cat08_05_task_schedul              |     3.5 |



### gemma31b-it-q8_0   => 10.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     3.2 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     1   |
| cat02_06_root_cause_1              |     1.5 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     1.8 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     1   |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     3.2 |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     1.5 |
| cat05_04_hyp_gen_temp_profile      |     1.2 |
| cat05_05_question_gen_nlp          |    10   |
| cat05_06_question_pseudo_bpmn      |     8.4 |
| cat05_07_question_interview        |     1   |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     3.2 |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     1   |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     4.2 |
| cat08_02_instance_spanning         |     3.2 |
| cat08_03_transport_opt             |     2.5 |
| cat08_04_resource_assign           |     2.5 |
| cat08_05_task_schedul              |     1   |



### ibmgranite4350m-h   => 7.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     1   |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1.2 |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     3.2 |
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
| cat04_01_pseudo_bpmn_description   |     1.2 |
| cat04_02_pseudo_bpmn_open_question |     1   |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     3.2 |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     4   |
| cat05_06_question_pseudo_bpmn      |     3.5 |
| cat05_07_question_interview        |     2   |
| cat06_01_bias_text                 |     2   |
| cat06_02_bias_event_log            |     1   |
| cat06_03_bias_powl                 |     1   |
| cat06_04_bias_two_logs             |     1   |
| cat06_05_bias_two_logs_2           |     1   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |
| cat08_01_queue_mining              |     3.2 |
| cat08_02_instance_spanning         |     2.5 |
| cat08_03_transport_opt             |     1.5 |
| cat08_04_resource_assign           |     2.5 |
| cat08_05_task_schedul              |     4   |

