A score in the range **27-33** is considered **sufficient**; a score in the range **33-39** is considered **good**; a score **>39** is considered **excellent**.

## Overall Leaderboard (1-shot; gpt-4o-2024-11-20 used as a judge)

| Model                  | Score    | OS   | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:-----------------------|:---------|:-----|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| o1-2024-12-05          | **22.9** | :x:  | 5.4                  | 6.8                  | **4.8**              | :mage_woman: **5.8** | :mage_woman: **0.0** | :mage_woman: **0.0** | :mage_woman: **0.0** |
| gpt-4o-2024-11-20      | **22.5** | :x:  | 5.0                  | :mage_woman: **7.5** | :mage_woman: **5.0** | 5.1                  | :mage_woman: **0.0** | :mage_woman: **0.0** | :mage_woman: **0.0** |
| o1-mini-2024-09-12     | **21.1** | :x:  | :mage_woman: **5.8** | 6.2                  | 4.0                  | 5.2                  | :mage_woman: **0.0** | :mage_woman: **0.0** | :mage_woman: **0.0** |
| gpt-4o-mini-2024-07-18 | **20.2** | :x:  | 4.1                  | 6.3                  | **4.7**              | 5.0                  | :mage_woman: **0.0** | :mage_woman: **0.0** | :mage_woman: **0.0** |
| gemini-1.5-pro-002     | **20.1** | :x:  | **5.5**              | 6.2                  | 3.7                  | 4.8                  | :mage_woman: **0.0** | :mage_woman: **0.0** | :mage_woman: **0.0** |
| gpt-3.5-turbo          | **17.1** | :x:  | 4.7                  | 6.3                  | 2.2                  | 4.0                  | :mage_woman: **0.0** | :mage_woman: **0.0** | :mage_woman: **0.0** |

### o1-2024-12-05   => 22.9 (/52) points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     9.2 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     8   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     7.5 |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     5.5 |
| cat02_06_root_cause_1              |     9   |
| cat02_07_root_cause_2              |     7   |
| cat02_08_underfitting_process_tree |     6.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     7.5 |
| cat03_03_log_skeleton_generation   |     7.5 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     7   |
| cat03_07_process_tree_discovery    |     8.5 |
| cat03_08_powl_discovery            |     5   |
| cat04_01_pseudo_bpmn_description   |     8.5 |
| cat04_02_pseudo_bpmn_open_question |     8.5 |
| cat04_03_declare_open_question     |     9   |
| cat04_04_declare_description       |     8.5 |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     6.5 |
| cat04_07_sql_filt_top_k_vars       |     8   |



### gpt-4o-2024-11-20   => 22.5 (/52) points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     8.5 |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     7   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     8.5 |
| cat02_02_conf_desiderata           |     8.5 |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     8   |
| cat02_07_root_cause_2              |     8.5 |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     5   |
| cat03_02_powl_generation           |     5   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     6.5 |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     7.5 |
| cat03_07_process_tree_discovery    |     8   |
| cat03_08_powl_discovery            |     8   |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     9.2 |
| cat04_03_declare_open_question     |     9   |
| cat04_04_declare_description       |     6.5 |
| cat04_05_sql_filt_num_events       |     7   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     7   |



### o1-mini-2024-09-12   => 21.1 (/52) points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     8.5 |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     7.5 |
| cat01_08_tables_to_log             |     5.5 |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     5   |
| cat02_03_anomaly_event_log         |     5   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     8.5 |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     5   |
| cat03_03_log_skeleton_generation   |     5   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     7   |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     9.4 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     8   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     6   |



### gpt-4o-mini-2024-07-18   => 20.2 (/52) points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     8   |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     6.5 |
| cat02_03_anomaly_event_log         |     7   |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     6.5 |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     7.5 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     6.5 |
| cat03_02_powl_generation           |     3.5 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     6.5 |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     6   |
| cat03_07_process_tree_discovery    |     6.5 |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     8   |
| cat04_03_declare_open_question     |     7   |
| cat04_04_declare_description       |     7.5 |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     8   |



### gemini-1.5-pro-002   => 20.1 (/52) points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     8   |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     3.5 |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     5   |
| cat02_05_two_powls_anomalies       |     8.5 |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     7.5 |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     4.5 |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     8.5 |
| cat03_08_powl_discovery            |     4.5 |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     8   |
| cat04_04_declare_description       |     7.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     5   |
| cat04_07_sql_filt_top_k_vars       |     4   |



### gpt-3.5-turbo   => 17.1 (/52) points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |     5.5 |
| cat02_02_conf_desiderata           |     7.5 |
| cat02_03_anomaly_event_log         |     7   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     4.5 |
| cat03_02_powl_generation           |     3.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     4   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     8.5 |
| cat04_03_declare_open_question     |     7.5 |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     4   |
| cat04_07_sql_filt_top_k_vars       |     4   |

