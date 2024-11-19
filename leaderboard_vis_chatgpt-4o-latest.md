A score in the range **27-33** is considered **sufficient**; a score in the range **33-45** is considered **good**; a score **>45** is considered **excellent**.

## Vision Leaderboard (1-shot; chatgpt-4o-latest used as a judge)

| Model                                   | Score(C1-C6)   | OS                 | PMI                  | DK                   | PMO                  | PQ                   | HG                   | FA                   | VI                   |
|:----------------------------------------|:---------------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| gemini-1.5-pro-002                      | **39.5**       | :x:                | :mage_woman: **8.7** | :mage_woman: **8.2** | :mage_woman: **6.2** | **6.2**              | **3.3**              | :mage_woman: **7.0** | **5.2**              |
| Gemini-1.5-Flash-002                    | **38.8**       | :x:                | 8.3                  | **8.1**              | **6.0**              | **6.0**              | **3.2**              | :mage_woman: **7.0** | 5.1                  |
| Gemini-Exp-1114-TEMP1                   | **38.5**       | :x:                | 7.8                  | 7.8                  | 5.8                  | :mage_woman: **6.3** | :mage_woman: **3.5** | :mage_woman: **7.0** | :mage_woman: **5.4** |
| chatgpt-4o-latest-2024-09-03            | **38.1**       | :x:                | 8.0                  | :mage_woman: **8.2** | 5.8                  | **6.1**              | **3.2**              | **6.8**              | **5.2**              |
| claude-3-5-sonnet-20241022              | **37.7**       | :x:                | **8.5**              | 7.5                  | 5.5                  | **6.0**              | **3.3**              | **6.8**              | **5.3**              |
| gpt-4o-2024-08-06                       | **37.1**       | :x:                | 8.2                  | **8.1**              | 5.6                  | 5.7                  | 3.1                  | 6.5                  | 5.0                  |
| Gemini-1.5-Flash-8B                     | **37.1**       | :x:                | 8.0                  | :mage_woman: **8.2** | 5.2                  | 5.8                  | **3.2**              | **6.7**              | 4.8                  |
| claude-3-5-sonnet-20240620              | **36.9**       | :x:                | 7.8                  | **7.9**              | 5.0                  | 5.8                  | **3.3**              | :mage_woman: **7.0** | **5.3**              |
| gpt-4o-2024-05-13                       | **36.2**       | :x:                | 7.9                  | **8.1**              | 5.1                  | 5.2                  | 3.1                  | **6.8**              | 4.5                  |
| pixtral-large-2411                      | **36.0**       | :white_check_mark: | 7.1                  | **8.1**              | 5.1                  | 5.8                  | 3.1                  | **6.8**              | 5.0                  |
| gpt-4-turbo-2024-04-09                  | **35.8**       | :x:                | 7.2                  | **8.0**              | 5.7                  | 5.3                  | 2.8                  | **6.7**              | **5.2**              |
| gpt-4o-mini-2024-07-18                  | **35.5**       | :x:                | 7.4                  | :mage_woman: **8.2** | 5.3                  | 5.2                  | 2.9                  | **6.7**              | 4.8                  |
| meta-llamaLlama-3.2-90B-Vision-Instruct | **35.2**       | :white_check_mark: | 7.7                  | 7.7                  | 4.8                  | 5.3                  | 3.1                  | 6.5                  | 4.0                  |
| claude-3-sonnet                         | **35.0**       | :x:                | 7.1                  | 7.8                  | 5.5                  | 5.3                  | 3.1                  | 6.2                  | 3.9                  |
| pixtral-12b-2409                        | **32.4**       | :white_check_mark: | 7.2                  | 7.8                  | 3.7                  | 5.5                  | 2.9                  | 5.3                  | 3.9                  |
| mistralaiPixtral-12B-2409               | **31.9**       | :white_check_mark: | 7.2                  | **8.1**              | 4.3                  | 4.2                  | 1.8                  | 6.4                  | 3.6                  |
| meta-llamaLlama-3.2-11B-Vision-Instruct | **25.9**       | :white_check_mark: | 6.0                  | 6.5                  | 2.9                  | 3.2                  | 2.0                  | 5.2                  | 3.6                  |
| QwenQwen2-VL-7B-Instruct                | **21.8**       | :white_check_mark: | 4.3                  | 6.0                  | 3.0                  | 3.0                  | 1.1                  | 4.3                  | 3.4                  |

