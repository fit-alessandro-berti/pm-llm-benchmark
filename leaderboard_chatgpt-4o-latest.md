## Leaderboard (1-shot; chatgpt-4o-latest used as a judge)

Overall leaderboard (a score in the range **27-33** is considered **sufficient**; a score in the range **33-45** is considered **good**; a score **>45** is considered **excellent**):

| Model                                  | Overall Score                |   C1 |   C2 |   C3 |   C4 |   C5 |   C6 |   C7 |
|:---------------------------------------|:-----------------------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| gemini-1.5-pro-002                     | **44.8** (**39.5** on C1-C6) |  8.7 |  8.2 |  6.2 |  6.2 |  3.3 |  7   |  5.2 |
| o1-preview-2024-09-12                  | **39.4**                     |  8.1 |  8.1 |  6.2 |  6.2 |  3.4 |  7.3 |  0   |
| Gemini-1.5-Flash-002                   | **43.9** (**38.8** on C1-C6) |  8.3 |  8.1 |  6   |  6   |  3.2 |  7   |  5.1 |
| chatgpt-4o-latest-2024-09-03           | **42.9** (**38.1** on C1-C6) |  8.3 |  8.2 |  5.5 |  5.7 |  3.2 |  7.1 |  4.8 |
| claude-3-5-sonnet-20241022             | **43.0** (**37.7** on C1-C6) |  8.5 |  7.5 |  5.5 |  6   |  3.3 |  6.8 |  5.3 |
| gpt-4o-2024-08-06                      | **42.1** (**37.1** on C1-C6) |  8.2 |  8.1 |  5.6 |  5.7 |  3.1 |  6.5 |  5   |
| Gemini-1.5-Flash-8B                    | **42.0** (**37.1** on C1-C6) |  8   |  8.2 |  5.2 |  5.8 |  3.2 |  6.7 |  4.8 |
| claude-3-5-sonnet-20240620             | **42.1** (**36.9** on C1-C6) |  7.8 |  7.9 |  5   |  5.8 |  3.3 |  7   |  5.3 |
| nemotron70b-instruct-q8_0              | **36.5**                     |  8   |  8.2 |  5.2 |  5.5 |  2.8 |  6.9 |  0   |
| gpt-4o-2024-05-13                      | **40.8** (**36.2** on C1-C6) |  7.9 |  8.1 |  5.1 |  5.2 |  3.1 |  6.8 |  4.5 |
| o1-mini-2024-09-12                     | **36.0**                     |  7.3 |  7.8 |  4.9 |  5.8 |  3.2 |  6.9 |  0   |
| gpt-4-turbo-2024-04-09                 | **41.0** (**35.8** on C1-C6) |  7.2 |  8   |  5.7 |  5.3 |  2.8 |  6.7 |  5.2 |
| gpt-4o-mini-2024-07-18                 | **40.4** (**35.5** on C1-C6) |  7.4 |  8.2 |  5.3 |  5.2 |  2.9 |  6.7 |  4.8 |
| microsoftWizardLM-2-8x22B              | **35.1**                     |  7.5 |  8   |  4.2 |  5.7 |  3   |  6.8 |  0   |
| gpt-4-0613                             | **35.1**                     |  7.3 |  7.6 |  5.3 |  5.4 |  3   |  6.5 |  0   |
| claude-3-sonnet                        | **38.9** (**35.0** on C1-C6) |  7.1 |  7.8 |  5.5 |  5.3 |  3.1 |  6.2 |  3.9 |
| meta-llamaMeta-Llama-3.1-405B-Instruct | **35.0**                     |  7.8 |  7.7 |  4.8 |  5.7 |  3.2 |  5.8 |  0   |
| mistral-large-2407                     | **34.7**                     |  7.4 |  8   |  4.5 |  5.3 |  2.8 |  6.8 |  0   |
| gemma29b-instruct-q6_K                 | **34.6**                     |  7.7 |  7.9 |  5.5 |  4   |  2.8 |  6.7 |  0   |
| qwen2.532b-instruct-q6_K               | **34.2**                     |  7.5 |  7.9 |  5.8 |  5.2 |  2   |  5.8 |  0   |
| meta-llamaMeta-Llama-3.1-70B-Instruct  | **34.2**                     |  7.2 |  7.8 |  4.5 |  5.6 |  2.8 |  6.4 |  0   |
| qwen2.572b-instruct-q6_K               | **33.9**                     |  6.7 |  7.8 |  5   |  4.8 |  3   |  6.5 |  0   |
| qwen2.514b-instruct-q6_K               | **33.6**                     |  7   |  7.8 |  4.8 |  4.8 |  2.8 |  6.5 |  0   |
| open-mixtral-8x22b                     | **33.5**                     |  7   |  7.7 |  5   |  4.8 |  2.9 |  6.1 |  0   |
| mistral-medium-2407                    | **32.8**                     |  6.7 |  7.7 |  4.3 |  4.9 |  3.3 |  6   |  0   |
| mistral-nemo12b-instruct-2407-fp16     | **32.6**                     |  7.5 |  7.6 |  4.8 |  4.1 |  2.5 |  6.2 |  0   |
| mistral-nemo12b-instruct-2407-q4_0     | **32.5**                     |  7   |  7.7 |  4.8 |  4.7 |  2.2 |  6   |  0   |
| pixtral-12b-2409                       | **36.2** (**32.4** on C1-C6) |  7.2 |  7.8 |  3.7 |  5.5 |  2.9 |  5.3 |  3.9 |
| open-mistral-nemo-2407                 | **32.3**                     |  6.5 |  7.6 |  5   |  5.3 |  2.6 |  5.4 |  0   |
| mistral-small-2409                     | **32.1**                     |  6   |  8   |  4.3 |  5.6 |  2.1 |  6.1 |  0   |
| mistralaiPixtral-12B-2409              | **35.6** (**31.9** on C1-C6) |  7.2 |  8.1 |  4.3 |  4.2 |  1.8 |  6.4 |  3.6 |
| qwen2.57b-instruct-q6_K                | **31.6**                     |  6.2 |  7.8 |  4.9 |  4.8 |  2   |  6   |  0   |
| gpt-3.5-turbo                          | **31.3**                     |  7   |  6.9 |  4   |  4.5 |  3   |  5.7 |  0   |
| open-mixtral-8x7b                      | **31.2**                     |  6   |  7.5 |  4.2 |  4.3 |  2.9 |  6.2 |  0   |
| ministral-8b-2410                      | **31.1**                     |  6.3 |  7.5 |  3.4 |  4.2 |  2.9 |  6.8 |  0   |
| codestral-2405                         | **31.1**                     |  5.7 |  7   |  4   |  4.8 |  3.1 |  6.7 |  0   |
| mistral7b-instruct-v0.3-q6_K           | **29.6**                     |  6.7 |  7.6 |  3.6 |  3   |  2.5 |  6.2 |  0   |
| ministral-3b-2410                      | **29.6**                     |  6.5 |  7.7 |  3   |  5   |  2.7 |  4.8 |  0   |
| microsoftWizardLM-2-7B                 | **29.6**                     |  7   |  7.9 |  3.5 |  3.8 |  1.7 |  5.8 |  0   |
| meta-llamaMeta-Llama-3.1-8B-Instruct   | **28.6**                     |  6.1 |  7.8 |  2.6 |  4.2 |  3   |  4.8 |  0   |
| qwen2.53b-instruct-q8_0                | **25.8**                     |  4.8 |  8   |  2.5 |  4.2 |  1.7 |  4.7 |  0   |
| open-codestral-mamba-2407              | **25.8**                     |  3.9 |  7   |  3.9 |  4.1 |  3.1 |  3.8 |  0   |
| gemma22b-instruct-q8_0                 | **25.6**                     |  5.7 |  7.3 |  3   |  3.3 |  1.8 |  4.5 |  0   |
| llama3.23b-instruct-q8_0               | **24.9**                     |  5.6 |  6.7 |  2   |  3.6 |  2.3 |  4.7 |  0   |
| QwenQwen2-VL-7B-Instruct               | **25.2** (**21.8** on C1-C6) |  4.3 |  6   |  3   |  3   |  1.1 |  4.3 |  3.4 |
| qwen2.51.5b-instruct-q6_K              | **19.1**                     |  4   |  6.2 |  2.2 |  2.7 |  1.8 |  2.3 |  0   |
| llama3.21b-instruct-q6_K               | **16.8**                     |  3.9 |  5.5 |  1.9 |  1.7 |  0.9 |  2.8 |  0   |
| smollm21.7b-instruct-q6_K              | **15.6**                     |  3.4 |  5.8 |  1.7 |  1.6 |  1.2 |  1.9 |  0   |

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



