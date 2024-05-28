# PM-LLM-Benchmark

Process mining benefits significantly from the domain knowledge provided by LLMs. However, no process-mining-specific LLM benchmarks have been proposed
until the current date.
We propose *PM-LLM-Benchmark*, a qualitative benchmark for PM-on-LLM. The LLM's answers are intended to be graded by another expert LLM (LLM-as-a-Judge).

The prompts are reported in the *questions/* folder.

Procedure for every prompt:
* Provide the prompt to a LLM:
  * For textual prompts, report the content as-is
  * (When supported) For images, upload the image to the LVLM and ask *Can you describe the provided visualization?*
* Annotate the output
* Use the expert LLM (LLM-as-a-Judge) to evaluate the output. Template:
  * For textual prompts, *Given the following question: ... How would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? ...*
  * (When supported) For images, upload the image to the LVLM and ask *Given the attached image, how would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? ...*

The final score of the benchmark is obtained by summing the scores and dividing by 10.0.

Different categories of questions are contained in the benchmark.
The first category checks the ability to perform process descriptions, anomaly detection, and root cause analysis starting from the DFG/variants abstractions of the event logs.
It also includes object-centric process mining artifacts for testing object-centric comprehension.
The second category checks the process mining domain knowledge of the LLM, with open and closed questions regarding process mining and Petri nets.
The third category checks the ability to generate procedural (process trees, POWLs) and declarative process models (control-flow and temporal) for mainstream processes. Moreover, the ability to propose constraints given some process data is tested.
The fourth category checks the ability to understand some proposed procedural (BPMN) and declarative (such as the Log Skeleton and DECLARE) process models.
The fifth category tests the ability of the LLM to generate hypotheses over the proposed data and process models.
The sixth category tests the ability of the LLM to identify sensible event log attributes and to perform a comparison between protected and non-protected groups.
The seventh category checks the visual capabilities (if supported) of the LLM/LVLM.

## Preliminary Scores (1-shot, gpt-4o-20240513 as a judge)

Overall leaderboard (a score in the range **27-34** is considered **sufficient**; a score **34-45** is considered **good**; a score **>45** is considered **excellent**):

| Model                                           | Context Length | Score                |
|-------------------------------------------------|----------------|----------------------|
| gpt-4o-20240513 (self-evaluation)               | 128K           | 43.4 (38 on C1-C6)   |
| gpt-4-turbo-20240409                            | 128K           | 42.3 (37.1 on C1-C6) |
| Mixtral v0.1 8x22b (instruct, 16b quantization) | 32K            | 34.7                 |
| Llama 3 70B (instruct, 16b quantization)        | 8K             | 34.1                 |
| gpt-3.5-turbo-0125                              | 16K            | 32.6                 |
| Mixtral v0.1 8x7b (instruct, 16b quantization)  | 32K            | 31.6                 |
| Llama 3 8B (instruct, 16b quantization)         | 8K             | 30.2                 |
| Llama 3 8B (instruct, Q6K quantization)         | 8K             | 27.3                 |
| Mistral 7B v0.3 (instruct, Q6K quantization)    | 32K            | 27.2                 |
| CodeGemma v1.5 7B (instruct, Q6K quantization)  | 8K             | 22.7                 |
| Mistral 7B v0.3 (instruct, Q3KS quantization)   | 32K            | 20.9                 |
| Qwen 4B v1.5 (text, Q6K quantization)           | 32K            | 11.6                 |


### Commercial models


#### gpt-4o-20240513 (self-evaluation) => 43,4 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 9.0   |
| cat01_02_variants_roadtraffic_anomalies| 8.0   |
| cat01_03_bpic2020_var_descr            | 8.0   |
| cat01_04_roadtraffic_var_descr         | 9.0   |
| cat01_05_bpic2020_dfg_descr            | 9.5   |
| cat01_06_roadtraffic_dfg_descr         | 8.0   |
| cat01_07_ocel_container_description    | 6.0   |
| cat01_08_ocel_logistics_description    | 8.0   |
| cat01_09_ocel_container_rca            | 8.5   |
| cat01_10_ocel_logistics_rca            | 8.0   |
| cat02_01_open_event_abstraction        | 9.0   |
| cat02_02_open_process_cubes            | 9.0   |
| cat02_03_open_decomposition_strategies | 10.0  |
| cat02_04_open_trace_clustering         | 9.0   |
| cat02_05_open_rpa                      | 9.0   |
| cat02_06_open_anomaly_detection        | 9.0   |
| cat02_07_open_process_enhancement      | 9.5   |
| cat02_08_closed_process_mining         | 9.0   |
| cat02_09_closed_petri_nets             | 8.5   |
| cat03_01_temp_profile_generation       | 9.0   |
| cat03_02_declare_generation            | 7.0   |
| cat03_03_log_skeleton_generation       | 7.0   |
| cat03_04_process_tree_generation       | 8.5   |
| cat03_05_powl_generation               | 8.5   |
| cat03_06_temp_profile_discovery        | 6.5   |
| cat03_07_declare_discovery             | 8.5   |
| cat03_08_log_skeleton_discovery        | 5.0   |
| cat04_01_bpmn_xml_tasks                | 10.0  |
| cat04_02_bpmn_json_description         | 7.0   |
| cat04_03_bpmn_simp_xml_description     | 7.5   |
| cat04_04_declare_description           | 7.5   |
| cat04_05_declare_anomalies             | 9.0   |
| cat04_06_log_skeleton_description      | 8.5   |
| cat04_07_log_skeleton_anomalies        | 7.5   |
| cat05_01_hypothesis_bpic2020           | 9.0   |
| cat05_02_hypothesis_roadtraffic        | 6.0   |
| cat05_03_hypothesis_bpmn_json          | 8.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 8.5   |
| cat06_01_renting_attributes            | 8.0   |
| cat06_02_hiring_attributes             | 9.0   |
| cat06_03_lending_attributes            | 8.5   |
| cat06_04_hospital_attributes           | 9.0   |
| cat06_05_renting_prot_comp             | 8.0   |
| cat06_06_hiring_prot_comp              | 8.0   |
| cat06_07_lending_prot_comp             | 9.0   |
| cat06_08_hospital_prot_comp            | 8.5   |
| cat07_01_dotted_chart                  | 8.5   |
| cat07_02_perf_spectrum                 | 9.0   |
| cat07_03_running-example               | 9.0   |
| cat07_04_credit-score                  | 9.5   |
| cat07_05_dfg_ru                        | 9.5   |
| cat07_06_process_tree_ru               | 8.0   |

#### gpt-4-turbo-20240409 => 42,3 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 8.5   |
| cat01_02_variants_roadtraffic_anomalies| 6.5   |
| cat01_03_bpic2020_var_descr            | 8.0   |
| cat01_04_roadtraffic_var_descr         | 8.5   |
| cat01_05_bpic2020_dfg_descr            | 7.5   |
| cat01_06_roadtraffic_dfg_descr         | 8.0   |
| cat01_07_ocel_container_description    | 8.0   |
| cat01_08_ocel_logistics_description    | 8.5   |
| cat01_09_ocel_container_rca            | 8.5   |
| cat01_10_ocel_logistics_rca            | 7.0   |
| cat02_01_open_event_abstraction        | 9.0   |
| cat02_02_open_process_cubes            | 9.0   |
| cat02_03_open_decomposition_strategies | 8.5   |
| cat02_04_open_trace_clustering         | 8.5   |
| cat02_05_open_rpa                      | 9.0   |
| cat02_06_open_anomaly_detection        | 9.2   |
| cat02_07_open_process_enhancement      | 8.5   |
| cat02_08_closed_process_mining         | 9.0   |
| cat02_09_closed_petri_nets             | 8.0   |
| cat03_01_temp_profile_generation       | 9.0   |
| cat03_02_declare_generation            | 7.0   |
| cat03_03_log_skeleton_generation       | 6.5   |
| cat03_04_process_tree_generation       | 9.0   |
| cat03_05_powl_generation               | 6.5   |
| cat03_06_temp_profile_discovery        | 7.0   |
| cat03_07_declare_discovery             | 9.0   |
| cat03_08_log_skeleton_discovery        | 7.5   |
| cat04_01_bpmn_xml_tasks                | 9.5   |
| cat04_02_bpmn_json_description         | 9.1   |
| cat04_03_bpmn_simp_xml_description     | 9.5   |
| cat04_04_declare_description           | 8.5   |
| cat04_05_declare_anomalies             | 8.0   |
| cat04_06_log_skeleton_description      | 7.0   |
| cat04_07_log_skeleton_anomalies        | 6.0   |
| cat05_01_hypothesis_bpic2020           | 8.0   |
| cat05_02_hypothesis_roadtraffic        | 8.5   |
| cat05_03_hypothesis_bpmn_json          | 7.5   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 7.0   |
| cat06_01_renting_attributes            | 9.0   |
| cat06_02_hiring_attributes             | 9.3   |
| cat06_03_lending_attributes            | 8.0   |
| cat06_04_hospital_attributes           | 9.0   |
| cat06_05_renting_prot_comp             | 8.0   |
| cat06_06_hiring_prot_comp              | 7.5   |
| cat06_07_lending_prot_comp             | 8.0   |
| cat06_08_hospital_prot_comp            | 4.5   |
| cat07_01_dotted_chart                  | 9.0   |
| cat07_02_perf_spectrum                 | 9.0   |
| cat07_03_running-example               | 9.0   |
| cat07_04_credit-score                  | 9.0   |
| cat07_05_dfg_ru                        | 8.0   |
| cat07_06_process_tree_ru               | 8.0   |


#### gpt-3.5-turbo-0125 => 32,6 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 8.9   |
| cat01_02_variants_roadtraffic_anomalies| 3.0   |
| cat01_03_bpic2020_var_descr            | 4.7   |
| cat01_04_roadtraffic_var_descr         | 7.5   |
| cat01_05_bpic2020_dfg_descr            | 8.0   |
| cat01_06_roadtraffic_dfg_descr         | 7.5   |
| cat01_07_ocel_container_description    | 7.0   |
| cat01_08_ocel_logistics_description    | 7.0   |
| cat01_09_ocel_container_rca            | 5.0   |
| cat01_10_ocel_logistics_rca            | 8.0   |
| cat02_01_open_event_abstraction        | 8.0   |
| cat02_02_open_process_cubes            | 8.5   |
| cat02_03_open_decomposition_strategies | 8.5   |
| cat02_04_open_trace_clustering         | 7.0   |
| cat02_05_open_rpa                      | 9.0   |
| cat02_06_open_anomaly_detection        | 8.0   |
| cat02_07_open_process_enhancement      | 8.5   |
| cat02_08_closed_process_mining         | 8.0   |
| cat02_09_closed_petri_nets             | 7.0   |
| cat03_01_temp_profile_generation       | 8.8   |
| cat03_02_declare_generation            | 4.0   |
| cat03_03_log_skeleton_generation       | 8.0   |
| cat03_04_process_tree_generation       | 7.0   |
| cat03_05_powl_generation               | 6.0   |
| cat03_06_temp_profile_discovery        | 3.0   |
| cat03_07_declare_discovery             | 5.0   |
| cat03_08_log_skeleton_discovery        | 6.0   |
| cat04_01_bpmn_xml_tasks                | 10.0  |
| cat04_02_bpmn_json_description         | 8.0   |
| cat04_03_bpmn_simp_xml_description     | 8.0   |
| cat04_04_declare_description           | 6.0   |
| cat04_05_declare_anomalies             | 3.0   |
| cat04_06_log_skeleton_description      | 5.5   |
| cat04_07_log_skeleton_anomalies        | 6.5   |
| cat05_01_hypothesis_bpic2020           | 8.0   |
| cat05_02_hypothesis_roadtraffic        | 9.0   |
| cat05_03_hypothesis_bpmn_json          | 8.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 9.0   |
| cat06_01_renting_attributes            | 9.0   |
| cat06_02_hiring_attributes             | 9.0   |
| cat06_03_lending_attributes            | 7.5   |
| cat06_04_hospital_attributes           | 9.0   |
| cat06_05_renting_prot_comp             | 7.5   |
| cat06_06_hiring_prot_comp              | 4.0   |
| cat06_07_lending_prot_comp             | 7.5   |
| cat06_08_hospital_prot_comp            | 5.0   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |


### Big Open-Source Models

#### Mixtral v0.1 8x22b (instruct, 16b quantization) => 34,7 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 7.0   |
| cat01_02_variants_roadtraffic_anomalies| 5.0   |
| cat01_03_bpic2020_var_descr            | 8.0   |
| cat01_04_roadtraffic_var_descr         | 7.0   |
| cat01_05_bpic2020_dfg_descr            | 8.0   |
| cat01_06_roadtraffic_dfg_descr         | 6.5   |
| cat01_07_ocel_container_description    | 7.0   |
| cat01_08_ocel_logistics_description    | 7.5   |
| cat01_09_ocel_container_rca            | 9.0   |
| cat01_10_ocel_logistics_rca            | 7.0   |
| cat02_01_open_event_abstraction        | 9.5   |
| cat02_02_open_process_cubes            | 8.5   |
| cat02_03_open_decomposition_strategies | 8.5   |
| cat02_04_open_trace_clustering         | 8.0   |
| cat02_05_open_rpa                      | 8.5   |
| cat02_06_open_anomaly_detection        | 9.0   |
| cat02_07_open_process_enhancement      | 9.0   |
| cat02_08_closed_process_mining         | 8.5   |
| cat02_09_closed_petri_nets             | 9.4   |
| cat03_01_temp_profile_generation       | 7.5   |
| cat03_02_declare_generation            | 6.0   |
| cat03_03_log_skeleton_generation       | 7.0   |
| cat03_04_process_tree_generation       | 2.0   |
| cat03_05_powl_generation               | 6.0   |
| cat03_06_temp_profile_discovery        | 4.5   |
| cat03_07_declare_discovery             | 6.0   |
| cat03_08_log_skeleton_discovery        | 4.0   |
| cat04_01_bpmn_xml_tasks                | 9.5   |
| cat04_02_bpmn_json_description         | 8.0   |
| cat04_03_bpmn_simp_xml_description     | 8.5   |
| cat04_04_declare_description           | 8.5   |
| cat04_05_declare_anomalies             | 5.5   |
| cat04_06_log_skeleton_description      | 6.0   |
| cat04_07_log_skeleton_anomalies        | 7.5   |
| cat05_01_hypothesis_bpic2020           | 8.0   |
| cat05_02_hypothesis_roadtraffic        | 9.0   |
| cat05_03_hypothesis_bpmn_json          | 9.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 8.5   |
| cat06_01_renting_attributes            | 9.0   |
| cat06_02_hiring_attributes             | 9.0   |
| cat06_03_lending_attributes            | 8.5   |
| cat06_04_hospital_attributes           | 9.0   |
| cat06_05_renting_prot_comp             | 8.0   |
| cat06_06_hiring_prot_comp              | 9.0   |
| cat06_07_lending_prot_comp             | 5.0   |
| cat06_08_hospital_prot_comp            | 7.5   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |


#### Llama 3 70B (instruct, 16b quantization) => 34,1 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 9.0   |
| cat01_02_variants_roadtraffic_anomalies| 5.0   |
| cat01_03_bpic2020_var_descr            | 8.0   |
| cat01_04_roadtraffic_var_descr         | 8.5   |
| cat01_05_bpic2020_dfg_descr            | 9.0   |
| cat01_06_roadtraffic_dfg_descr         | 8.0   |
| cat01_07_ocel_container_description    | 7.5   |
| cat01_08_ocel_logistics_description    | 6.5   |
| cat01_09_ocel_container_rca            | 7.5   |
| cat01_10_ocel_logistics_rca            | 7.0   |
| cat02_01_open_event_abstraction        | 8.0   |
| cat02_02_open_process_cubes            | 7.5   |
| cat02_03_open_decomposition_strategies | 8.5   |
| cat02_04_open_trace_clustering         | 8.0   |
| cat02_05_open_rpa                      | 9.0   |
| cat02_06_open_anomaly_detection        | 8.0   |
| cat02_07_open_process_enhancement      | 9.0   |
| cat02_08_closed_process_mining         | 9.4   |
| cat02_09_closed_petri_nets             | 8.6   |
| cat03_01_temp_profile_generation       | 7.5   |
| cat03_02_declare_generation            | 7.5   |
| cat03_03_log_skeleton_generation       | 9.0   |
| cat03_04_process_tree_generation       | 9.0   |
| cat03_05_powl_generation               | 5.0   |
| cat03_06_temp_profile_discovery        | 6.5   |
| cat03_07_declare_discovery             | 3.0   |
| cat03_08_log_skeleton_discovery        | 6.5   |
| cat04_01_bpmn_xml_tasks                | 9.5   |
| cat04_02_bpmn_json_description         | 5.5   |
| cat04_03_bpmn_simp_xml_description     | 7.0   |
| cat04_04_declare_description           | 7.5   |
| cat04_05_declare_anomalies             | 6.5   |
| cat04_06_log_skeleton_description      | 8.5   |
| cat04_07_log_skeleton_anomalies        | 6.5   |
| cat05_01_hypothesis_bpic2020           | 7.8   |
| cat05_02_hypothesis_roadtraffic        | 6.5   |
| cat05_03_hypothesis_bpmn_json          | 7.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 3.5   |
| cat06_01_renting_attributes            | 8.0   |
| cat06_02_hiring_attributes             | 9.0   |
| cat06_03_lending_attributes            | 8.5   |
| cat06_04_hospital_attributes           | 9.0   |
| cat06_05_renting_prot_comp             | 7.0   |
| cat06_06_hiring_prot_comp              | 4.0   |
| cat06_07_lending_prot_comp             | 7.5   |
| cat06_08_hospital_prot_comp            | 6.5   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |

## Consumer-Grade Open-Source Models (> 8GB RAM)

#### Mixtral v0.1 8x7b (instruct, 16b quantization) => 31,6 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 7.0   |
| cat01_02_variants_roadtraffic_anomalies| 6.8   |
| cat01_03_bpic2020_var_descr            | 8.6   |
| cat01_04_roadtraffic_var_descr         | 8.0   |
| cat01_05_bpic2020_dfg_descr            | 8.5   |
| cat01_06_roadtraffic_dfg_descr         | 5.5   |
| cat01_07_ocel_container_description    | 7.0   |
| cat01_08_ocel_logistics_description    | 5.5   |
| cat01_09_ocel_container_rca            | 7.5   |
| cat01_10_ocel_logistics_rca            | 5.0   |
| cat02_01_open_event_abstraction        | 8.0   |
| cat02_02_open_process_cubes            | 9.0   |
| cat02_03_open_decomposition_strategies | 8.0   |
| cat02_04_open_trace_clustering         | 8.0   |
| cat02_05_open_rpa                      | 9.0   |
| cat02_06_open_anomaly_detection        | 9.0   |
| cat02_07_open_process_enhancement      | 8.0   |
| cat02_08_closed_process_mining         | 6.5   |
| cat02_09_closed_petri_nets             | 5.0   |
| cat03_01_temp_profile_generation       | 6.0   |
| cat03_02_declare_generation            | 4.0   |
| cat03_03_log_skeleton_generation       | 6.0   |
| cat03_04_process_tree_generation       | 5.0   |
| cat03_05_powl_generation               | 7.5   |
| cat03_06_temp_profile_discovery        | 5.0   |
| cat03_07_declare_discovery             | 5.0   |
| cat03_08_log_skeleton_discovery        | 3.0   |
| cat04_01_bpmn_xml_tasks                | 8.0   |
| cat04_02_bpmn_json_description         | 6.0   |
| cat04_03_bpmn_simp_xml_description     | 5.0   |
| cat04_04_declare_description           | 6.0   |
| cat04_05_declare_anomalies             | 4.0   |
| cat04_06_log_skeleton_description      | 7.0   |
| cat04_07_log_skeleton_anomalies        | 6.5   |
| cat05_01_hypothesis_bpic2020           | 8.5   |
| cat05_02_hypothesis_roadtraffic        | 6.0   |
| cat05_03_hypothesis_bpmn_json          | 8.5   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 8.3   |
| cat06_01_renting_attributes            | 9.5   |
| cat06_02_hiring_attributes             | 10.0  |
| cat06_03_lending_attributes            | 8.0   |
| cat06_04_hospital_attributes           | 7.0   |
| cat06_05_renting_prot_comp             | 7.0   |
| cat06_06_hiring_prot_comp              | 7.0   |
| cat06_07_lending_prot_comp             | 9.0   |
| cat06_08_hospital_prot_comp            | 4.0   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |

#### Llama 3 8B (instruct, 16b quantization) => 30,2 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 7.5   |
| cat01_02_variants_roadtraffic_anomalies| 3.0   |
| cat01_03_bpic2020_var_descr            | 7.0   |
| cat01_04_roadtraffic_var_descr         | 8.0   |
| cat01_05_bpic2020_dfg_descr            | 9.0   |
| cat01_06_roadtraffic_dfg_descr         | 2.0   |
| cat01_07_ocel_container_description    | 7.0   |
| cat01_08_ocel_logistics_description    | 9.0   |
| cat01_09_ocel_container_rca            | 6.0   |
| cat01_10_ocel_logistics_rca            | 3.0   |
| cat02_01_open_event_abstraction        | 8.0   |
| cat02_02_open_process_cubes            | 8.0   |
| cat02_03_open_decomposition_strategies | 9.0   |
| cat02_04_open_trace_clustering         | 8.0   |
| cat02_05_open_rpa                      | 8.5   |
| cat02_06_open_anomaly_detection        | 9.0   |
| cat02_07_open_process_enhancement      | 8.5   |
| cat02_08_closed_process_mining         | 8.0   |
| cat02_09_closed_petri_nets             | 8.0   |
| cat03_01_temp_profile_generation       | 8.0   |
| cat03_02_declare_generation            | 5.0   |
| cat03_03_log_skeleton_generation       | 7.0   |
| cat03_04_process_tree_generation       | 5.0   |
| cat03_05_powl_generation               | 5.0   |
| cat03_06_temp_profile_discovery        | 3.0   |
| cat03_07_declare_discovery             | 3.0   |
| cat03_08_log_skeleton_discovery        | 3.0   |
| cat04_01_bpmn_xml_tasks                | 10.0  |
| cat04_02_bpmn_json_description         | 7.0   |
| cat04_03_bpmn_simp_xml_description     | 7.0   |
| cat04_04_declare_description           | 6.5   |
| cat04_05_declare_anomalies             | 6.5   |
| cat04_06_log_skeleton_description      | 6.0   |
| cat04_07_log_skeleton_anomalies        | 4.0   |
| cat05_01_hypothesis_bpic2020           | 7.5   |
| cat05_02_hypothesis_roadtraffic        | 8.0   |
| cat05_03_hypothesis_bpmn_json          | 6.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 4.5   |
| cat06_01_renting_attributes            | 7.0   |
| cat06_02_hiring_attributes             | 8.5   |
| cat06_03_lending_attributes            | 8.0   |
| cat06_04_hospital_attributes           | 8.5   |
| cat06_05_renting_prot_comp             | 5.0   |
| cat06_06_hiring_prot_comp              | 5.0   |
| cat06_07_lending_prot_comp             | 7.0   |
| cat06_08_hospital_prot_comp            | 5.0   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |


### Small Models (< 8GB RAM)


#### Llama 3 8B (instruct, Q6K quantization) => 27,3 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 4.5   |
| cat01_02_variants_roadtraffic_anomalies| 3.0   |
| cat01_03_bpic2020_var_descr            | 7.5   |
| cat01_04_roadtraffic_var_descr         | 7.5   |
| cat01_05_bpic2020_dfg_descr            | 6.0   |
| cat01_06_roadtraffic_dfg_descr         | 7.5   |
| cat01_07_ocel_container_description    | 3.5   |
| cat01_08_ocel_logistics_description    | 5.0   |
| cat01_09_ocel_container_rca            | 6.0   |
| cat01_10_ocel_logistics_rca            | 4.0   |
| cat02_01_open_event_abstraction        | 9.0   |
| cat02_02_open_process_cubes            | 8.0   |
| cat02_03_open_decomposition_strategies | 8.5   |
| cat02_04_open_trace_clustering         | 8.5   |
| cat02_05_open_rpa                      | 9.0   |
| cat02_06_open_anomaly_detection        | 8.0   |
| cat02_07_open_process_enhancement      | 8.5   |
| cat02_08_closed_process_mining         | 8.5   |
| cat02_09_closed_petri_nets             | 7.0   |
| cat03_01_temp_profile_generation       | 8.5   |
| cat03_02_declare_generation            | 3.0   |
| cat03_03_log_skeleton_generation       | 6.0   |
| cat03_04_process_tree_generation       | 6.0   |
| cat03_05_powl_generation               | 8.0   |
| cat03_06_temp_profile_discovery        | 3.0   |
| cat03_07_declare_discovery             | 1.0   |
| cat03_08_log_skeleton_discovery        | 2.0   |
| cat04_01_bpmn_xml_tasks                | 1.0   |
| cat04_02_bpmn_json_description         | 2.0   |
| cat04_03_bpmn_simp_xml_description     | 6.5   |
| cat04_04_declare_description           | 5.0   |
| cat04_05_declare_anomalies             | 4.0   |
| cat04_06_log_skeleton_description      | 7.0   |
| cat04_07_log_skeleton_anomalies        | 1.5   |
| cat05_01_hypothesis_bpic2020           | 7.5   |
| cat05_02_hypothesis_roadtraffic        | 9.0   |
| cat05_03_hypothesis_bpmn_json          | 8.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 7.0   |
| cat06_01_renting_attributes            | 7.0   |
| cat06_02_hiring_attributes             | 8.0   |
| cat06_03_lending_attributes            | 9.0   |
| cat06_04_hospital_attributes           | 8.5   |
| cat06_05_renting_prot_comp             | 3.0   |
| cat06_06_hiring_prot_comp              | 6.0   |
| cat06_07_lending_prot_comp             | 4.0   |
| cat06_08_hospital_prot_comp            | 2.0   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |


#### Mistral 7B v0.3 (instruct, Q6K quantization) => 27,2 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 7.5   |
| cat01_02_variants_roadtraffic_anomalies| 3.5   |
| cat01_03_bpic2020_var_descr            | 8.0   |
| cat01_04_roadtraffic_var_descr         | 6.0   |
| cat01_05_bpic2020_dfg_descr            | 4.0   |
| cat01_06_roadtraffic_dfg_descr         | 6.0   |
| cat01_07_ocel_container_description    | 6.0   |
| cat01_08_ocel_logistics_description    | 6.3   |
| cat01_09_ocel_container_rca            | 5.0   |
| cat01_10_ocel_logistics_rca            | 4.0   |
| cat02_01_open_event_abstraction        | 8.5   |
| cat02_02_open_process_cubes            | 8.0   |
| cat02_03_open_decomposition_strategies | 8.5   |
| cat02_04_open_trace_clustering         | 8.5   |
| cat02_05_open_rpa                      | 9.0   |
| cat02_06_open_anomaly_detection        | 9.0   |
| cat02_07_open_process_enhancement      | 9.0   |
| cat02_08_closed_process_mining         | 9.9   |
| cat02_09_closed_petri_nets             | 8.0   |
| cat03_01_temp_profile_generation       | 9.0   |
| cat03_02_declare_generation            | 3.0   |
| cat03_03_log_skeleton_generation       | 8.0   |
| cat03_04_process_tree_generation       | 5.0   |
| cat03_05_powl_generation               | 8.5   |
| cat03_06_temp_profile_discovery        | 2.0   |
| cat03_07_declare_discovery             | 1.0   |
| cat03_08_log_skeleton_discovery        | 2.0   |
| cat04_01_bpmn_xml_tasks                | 2.0   |
| cat04_02_bpmn_json_description         | 3.0   |
| cat04_03_bpmn_simp_xml_description     | 3.0   |
| cat04_04_declare_description           | 7.6   |
| cat04_05_declare_anomalies             | 2.0   |
| cat04_06_log_skeleton_description      | 7.0   |
| cat04_07_log_skeleton_anomalies        | 6.0   |
| cat05_01_hypothesis_bpic2020           | 7.5   |
| cat05_02_hypothesis_roadtraffic        | 8.3   |
| cat05_03_hypothesis_bpmn_json          | 6.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 8.0   |
| cat06_01_renting_attributes            | 3.0   |
| cat06_02_hiring_attributes             | 8.0   |
| cat06_03_lending_attributes            | 7.5   |
| cat06_04_hospital_attributes           | 7.0   |
| cat06_05_renting_prot_comp             | 4.0   |
| cat06_06_hiring_prot_comp              | 3.6   |
| cat06_07_lending_prot_comp             | 2.0   |
| cat06_08_hospital_prot_comp            | 4.0   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |


#### CodeGemma v1.5 7B (instruct, Q6K quantization) => 22,7 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 1.0   |
| cat01_02_variants_roadtraffic_anomalies| 2.5   |
| cat01_03_bpic2020_var_descr            | 7.5   |
| cat01_04_roadtraffic_var_descr         | 5.0   |
| cat01_05_bpic2020_dfg_descr            | 9.0   |
| cat01_06_roadtraffic_dfg_descr         | 4.5   |
| cat01_07_ocel_container_description    | 3.5   |
| cat01_08_ocel_logistics_description    | 3.0   |
| cat01_09_ocel_container_rca            | 4.5   |
| cat01_10_ocel_logistics_rca            | 4.0   |
| cat02_01_open_event_abstraction        | 8.0   |
| cat02_02_open_process_cubes            | 8.5   |
| cat02_03_open_decomposition_strategies | 8.0   |
| cat02_04_open_trace_clustering         | 9.0   |
| cat02_05_open_rpa                      | 8.5   |
| cat02_06_open_anomaly_detection        | 8.5   |
| cat02_07_open_process_enhancement      | 9.0   |
| cat02_08_closed_process_mining         | 8.5   |
| cat02_09_closed_petri_nets             | 7.0   |
| cat03_01_temp_profile_generation       | 7.5   |
| cat03_02_declare_generation            | 4.0   |
| cat03_03_log_skeleton_generation       | 7.0   |
| cat03_04_process_tree_generation       | 4.0   |
| cat03_05_powl_generation               | 7.0   |
| cat03_06_temp_profile_discovery        | 3.0   |
| cat03_07_declare_discovery             | 2.0   |
| cat03_08_log_skeleton_discovery        | 1.0   |
| cat04_01_bpmn_xml_tasks                | 1.0   |
| cat04_02_bpmn_json_description         | 3.0   |
| cat04_03_bpmn_simp_xml_description     | 1.5   |
| cat04_04_declare_description           | 3.0   |
| cat04_05_declare_anomalies             | 4.0   |
| cat04_06_log_skeleton_description      | 5.0   |
| cat04_07_log_skeleton_anomalies        | 2.5   |
| cat05_01_hypothesis_bpic2020           | 7.0   |
| cat05_02_hypothesis_roadtraffic        | 3.0   |
| cat05_03_hypothesis_bpmn_json          | 8.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 1.0   |
| cat06_01_renting_attributes            | 3.0   |
| cat06_02_hiring_attributes             | 3.0   |
| cat06_03_lending_attributes            | 8.5   |
| cat06_04_hospital_attributes           | 4.5   |
| cat06_05_renting_prot_comp             | 2.0   |
| cat06_06_hiring_prot_comp              | 3.0   |
| cat06_07_lending_prot_comp             | 3.0   |
| cat06_08_hospital_prot_comp            | 6.0   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |


### Very Small Models (< 4GB RAM)

#### Mistral 7B v0.3 (instruct, Q3KS quantization) => 20,9 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 4.0   |
| cat01_02_variants_roadtraffic_anomalies| 2.0   |
| cat01_03_bpic2020_var_descr            | 6.0   |
| cat01_04_roadtraffic_var_descr         | 2.0   |
| cat01_05_bpic2020_dfg_descr            | 6.0   |
| cat01_06_roadtraffic_dfg_descr         | 4.0   |
| cat01_07_ocel_container_description    | 4.0   |
| cat01_08_ocel_logistics_description    | 6.0   |
| cat01_09_ocel_container_rca            | 2.0   |
| cat01_10_ocel_logistics_rca            | 3.0   |
| cat02_01_open_event_abstraction        | 7.0   |
| cat02_02_open_process_cubes            | 7.5   |
| cat02_03_open_decomposition_strategies | 8.0   |
| cat02_04_open_trace_clustering         | 7.5   |
| cat02_05_open_rpa                      | 9.0   |
| cat02_06_open_anomaly_detection        | 8.0   |
| cat02_07_open_process_enhancement      | 8.0   |
| cat02_08_closed_process_mining         | 9.0   |
| cat02_09_closed_petri_nets             | 3.0   |
| cat03_01_temp_profile_generation       | 4.0   |
| cat03_02_declare_generation            | 3.0   |
| cat03_03_log_skeleton_generation       | 3.0   |
| cat03_04_process_tree_generation       | 6.0   |
| cat03_05_powl_generation               | 5.0   |
| cat03_06_temp_profile_discovery        | 2.0   |
| cat03_07_declare_discovery             | 1.0   |
| cat03_08_log_skeleton_discovery        | 1.0   |
| cat04_01_bpmn_xml_tasks                | 3.0   |
| cat04_02_bpmn_json_description         | 4.0   |
| cat04_03_bpmn_simp_xml_description     | 2.0   |
| cat04_04_declare_description           | 3.0   |
| cat04_05_declare_anomalies             | 3.0   |
| cat04_06_log_skeleton_description      | 3.0   |
| cat04_07_log_skeleton_anomalies        | 3.0   |
| cat05_01_hypothesis_bpic2020           | 5.5   |
| cat05_02_hypothesis_roadtraffic        | 5.0   |
| cat05_03_hypothesis_bpmn_json          | 7.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 5.9   |
| cat06_01_renting_attributes            | 4.0   |
| cat06_02_hiring_attributes             | 8.0   |
| cat06_03_lending_attributes            | 4.0   |
| cat06_04_hospital_attributes           | 7.0   |
| cat06_05_renting_prot_comp             | 2.0   |
| cat06_06_hiring_prot_comp              | 3.5   |
| cat06_07_lending_prot_comp             | 3.0   |
| cat06_08_hospital_prot_comp            | 3.0   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |

#### Qwen 4B v1.5 (text, Q6K quantization) => 11,6 (/52) points

| Question                               | Score |
|----------------------------------------|-------|
| cat01_01_variants_bpic2020_rca         | 1.0   |
| cat01_02_variants_roadtraffic_anomalies| 1.0   |
| cat01_03_bpic2020_var_descr            | 1.6   |
| cat01_04_roadtraffic_var_descr         | 1.0   |
| cat01_05_bpic2020_dfg_descr            | 1.0   |
| cat01_06_roadtraffic_dfg_descr         | 8.0   |
| cat01_07_ocel_container_description    | 2.0   |
| cat01_08_ocel_logistics_description    | 2.0   |
| cat01_09_ocel_container_rca            | 2.0   |
| cat01_10_ocel_logistics_rca            | 1.0   |
| cat02_01_open_event_abstraction        | 3.0   |
| cat02_02_open_process_cubes            | 3.5   |
| cat02_03_open_decomposition_strategies | 5.0   |
| cat02_04_open_trace_clustering         | 6.5   |
| cat02_05_open_rpa                      | 6.5   |
| cat02_06_open_anomaly_detection        | 5.0   |
| cat02_07_open_process_enhancement      | 5.5   |
| cat02_08_closed_process_mining         | 3.0   |
| cat02_09_closed_petri_nets             | 2.0   |
| cat03_01_temp_profile_generation       | 1.0   |
| cat03_02_declare_generation            | 1.0   |
| cat03_03_log_skeleton_generation       | 3.5   |
| cat03_04_process_tree_generation       | 4.4   |
| cat03_05_powl_generation               | 1.0   |
| cat03_06_temp_profile_discovery        | 1.0   |
| cat03_07_declare_discovery             | 1.0   |
| cat03_08_log_skeleton_discovery        | 1.0   |
| cat04_01_bpmn_xml_tasks                | 1.0   |
| cat04_02_bpmn_json_description         | 1.0   |
| cat04_03_bpmn_simp_xml_description     | 1.0   |
| cat04_04_declare_description           | 1.0   |
| cat04_05_declare_anomalies             | 2.0   |
| cat04_06_log_skeleton_description      | 1.0   |
| cat04_07_log_skeleton_anomalies        | 2.0   |
| cat05_01_hypothesis_bpic2020           | 2.0   |
| cat05_02_hypothesis_roadtraffic        | 9.0   |
| cat05_03_hypothesis_bpmn_json          | 2.0   |
| cat05_04_hypothesis_bpmn_simpl_xml     | 9.0   |
| cat06_01_renting_attributes            | 1.0   |
| cat06_02_hiring_attributes             | 1.0   |
| cat06_03_lending_attributes            | 1.0   |
| cat06_04_hospital_attributes           | 2.0   |
| cat06_05_renting_prot_comp             | 2.0   |
| cat06_06_hiring_prot_comp              | 1.0   |
| cat06_07_lending_prot_comp             | 2.0   |
| cat06_08_hospital_prot_comp            | 1.0   |
| cat07_01_dotted_chart                  |       |
| cat07_02_perf_spectrum                 |       |
| cat07_03_running-example               |       |
| cat07_04_credit-score                  |       |
| cat07_05_dfg_ru                        |       |
| cat07_06_process_tree_ru               |       |