### gemini-1.5-pro-002   => 44.8 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     8.5 |
| cat01_05_bpic2020_dfg_descr             |     8.5 |
| cat01_06_roadtraffic_dfg_descr          |     9   |
| cat01_07_ocel_container_description     |     9   |
| cat01_08_ocel_logistics_description     |     9   |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     9   |
| cat02_01_open_event_abstraction         |     9.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     8.5 |
| cat03_04_process_tree_generation        |     9   |
| cat03_05_powl_generation                |     7.5 |
| cat03_06_temp_profile_discovery         |     4.5 |
| cat03_07_declare_discovery              |     8.5 |
| cat03_08_log_skeleton_discovery         |     7   |
| cat04_01_bpmn_xml_tasks                 |    10   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     8.5 |
| cat04_05_declare_anomalies              |     8.5 |
| cat04_06_log_skeleton_description       |     8   |
| cat04_07_log_skeleton_anomalies         |     8.5 |
| cat05_01_hypothesis_bpic2020            |     9   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     9.5 |
| cat07_01_dotted_chart                   |     8.5 |
| cat07_02_perf_spectrum                  |     9   |
| cat07_03_running-example                |     8.5 |
| cat07_04_credit-score                   |     9   |
| cat07_05_dfg_ru                         |     9   |
| cat07_06_process_tree_ru                |     8.5 |



### Gemini-1.5-Flash-002   => 43.9 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     8.5 |
| cat01_04_roadtraffic_var_descr          |     9   |
| cat01_05_bpic2020_dfg_descr             |     9   |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     8   |
| cat01_08_ocel_logistics_description     |     9   |
| cat01_09_ocel_container_rca             |     7.5 |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9.5 |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     7.5 |
| cat03_05_powl_generation                |     9   |
| cat03_06_temp_profile_discovery         |     6   |
| cat03_07_declare_discovery              |     6.5 |
| cat03_08_log_skeleton_discovery         |     7   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9.5 |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     9   |
| cat04_05_declare_anomalies              |     8.5 |
| cat04_06_log_skeleton_description       |     8.5 |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     7   |
| cat05_02_hypothesis_roadtraffic         |     9   |
| cat05_03_hypothesis_bpmn_json           |     8.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     8.5 |
| cat06_03_lending_attributes             |     8.5 |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8.5 |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     9   |
| cat07_01_dotted_chart                   |     9   |
| cat07_02_perf_spectrum                  |     8   |
| cat07_03_running-example                |     7.5 |
| cat07_04_credit-score                   |     9   |
| cat07_05_dfg_ru                         |     9   |
| cat07_06_process_tree_ru                |     8.5 |



### Gemini-Exp-1114-TEMP1   => 43.9 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8.5 |
| cat01_02_variants_roadtraffic_anomalies |     7   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     6   |
| cat01_05_bpic2020_dfg_descr             |     7.5 |
| cat01_06_roadtraffic_dfg_descr          |     7.5 |
| cat01_07_ocel_container_description     |     8.5 |
| cat01_08_ocel_logistics_description     |     8.5 |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     8   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     7   |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     9   |
| cat03_04_process_tree_generation        |     7   |
| cat03_05_powl_generation                |     9   |
| cat03_06_temp_profile_discovery         |     7.5 |
| cat03_07_declare_discovery              |     4   |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9.5 |
| cat04_03_bpmn_simp_xml_description      |     9.5 |
| cat04_04_declare_description            |     9   |
| cat04_05_declare_anomalies              |     8   |
| cat04_06_log_skeleton_description       |     9.5 |
| cat04_07_log_skeleton_anomalies         |     9   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     9   |
| cat05_03_hypothesis_bpmn_json           |     9.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     9   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     8.5 |
| cat06_08_hospital_prot_comp             |     9   |
| cat07_01_dotted_chart                   |     9   |
| cat07_02_perf_spectrum                  |     9   |
| cat07_03_running-example                |     8.5 |
| cat07_04_credit-score                   |     9   |
| cat07_05_dfg_ru                         |     9   |
| cat07_06_process_tree_ru                |     9.5 |