### o1-preview-2024-09-12   => 39.4 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     9   |
| cat01_03_bpic2020_var_descr             |     9   |
| cat01_04_roadtraffic_var_descr          |     9   |
| cat01_05_bpic2020_dfg_descr             |     8.5 |
| cat01_06_roadtraffic_dfg_descr          |     4   |
| cat01_07_ocel_container_description     |     8.5 |
| cat01_08_ocel_logistics_description     |     9   |
| cat01_09_ocel_container_rca             |     7.5 |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9.5 |
| cat02_09_closed_petri_nets              |     9.5 |
| cat03_01_temp_profile_generation        |     7   |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     8.5 |
| cat03_04_process_tree_generation        |     9   |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     9.5 |
| cat03_07_declare_discovery              |     5   |
| cat03_08_log_skeleton_discovery         |     9   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |    10   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     9   |
| cat04_06_log_skeleton_description       |     8.5 |
| cat04_07_log_skeleton_anomalies         |     9   |
| cat05_01_hypothesis_bpic2020            |     9   |
| cat05_02_hypothesis_roadtraffic         |     7   |
| cat05_03_hypothesis_bpmn_json           |     9   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8.5 |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9.5 |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     9.5 |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     9.5 |



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



### chatgpt-4o-latest-2024-09-03   => 42.9 (/52) points

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
| cat07_01_dotted_chart                   |     4   |
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



### nemotron70b-instruct-q8_0   => 36.5 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7   |
| cat01_02_variants_roadtraffic_anomalies |     6   |
| cat01_03_bpic2020_var_descr             |     8.5 |
| cat01_04_roadtraffic_var_descr          |     8.5 |
| cat01_05_bpic2020_dfg_descr             |     9   |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     8   |
| cat01_09_ocel_container_rca             |     9.5 |
| cat01_10_ocel_logistics_rca             |     8   |
| cat02_01_open_event_abstraction         |     9.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9.5 |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     8.5 |
| cat03_04_process_tree_generation        |     9   |
| cat03_05_powl_generation                |     6.5 |
| cat03_06_temp_profile_discovery         |     4   |
| cat03_07_declare_discovery              |     2   |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     6   |
| cat04_04_declare_description            |     8.5 |
| cat04_05_declare_anomalies              |     8   |
| cat04_06_log_skeleton_description       |     8   |
| cat04_07_log_skeleton_anomalies         |     6   |
| cat05_01_hypothesis_bpic2020            |     9   |
| cat05_02_hypothesis_roadtraffic         |     7   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     4   |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     9.5 |
| cat06_03_lending_attributes             |     8.5 |
| cat06_04_hospital_attributes            |     8.5 |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     9.5 |
| cat06_08_hospital_prot_comp             |     8   |



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



### o1-mini-2024-09-12   => 36.0 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     5   |
| cat01_05_bpic2020_dfg_descr             |     4   |
| cat01_06_roadtraffic_dfg_descr          |     9   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     6.5 |
| cat01_09_ocel_container_rca             |     7.5 |
| cat01_10_ocel_logistics_rca             |     9.5 |
| cat02_01_open_event_abstraction         |     9.5 |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     4   |
| cat03_03_log_skeleton_generation        |     9   |
| cat03_04_process_tree_generation        |     8   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     7   |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     1   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     9.5 |
| cat04_03_bpmn_simp_xml_description      |     7.5 |
| cat04_04_declare_description            |     9   |
| cat04_05_declare_anomalies              |     8.5 |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     7.5 |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8.5 |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     8   |



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



### microsoftWizardLM-2-8x22B   => 35.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8   |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     7   |
| cat01_04_roadtraffic_var_descr          |     7.5 |
| cat01_05_bpic2020_dfg_descr             |     7.5 |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     6.5 |
| cat01_08_ocel_logistics_description     |     7   |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     7   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     8.5 |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     4.5 |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     2   |
| cat03_05_powl_generation                |     7.5 |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     4   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |    10   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     7.5 |
| cat04_06_log_skeleton_description       |     7.5 |
| cat04_07_log_skeleton_anomalies         |     6.5 |
| cat05_01_hypothesis_bpic2020            |     7   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     7   |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     7.5 |
| cat06_08_hospital_prot_comp             |     8   |



