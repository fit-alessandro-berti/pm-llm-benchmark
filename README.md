# PM-LLM-Benchmark v 2.1

**The current repository shows PM-LLM-Benchmark v 2.1, which contains a different and more complex set of prompts than PM-LLM-Benchmark v 1.0**
The paper describing PM-LLM-Benchmark v 1.0 is available [here](https://arxiv.org/pdf/2407.13244)

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

(**2025-03-27 TO NOW**) [gemini-2.5-pro](leaderboard_gemini-2.5-pro.md)

* (v2.0, OLD, 2024-12-13 TO 2025-03-26) [gpt-4o-2024-11-20](old/OLD_v2_leaderboard_gpt-4o-2024-11-20.md)
* (v1, OLD, 2024-10-31 TO 2024-12-12) [v1-leaderboard](old/OLD_v1_leaderboard_chatgpt-4o-latest.md)