### chatgpt-4o-latest-2024-09-03   => 43.3 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8.5 |
| cat01_02_variants_roadtraffic_anomalies |     7.5 |
| cat01_03_bpic2020_var_descr             |     9   |
| cat01_04_roadtraffic_var_descr          |     7   |
| cat01_05_bpic2020_dfg_descr             |     9   |
| cat01_06_roadtraffic_dfg_descr          |     7.5 |
| cat01_07_ocel_container_description     |     7.5 |
| cat01_08_ocel_logistics_description     |     9   |
| cat01_09_ocel_container_rca             |     7.5 |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9.5 |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9.5 |
| cat02_09_closed_petri_nets              |     8.5 |
| cat03_01_temp_profile_generation        |     6.5 |
| cat03_02_declare_generation             |     6.5 |
| cat03_03_log_skeleton_generation        |     9.5 |
| cat03_04_process_tree_generation        |     7   |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     7   |
| cat03_07_declare_discovery              |     8   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9.5 |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     9   |
| cat04_05_declare_anomalies              |     8.5 |
| cat04_06_log_skeleton_description       |     9   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     8.5 |
| cat05_02_hypothesis_roadtraffic         |     8.5 |
| cat05_03_hypothesis_bpmn_json           |     8.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     7   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     8.5 |
| cat06_07_lending_prot_comp              |     7.5 |
| cat06_08_hospital_prot_comp             |     9   |
| cat07_01_dotted_chart                   |     8.5 |
| cat07_02_perf_spectrum                  |     9   |
| cat07_03_running-example                |     8   |
| cat07_04_credit-score                   |     9   |
| cat07_05_dfg_ru                         |     8.5 |
| cat07_06_process_tree_ru                |     9   |



### claude-3-5-sonnet-20241022   => 43.0 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8   |
| cat01_02_variants_roadtraffic_anomalies |     7.5 |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     9   |
| cat01_05_bpic2020_dfg_descr             |     8.5 |
| cat01_06_roadtraffic_dfg_descr          |     8.5 |
| cat01_07_ocel_container_description     |     8.5 |
| cat01_08_ocel_logistics_description     |     9.5 |
| cat01_09_ocel_container_rca             |     8.5 |
| cat01_10_ocel_logistics_rca             |     9   |
| cat02_01_open_event_abstraction         |     7.5 |
| cat02_02_open_process_cubes             |     7.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     6.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     8.5 |
| cat03_04_process_tree_generation        |     8   |
| cat03_05_powl_generation                |     9   |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     4   |
| cat03_08_log_skeleton_discovery         |     6.5 |
| cat04_01_bpmn_xml_tasks                 |    10   |
| cat04_02_bpmn_json_description          |     9.5 |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     8.5 |
| cat04_06_log_skeleton_description       |     8.5 |
| cat04_07_log_skeleton_anomalies         |     8   |
| cat05_01_hypothesis_bpic2020            |     9   |
| cat05_02_hypothesis_roadtraffic         |     6   |
| cat05_03_hypothesis_bpmn_json           |     9   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     9   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     7.5 |
| cat06_07_lending_prot_comp              |     8.5 |
| cat06_08_hospital_prot_comp             |     8.5 |
| cat07_01_dotted_chart                   |     8   |
| cat07_02_perf_spectrum                  |     9   |
| cat07_03_running-example                |     9   |
| cat07_04_credit-score                   |     9   |
| cat07_05_dfg_ru                         |     9   |
| cat07_06_process_tree_ru                |     9   |



