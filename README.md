# PM-LLM-Benchmark v 2.2

**The current repository shows PM-LLM-Benchmark v 2.2, which contains a different and more complex set of prompts than PM-LLM-Benchmark v 1.0**
The paper describing PM-LLM-Benchmark v 1.0 is available [here](https://arxiv.org/pdf/2407.13244)

Process mining benefits significantly from the domain knowledge provided by LLMs. However, no process-mining-specific LLM benchmarks have been proposed
until the current date.
We propose *PM-LLM-Benchmark*, a qualitative benchmark for PM-on-LLM. The LLM's answers are intended to be graded by another expert LLM (LLM-as-a-Judge).

The prompts are reported in the *questions/* folder.

## Textual Question Index

| Question | First 50 chars | Last 50 chars |
| --- | --- | --- |
| `cat01_01` | Below is a complex, interleaved sequence of hospit | e case IDs from this complex interleaved sequence. |
| `cat01_02` | **Prompt:**  You are given a process event log fro | ng the contextual clues that led to those changes. |
| `cat01_03` | **Prompt:**  You are given a complex event log fro | nces to more meaningful aggregated process stages. |
| `cat01_04` | **Prompt:**  You have been given a log of events f | , deriving a labeled process from a raw event log. |
| `cat01_05` | **Prompt:**  You are given two separate event logs | l as how you integrated attributes from both logs. |
| `cat01_06` | You are an expert AI assistant with deep knowledge | pp=Microsoft Word,Window=Quarterly_Report.docx ``` |
| `cat01_07` | **Prompt:**  **Context:**   You have been provided | eptions within a fairly standard business process. |
| `cat01_08` | **Prompt:**  You are given several tables extracte |       \| Irene Park       \| Billing Clerk    \|  --- |
| `cat02_01` | **Prompt:**  You are given a textual description o | d interpreting any ambiguities as best as you can. |
| `cat02_02` | **Part 1: Normative Process Behavior (Strict Rules | ne with the given constraints and recommendations. |
| `cat02_03` | **Prompt:**  You are given an event log from a wel |  Explain why these anomalies might be problematic. |
| `cat02_04` | **Prompt:**  You are given a POWL (Partially Order | loop_approve_invoice, P) root.order.add_edge(P, O) |
| `cat02_05` | **Prompt:**  In this task, you are given two POWL  | ch model affect process correctness and integrity. |
| `cat02_06` | **Prompt:**  You are presented with an event log o |  that might address these performance bottlenecks. |
| `cat02_07` | **Prompt:**  You are given an event log of an “I | d offer suggestions to mitigate these root causes. |
| `cat02_08` | **Prompt:**  You are given a process tree model th |  operations required by the Order-to-Cash process. |
| `cat02_09` | **Prompt:**  Below is a process tree model represe | e domain’s logic and prevents unwanted behavior. |
| `cat03_01` | **Prompt:**  PROCESS TREE   A process tree is a hi | the notation for activities or silent steps (tau). |
| `cat03_02` | **Prompt:**  POWL (PARTIALLY ORDERED WORKFLOW LANG | rating the loop and exclusive choice as described. |
| `cat03_03` | **Prompt:**  LOG SKELETON   The Log Skeleton proce | resenting the Log Skeleton for the given scenario. |
| `cat03_04` | **Prompt:**  DECLARE   A DECLARE model in pm4py is |  representing the DECLARE model for this scenario. |
| `cat03_05` | **Prompt:**  TEMPORAL PROFILE   The temporal profi | ctivities that may be separated by multiple steps. |
| `cat03_06` | **Prompt:**  ACCEPTING PETRI NET   A Petri net plu | h the initial marking (im) and final marking (fm). |
| `cat03_07` | **Prompt:**  PROCESS TREE   A process tree is a hi | the eventual approval, confirmation, and archival. |
| `cat03_08` | **Prompt:**  POWL (PARTIALLY ORDERED WORKFLOW LANG |  \| 5       \| D         \| 2024-06-03 14:00   \|  --- |
| `cat04_01` | **Pseudo-BPMN Representation:**  ``` Start Event - | nditions approvals or rework steps are triggered." |
| `cat04_02` | **Pseudo-BPMN Representation:**  ``` Start Event - | ustomer satisfaction, and operational complexity." |
| `cat04_03` | **Real-Life DECLARE Model Representation:**  ```py | might lead to such a stringent set of conditions." |
| `cat04_04` | Below is a complete prompt you could provide to a  | scribed order or if mandatory steps were omitted." |
| `cat04_05` | **Draft Prompt for the Benchmark:**  "Assume you h | ct grouping and filtering to achieve this result." |
| `cat04_06` | **Prompt for the Benchmark:**  "Consider an event  |  events from the cases that are not filtered out." |
| `cat04_07` | **Prompt for the Benchmark:**  "Consider an event  | e corresponding events from those filtered cases." |
| `cat05_01` | ### Underlying Database and Schema  **Database Typ | rther without any hints or guidance provided here. |
| `cat05_02` | ### Underlying Database Context  **Database Type:* | fication steps are frequently skipped in practice. |
| `cat05_03` | ### Underlying Database Context  **Database Type:* |  SQL-based investigation strategies independently. |
| `cat05_04` | Below is a proposed scenario involving a temporal  | e reasons, and verification queries independently. |
| `cat05_05` | **Process Description (in natural language):**  Co |  provide any SQL queries; just list the questions. |
| `cat05_06` | **Pseudo-BPMN Representation of the Process (Textu |  provide any SQL queries; just list the questions. |
| `cat05_07` | **Long Process Description:**  Imagine a large-sca | arity on this complex property onboarding process. |
| `cat06_01` | **Process Description:**  The lending division of  | impact on fairness and equity for all applicants.* |
| `cat06_02` | **Event Log**  \| CaseID \| Activity             \| T | hen their underlying creditworthiness is similar.* |
| `cat06_03` | ```python import pm4py from pm4py.objects.powl.obj | irness and equity in the final loan decisions.”* |
| `cat06_04` | ---  **Event Log for Group A (Protected Group)**   |  to systematic differences in final decisions.”* |
| `cat06_05` | ---  **Event Log for Group A (Protected Group)**   | for fairness and equity in the hiring process.”* |
| `cat06_06` | ---  **Prompt:**  You are given a process model re | aints reduce bias in the loan application process. |
| `cat06_07` | The following is a long textual description of a c | (nodes=[loop, xor]) root.order.add_edge(loop, xor) |
| `cat08_01` | **Scenario Context:**  A large multi-specialty out | ta-driven insights and actionable recommendations. |
| `cat08_02` | **Scenario Context:**  An e-commerce company opera | roduced by dependencies between process instances. |
| `cat08_03` | **Scenario Context:**  "Speedy Parcels," a regiona | otential insights within the described event data. |
| `cat08_04` | **Scenario Context:**  "TechSolve Solutions" provi | and assignment patterns within the event log data. |
| `cat08_05` | **Scenario Context:**  "Precision Parts Inc." oper | ifficulty and complexity inherent in the scenario. |

Procedure for every prompt:
* Provide the prompt to a LLM:
  * For textual prompts, report the content as-is
  * (When supported) For images, upload the image to the LVLM and ask *Can you describe the provided visualization?*
* Annotate the output
* Use the expert LLM (LLM-as-a-Judge) to evaluate the output. Template:
  * For textual prompts, *Given the following question: ... How would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? ...*
  * (When supported) For images, upload the image to the LVLM and ask *Given the attached image, how would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? ...*

The final score of the benchmark is obtained by summing the scores and dividing by 10.0.

Some scripts to execute and evaluate the questions against OpenAI's APIs are available in **answer.py** and **evalscript.py**.
The API key should be configured inside **answering_api_key.txt** and **judge_api_key.txt**.
The responding model (and the API URL) can be configured inside the corresponding scripts.

The benchmark includes different categories of questions:
- **Category 1:** Assesses the contextual understanding of the LLM in process mining tasks. Various tasks, such as case ID inference, contextual splitting of activity labels, and defining high-level events, are considered.  
- **Category 2:** Evaluates the LLM’s ability to perform conformance checking and anomaly detection, starting from textual descriptions, event logs, or procedural process models.  
- **Category 3:** Tests the LLM’s capacity to generate and modify declarative and procedural process models.  
- **Category 4:** Measures the LLM’s process querying abilities, encompassing both procedural and declarative process models.  
- **Category 5:** Examines the LLM’s ability to generate valid hypotheses and questions based on the provided artifacts.  
- **Category 6:** Assesses the LLM’s ability to identify and propose solutions for unfairness in processes.  
- **Category 7:** Evaluates the LLM’s ability to read and interpret process mining diagrams.  
- **Category 8:** Evaluates the LLM’s ability to perform process optimizations in popular scenarios.  

## Leaderboards

The leaderboards include the results of the benchmark, as evaluated by the considered judge LLM:

(**2026-03-11 TO NOW**) [gpt-5.4](leaderboard_gpt-5.4.md)

* (v2.2, OLD, 2025-11-20 TO NOW) [grok-4-1-fast](old/OLD_v2_2_leaderboard_grok-4-1-fast-reasoning.md)
* (v2.2, OLD, 2025-09-20 TO 2025-11-20) [grok-4-fast](old/OLD_v2_2_leaderboard_grok-4-fast.md)
* (v2.2, OLD, 2025-03-27 TO 2025-09-19) [gemini-2.5-pro](old/OLD_v2_2_leaderboard_gemini-2.5-pro.md)
* (v2.0, OLD, 2024-12-13 TO 2025-03-26) [gpt-4o-2024-11-20](old/OLD_v2_leaderboard_gpt-4o-2024-11-20.md)
* (v1, OLD, 2024-10-31 TO 2024-12-12) [v1-leaderboard](old/OLD_v1_leaderboard_chatgpt-4o-latest.md)