### gpt-4-0613   => 35.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8.5 |
| cat01_02_variants_roadtraffic_anomalies |     4   |
| cat01_03_bpic2020_var_descr             |     9   |
| cat01_04_roadtraffic_var_descr          |     7.5 |
| cat01_05_bpic2020_dfg_descr             |     8.5 |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     7.5 |
| cat01_08_ocel_logistics_description     |     7   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     7   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     7.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     8.5 |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     8   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     7   |
| cat03_07_declare_discovery              |     4   |
| cat03_08_log_skeleton_discovery         |     2   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     8   |
| cat04_03_bpmn_simp_xml_description      |     7.5 |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     6.5 |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     8   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     9   |
| cat05_03_hypothesis_bpmn_json           |     4   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     9   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     8.5 |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     8.5 |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     7.5 |
| cat06_08_hospital_prot_comp             |     7.5 |



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



### meta-llamaMeta-Llama-3.1-405B-Instruct   => 35.0 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7.5 |
| cat01_02_variants_roadtraffic_anomalies |     9   |
| cat01_03_bpic2020_var_descr             |     9   |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     7   |
| cat01_06_roadtraffic_dfg_descr          |     8.5 |
| cat01_07_ocel_container_description     |     7.5 |
| cat01_08_ocel_logistics_description     |     7   |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     8   |
| cat02_04_open_trace_clustering          |     8   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9.5 |
| cat02_08_closed_process_mining          |     7.5 |
| cat02_09_closed_petri_nets              |     8.5 |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     7.5 |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     5   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     7   |
| cat04_04_declare_description            |     7.5 |
| cat04_05_declare_anomalies              |     8   |
| cat04_06_log_skeleton_description       |     7.5 |
| cat04_07_log_skeleton_anomalies         |     8.5 |
| cat05_01_hypothesis_bpic2020            |     8.5 |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     7.5 |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     7   |
| cat06_06_hiring_prot_comp               |     4   |
| cat06_07_lending_prot_comp              |     8.5 |
| cat06_08_hospital_prot_comp             |     4   |



### mistral-large-2407   => 34.7 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     7   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     7   |
| cat01_05_bpic2020_dfg_descr             |     6.5 |
| cat01_06_roadtraffic_dfg_descr          |     7.5 |
| cat01_07_ocel_container_description     |     8   |
| cat01_08_ocel_logistics_description     |     6   |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     9.5 |
| cat02_02_open_process_cubes             |     8   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     7   |
| cat03_05_powl_generation                |     7.5 |
| cat03_06_temp_profile_discovery         |     4   |
| cat03_07_declare_discovery              |     2   |
| cat03_08_log_skeleton_discovery         |     1   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     7.5 |
| cat04_03_bpmn_simp_xml_description      |     7.5 |
| cat04_04_declare_description            |     9.5 |
| cat04_05_declare_anomalies              |     8   |
| cat04_06_log_skeleton_description       |     8.5 |
| cat04_07_log_skeleton_anomalies         |     3   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     7   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     5   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     7   |



### gemma29b-instruct-q6_K   => 34.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     7.5 |
| cat01_03_bpic2020_var_descr             |     8.5 |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     7   |
| cat01_07_ocel_container_description     |     7.5 |
| cat01_08_ocel_logistics_description     |     6.5 |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     8.5 |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     9   |
| cat03_04_process_tree_generation        |     8.5 |
| cat03_05_powl_generation                |     7.5 |
| cat03_06_temp_profile_discovery         |     8   |
| cat03_07_declare_discovery              |     5   |
| cat03_08_log_skeleton_discovery         |     2   |
| cat04_01_bpmn_xml_tasks                 |    10   |
| cat04_02_bpmn_json_description          |     2.5 |
| cat04_04_declare_description            |     7.5 |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     6.5 |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     6   |
| cat05_02_hypothesis_roadtraffic         |     7   |
| cat05_03_hypothesis_bpmn_json           |     7   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     8.5 |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     8   |
| cat06_08_hospital_prot_comp             |     9   |



### qwen2.532b-instruct-q6_K   => 34.2 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8.5 |
| cat01_02_variants_roadtraffic_anomalies |     4   |
| cat01_03_bpic2020_var_descr             |     7   |
| cat01_04_roadtraffic_var_descr          |     9   |
| cat01_05_bpic2020_dfg_descr             |     7.5 |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     9.5 |
| cat01_09_ocel_container_rca             |     8   |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     9   |
| cat03_04_process_tree_generation        |     8.5 |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     3.5 |
| cat03_07_declare_discovery              |     7   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     4   |
| cat04_03_bpmn_simp_xml_description      |     7.5 |
| cat04_04_declare_description            |     9   |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     7.5 |
| cat04_07_log_skeleton_anomalies         |     8.5 |
| cat05_01_hypothesis_bpic2020            |     4   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     7.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     1   |
| cat06_01_renting_attributes             |     7   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     2   |
| cat06_06_hiring_prot_comp               |     6.5 |
| cat06_07_lending_prot_comp              |     8.5 |
| cat06_08_hospital_prot_comp             |     8   |



### meta-llamaMeta-Llama-3.1-70B-Instruct   => 34.2 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8   |
| cat01_02_variants_roadtraffic_anomalies |     7   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     9   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     6.5 |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     5   |
| cat01_09_ocel_container_rca             |     7   |
| cat01_10_ocel_logistics_rca             |     6.5 |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     8   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     9.5 |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     6   |
| cat03_04_process_tree_generation        |     1   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     4   |
| cat03_07_declare_discovery              |     5   |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     6.5 |
| cat04_06_log_skeleton_description       |     8   |
| cat04_07_log_skeleton_anomalies         |     8.5 |
| cat05_01_hypothesis_bpic2020            |     6.5 |
| cat05_02_hypothesis_roadtraffic         |     7.5 |
| cat05_03_hypothesis_bpmn_json           |     6   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     7.5 |
| cat06_01_renting_attributes             |     7   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8.5 |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     6.5 |
| cat06_08_hospital_prot_comp             |     7   |



### qwen2.572b-instruct-q6_K   => 33.9 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7   |
| cat01_02_variants_roadtraffic_anomalies |     5.5 |
| cat01_03_bpic2020_var_descr             |     8.5 |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     7.5 |
| cat01_06_roadtraffic_dfg_descr          |     7.5 |
| cat01_07_ocel_container_description     |     2   |
| cat01_08_ocel_logistics_description     |     5   |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     7   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9.5 |
| cat02_06_open_anomaly_detection         |     9.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     7.5 |
| cat03_01_temp_profile_generation        |     7   |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     4   |
| cat03_05_powl_generation                |     8.5 |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     8   |
| cat03_08_log_skeleton_discovery         |     7   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     4   |
| cat04_03_bpmn_simp_xml_description      |     6.5 |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     8   |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     6.5 |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     6.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     7.5 |
| cat06_01_renting_attributes             |     9.5 |
| cat06_02_hiring_attributes              |     8.5 |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     6.5 |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     7   |