### gpt-4o-2024-08-06   => 42.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8.5 |
| cat01_02_variants_roadtraffic_anomalies |     7.5 |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     8.5 |
| cat01_05_bpic2020_dfg_descr             |     8.5 |
| cat01_06_roadtraffic_dfg_descr          |     9   |
| cat01_07_ocel_container_description     |     8.5 |
| cat01_08_ocel_logistics_description     |     8   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     8.5 |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     8   |
| cat03_05_powl_generation                |     9   |
| cat03_06_temp_profile_discovery         |     7   |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     8.5 |
| cat04_02_bpmn_json_description          |     8.5 |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     9   |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     8   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     7   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     8.5 |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     8   |
| cat06_08_hospital_prot_comp             |     8   |
| cat07_01_dotted_chart                   |     8.5 |
| cat07_02_perf_spectrum                  |     8.5 |
| cat07_03_running-example                |     8   |
| cat07_04_credit-score                   |     8.5 |
| cat07_05_dfg_ru                         |     7.5 |
| cat07_06_process_tree_ru                |     9.5 |



### Gemini-1.5-Flash-8B   => 42.0 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     8.5 |
| cat01_04_roadtraffic_var_descr          |     6.5 |
| cat01_05_bpic2020_dfg_descr             |     9   |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     8   |
| cat01_09_ocel_container_rca             |     8   |
| cat01_10_ocel_logistics_rca             |     8   |
| cat02_01_open_event_abstraction         |    10   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     7.5 |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     6.5 |
| cat03_04_process_tree_generation        |     7   |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     5   |
| cat03_07_declare_discovery              |     8   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     7.5 |
| cat04_05_declare_anomalies              |     9   |
| cat04_06_log_skeleton_description       |     8   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     8.5 |
| cat05_02_hypothesis_roadtraffic         |     6   |
| cat05_03_hypothesis_bpmn_json           |     9   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8.5 |
| cat06_01_renting_attributes             |     8.5 |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     8.5 |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     6.5 |
| cat07_01_dotted_chart                   |     8   |
| cat07_02_perf_spectrum                  |     6.5 |
| cat07_03_running-example                |     9   |
| cat07_04_credit-score                   |     8.5 |
| cat07_05_dfg_ru                         |     8.5 |
| cat07_06_process_tree_ru                |     8   |



### claude-3-5-sonnet-20240620   => 42.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8.5 |
| cat01_02_variants_roadtraffic_anomalies |     8.5 |
| cat01_03_bpic2020_var_descr             |     8.5 |
| cat01_04_roadtraffic_var_descr          |     8.5 |
| cat01_05_bpic2020_dfg_descr             |     7   |
| cat01_06_roadtraffic_dfg_descr          |     7.5 |
| cat01_07_ocel_container_description     |     6.5 |
| cat01_08_ocel_logistics_description     |     7   |
| cat01_09_ocel_container_rca             |     8   |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     8   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9.5 |
| cat04_03_bpmn_simp_xml_description      |     9.5 |
| cat04_04_declare_description            |     7.5 |
| cat04_05_declare_anomalies              |     9   |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     8.5 |
| cat05_03_hypothesis_bpmn_json           |     8.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     8.5 |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     9.5 |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     8.5 |
| cat06_08_hospital_prot_comp             |     9   |
| cat07_01_dotted_chart                   |     9   |
| cat07_02_perf_spectrum                  |     8.5 |
| cat07_03_running-example                |     9   |
| cat07_04_credit-score                   |     9.5 |
| cat07_05_dfg_ru                         |     9   |
| cat07_06_process_tree_ru                |     8   |



### gpt-4o-2024-05-13   => 40.8 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     9   |
| cat01_04_roadtraffic_var_descr          |     9   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     6   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     7.5 |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     6.5 |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9.5 |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     7   |
| cat03_05_powl_generation                |     7.5 |
| cat03_06_temp_profile_discovery         |     5   |
| cat03_07_declare_discovery              |     6   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     7   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     6   |
| cat04_06_log_skeleton_description       |     8   |
| cat04_07_log_skeleton_anomalies         |     6.5 |
| cat05_01_hypothesis_bpic2020            |     7.5 |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     8   |
| cat07_01_dotted_chart                   |     9   |
| cat07_02_perf_spectrum                  |     9   |
| cat07_03_running-example                |     9   |
| cat07_04_credit-score                   |     9.5 |
| cat07_05_dfg_ru                         |     8   |
| cat07_06_process_tree_ru                |     1   |



