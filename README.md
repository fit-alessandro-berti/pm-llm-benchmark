# PM-LLM-Benchmark

A qualitative benchmark for PM-on-LLM. The LLM's answers are intended to be graded by another expert LLM (LLM-as-a-Judge).

The prompts are reported in the *questions/* folder.

Procedure for every prompt:
* Provide the prompt to a LLM:
  * For textual prompts, report the content as-is
  * (When supported) For images, upload the image to the LVLM and ask *Can you describe the provided visualization?*
* Annotate the output
* Use the expert LLM (LLM-as-a-Judge) to evaluate the output. Template:
  * For textual prompts, *Given the following question: ... How would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? ...*
  * (When supported) For images, upload the image to the LVLM and ask *Given the attached image, how would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? ...*

The final score of the benchmark is obtained summing the scores and dividing by 10.0.

## Preliminary Scores (1-shot, gpt-4o as a judge)

### Commercial models


#### gpt-4o (self-evaluation) => 43,4 (/53) points

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

