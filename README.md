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

Some scripts to execute and evaluate the questions against OpenAI's APIs are available in **answer.py** and **evalscript.py**.
The API key should be configured inside **api_key.txt**. The responding model (and the API URL) can be configured inside the corresponding scripts.

Different categories of questions are contained in the benchmark.
The first category checks the ability to perform process descriptions, anomaly detection, and root cause analysis starting from the DFG/variants abstractions of the event logs.
It also includes object-centric process mining artifacts for testing object-centric comprehension.
The second category checks the process mining domain knowledge of the LLM, with open and closed questions regarding process mining and Petri nets.
The third category checks the ability to generate procedural (process trees, POWLs) and declarative process models (control-flow and temporal) for mainstream processes. Moreover, the ability to propose constraints given some process data is tested.
The fourth category checks the ability to understand some proposed procedural (BPMN) and declarative (such as the Log Skeleton and DECLARE) process models.
The fifth category tests the ability of the LLM to generate hypotheses over the proposed data and process models.
The sixth category tests the ability of the LLM to identify sensible event log attributes and to perform a comparison between protected and non-protected groups.
The seventh category checks the visual capabilities (if supported) of the LLM/LVLM.

## Leaderboards

The leaderboards include the results of the benchmark, as evaluated by the considered judge LLM:

* [gpt-4o-2024-05-13](leaderboard_gpt-4o_2024_05_13.md)