### pixtral-large-2411   => 41.0 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7.5 |
| cat01_02_variants_roadtraffic_anomalies |     7   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     7.5 |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     7   |
| cat01_07_ocel_container_description     |     5.5 |
| cat01_08_ocel_logistics_description     |     7   |
| cat01_09_ocel_container_rca             |     7.5 |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     6   |
| cat03_03_log_skeleton_generation        |     7.5 |
| cat03_04_process_tree_generation        |     7.5 |
| cat03_05_powl_generation                |     6   |
| cat03_06_temp_profile_discovery         |     7   |
| cat03_07_declare_discovery              |     4   |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     8.5 |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     8.5 |
| cat04_06_log_skeleton_description       |     7.5 |
| cat04_07_log_skeleton_anomalies         |     8.5 |
| cat05_01_hypothesis_bpic2020            |     7   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     7.5 |
| cat06_08_hospital_prot_comp             |     6.5 |
| cat07_01_dotted_chart                   |     7.5 |
| cat07_02_perf_spectrum                  |     7   |
| cat07_03_running-example                |     8.5 |
| cat07_04_credit-score                   |     8.5 |
| cat07_05_dfg_ru                         |    10   |
| cat07_06_process_tree_ru                |     8.5 |



### gpt-4-turbo-2024-04-09   => 41.0 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7.5 |
| cat01_02_variants_roadtraffic_anomalies |     4   |
| cat01_03_bpic2020_var_descr             |     9   |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     8.5 |
| cat01_07_ocel_container_description     |     8.5 |
| cat01_08_ocel_logistics_description     |     5   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9.5 |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     8   |
| cat03_05_powl_generation                |     4   |
| cat03_06_temp_profile_discovery         |     7.5 |
| cat03_07_declare_discovery              |     7   |
| cat03_08_log_skeleton_discovery         |     7   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     8.5 |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     6.5 |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     9   |
| cat05_03_hypothesis_bpmn_json           |     8.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     2.5 |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     8.5 |
| cat06_08_hospital_prot_comp             |     8   |
| cat07_01_dotted_chart                   |     8.5 |
| cat07_02_perf_spectrum                  |     9   |
| cat07_03_running-example                |     9.5 |
| cat07_04_credit-score                   |     9   |
| cat07_05_dfg_ru                         |     8   |
| cat07_06_process_tree_ru                |     8.5 |



### gpt-4o-mini-2024-07-18   => 40.4 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8.5 |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     9   |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     9   |
| cat01_06_roadtraffic_dfg_descr          |     6   |
| cat01_07_ocel_container_description     |     4   |
| cat01_08_ocel_logistics_description     |     7.5 |
| cat01_09_ocel_container_rca             |     8   |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     8.5 |
| cat03_04_process_tree_generation        |     4   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     4   |
| cat03_07_declare_discovery              |     7   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     7.5 |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     8   |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     5   |
| cat05_01_hypothesis_bpic2020            |     7.5 |
| cat05_02_hypothesis_roadtraffic         |     8.5 |
| cat05_03_hypothesis_bpmn_json           |     4.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     7.5 |
| cat06_08_hospital_prot_comp             |     8   |
| cat07_01_dotted_chart                   |     8   |
| cat07_02_perf_spectrum                  |     8.5 |
| cat07_03_running-example                |     6   |
| cat07_04_credit-score                   |     8   |
| cat07_05_dfg_ru                         |     9   |
| cat07_06_process_tree_ru                |     8.5 |



### meta-llamaLlama-3.2-90B-Vision-Instruct   => 39.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8   |
| cat01_02_variants_roadtraffic_anomalies |     6   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     6.5 |
| cat01_05_bpic2020_dfg_descr             |     8.5 |
| cat01_06_roadtraffic_dfg_descr          |     8.5 |
| cat01_07_ocel_container_description     |     8.5 |
| cat01_08_ocel_logistics_description     |     6.5 |
| cat01_09_ocel_container_rca             |     8.5 |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     8   |
| cat02_02_open_process_cubes             |     6.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     7.5 |
| cat03_04_process_tree_generation        |     7.5 |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     6   |
| cat03_08_log_skeleton_discovery         |     2   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     8.5 |
| cat04_05_declare_anomalies              |     7.5 |
| cat04_06_log_skeleton_description       |     4   |
| cat04_07_log_skeleton_anomalies         |     7.5 |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     7.5 |
| cat05_03_hypothesis_bpmn_json           |     7.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8.5 |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     6   |
| cat07_01_dotted_chart                   |     8   |
| cat07_02_perf_spectrum                  |     5.5 |
| cat07_03_running-example                |     5   |
| cat07_04_credit-score                   |     7   |
| cat07_05_dfg_ru                         |     6   |
| cat07_06_process_tree_ru                |     8   |