### qwen2.514b-instruct-q6_K   => 33.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     4.5 |
| cat01_02_variants_roadtraffic_anomalies |     3   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     6.5 |
| cat01_08_ocel_logistics_description     |     8   |
| cat01_09_ocel_container_rca             |     8.5 |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     8   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9.5 |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     4   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     5   |
| cat03_05_powl_generation                |     5   |
| cat03_06_temp_profile_discovery         |     4.5 |
| cat03_07_declare_discovery              |     7   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     2   |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     8.5 |
| cat04_07_log_skeleton_anomalies         |     4   |
| cat05_01_hypothesis_bpic2020            |     6   |
| cat05_02_hypothesis_roadtraffic         |     9   |
| cat05_03_hypothesis_bpmn_json           |     4   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8.5 |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     7.5 |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     6.5 |
| cat06_05_renting_prot_comp              |     8.5 |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     7.5 |
| cat06_08_hospital_prot_comp             |     8   |



### open-mixtral-8x22b   => 33.5 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7.5 |
| cat01_02_variants_roadtraffic_anomalies |     6   |
| cat01_03_bpic2020_var_descr             |     7.5 |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     6   |
| cat01_07_ocel_container_description     |     6   |
| cat01_08_ocel_logistics_description     |     8   |
| cat01_09_ocel_container_rca             |     6   |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     8   |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     6   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     6   |
| cat03_08_log_skeleton_discovery         |     4   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     5   |
| cat04_06_log_skeleton_description       |     5.5 |
| cat04_07_log_skeleton_anomalies         |     3   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     9.5 |
| cat05_03_hypothesis_bpmn_json           |     3   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8.5 |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     7.5 |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     7.5 |
| cat06_06_hiring_prot_comp               |     4.5 |
| cat06_07_lending_prot_comp              |     8.5 |
| cat06_08_hospital_prot_comp             |     8   |



### mistral-medium-2407   => 32.8 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7   |
| cat01_02_variants_roadtraffic_anomalies |     6   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     6   |
| cat01_05_bpic2020_dfg_descr             |     7   |
| cat01_06_roadtraffic_dfg_descr          |     6.5 |
| cat01_07_ocel_container_description     |     6   |
| cat01_08_ocel_logistics_description     |     6   |
| cat01_09_ocel_container_rca             |     7   |
| cat01_10_ocel_logistics_rca             |     7   |
| cat02_01_open_event_abstraction         |     7.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     7.5 |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     7   |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     4   |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     2   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     8.5 |
| cat04_03_bpmn_simp_xml_description      |     8.5 |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     6   |
| cat04_06_log_skeleton_description       |     3   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     9   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8.5 |
| cat06_04_hospital_attributes            |    10   |
| cat06_05_renting_prot_comp              |     7   |
| cat06_06_hiring_prot_comp               |     4   |
| cat06_07_lending_prot_comp              |     6.5 |
| cat06_08_hospital_prot_comp             |     6   |



### mistral-nemo12b-instruct-2407-fp16   => 32.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6.5 |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     8.5 |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     7.5 |
| cat01_07_ocel_container_description     |     5   |
| cat01_08_ocel_logistics_description     |     6   |
| cat01_09_ocel_container_rca             |     8   |
| cat01_10_ocel_logistics_rca             |     9   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     7.5 |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     6.5 |
| cat03_01_temp_profile_generation        |     7   |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     8.5 |
| cat03_04_process_tree_generation        |     1   |
| cat03_05_powl_generation                |     7.5 |
| cat03_06_temp_profile_discovery         |     6   |
| cat03_07_declare_discovery              |     6   |
| cat03_08_log_skeleton_discovery         |     4   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     7   |
| cat04_04_declare_description            |     6   |
| cat04_05_declare_anomalies              |     5   |
| cat04_06_log_skeleton_description       |     6.5 |
| cat04_07_log_skeleton_anomalies         |     6   |
| cat05_01_hypothesis_bpic2020            |     7   |
| cat05_02_hypothesis_roadtraffic         |     8.5 |
| cat05_03_hypothesis_bpmn_json           |     3   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     7   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     7.5 |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     6   |
| cat06_06_hiring_prot_comp               |     9   |
| cat06_07_lending_prot_comp              |     8   |
| cat06_08_hospital_prot_comp             |     4   |



### mistral-nemo12b-instruct-2407-q4_0   => 32.5 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6   |
| cat01_02_variants_roadtraffic_anomalies |     4   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     7.5 |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     4   |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     8.5 |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9.5 |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     7   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     8   |
| cat03_03_log_skeleton_generation        |     7.5 |
| cat03_04_process_tree_generation        |     4.5 |
| cat03_05_powl_generation                |     2   |
| cat03_06_temp_profile_discovery         |     7   |
| cat03_07_declare_discovery              |     6.5 |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     2   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     5   |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     2   |
| cat05_03_hypothesis_bpmn_json           |     4   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     7   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     8.5 |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     7   |
| cat06_08_hospital_prot_comp             |     6   |



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



### open-mistral-nemo-2407   => 32.3 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7   |
| cat01_02_variants_roadtraffic_anomalies |     2   |
| cat01_03_bpic2020_var_descr             |     5   |
| cat01_04_roadtraffic_var_descr          |     7   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     7   |
| cat01_07_ocel_container_description     |     7.5 |
| cat01_08_ocel_logistics_description     |     5   |
| cat01_09_ocel_container_rca             |     9   |
| cat01_10_ocel_logistics_rca             |     7   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     6.5 |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     8.5 |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     2   |
| cat03_05_powl_generation                |     8   |
| cat03_06_temp_profile_discovery         |     5   |
| cat03_07_declare_discovery              |     5   |
| cat03_08_log_skeleton_discovery         |     6   |
| cat04_01_bpmn_xml_tasks                 |     8   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     6   |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     6.5 |
| cat04_07_log_skeleton_anomalies         |     7.5 |
| cat05_01_hypothesis_bpic2020            |     7   |
| cat05_02_hypothesis_roadtraffic         |     7   |
| cat05_03_hypothesis_bpmn_json           |     5.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     6.5 |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     6   |
| cat06_06_hiring_prot_comp               |     3.5 |
| cat06_07_lending_prot_comp              |     5   |
| cat06_08_hospital_prot_comp             |     6.5 |



