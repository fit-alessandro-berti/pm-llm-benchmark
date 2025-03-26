A score in the range **25-30** is considered **sufficient**; a score in the range **30-35** is considered **good**; and a score **>35** is considered **excellent**.


**As of 2025-01-26, the chain of thought of Large Reasoning Models, if provided, is considered in the assessment of answers.**

## Overall Leaderboard (1-shot; gemini-2.5-pro-exp-03-25 used as a judge)

| Model             | Avg     | Score    | OS   | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:------------------|:--------|:---------|:-----|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| o1-pro-2024-12-17 | **7.3** | **33.7** | :x:  | :mage_woman: **5.9** | :mage_woman: **7.7** | :mage_woman: **4.5** | :mage_woman: **5.0** | :mage_woman: **5.5** | :mage_woman: **5.2** | :mage_woman: **5.6** |
| ministral-3b-2410 | **4.1** | **18.6** | :x:  | 2.9                  | 3.4                  | 2.0                  | 3.3                  | 3.7                  | 3.4                  | 0.0                  |

### o1-pro-2024-12-17   => 33.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     9.2 |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     9   |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     6   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     8.8 |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     9   |
| cat02_06_root_cause_1              |     9.2 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     6.5 |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     9   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     8.7 |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     5   |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     8.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     8.8 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     9.5 |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |    10   |
| cat07_03_bpmn_dispatch             |     8.5 |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     9.8 |
| cat07_06_perf_spectrum             |     9.8 |



### ministral-3b-2410   => 18.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     2   |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     5.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8.7 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     7   |
| cat06_02_bias_event_log            |     3   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     3   |

