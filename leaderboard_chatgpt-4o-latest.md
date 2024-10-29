## Leaderboard (1-shot; chatgpt-4o-latest used as a judge)

Overall leaderboard (a score in the range **27-34** is considered **sufficient**; a score in the range **34-45** is considered **good**; a score **>45** is considered **excellent**):

| Model                        | Overall Score        |
|:-----------------------------|:---------------------|
| gemini-1.5-pro-002           | 44.1 (38.9 on C1-C6) |
| Gemini-1.5-Flash-002         | 43.9 (38.8 on C1-C6) |
| chatgpt-4o-latest-2024-09-03 | 42.6 (38.1 on C1-C6) |
| claude-3-5-sonnet-20241022   | 43.0 (37.7 on C1-C6) |
| Gemini-1.5-Flash-8B          | 42.0 (37.1 on C1-C6) |
| claude-3-5-sonnet-20240620   | 42.1 (36.9 on C1-C6) |
| claude-3-sonnet              | 38.9 (35.0 on C1-C6) |
| gpt-3.5-turbo                | 31.3                 |
| gemma29b-instruct-q6_K       | 24.2                 |
| codegemma7b-instruct-q6_K    | 18.6                 |

### gemini-1.5-pro-002   => 44.1 (/52) points

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
| cat05_02_hypothesis_roadtraffic         |     1   |
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



### chatgpt-4o-latest-2024-09-03   => 42.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     9   |
| cat01_03_bpic2020_var_descr             |     8.5 |
| cat01_04_roadtraffic_var_descr          |     9.5 |
| cat01_05_bpic2020_dfg_descr             |     9   |
| cat01_06_roadtraffic_dfg_descr          |     8.5 |
| cat01_07_ocel_container_description     |     6.5 |
| cat01_08_ocel_logistics_description     |     8   |
| cat01_09_ocel_container_rca             |     8   |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     8.5 |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     7.5 |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     4   |
| cat03_07_declare_discovery              |     9   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |    10   |
| cat04_02_bpmn_json_description          |     9.5 |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     7.5 |
| cat04_05_declare_anomalies              |     6   |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     9   |
| cat05_01_hypothesis_bpic2020            |     9   |
| cat05_02_hypothesis_roadtraffic         |     8.5 |
| cat05_03_hypothesis_bpmn_json           |     6.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     9.5 |
| cat06_07_lending_prot_comp              |     9.5 |
| cat06_08_hospital_prot_comp             |     9.2 |
| cat07_01_dotted_chart                   |     1   |
| cat07_02_perf_spectrum                  |     9   |
| cat07_03_running-example                |     9   |
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



### gpt-3.5-turbo   => 31.3 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8   |
| cat01_02_variants_roadtraffic_anomalies |     4   |
| cat01_03_bpic2020_var_descr             |     6.5 |
| cat01_04_roadtraffic_var_descr          |     7   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     7   |
| cat01_07_ocel_container_description     |     8.5 |
| cat01_08_ocel_logistics_description     |     6   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     9   |
| cat02_01_open_event_abstraction         |     8   |
| cat02_02_open_process_cubes             |     7   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8   |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     4   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     6   |
| cat03_03_log_skeleton_generation        |     7.5 |
| cat03_04_process_tree_generation        |     6.5 |
| cat03_05_powl_generation                |     3   |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     4   |
| cat03_08_log_skeleton_discovery         |     2   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     8.5 |
| cat04_04_declare_description            |     4   |
| cat04_05_declare_anomalies              |     3   |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     6   |
| cat05_01_hypothesis_bpic2020            |     9   |
| cat05_02_hypothesis_roadtraffic         |     7.5 |
| cat05_03_hypothesis_bpmn_json           |     6   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9.5 |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     7   |
| cat06_06_hiring_prot_comp               |     3   |
| cat06_07_lending_prot_comp              |     7.5 |
| cat06_08_hospital_prot_comp             |     4   |



### gemma29b-instruct-q6_K   => 24.2 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     5.5 |
| cat01_02_variants_roadtraffic_anomalies |     2   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     7   |
| cat01_06_roadtraffic_dfg_descr          |     7.5 |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     2   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     1   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     7.5 |
| cat03_04_process_tree_generation        |     8.5 |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     1   |
| cat03_07_declare_discovery              |     1   |
| cat03_08_log_skeleton_discovery         |     1   |
| cat04_01_bpmn_xml_tasks                 |     1   |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     1   |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     3   |
| cat04_06_log_skeleton_description       |     2   |
| cat04_07_log_skeleton_anomalies         |     3   |
| cat05_01_hypothesis_bpic2020            |     9   |
| cat05_02_hypothesis_roadtraffic         |     2   |
| cat05_03_hypothesis_bpmn_json           |     1   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     1   |
| cat06_01_renting_attributes             |     4   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     7   |
| cat06_04_hospital_attributes            |     1   |
| cat06_05_renting_prot_comp              |     5   |
| cat06_06_hiring_prot_comp               |     1   |
| cat06_07_lending_prot_comp              |     4   |
| cat06_08_hospital_prot_comp             |     4   |



### codegemma7b-instruct-q6_K   => 18.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     3   |
| cat01_02_variants_roadtraffic_anomalies |     2.5 |
| cat01_03_bpic2020_var_descr             |     5   |
| cat01_04_roadtraffic_var_descr          |     3   |
| cat01_05_bpic2020_dfg_descr             |     6.5 |
| cat01_06_roadtraffic_dfg_descr          |     2   |
| cat01_07_ocel_container_description     |     2   |
| cat01_08_ocel_logistics_description     |     2   |
| cat01_09_ocel_container_rca             |     3   |
| cat01_10_ocel_logistics_rca             |     1   |
| cat02_01_open_event_abstraction         |     7.5 |
| cat02_02_open_process_cubes             |     7   |
| cat02_03_open_decomposition_strategies  |     8   |
| cat02_04_open_trace_clustering          |     7   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     7.5 |
| cat02_07_open_process_enhancement       |     7.5 |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     6   |
| cat03_01_temp_profile_generation        |     7.5 |
| cat03_02_declare_generation             |     1   |
| cat03_03_log_skeleton_generation        |     6   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     6   |
| cat03_06_temp_profile_discovery         |     1   |
| cat03_07_declare_discovery              |     2   |
| cat03_08_log_skeleton_discovery         |     1   |
| cat04_01_bpmn_xml_tasks                 |     1   |
| cat04_02_bpmn_json_description          |     3   |
| cat04_03_bpmn_simp_xml_description      |     1   |
| cat04_04_declare_description            |     4.5 |
| cat04_05_declare_anomalies              |     4   |
| cat04_06_log_skeleton_description       |     3   |
| cat04_07_log_skeleton_anomalies         |     3   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     1   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     1   |
| cat06_01_renting_attributes             |     4   |
| cat06_02_hiring_attributes              |     3   |
| cat06_03_lending_attributes             |     3   |
| cat06_04_hospital_attributes            |     3   |
| cat06_05_renting_prot_comp              |     2   |
| cat06_06_hiring_prot_comp               |     3   |
| cat06_07_lending_prot_comp              |     1   |
| cat06_08_hospital_prot_comp             |     4   |