### mistral-small-2409   => 32.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     7.5 |
| cat01_02_variants_roadtraffic_anomalies |     3   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     4.5 |
| cat01_05_bpic2020_dfg_descr             |     7   |
| cat01_06_roadtraffic_dfg_descr          |     2   |
| cat01_07_ocel_container_description     |     6.5 |
| cat01_08_ocel_logistics_description     |     7.5 |
| cat01_09_ocel_container_rca             |     6   |
| cat01_10_ocel_logistics_rca             |     8   |
| cat02_01_open_event_abstraction         |     9.5 |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9.5 |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     8.5 |
| cat03_01_temp_profile_generation        |     4   |
| cat03_02_declare_generation             |     7   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     6.5 |
| cat03_05_powl_generation                |     6   |
| cat03_06_temp_profile_discovery         |     2.5 |
| cat03_07_declare_discovery              |     5   |
| cat03_08_log_skeleton_discovery         |     4   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     9   |
| cat04_03_bpmn_simp_xml_description      |     7.5 |
| cat04_04_declare_description            |     8.5 |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     8   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     2   |
| cat05_02_hypothesis_roadtraffic         |     4   |
| cat05_03_hypothesis_bpmn_json           |     7   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     5   |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     8   |
| cat06_08_hospital_prot_comp             |     6   |



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



### qwen2.57b-instruct-q6_K   => 31.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8   |
| cat01_02_variants_roadtraffic_anomalies |     3   |
| cat01_03_bpic2020_var_descr             |     6.5 |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     4   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     8   |
| cat01_09_ocel_container_rca             |     6   |
| cat01_10_ocel_logistics_rca             |     4   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     9.5 |
| cat02_03_open_decomposition_strategies  |     9.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     7.5 |
| cat02_09_closed_petri_nets              |     7.5 |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     6   |
| cat03_03_log_skeleton_generation        |     8   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     6.5 |
| cat03_07_declare_discovery              |     5.5 |
| cat03_08_log_skeleton_discovery         |     5   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     3   |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     8.5 |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     4   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     4   |
| cat05_02_hypothesis_roadtraffic         |     7   |
| cat05_03_hypothesis_bpmn_json           |     3   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     6   |
| cat06_01_renting_attributes             |     7   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     6.5 |
| cat06_06_hiring_prot_comp               |     5   |
| cat06_07_lending_prot_comp              |     8   |
| cat06_08_hospital_prot_comp             |     8   |



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



### open-mixtral-8x7b   => 31.2 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6   |
| cat01_02_variants_roadtraffic_anomalies |     5   |
| cat01_03_bpic2020_var_descr             |     7.5 |
| cat01_04_roadtraffic_var_descr          |     8.5 |
| cat01_05_bpic2020_dfg_descr             |     8.5 |
| cat01_06_roadtraffic_dfg_descr          |     6.5 |
| cat01_07_ocel_container_description     |     5.5 |
| cat01_08_ocel_logistics_description     |     4   |
| cat01_09_ocel_container_rca             |     6   |
| cat01_10_ocel_logistics_rca             |     3   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     8   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     6   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     5   |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     8   |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     1   |
| cat03_08_log_skeleton_discovery         |     4   |
| cat04_01_bpmn_xml_tasks                 |     5   |
| cat04_02_bpmn_json_description          |     9.5 |
| cat04_03_bpmn_simp_xml_description      |     7   |
| cat04_04_declare_description            |     3   |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     5   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     6.5 |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     6.5 |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     8   |
| cat06_08_hospital_prot_comp             |     3   |



### ministral-8b-2410   => 31.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     6   |
| cat01_03_bpic2020_var_descr             |     6.5 |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     3   |
| cat01_06_roadtraffic_dfg_descr          |     3   |
| cat01_07_ocel_container_description     |     6   |
| cat01_08_ocel_logistics_description     |     7   |
| cat01_09_ocel_container_rca             |     7   |
| cat01_10_ocel_logistics_rca             |     7.5 |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     5.5 |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     7.5 |
| cat03_02_declare_generation             |     7.5 |
| cat03_03_log_skeleton_generation        |     6   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     4   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     1   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     8   |
| cat04_03_bpmn_simp_xml_description      |     7   |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     4   |
| cat04_06_log_skeleton_description       |     5   |
| cat04_07_log_skeleton_anomalies         |     2   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     9   |
| cat05_03_hypothesis_bpmn_json           |     6   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     6   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     8.5 |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     8.5 |
| cat06_05_renting_prot_comp              |     9   |
| cat06_06_hiring_prot_comp               |     8.5 |
| cat06_07_lending_prot_comp              |     9   |
| cat06_08_hospital_prot_comp             |     8   |



### codestral-2405   => 31.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6.5 |
| cat01_02_variants_roadtraffic_anomalies |     3   |
| cat01_03_bpic2020_var_descr             |     7   |
| cat01_04_roadtraffic_var_descr          |     6   |
| cat01_05_bpic2020_dfg_descr             |     4   |
| cat01_06_roadtraffic_dfg_descr          |     8.5 |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     4   |
| cat01_09_ocel_container_rca             |     5   |
| cat01_10_ocel_logistics_rca             |     6   |
| cat02_01_open_event_abstraction         |     8   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8   |
| cat02_08_closed_process_mining          |     6.5 |
| cat02_09_closed_petri_nets              |     5   |
| cat03_01_temp_profile_generation        |     8   |
| cat03_02_declare_generation             |     9   |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     6.5 |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     6   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     6   |
| cat04_05_declare_anomalies              |     5   |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     7   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     8.5 |
| cat06_02_hiring_attributes              |     9.5 |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     8.5 |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     8   |
| cat06_08_hospital_prot_comp             |     6   |



### mistral7b-instruct-v0.3-q6_K   => 29.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     8   |
| cat01_02_variants_roadtraffic_anomalies |     4   |
| cat01_03_bpic2020_var_descr             |     7   |
| cat01_04_roadtraffic_var_descr          |     7   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     3   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     6   |
| cat01_09_ocel_container_rca             |     8   |
| cat01_10_ocel_logistics_rca             |     9   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     7.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     8   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     9   |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     6   |
| cat03_02_declare_generation             |     4   |
| cat03_03_log_skeleton_generation        |     6   |
| cat03_04_process_tree_generation        |     6   |
| cat03_05_powl_generation                |     7   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     2   |
| cat04_01_bpmn_xml_tasks                 |     4   |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     2   |
| cat04_04_declare_description            |     6.5 |
| cat04_05_declare_anomalies              |     6.5 |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     4.5 |
| cat05_01_hypothesis_bpic2020            |     9.5 |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     4   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     3   |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     9   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     7   |
| cat06_06_hiring_prot_comp               |     7   |
| cat06_07_lending_prot_comp              |     7.5 |
| cat06_08_hospital_prot_comp             |     7   |



