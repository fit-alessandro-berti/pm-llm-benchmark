# PM-LLM-Benchmark v 2.0 (!! IN ACTIVE DEVELOPMENT !!)

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

Different categories of questions are contained in the benchmark.
* The first category checks the contextual understanding of the LLM in process mining tasks. Different types of tasks (case ID inference, contextual splitting of activity labels, definition of high-level events ...) are considered.
* The second category checks the conformance checking/anomaly detection of the LLM, starting from textual descriptions/event logs/procedural process models.
* The third category checks the ability of the LLM to generate and modify declarative and procedural process models.
* The fourth category checks the process querying abilities of the LLM, including procedural and declarative process models.
* The fifth category ...
* The sixth category ...
* The seventh category ...

## Leaderboards

The leaderboards include the results of the benchmark, as evaluated by the considered judge LLM:

* (2024-XX-YY TO NOW) [gpt-4o-2024-11-20](leaderboard_gpt-4o-2024-11-20.md)
