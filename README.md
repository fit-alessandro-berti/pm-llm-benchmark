# PM-LLM-Benchmark v 2.2

**The current repository shows PM-LLM-Benchmark v 2.2, which contains a different and more complex set of prompts than PM-LLM-Benchmark v 1.0**
The paper describing PM-LLM-Benchmark v 1.0 is available [here](https://arxiv.org/pdf/2407.13244)

Process mining benefits significantly from the domain knowledge provided by LLMs. However, no process-mining-specific LLM benchmarks have been proposed
until the current date.
We propose *PM-LLM-Benchmark*, a qualitative benchmark for PM-on-LLM. The LLM's answers are intended to be graded by another expert LLM (LLM-as-a-Judge).

The prompts are reported in the *questions/* folder.

## Textual Question Index

| Question | First 80 chars |
| --- | --- |
| `cat01_01` | Below is a complex, interleaved sequence of hospital process events. Each line r |
| `cat01_02` | **Prompt:**  You are given a process event log from a complex support workflow a |
| `cat01_03` | **Prompt:**  You are given a complex event log from a manufacturing process that |
| `cat01_04` | **Prompt:**  You have been given a log of events from a manufacturing assembly l |
| `cat01_05` | **Prompt:**  You are given two separate event logs, **Log A** (from System A) an |
| `cat01_06` | You are an expert AI assistant with deep knowledge in process mining. Your task  |
| `cat01_07` | **Prompt:**  **Context:**   You have been provided with transcripts from a serie |
| `cat01_08` | **Prompt:**  You are given several tables extracted from an ERP system. These ta |
| `cat02_01` | **Prompt:**  You are given a textual description of a normative process for hand |
| `cat02_02` | **Part 1: Normative Process Behavior (Strict Rules)**   **Textual Description:** |
| `cat02_03` | **Prompt:**  You are given an event log from a well-known business process commo |
| `cat02_04` | **Prompt:**  You are given a POWL (Partially Ordered Workflow Language) model de |
| `cat02_05` | **Prompt:**  In this task, you are given two POWL (Partially Ordered Workflow La |
| `cat02_06` | **Prompt:**  You are presented with an event log of a “Customer Support Ticket |
| `cat02_07` | **Prompt:**  You are given an event log of an “Insurance Claims Processing”  |
| `cat02_08` | **Prompt:**  You are given a process tree model that is intended to represent a  |
| `cat02_09` | **Prompt:**  Below is a process tree model representing a simplified "Procure-to |
| `cat03_01` | **Prompt:**  PROCESS TREE   A process tree is a hierarchical process model.   Th |
| `cat03_02` | **Prompt:**  POWL (PARTIALLY ORDERED WORKFLOW LANGUAGE) MODELS   A partially ord |
| `cat03_03` | **Prompt:**  LOG SKELETON   The Log Skeleton process model contains the followin |
| `cat03_04` | **Prompt:**  DECLARE   A DECLARE model in pm4py is expressed as a Python diction |
| `cat03_05` | **Prompt:**  TEMPORAL PROFILE   The temporal profile is a model describing the a |
| `cat03_06` | **Prompt:**  ACCEPTING PETRI NET   A Petri net plus an initial and a final marki |
| `cat03_07` | **Prompt:**  PROCESS TREE   A process tree is a hierarchical process model.   Th |
| `cat03_08` | **Prompt:**  POWL (PARTIALLY ORDERED WORKFLOW LANGUAGE) MODELS   A partially ord |
| `cat04_01` | **Pseudo-BPMN Representation:**  ``` Start Event --> Task A: "Receive Customer R |
| `cat04_02` | **Pseudo-BPMN Representation:**  ``` Start Event --> Task A: "Receive Customer R |
| `cat04_03` | **Real-Life DECLARE Model Representation:**  ```python declare_model = {     'ex |
| `cat04_04` | Below is a complete prompt you could provide to a target LLM, including the DECL |
| `cat04_05` | **Draft Prompt for the Benchmark:**  "Assume you have an event log stored in a D |
| `cat04_06` | **Prompt for the Benchmark:**  "Consider an event log stored in a DuckDB table n |
| `cat04_07` | **Prompt for the Benchmark:**  "Consider an event log stored in a DuckDB table n |
| `cat05_01` | ### Underlying Database and Schema  **Database Type:** PostgreSQL  **Schema Desc |
| `cat05_02` | ### Underlying Database Context  **Database Type:** PostgreSQL  **Schema Descrip |
| `cat05_03` | ### Underlying Database Context  **Database Type:** PostgreSQL  **Schema Descrip |
| `cat05_04` | Below is a proposed scenario involving a temporal profile model for an insurance |
| `cat05_05` | **Process Description (in natural language):**  Consider a complex, multinationa |
| `cat05_06` | **Pseudo-BPMN Representation of the Process (Textual Approximation)**  ``` Start |
| `cat05_07` | **Long Process Description:**  Imagine a large-scale property management company |
| `cat06_01` | **Process Description:**  The lending division of Argentum Financial Inc. uses a |
| `cat06_02` | **Event Log**  \| CaseID \| Activity             \| Timestamp           \| LocalResi |
| `cat06_03` | ```python import pm4py from pm4py.objects.powl.obj import StrictPartialOrder, Op |
| `cat06_04` | ---  **Event Log for Group A (Protected Group)**  \| CaseID \| Activity            |
| `cat06_05` | ---  **Event Log for Group A (Protected Group)**  \| CaseID \| Activity            |
| `cat06_06` | ---  **Prompt:**  You are given a process model represented in the DECLARE const |
| `cat06_07` | The following is a long textual description of a complex hiring process at a mul |
| `cat08_01` | **Scenario Context:**  A large multi-specialty outpatient clinic is facing chall |
| `cat08_02` | **Scenario Context:**  An e-commerce company operates a large warehouse fulfillm |
| `cat08_03` | **Scenario Context:**  "Speedy Parcels," a regional logistics company, operates  |
| `cat08_04` | **Scenario Context:**  "TechSolve Solutions" provides IT support services via a  |
| `cat08_05` | **Scenario Context:**  "Precision Parts Inc." operates a manufacturing job shop  |

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