### ministral-3b-2410   => 29.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     9   |
| cat01_02_variants_roadtraffic_anomalies |     2   |
| cat01_03_bpic2020_var_descr             |     7.5 |
| cat01_04_roadtraffic_var_descr          |     7.5 |
| cat01_05_bpic2020_dfg_descr             |     9   |
| cat01_06_roadtraffic_dfg_descr          |     3   |
| cat01_07_ocel_container_description     |     7.5 |
| cat01_08_ocel_logistics_description     |     7.5 |
| cat01_09_ocel_container_rca             |     7   |
| cat01_10_ocel_logistics_rca             |     5   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     8   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     6.5 |
| cat03_02_declare_generation             |     4   |
| cat03_03_log_skeleton_generation        |     3   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     3   |
| cat03_06_temp_profile_discovery         |     5   |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     8   |
| cat04_03_bpmn_simp_xml_description      |     7   |
| cat04_04_declare_description            |     3   |
| cat04_05_declare_anomalies              |     8   |
| cat04_06_log_skeleton_description       |     7.5 |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     8   |
| cat05_03_hypothesis_bpmn_json           |     8   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     3   |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     7   |
| cat06_03_lending_attributes             |     7.5 |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     3   |
| cat06_06_hiring_prot_comp               |     3   |
| cat06_07_lending_prot_comp              |     4   |
| cat06_08_hospital_prot_comp             |     6.5 |



### microsoftWizardLM-2-7B   => 29.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6.5 |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     7.5 |
| cat01_04_roadtraffic_var_descr          |     5   |
| cat01_05_bpic2020_dfg_descr             |     8   |
| cat01_06_roadtraffic_dfg_descr          |     6   |
| cat01_07_ocel_container_description     |     8   |
| cat01_08_ocel_logistics_description     |     8.5 |
| cat01_09_ocel_container_rca             |     7.5 |
| cat01_10_ocel_logistics_rca             |     5   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     8   |
| cat03_01_temp_profile_generation        |     9   |
| cat03_02_declare_generation             |     6   |
| cat03_03_log_skeleton_generation        |     4   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     6.5 |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     2   |
| cat03_08_log_skeleton_discovery         |     1   |
| cat04_01_bpmn_xml_tasks                 |     2   |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     8   |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     6.5 |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     6   |
| cat05_01_hypothesis_bpic2020            |     6   |
| cat05_02_hypothesis_roadtraffic         |     9   |
| cat05_03_hypothesis_bpmn_json           |     1   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     1   |
| cat06_01_renting_attributes             |     8.5 |
| cat06_02_hiring_attributes              |     9   |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     6   |
| cat06_06_hiring_prot_comp               |     8   |
| cat06_07_lending_prot_comp              |     3   |
| cat06_08_hospital_prot_comp             |     7   |



### meta-llamaMeta-Llama-3.1-8B-Instruct   => 28.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6   |
| cat01_02_variants_roadtraffic_anomalies |     8   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     5   |
| cat01_05_bpic2020_dfg_descr             |     4.5 |
| cat01_06_roadtraffic_dfg_descr          |     7   |
| cat01_07_ocel_container_description     |     6   |
| cat01_08_ocel_logistics_description     |     6   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     4   |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     8   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     8.5 |
| cat03_01_temp_profile_generation        |     5   |
| cat03_02_declare_generation             |     3   |
| cat03_03_log_skeleton_generation        |     5   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     4   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     1   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     4   |
| cat04_03_bpmn_simp_xml_description      |     6.5 |
| cat04_04_declare_description            |     3   |
| cat04_05_declare_anomalies              |     5   |
| cat04_06_log_skeleton_description       |     7.5 |
| cat04_07_log_skeleton_anomalies         |     7   |
| cat05_01_hypothesis_bpic2020            |     7   |
| cat05_02_hypothesis_roadtraffic         |     6   |
| cat05_03_hypothesis_bpmn_json           |     9   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     7   |
| cat06_02_hiring_attributes              |     6   |
| cat06_03_lending_attributes             |     6   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     4   |
| cat06_06_hiring_prot_comp               |     2   |
| cat06_07_lending_prot_comp              |     7   |
| cat06_08_hospital_prot_comp             |     8.5 |



### qwen2.53b-instruct-q8_0   => 25.8 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6.5 |
| cat01_02_variants_roadtraffic_anomalies |     1   |
| cat01_03_bpic2020_var_descr             |     1   |
| cat01_04_roadtraffic_var_descr          |     8   |
| cat01_05_bpic2020_dfg_descr             |     7   |
| cat01_06_roadtraffic_dfg_descr          |     5   |
| cat01_07_ocel_container_description     |     6   |
| cat01_08_ocel_logistics_description     |     3   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     4.5 |
| cat02_01_open_event_abstraction         |     8.5 |
| cat02_02_open_process_cubes             |     8.5 |
| cat02_03_open_decomposition_strategies  |     9   |
| cat02_04_open_trace_clustering          |     9   |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     8.5 |
| cat02_09_closed_petri_nets              |     9   |
| cat03_01_temp_profile_generation        |     3   |
| cat03_02_declare_generation             |     5   |
| cat03_03_log_skeleton_generation        |     3.5 |
| cat03_04_process_tree_generation        |     2   |
| cat03_05_powl_generation                |     4   |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     1   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     4   |
| cat04_02_bpmn_json_description          |     4   |
| cat04_03_bpmn_simp_xml_description      |     9   |
| cat04_04_declare_description            |     8   |
| cat04_05_declare_anomalies              |     7   |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     3   |
| cat05_01_hypothesis_bpic2020            |     1   |
| cat05_02_hypothesis_roadtraffic         |     4   |
| cat05_03_hypothesis_bpmn_json           |     6   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     6   |
| cat06_01_renting_attributes             |     6   |
| cat06_02_hiring_attributes              |     6.5 |
| cat06_03_lending_attributes             |     8   |
| cat06_04_hospital_attributes            |     8   |
| cat06_05_renting_prot_comp              |     8   |
| cat06_06_hiring_prot_comp               |     3.5 |
| cat06_07_lending_prot_comp              |     3.5 |
| cat06_08_hospital_prot_comp             |     3   |



