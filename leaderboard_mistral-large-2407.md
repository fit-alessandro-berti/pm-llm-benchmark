## Leaderboard (1-shot, mistral-large-2407 as a judge)

Overall leaderboard (a score in the range **27-34** is considered **sufficient**; a score in the range **34-45** is considered **good**; a score **>45** is considered **excellent**):


| Model                                               | Context Length | Score (C1-C6) |
|-----------------------------------------------------|----------------|---------------|
| gpt-4o-20240513                                     | 128K           | 41.6          |
| Mistral Large 2 123B (20240724, fp16 quantization)  | 128K           | 40.3          |


### Commercial models

#### gpt-4o-20240513 => 41,6 (/46) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 8.5   |
| cat01_02_variants_roadtraffic_anomalies| 8.5   |
| cat01_03_bpic2020_var_descr            | 10.0  |
| cat01_04_roadtraffic_var_descr         | 9.5   |
| cat01_05_bpic2020_dfg_descr            | 9.1   |
| cat01_06_roadtraffic_dfg_descr         | 8.5   |
| cat01_07_ocel_container_description    | 8.5   |
| cat01_08_ocel_logistics_description    | 8.5   |
| cat01_09_ocel_container_rca            | 9.0   |
| cat01_10_ocel_logistics_rca            | 8.5   |
| cat02_01_open_event_abstraction        | 9.0   |
| cat02_02_open_process_cubes            | 5.9   |
| cat02_03_open_decomposition_strategies | 9.5   |
| cat02_04_open_trace_clustering         | 9.0   |
| cat02_05_open_rpa                      | 10.0  |
| cat02_06_open_anomaly_detection        | 10.0  |
| cat02_07_open_process_enhancement      | 9.0   |
| cat02_08_closed_process_mining         | 9.2   |
| cat02_09_closed_petri_nets             | 9.0   |
| cat03_01_temp_profile_generation       | 9.5   |
| cat03_02_declare_generation            | 9.0   |
| cat03_03_log_skeleton_generation       | 10.0  |
| cat03_04_process_tree_generation       | 9.0   |
| cat03_05_powl_generation               | 9.0   |
| cat03_06_temp_profile_discovery        | 8.0   |
| cat03_07_declare_discovery             | 8.5   |
| cat03_08_log_skeleton_discovery        | 8.4   |
| cat04_01_bpmn_xml_tasks                | 9.5   |
| cat04_02_bpmn_json_description         | 9.5   |
| cat04_03_bpmn_simp_xml_description     | 9.5   |
| cat04_04_declare_description           | 10.0  |
| cat04_05_declare_anomalies             | 8.0   |
| cat04_06_log_skeleton_description      | 8.5   |
| cat04_07_log_skeleton_anomalies        | 8.5   |
| cat05_01_hypothesis_bpic2020           | 9.5   |
| cat05_02_hypothesis_roadtraffic        | 9.5   |
| cat05_03_hypothesis_bpmn_json          | 9.5   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 9.5   |
| cat06_01_renting_attributes            | 9.5   |
| cat06_02_hiring_attributes             | 9.5   |
| cat06_03_lending_attributes            | 9.5   |
| cat06_04_hospital_attributes           | 9.5   |
| cat06_05_renting_prot_comp             | 8.5   |
| cat06_06_hiring_prot_comp              | 9.0   |
| cat06_07_lending_prot_comp             | 8.5   |
| cat06_08_hospital_prot_comp            | 8.5   |


### Big Open-Source Models

#### Mistral Large 2 123B (20240724, fp16 quantization) => 40.3 (/46) points

| Question                                | Score |
|-----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca          | 8.5   |
| cat01_02_variants_roadtraffic_anomalies | 8.5   |
| cat01_03_bpic2020_var_descr             | 8.5   |
| cat01_04_roadtraffic_var_descr          | 9.0   |
| cat01_05_bpic2020_dfg_descr             | 9.0   |
| cat01_06_roadtraffic_dfg_descr          | 8.5   |
| cat01_07_ocel_container_description     | 9.0   |
| cat01_08_ocel_logistics_description     | 8.5   |
| cat01_09_ocel_container_rca             | 8.5   |
| cat01_10_ocel_logistics_rca             | 8.5   |
| cat02_01_open_event_abstraction         | 9.0   |
| cat02_02_open_process_cubes             | 10.0  |
| cat02_03_open_decomposition_strategies  | 8.0   |
| cat02_04_open_trace_clustering          | 6.3   |
| cat02_05_open_rpa                       | 9.5   |
| cat02_06_open_anomaly_detection         | 9.0   |
| cat02_07_open_process_enhancement       | 9.5   |
| cat02_08_closed_process_mining          | 9.0   |
| cat02_09_closed_petri_nets              | 9.0   |
| cat03_01_temp_profile_generation        | 9.0   |
| cat03_02_declare_generation             | 9.0   |
| cat03_03_log_skeleton_generation        | 9.0   |
| cat03_04_process_tree_generation        | 9.9   |
| cat03_05_powl_generation                | 9.0   |
| cat03_06_temp_profile_discovery         | 7.0   |
| cat03_07_declare_discovery              | 7.5   |
| cat03_08_log_skeleton_discovery         | 7.5   |
| cat04_01_bpmn_xml_tasks                 | 9.5   |
| cat04_02_bpmn_json_description          | 9.3   |
| cat04_03_bpmn_simp_xml_description      | 9.0   |
| cat04_04_declare_description            | 9.0   |
| cat04_05_declare_anomalies              | 8.5   |
| cat04_06_log_skeleton_description       | 8.5   |
| cat04_07_log_skeleton_anomalies         | 8.5   |
| cat05_01_hypothesis_bpic2020            | 8.5   |
| cat05_02_hypothesis_roadtraffic         | 8.5   |
| cat05_03_hypothesis_bpmn_json           | 9.5   |
| cat05_04_hypothesis_bpmn_simpl_xml      | 9.5   |
| cat06_01_renting_attributes             | 9.5   |
| cat06_02_hiring_attributes              | 9.0   |
| cat06_03_lending_attributes             | 9.0   |
| cat06_04_hospital_attributes            | 9.5   |
| cat06_05_renting_prot_comp              | 8.5   |
| cat06_06_hiring_prot_comp               | 8.6   |
| cat06_07_lending_prot_comp              | 8.5   |
| cat06_08_hospital_prot_comp             | 8.5   |
