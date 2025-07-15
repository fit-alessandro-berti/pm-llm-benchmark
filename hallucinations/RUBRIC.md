### 1  Prompt‑faithfulness hallucinations

*The model drifts away from **what is explicitly given or asked**.*

| Sub‑class                                                | Typical signal in PM‑LLM‑Benchmark                                                                                                                                               | Why it matters                                                                                               |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **1 a — Instruction‑override**                           | The answer uses generic PM know‑how but ignores a constraint spelled out in the prompt (e.g., produces a split activity label although the prompt says “do *not* split labels”). | Lowers the judge score because following fine‑grained instructions is part of Category 1 tasks ([GitHub][1]) |
| **1 b — Context‑omission**                               | Data, metric, or artifact that was pasted in the prompt (log excerpt, BPMN fragment, fairness definition, …) is silently dropped from the reasoning chain.                       | Breaks trust and often leads to wrong conformance or optimisation advice                                     |
| **1 c — Prompt‑contradiction (intrinsic hallucination)** | The answer states something *opposite* to the prompt (e.g., claims the model is declarative while the prompt shows a Petri net).                                                 | Classic “intrinsic” error in the hallucination literature ([arXiv][2])                                       |

---

### 2  Domain‑factual hallucinations

*The model invents or distorts **process‑mining knowledge** that should be objectively verifiable.*

| Sub‑class                                       | Example symptoms                                                                                                                 | Benchmark categories most exposed                                         |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **2 a — Concept fabrication**                   | Mentions a non‑existent PM algorithm (“Hybrid Alpha++ Miner”), or fabricates KPI definitions.                                    | Cat. 1 (concept questions) & Cat. 5 (hypothesis generation)               |
| **2 b — Spurious numeric claims**               | Gives throughput time averages, support counts, or deviation frequencies that are neither in the prompt nor in known literature. | Cat. 2 (conformance/anomaly) & Cat. 8 (optimisation)                      |
| **2 c — False citation / source hallucination** | Attributes a statement to Wil van der Aalst 2023 when no such paper exists.                                                      | Cross‑cuts all categories that ask for “justify your answer with sources” |

These correspond to what the taxonomy calls **extrinsic hallucinations** (new, unverifiable facts) ([lakera.ai][3]).

---

### 3  Reasoning‑logic hallucinations

*The chain of thought is internally unsound even if individual facts look correct.*

| Sub‑class                                    | Telltale signs                                                                                                                  | Impact                                              |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **3 a — Unsupported leap**                   | Jumps from “98 % of cases rework” to “therefore the process is non‑conforming” without linking to a declared threshold or rule. | Can fool a superficial reader; harms Cat. 2 scoring |
| **3 b — Self‑contradiction**                 | Early sentence: “Only one end‑event exists.” Later: “If multiple end‑events appear, …”                                          | Downgrades LLM‑as‑judge score                       |
| **3 c — Circular or tautological reasoning** | Uses the claim it must prove as the proof itself (“The process is efficient because it has high efficiency”).                   | Especially harmful in Cat. 5 hypothesis tasks       |

---

### 4  Structural / format hallucinations

*The answer deviates from **the required output structure or modelling formalism**.*

| Sub‑class                             | Typical failure                                                                                                      | Affected categories                           |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **4 a — Syntax errors**               | Returns invalid JSON / Python / SQL that will not run.                                                               | Cat. 3 (model generation) & Cat. 4 (querying) |
| **4 b — Model‑semantics breach**      | Emits a BPMN model with disconnected gateways or a DCR graph that violates notation rules.                           | Cat. 3                                        |
| **4 c — Visual/descriptive mismatch** | Describes an image or diagram element that is not present (e.g., “the green loop” when the figure contains no loop). | Cat. 7 (diagram interpretation)               |