### open-codestral-mamba-2407   => 25.8 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6   |
| cat01_02_variants_roadtraffic_anomalies |     2   |
| cat01_03_bpic2020_var_descr             |     7   |
| cat01_04_roadtraffic_var_descr          |     4.5 |
| cat01_05_bpic2020_dfg_descr             |     7   |
| cat01_06_roadtraffic_dfg_descr          |     4   |
| cat01_07_ocel_container_description     |     5   |
| cat01_08_ocel_logistics_description     |     2   |
| cat01_10_ocel_logistics_rca             |     1.5 |
| cat02_01_open_event_abstraction         |     7.5 |
| cat02_02_open_process_cubes             |     7.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     7.5 |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     8   |
| cat02_07_open_process_enhancement       |     8.5 |
| cat02_08_closed_process_mining          |     8   |
| cat02_09_closed_petri_nets              |     6   |
| cat03_01_temp_profile_generation        |     8.5 |
| cat03_02_declare_generation             |     4   |
| cat03_03_log_skeleton_generation        |     6   |
| cat03_04_process_tree_generation        |     7   |
| cat03_05_powl_generation                |     3   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     4   |
| cat03_08_log_skeleton_discovery         |     4   |
| cat04_01_bpmn_xml_tasks                 |     9.5 |
| cat04_02_bpmn_json_description          |     7.5 |
| cat04_03_bpmn_simp_xml_description      |     6   |
| cat04_04_declare_description            |     4   |
| cat04_05_declare_anomalies              |     3   |
| cat04_06_log_skeleton_description       |     5   |
| cat04_07_log_skeleton_anomalies         |     6   |
| cat05_01_hypothesis_bpic2020            |     8.5 |
| cat05_02_hypothesis_roadtraffic         |     9   |
| cat05_03_hypothesis_bpmn_json           |     6   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     9   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     7   |
| cat06_04_hospital_attributes            |     4.5 |
| cat06_05_renting_prot_comp              |     2   |
| cat06_06_hiring_prot_comp               |     1   |
| cat06_07_lending_prot_comp              |     3.5 |
| cat06_08_hospital_prot_comp             |     3   |



### gemma22b-instruct-q8_0   => 25.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     3.5 |
| cat01_02_variants_roadtraffic_anomalies |     3   |
| cat01_03_bpic2020_var_descr             |     7   |
| cat01_04_roadtraffic_var_descr          |     7   |
| cat01_05_bpic2020_dfg_descr             |     6   |
| cat01_06_roadtraffic_dfg_descr          |     8   |
| cat01_07_ocel_container_description     |     6.5 |
| cat01_08_ocel_logistics_description     |     6   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     3   |
| cat02_01_open_event_abstraction         |     9.5 |
| cat02_02_open_process_cubes             |     9   |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8.5 |
| cat02_05_open_rpa                       |     9   |
| cat02_06_open_anomaly_detection         |     9   |
| cat02_07_open_process_enhancement       |     8   |
| cat02_08_closed_process_mining          |     6.5 |
| cat02_09_closed_petri_nets              |     5   |
| cat03_01_temp_profile_generation        |     6.5 |
| cat03_02_declare_generation             |     4   |
| cat03_03_log_skeleton_generation        |     7   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     3   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     2   |
| cat04_01_bpmn_xml_tasks                 |     7.5 |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     4   |
| cat04_04_declare_description            |     7.5 |
| cat04_05_declare_anomalies              |     6   |
| cat04_06_log_skeleton_description       |     3   |
| cat04_07_log_skeleton_anomalies         |     4   |
| cat05_01_hypothesis_bpic2020            |     3   |
| cat05_02_hypothesis_roadtraffic         |     7   |
| cat05_03_hypothesis_bpmn_json           |     6   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     2   |
| cat06_01_renting_attributes             |     5   |
| cat06_02_hiring_attributes              |     6   |
| cat06_03_lending_attributes             |     3   |
| cat06_04_hospital_attributes            |     9   |
| cat06_05_renting_prot_comp              |     7   |
| cat06_06_hiring_prot_comp               |     3.5 |
| cat06_07_lending_prot_comp              |     7   |
| cat06_08_hospital_prot_comp             |     4   |



### llama3.23b-instruct-q8_0   => 24.9 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     2   |
| cat01_02_variants_roadtraffic_anomalies |     5   |
| cat01_03_bpic2020_var_descr             |     8   |
| cat01_04_roadtraffic_var_descr          |     7   |
| cat01_05_bpic2020_dfg_descr             |     6.5 |
| cat01_06_roadtraffic_dfg_descr          |     7   |
| cat01_07_ocel_container_description     |     6   |
| cat01_08_ocel_logistics_description     |     4   |
| cat01_09_ocel_container_rca             |     6.5 |
| cat01_10_ocel_logistics_rca             |     4   |
| cat02_01_open_event_abstraction         |     7   |
| cat02_02_open_process_cubes             |     7.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     8   |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     8.5 |
| cat02_07_open_process_enhancement       |     9   |
| cat02_08_closed_process_mining          |     5   |
| cat02_09_closed_petri_nets              |     4.5 |
| cat03_01_temp_profile_generation        |     2   |
| cat03_02_declare_generation             |     3   |
| cat03_03_log_skeleton_generation        |     4   |
| cat03_04_process_tree_generation        |     1   |
| cat03_05_powl_generation                |     4   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     1   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     9   |
| cat04_02_bpmn_json_description          |     2   |
| cat04_03_bpmn_simp_xml_description      |     6   |
| cat04_04_declare_description            |     3   |
| cat04_05_declare_anomalies              |     4.5 |
| cat04_06_log_skeleton_description       |     6   |
| cat04_07_log_skeleton_anomalies         |     6   |
| cat05_01_hypothesis_bpic2020            |     8   |
| cat05_02_hypothesis_roadtraffic         |     4   |
| cat05_03_hypothesis_bpmn_json           |     3   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     8   |
| cat06_01_renting_attributes             |     8   |
| cat06_02_hiring_attributes              |     8   |
| cat06_03_lending_attributes             |     7   |
| cat06_04_hospital_attributes            |     7   |
| cat06_05_renting_prot_comp              |     2.5 |
| cat06_06_hiring_prot_comp               |     4   |
| cat06_07_lending_prot_comp              |     4   |
| cat06_08_hospital_prot_comp             |     6   |



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