### claude-3-sonnet   => 38.9 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8   |
| cat01_02_variants_roadtraffic_anomalies |     5.5 |
| cat01_03_bpic2020_var_descr             |     7.5 |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     7   |
| cat01_06_roadtraffic_dfg_descr          |     6   |
| cat01_07_ocel_container_description     |     7.5 |
| cat01_08_ocel_logistics_description     |     7   |
| cat01_09_ocel_container_rca             |     8.5 |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     7   |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     9   |
| cat03_04_process_tree_generation        |     8   |
| cat03_05_powl_generation                |     7.5 |
| cat03_06_temp_profile_discovery         |     3.5 |
| cat03_07_declare_discovery              |     4   |
| cat03_08_log_skeleton_discovery         |     8   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     5.5 |
| cat05_01_hypothesis_bpic2020            |     7.5 |
| cat05_02_hypothesis_roadtraffic         |     7.5 |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8.5 |
| cat06_01_renting_attributes             |     8.5 |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     5   |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     8   |
| cat06_08_hospital_prot_comp             |     7   |
| cat07_01_dotted_chart                   |     8.5 |
| cat07_02_perf_spectrum                  |     7   |
| cat07_03_running-example                |     1.5 |
| cat07_04_credit-score                   |     7.5 |
| cat07_05_dfg_ru                         |     7   |
| cat07_06_process_tree_ru                |     7.5 |



### pixtral-12b-2409   => 36.2 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8.5 |
| cat01_02_variants_roadtraffic_anomalies |     6   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     8.5 |
| cat01_05_bpic2020_dfg_descr             |     8.5 |
| cat01_06_roadtraffic_dfg_descr          |     7   |
| cat01_07_ocel_container_description     |     6   |
| cat01_08_ocel_logistics_description     |     7   |
| cat01_09_ocel_container_rca             |     6   |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     7   |
| cat03_02_declare_generation             |     5   |
| cat03_03_log_skeleton_generation        |     7.5 |
| cat03_04_process_tree_generation        |     2   |
| cat03_05_powl_generation                |     7.5 |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     1   |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     6   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     8   |
| cat04_07_log_skeleton_anomalies         |     8   |
| cat05_01_hypothesis_bpic2020            |     7   |
| cat05_02_hypothesis_roadtraffic         |     7.5 |
| cat05_03_hypothesis_bpmn_json           |     6   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     8.5 |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     6   |
| cat06_06_hiring_prot_comp               |     4   |
| cat06_07_lending_prot_comp              |     4   |
| cat06_08_hospital_prot_comp             |     4   |
| cat07_01_dotted_chart                   |     8   |
| cat07_03_running-example                |     6.5 |
| cat07_04_credit-score                   |     9   |
| cat07_05_dfg_ru                         |     8.5 |
| cat07_06_process_tree_ru                |     7   |



### mistralaiPixtral-12B-2409   => 35.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7.5 |
| cat01_02_variants_roadtraffic_anomalies |     4   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     9   |
| cat01_05_bpic2020_dfg_descr             |     6   |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     7.5 |
| cat01_08_ocel_logistics_description     |     6   |
| cat01_09_ocel_container_rca             |     8.5 |
| cat01_10_ocel_logistics_rca             |     8   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     4   |
| cat03_02_declare_generation             |     6.5 |
| cat03_03_log_skeleton_generation        |     9   |
| cat03_04_process_tree_generation        |     7.5 |
| cat03_05_powl_generation                |     6   |
| cat03_06_temp_profile_discovery         |     1.5 |
| cat03_07_declare_discovery              |     3.5 |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     1   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     8   |
| cat04_06_log_skeleton_description       |     8   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     7.5 |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     1   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     1   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     7   |
| cat06_06_hiring_prot_comp               |     5   |
| cat06_07_lending_prot_comp              |     8.5 |
| cat06_08_hospital_prot_comp             |     8.5 |
| cat07_01_dotted_chart                   |     5.5 |
| cat07_03_running-example                |     7.5 |
| cat07_04_credit-score                   |     8.5 |
| cat07_05_dfg_ru                         |     8.5 |
| cat07_06_process_tree_ru                |     6.5 |



### meta-llamaLlama-3.2-11B-Vision-Instruct   => 29.5 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     2.5 |
| cat01_02_variants_roadtraffic_anomalies |     3   |
| cat01_03_bpic2020_var_descr             |     7.5 |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     4   |
| cat01_08_ocel_logistics_description     |     4   |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     8   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     5.5 |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     8   |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     1   |
| cat03_01_temp_profile_generation        |     4   |
| cat03_02_declare_generation             |     4   |
| cat03_03_log_skeleton_generation        |     3.5 |
| cat03_04_process_tree_generation        |     2   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     2   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     8.5 |
| cat04_02_bpmn_json_description          |     4   |
| cat04_03_bpmn_simp_xml_description      |     5   |
| cat04_04_declare_description            |     5   |
| cat04_05_declare_anomalies              |     2   |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     2   |
| cat05_01_hypothesis_bpic2020            |     7.5 |
| cat05_02_hypothesis_roadtraffic         |     2   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     3   |
| cat06_01_renting_attributes             |     8.5 |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     4   |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     3   |
| cat06_08_hospital_prot_comp             |     5   |
| cat07_01_dotted_chart                   |     6.5 |
| cat07_02_perf_spectrum                  |     3   |
| cat07_03_running-example                |     6   |
| cat07_04_credit-score                   |     7.5 |
| cat07_05_dfg_ru                         |     7   |
| cat07_06_process_tree_ru                |     6   |



### QwenQwen2-VL-7B-Instruct   => 25.2 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     3   |
| cat01_02_variants_roadtraffic_anomalies |     3   |
| cat01_03_bpic2020_var_descr             |     5.5 |
| cat01_04_roadtraffic_var_descr          |     4   |
| cat01_05_bpic2020_dfg_descr             |     5   |
| cat01_06_roadtraffic_dfg_descr          |     4   |
| cat01_07_ocel_container_description     |     6   |
| cat01_08_ocel_logistics_description     |     3   |
| cat01_09_ocel_container_rca             |     4   |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     8   |
| cat02_02_open_process_cubes             |     6.5 |
| cat02_03_open_decomposition_strategies  |     8   |
| cat02_04_open_trace_clustering          |     7   |
| cat02_05_open_rpa                       |     8   |
| cat02_06_open_anomaly_detection         |     8   |
| cat02_07_open_process_enhancement       |     8   |
| cat02_08_closed_process_mining          |     4   |
| cat02_09_closed_petri_nets              |     3   |
| cat03_01_temp_profile_generation        |     3   |
| cat03_02_declare_generation             |     3   |
| cat03_03_log_skeleton_generation        |     7.5 |
| cat03_04_process_tree_generation        |     6   |
| cat03_05_powl_generation                |     4   |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     1   |
| cat03_08_log_skeleton_discovery         |     2   |
| cat04_01_bpmn_xml_tasks                 |     6   |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     7.5 |
| cat04_04_declare_description            |     3   |
| cat04_05_declare_anomalies              |     2   |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     4   |
| cat05_01_hypothesis_bpic2020            |     3   |
| cat05_02_hypothesis_roadtraffic         |     3   |
| cat05_03_hypothesis_bpmn_json           |     1   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     4.5 |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     7   |
| cat06_03_lending_attributes             |     5   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     2   |
| cat06_06_hiring_prot_comp               |     3   |
| cat06_07_lending_prot_comp              |     7   |
| cat06_08_hospital_prot_comp             |     3.5 |
| cat07_01_dotted_chart                   |     7   |
| cat07_02_perf_spectrum                  |     1   |
| cat07_03_running-example                |     4   |
| cat07_04_credit-score                   |     9   |
| cat07_05_dfg_ru                         |     6.5 |
| cat07_06_process_tree_ru                |     6.5 |