### qwen2.51.5b-instruct-q6_K   => 19.1 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6   |
| cat01_02_variants_roadtraffic_anomalies |     4   |
| cat01_03_bpic2020_var_descr             |     2   |
| cat01_04_roadtraffic_var_descr          |     3.5 |
| cat01_05_bpic2020_dfg_descr             |     2   |
| cat01_06_roadtraffic_dfg_descr          |     3   |
| cat01_07_ocel_container_description     |     7   |
| cat01_08_ocel_logistics_description     |     3   |
| cat01_09_ocel_container_rca             |     5   |
| cat01_10_ocel_logistics_rca             |     4   |
| cat02_01_open_event_abstraction         |     9   |
| cat02_02_open_process_cubes             |     6.5 |
| cat02_03_open_decomposition_strategies  |     8.5 |
| cat02_04_open_trace_clustering          |     7.5 |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     8   |
| cat02_07_open_process_enhancement       |     7.5 |
| cat02_08_closed_process_mining          |     4   |
| cat02_09_closed_petri_nets              |     3   |
| cat03_01_temp_profile_generation        |     4   |
| cat03_02_declare_generation             |     2   |
| cat03_03_log_skeleton_generation        |     3   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     2   |
| cat03_06_temp_profile_discovery         |     2   |
| cat03_07_declare_discovery              |     3   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     2   |
| cat04_02_bpmn_json_description          |     2   |
| cat04_03_bpmn_simp_xml_description      |     4   |
| cat04_04_declare_description            |     7   |
| cat04_05_declare_anomalies              |     3   |
| cat04_06_log_skeleton_description       |     5   |
| cat04_07_log_skeleton_anomalies         |     4   |
| cat05_01_hypothesis_bpic2020            |     6   |
| cat05_02_hypothesis_roadtraffic         |     5   |
| cat05_03_hypothesis_bpmn_json           |     3   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     3.5 |
| cat06_01_renting_attributes             |     1   |
| cat06_02_hiring_attributes              |     3   |
| cat06_03_lending_attributes             |     4   |
| cat06_04_hospital_attributes            |     2   |
| cat06_05_renting_prot_comp              |     5   |
| cat06_06_hiring_prot_comp               |     2   |
| cat06_07_lending_prot_comp              |     2   |
| cat06_08_hospital_prot_comp             |     4   |



### llama3.21b-instruct-q6_K   => 16.8 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     6   |
| cat01_02_variants_roadtraffic_anomalies |     2   |
| cat01_03_bpic2020_var_descr             |     6.5 |
| cat01_04_roadtraffic_var_descr          |     2   |
| cat01_05_bpic2020_dfg_descr             |     5.5 |
| cat01_06_roadtraffic_dfg_descr          |     6   |
| cat01_07_ocel_container_description     |     4   |
| cat01_08_ocel_logistics_description     |     2   |
| cat01_09_ocel_container_rca             |     2   |
| cat01_10_ocel_logistics_rca             |     3   |
| cat02_01_open_event_abstraction         |     7   |
| cat02_02_open_process_cubes             |     4   |
| cat02_03_open_decomposition_strategies  |     8   |
| cat02_04_open_trace_clustering          |     6.5 |
| cat02_05_open_rpa                       |     8.5 |
| cat02_06_open_anomaly_detection         |     8   |
| cat02_07_open_process_enhancement       |     7.5 |
| cat02_08_closed_process_mining          |     5   |
| cat02_09_closed_petri_nets              |     1   |
| cat03_01_temp_profile_generation        |     2   |
| cat03_02_declare_generation             |     3   |
| cat03_03_log_skeleton_generation        |     2   |
| cat03_04_process_tree_generation        |     1   |
| cat03_05_powl_generation                |     3   |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     2   |
| cat03_08_log_skeleton_discovery         |     3   |
| cat04_01_bpmn_xml_tasks                 |     1   |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     3   |
| cat04_04_declare_description            |     1   |
| cat04_05_declare_anomalies              |     2   |
| cat04_06_log_skeleton_description       |     7   |
| cat04_07_log_skeleton_anomalies         |     2   |
| cat05_01_hypothesis_bpic2020            |     3   |
| cat05_02_hypothesis_roadtraffic         |     2   |
| cat05_03_hypothesis_bpmn_json           |     2.5 |
| cat05_04_hypothesis_bpmn_simpl_xml      |     2   |
| cat06_01_renting_attributes             |     4   |
| cat06_02_hiring_attributes              |     7.5 |
| cat06_03_lending_attributes             |     3   |
| cat06_04_hospital_attributes            |     3   |
| cat06_05_renting_prot_comp              |     3.5 |
| cat06_06_hiring_prot_comp               |     3   |
| cat06_07_lending_prot_comp              |     3   |
| cat06_08_hospital_prot_comp             |     1   |



### smollm21.7b-instruct-q6_K   => 15.6 (/52) points

| Question                                |   Score |
|:----------------------------------------|--------:|
| cat01_01_variants_bpic2020_rca          |     2   |
| cat01_02_variants_roadtraffic_anomalies |     2   |
| cat01_03_bpic2020_var_descr             |     4   |
| cat01_04_roadtraffic_var_descr          |     2   |
| cat01_05_bpic2020_dfg_descr             |     3   |
| cat01_06_roadtraffic_dfg_descr          |     1   |
| cat01_07_ocel_container_description     |     5   |
| cat01_08_ocel_logistics_description     |     7.5 |
| cat01_09_ocel_container_rca             |     4   |
| cat01_10_ocel_logistics_rca             |     3   |
| cat02_01_open_event_abstraction         |     7.5 |
| cat02_02_open_process_cubes             |     7.5 |
| cat02_03_open_decomposition_strategies  |     6.5 |
| cat02_04_open_trace_clustering          |     8   |
| cat02_05_open_rpa                       |     7.5 |
| cat02_06_open_anomaly_detection         |     8   |
| cat02_07_open_process_enhancement       |     7.5 |
| cat02_08_closed_process_mining          |     4   |
| cat02_09_closed_petri_nets              |     2   |
| cat03_01_temp_profile_generation        |     1   |
| cat03_02_declare_generation             |     1   |
| cat03_03_log_skeleton_generation        |     4   |
| cat03_04_process_tree_generation        |     3   |
| cat03_05_powl_generation                |     3   |
| cat03_06_temp_profile_discovery         |     3   |
| cat03_07_declare_discovery              |     1   |
| cat03_08_log_skeleton_discovery         |     1   |
| cat04_01_bpmn_xml_tasks                 |     1   |
| cat04_02_bpmn_json_description          |     1   |
| cat04_03_bpmn_simp_xml_description      |     2   |
| cat04_04_declare_description            |     1.5 |
| cat04_05_declare_anomalies              |     3   |
| cat04_06_log_skeleton_description       |     4   |
| cat04_07_log_skeleton_anomalies         |     3   |
| cat05_01_hypothesis_bpic2020            |     5   |
| cat05_02_hypothesis_roadtraffic         |     1   |
| cat05_03_hypothesis_bpmn_json           |     3   |
| cat05_04_hypothesis_bpmn_simpl_xml      |     3   |
| cat06_01_renting_attributes             |     3   |
| cat06_02_hiring_attributes              |     2   |
| cat06_03_lending_attributes             |     3   |
| cat06_04_hospital_attributes            |     3   |
| cat06_05_renting_prot_comp              |     2   |
| cat06_06_hiring_prot_comp               |     2   |
| cat06_07_lending_prot_comp              |     2   |
| cat06_08_hospital_prot_comp             |     2   |

