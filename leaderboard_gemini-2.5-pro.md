A score in the range **22-26** is considered **sufficient**; a score in the range **26-30** is considered **fair**; a score in the range **30-34** is considered **good**; and a score **>34** is considered **excellent**.

## Overall Leaderboard (1-shot; gemini-2.5-pro-preview-03-25 used as a judge)

| Model                           | Avg     | Score    | OS                 | PCo                  | CC                   | PMo                  | PQ                   | HG                   | FA                   | :nerd_face: VI       |
|:--------------------------------|:--------|:---------|:-------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| Grok-3-beta-thinking-20250221   | **8.4** | **38.8** | :x:                | 6.4                  | :mage_woman: **8.1** | :mage_woman: **6.3** | **5.8**              | **5.9**              | :mage_woman: **6.4** | 0.0                  |
| gemini-2.5-pro-exp-03-25        | **8.2** | **37.9** | :x:                | 6.4                  | **8.0**              | 5.7                  | :mage_woman: **5.9** | :mage_woman: **6.2** | 5.8                  | :mage_woman: **5.8** |
| o1-2024-12-17                   | **7.7** | **35.5** | :x:                | :mage_woman: **7.0** | **8.0**              | 4.8                  | 5.1                  | 5.6                  | 5.0                  | 4.8                  |
| qwen-qwq-32b-nostepbystep       | **7.7** | **35.3** | :white_check_mark: | 6.2                  | 7.0                  | :mage_woman: **6.3** | 4.7                  | 5.0                  | 6.1                  | 0.0                  |
| DeepSeek-R1                     | **7.6** | **34.8** | :white_check_mark: | 6.2                  | :mage_woman: **8.1** | 4.8                  | 5.6                  | 4.7                  | 5.4                  | 0.0                  |
| qwen-qwq-32b-stepbystep         | **7.5** | **34.4** | :white_check_mark: | 5.9                  | 7.3                  | 4.6                  | 4.9                  | 5.5                  | **6.2**              | 0.0                  |
| nemotron-super-49b-v1-thinkenab | **7.4** | **33.9** | :white_check_mark: | 5.1                  | 7.7                  | **6.1**              | 4.9                  | 4.6                  | 5.5                  | 0.0                  |
| o3-mini-20250131-HIGH           | **7.3** | **33.8** | :x:                | 5.9                  | 7.6                  | 4.3                  | 4.9                  | 5.4                  | 5.6                  | 3.5                  |
| o1-pro-2024-12-17               | **7.3** | **33.7** | :x:                | 5.9                  | 7.7                  | 4.5                  | 5.0                  | 5.5                  | 5.2                  | 4.8                  |
| openrouterquasar-alpha          | **7.2** | **33.3** | :white_check_mark: | 5.5                  | 7.5                  | 3.5                  | 5.5                  | 5.5                  | 5.8                  | 0.0                  |
| o3-mini-2025-01-31              | **7.2** | **33.1** | :x:                | 6.1                  | 7.5                  | 4.0                  | 5.2                  | 5.8                  | 4.6                  | 0.0                  |
| claude-3-7-sonnet-thinkhigh     | **7.2** | **33.1** | :x:                | 5.5                  | **8.0**              | 5.0                  | 4.5                  | 5.5                  | 4.5                  | 4.3                  |
| gpt-4.5-preview                 | **7.1** | **32.6** | :x:                | 5.7                  | 7.4                  | 4.2                  | 4.9                  | 5.2                  | 5.3                  | 4.2                  |
| gemini-2.0-flash-thinking-exp   | **7.0** | **32.2** | :x:                | 4.6                  | 7.4                  | 3.1                  | 5.6                  | **5.9**              | 5.5                  | 5.0                  |
| o1-preview-2024-09-12           | **6.9** | **31.9** | :x:                | 5.9                  | 7.1                  | 3.3                  | 4.9                  | 5.7                  | 5.0                  | 0.0                  |
| chatgpt-4o-latest-2025-03-26    | **6.7** | **30.9** | :x:                | 5.5                  | 6.3                  | 3.8                  | 4.7                  | 5.1                  | 5.5                  | 4.9                  |
| Grok-3-beta-20250220            | **6.6** | **30.4** | :x:                | 5.2                  | 6.5                  | 3.7                  | 3.9                  | 5.7                  | 5.4                  | 3.8                  |
| DeepSeek-V3-0324                | **6.6** | **30.4** | :white_check_mark: | 5.8                  | 6.5                  | 3.8                  | 4.8                  | 4.8                  | 4.6                  | 0.0                  |
| DeepSeek-R1-Dynamic-Quant       | **6.6** | **30.4** | :white_check_mark: | 5.4                  | 7.4                  | 3.5                  | 4.6                  | 5.3                  | 4.2                  | 0.0                  |
| r1-1776                         | **6.5** | **30.0** | :white_check_mark: | 4.7                  | 7.7                  | 2.6                  | 4.9                  | 5.0                  | 5.0                  | 0.0                  |
| exaone-deep32b-fp16             | **6.4** | **29.5** | :white_check_mark: | 5.7                  | 6.3                  | 3.6                  | 4.5                  | 4.3                  | 5.2                  | 0.0                  |
| claude-3-7-sonnet-20250219      | **6.3** | **29.0** | :x:                | 5.2                  | 5.9                  | 4.1                  | 3.6                  | 5.0                  | 5.2                  | 3.6                  |
| claude-3-5-sonnet-20241022      | **6.3** | **28.8** | :x:                | 4.2                  | 6.7                  | 3.8                  | 3.9                  | 5.5                  | 4.8                  | 3.2                  |
| gemini-2.0-pro-exp-02-05        | **6.2** | **28.7** | :x:                | 4.9                  | 5.7                  | 3.6                  | 4.2                  | 5.1                  | 5.4                  | 5.0                  |
| gemini-1.5-pro-002              | **6.2** | **28.7** | :x:                | 4.4                  | 5.8                  | 3.0                  | 4.4                  | 5.5                  | 5.6                  | 4.7                  |
| exaone-deep7.8b-fp16            | **6.1** | **28.1** | :white_check_mark: | 5.2                  | 6.8                  | 2.7                  | 3.8                  | 4.5                  | 5.1                  | 0.0                  |
| DeepSeek-R1-Zero                | **6.1** | **28.0** | :white_check_mark: | 5.3                  | 5.1                  | 3.6                  | 4.2                  | 5.5                  | 4.3                  | 0.0                  |
| nemotron-70b-instruct           | **6.0** | **27.8** | :white_check_mark: | 4.5                  | 5.7                  | 3.5                  | 4.3                  | 4.7                  | 5.0                  | 0.0                  |
| claude-3-opus-20240229          | **6.0** | **27.6** | :x:                | 4.6                  | 5.6                  | 4.2                  | 3.5                  | 4.7                  | 5.0                  | 2.7                  |
| o1-mini-2024-09-12              | **6.0** | **27.5** | :x:                | 4.6                  | 5.7                  | 3.2                  | 4.8                  | 4.7                  | 4.5                  | 0.0                  |
| QwQ-32B-Preview                 | **6.0** | **27.4** | :white_check_mark: | 5.1                  | 6.7                  | 3.1                  | 3.4                  | 5.1                  | 4.0                  | 0.0                  |
| qwen-plus-2025-01-25            | **5.9** | **27.2** | :x:                | 4.3                  | 5.8                  | 2.8                  | 3.9                  | 5.2                  | 5.2                  | 3.0                  |
| DeepSeek-V3                     | **5.9** | **27.2** | :white_check_mark: | 4.5                  | 5.8                  | 2.8                  | 4.3                  | 5.1                  | 4.7                  | 0.0                  |
| gpt-4o-2024-11-20               | **5.9** | **27.1** | :x:                | 4.5                  | 5.8                  | 3.0                  | 3.6                  | 5.1                  | 5.1                  | 4.5                  |
| grok-2-1212                     | **5.9** | **27.0** | :x:                | 4.9                  | 6.2                  | 3.3                  | 3.5                  | 4.5                  | 4.6                  | 0.0                  |
| qwen-max-2025-01-25             | **5.8** | **26.9** | :x:                | 4.7                  | 5.5                  | 3.0                  | 3.6                  | 5.0                  | 5.0                  | 3.8                  |
| gemini-2.0-flash                | **5.8** | **26.8** | :x:                | 4.6                  | 6.1                  | 3.4                  | 3.0                  | 4.5                  | 5.2                  | 3.8                  |
| nemotron-super-49b-v1           | **5.8** | **26.8** | :white_check_mark: | 3.8                  | 5.7                  | 3.1                  | 4.7                  | 5.0                  | 4.6                  | 0.0                  |
| gpt-4o-2024-05-13               | **5.8** | **26.8** | :x:                | 5.1                  | 5.4                  | 3.2                  | 4.0                  | 4.8                  | 4.2                  | 3.5                  |
| Llama-3.3-70B-Instruct          | **5.8** | **26.5** | :white_check_mark: | 4.7                  | 5.7                  | 2.7                  | 4.5                  | 4.4                  | 4.5                  | 0.0                  |
| qwen2.5-72b-instruct            | **5.7** | **26.2** | :white_check_mark: | 4.5                  | 5.8                  | 2.9                  | 4.2                  | 3.8                  | 4.9                  | 0.0                  |
| pixtral-large-2411              | **5.7** | **26.0** | :white_check_mark: | 5.1                  | 5.2                  | 3.2                  | 4.0                  | 4.5                  | 4.1                  | 4.7                  |
| gpt-4-turbo-2024-04-09          | **5.6** | **25.9** | :x:                | 4.5                  | 5.4                  | 3.6                  | 3.9                  | 4.7                  | 4.0                  | 4.1                  |
| sonar-pro                       | **5.6** | **25.9** | :x:                | 4.5                  | 5.3                  | 3.0                  | 4.0                  | 5.0                  | 4.0                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-32B    | **5.6** | **25.8** | :white_check_mark: | 5.1                  | 6.2                  | 3.5                  | 3.2                  | 3.8                  | 4.0                  | 0.0                  |
| gemini-2.0-flash-lite           | **5.5** | **25.5** | :x:                | 4.3                  | 6.2                  | 2.5                  | 3.3                  | 4.9                  | 4.2                  | 4.2                  |
| Sonus-1-Pro-Reasoning           | **5.4** | **24.7** | :x:                | 4.4                  | 5.2                  | 3.0                  | 2.9                  | 4.8                  | 4.6                  | 0.0                  |
| mistral-large-2411              | **5.3** | **24.6** | :white_check_mark: | 4.0                  | 5.3                  | 2.8                  | 3.6                  | 4.3                  | 4.5                  | 0.0                  |
| WizardLM-2-8x22B                | **5.3** | **24.4** | :white_check_mark: | 3.8                  | 4.8                  | 2.5                  | 3.9                  | 5.0                  | 4.4                  | 0.0                  |
| mistral-small-2503              | **5.3** | **24.3** | :white_check_mark: | 3.1                  | 5.0                  | 2.4                  | 4.3                  | 4.7                  | 4.8                  | 3.6                  |
| DeepSeek-R1-Distill-Llama-70B   | **5.3** | **24.3** | :white_check_mark: | 4.1                  | 5.7                  | 2.2                  | 3.6                  | 4.4                  | 4.4                  | 0.0                  |
| phi-4                           | **5.2** | **24.1** | :white_check_mark: | 4.1                  | 5.2                  | 3.2                  | 3.4                  | 4.2                  | 4.0                  | 0.0                  |
| mistral-small-2501              | **5.2** | **24.1** | :white_check_mark: | 3.9                  | 5.0                  | 3.3                  | 3.3                  | 4.4                  | 4.2                  | 0.0                  |
| open-mixtral-8x22b              | **5.2** | **23.8** | :white_check_mark: | 4.3                  | 5.0                  | 1.9                  | 3.9                  | 4.4                  | 4.2                  | 0.0                  |
| gemma327b-it-q8_0               | **5.1** | **23.6** | :white_check_mark: | 4.2                  | 4.5                  | 1.8                  | 3.5                  | 4.9                  | 4.8                  | 2.1                  |
| Qwen2.5-Coder-32B-Instruct      | **5.1** | **23.5** | :white_check_mark: | 3.9                  | 4.5                  | 3.1                  | 3.8                  | 4.2                  | 4.1                  | 0.0                  |
| qwen2.5-32b-instruct            | **5.1** | **23.4** | :white_check_mark: | 4.1                  | 5.2                  | 2.0                  | 3.4                  | 4.5                  | 4.2                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-14B    | **5.0** | **22.9** | :white_check_mark: | 3.3                  | 6.1                  | 3.4                  | 2.4                  | 4.0                  | 3.8                  | 0.0                  |
| MiniMax-01                      | **4.8** | **22.2** | :white_check_mark: | 3.5                  | 4.7                  | 2.5                  | 2.9                  | 4.5                  | 4.1                  | 0.0                  |
| gpt-4o-mini-2024-07-18          | **4.8** | **22.1** | :x:                | 3.7                  | 4.5                  | 1.9                  | 3.3                  | 4.5                  | 4.1                  | 4.2                  |
| codestral-2501                  | **4.8** | **22.1** | :white_check_mark: | 4.2                  | 4.5                  | 2.2                  | 3.4                  | 4.2                  | 3.6                  | 0.0                  |
| gemma312b-it-q8_0               | **4.8** | **22.1** | :white_check_mark: | 3.8                  | 3.6                  | 1.9                  | 3.3                  | 4.6                  | 4.8                  | 2.9                  |
| claude-3-5-haiku-20241022       | **4.8** | **22.1** | :x:                | 4.6                  | 4.2                  | 2.0                  | 4.2                  | 4.3                  | 2.8                  | 0.0                  |
| qwen2.5-14b-instruct            | **4.8** | **22.0** | :white_check_mark: | 3.4                  | 4.8                  | 2.4                  | 3.0                  | 4.3                  | 4.0                  | 0.0                  |
| qwen2.5-14b-instruct-1m         | **4.8** | **22.0** | :white_check_mark: | 3.7                  | 4.7                  | 1.7                  | 3.6                  | 4.5                  | 3.9                  | 0.0                  |
| Llama-3.2-90B-Vision-Instruct   | **4.7** | **21.8** | :white_check_mark: | 3.9                  | 4.3                  | 2.5                  | 3.6                  | 4.5                  | 3.0                  | 2.5                  |
| falcon310b-instruct-q8_0        | **4.7** | **21.5** | :white_check_mark: | 3.5                  | 4.8                  | 1.9                  | 3.2                  | 4.2                  | 3.9                  | 0.0                  |
| sonar-reasoning-pro             | **4.7** | **21.5** | :x:                | 3.4                  | 5.6                  | 2.1                  | 2.4                  | 4.8                  | 3.2                  | 0.0                  |
| exaone-deep2.4b-fp16            | **4.6** | **21.1** | :white_check_mark: | 3.8                  | 5.8                  | 1.8                  | 2.9                  | 3.4                  | 3.3                  | 0.0                  |
| googlegemma-2-9b-it             | **4.6** | **21.0** | :white_check_mark: | 3.2                  | 3.5                  | 2.9                  | 3.3                  | 4.7                  | 3.5                  | 0.0                  |
| qwen-turbo-2024-11-01           | **4.5** | **20.6** | :x:                | 3.4                  | 4.2                  | 2.1                  | 3.2                  | 4.1                  | 3.6                  | 0.0                  |
| pixtral-12b-2409                | **4.5** | **20.5** | :white_check_mark: | 2.8                  | 4.5                  | 2.5                  | 3.1                  | 4.0                  | 3.7                  | 4.0                  |
| falcon37b-instruct-q8_0         | **4.4** | **20.4** | :white_check_mark: | 3.0                  | 4.1                  | 2.6                  | 3.0                  | 4.5                  | 3.1                  | 0.0                  |
| qwen2.5-omni-7b                 | **4.1** | **18.9** | :white_check_mark: | 3.2                  | 3.5                  | 1.9                  | 3.0                  | 4.0                  | 3.1                  | 2.2                  |
| qwen2.5-7b-instruct             | **4.1** | **18.9** | :white_check_mark: | 3.1                  | 3.5                  | 2.1                  | 3.3                  | 3.8                  | 3.0                  | 0.0                  |
| gpt-3.5-turbo                   | **4.1** | **18.7** | :x:                | 3.7                  | 3.8                  | 1.6                  | 2.5                  | 3.9                  | 3.1                  | 0.0                  |
| ministral-3b-2410               | **4.1** | **18.6** | :x:                | 2.9                  | 3.4                  | 2.0                  | 3.3                  | 3.7                  | 3.4                  | 0.0                  |
| DeepSeek-R1-Distill-Llama-8B    | **4.0** | **18.6** | :white_check_mark: | 2.9                  | 3.6                  | 2.0                  | 2.6                  | 3.3                  | 4.3                  | 0.0                  |
| granite3.28b-instruct-q4_K_M    | **3.8** | **17.6** | :white_check_mark: | 2.7                  | 3.0                  | 1.7                  | 3.0                  | 4.1                  | 3.0                  | 0.0                  |
| gemma34b-it-q8_0                | **3.7** | **17.2** | :white_check_mark: | 2.2                  | 3.5                  | 1.3                  | 2.7                  | 4.3                  | 3.1                  | 2.0                  |
| qwen2.5-7b-instruct-1m          | **3.7** | **17.1** | :white_check_mark: | 3.0                  | 3.0                  | 1.9                  | 2.6                  | 3.5                  | 3.0                  | 0.0                  |
| command-r7b7b-12-2024-q4_K_M    | **3.7** | **16.9** | :white_check_mark: | 2.5                  | 3.0                  | 1.9                  | 2.6                  | 3.5                  | 3.3                  | 0.0                  |
| Llama-3.1-8B-Instruct           | **3.6** | **16.3** | :white_check_mark: | 2.4                  | 2.8                  | 1.6                  | 2.3                  | 4.5                  | 2.8                  | 0.0                  |
| falcon33b-instruct-q8_0         | **3.4** | **15.6** | :white_check_mark: | 2.5                  | 3.2                  | 1.6                  | 2.2                  | 3.1                  | 2.9                  | 0.0                  |
| Phi-4-multimodal-instruct       | **3.2** | **14.9** | :white_check_mark: | 2.1                  | 3.0                  | 1.2                  | 2.5                  | 3.4                  | 2.9                  | 2.8                  |
| Llama-3.2-11B-Vision-Instruct   | **3.2** | **14.9** | :white_check_mark: | 2.8                  | 3.0                  | 1.9                  | 2.0                  | 3.1                  | 2.0                  | 2.1                  |
| olmo27b-1124-instruct-q8_0      | **3.2** | **14.6** | :white_check_mark: | 2.2                  | 3.0                  | 1.4                  | 2.0                  | 3.1                  | 2.9                  | 0.0                  |
| Llama-3.2-3B-Instruct           | **3.1** | **14.2** | :white_check_mark: | 2.4                  | 2.7                  | 1.3                  | 2.1                  | 3.5                  | 2.1                  | 0.0                  |
| qwen2.53b-instruct-q8_0         | **3.1** | **14.2** | :white_check_mark: | 2.1                  | 2.1                  | 1.6                  | 2.1                  | 3.5                  | 2.7                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-7B     | **2.9** | **13.1** | :white_check_mark: | 1.7                  | 2.6                  | 1.5                  | 2.2                  | 3.1                  | 2.0                  | 0.0                  |
| qwen2.51.5b-instruct-q6_K       | **2.4** | **11.2** | :white_check_mark: | 2.2                  | 1.8                  | 1.1                  | 1.6                  | 2.8                  | 1.7                  | 0.0                  |
| gemma31b-it-q8_0                | **2.3** | **10.7** | :white_check_mark: | 1.1                  | 1.9                  | 1.0                  | 1.4                  | 3.2                  | 2.0                  | 0.0                  |
| Llama-3.2-1B-Instruct           | **1.9** | **8.9**  | :white_check_mark: | 1.3                  | 1.7                  | 0.8                  | 1.1                  | 2.4                  | 1.6                  | 0.0                  |
| DeepSeek-R1-Distill-Qwen-1.5B   | **1.7** | **7.8**  | :white_check_mark: | 1.1                  | 1.6                  | 1.1                  | 1.0                  | 1.7                  | 1.4                  | 0.0                  |

### Grok-3-beta-thinking-20250221   => 38.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     9.7 |
| cat01_05_merge_two_logs            |     8.6 |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     7.1 |
| cat01_08_tables_to_log             |     8.6 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     9.4 |
| cat02_05_two_powls_anomalies       |     9.4 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     9.4 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     9.7 |
| cat03_03_log_skeleton_generation   |     7.7 |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     9.3 |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     8.3 |
| cat03_08_powl_discovery            |     7.7 |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     8.3 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     8.9 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |     8.3 |
| cat05_01_hyp_generation_log        |     9.1 |
| cat05_02_hyp_gen_powl              |     7.7 |
| cat05_03_hyp_gen_declare           |     9.4 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.1 |
| cat06_01_bias_text                 |     9.2 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     8.9 |
| cat06_07_fair_unfair_powl          |     9.4 |



### gemini-2.5-pro-exp-03-25   => 37.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     6.5 |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     7.5 |
| cat01_08_tables_to_log             |     8.5 |
| cat02_01_conformance_textual       |     9.8 |
| cat02_02_conf_desiderata           |     9.2 |
| cat02_03_anomaly_event_log         |     9.2 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     9   |
| cat02_06_root_cause_1              |     9.5 |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     9.5 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     8   |
| cat03_06_petri_net_generation      |     8   |
| cat03_07_process_tree_discovery    |     9.8 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     9.1 |
| cat04_03_declare_open_question     |     9   |
| cat04_04_declare_description       |     8.2 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.5 |
| cat04_07_sql_filt_top_k_vars       |     5.5 |
| cat05_01_hyp_generation_log        |     8.5 |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     9   |
| cat05_04_hyp_gen_temp_profile      |     8.7 |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     9   |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8.5 |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |     9.5 |
| cat07_03_bpmn_dispatch             |     9.5 |
| cat07_04_causal_net                |    10   |
| cat07_05_proclets                  |     9   |
| cat07_06_perf_spectrum             |     9.8 |



### o1-2024-12-17   => 35.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     8.5 |
| cat01_05_merge_two_logs            |     7.8 |
| cat01_06_system_logs               |     8.8 |
| cat01_07_interv_to_pseudo_bpmn     |     7   |
| cat01_08_tables_to_log             |     9.5 |
| cat02_01_conformance_textual       |     9.8 |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     7.8 |
| cat02_06_root_cause_1              |     9.5 |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |     9   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     6.5 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     1.5 |
| cat03_05_temp_profile_generation   |     8   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     7   |
| cat03_08_powl_discovery            |     9.5 |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     7   |
| cat04_03_declare_open_question     |     6.5 |
| cat04_04_declare_description       |     6.5 |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     8.5 |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     5   |
| cat05_02_hyp_gen_powl              |     9   |
| cat05_03_hyp_gen_declare           |     6.5 |
| cat05_04_hyp_gen_temp_profile      |     8.8 |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     9.2 |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     7.8 |
| cat06_04_bias_two_logs             |     8.2 |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     6   |
| cat07_01_ocdfg                     |    10   |
| cat07_02_bpmn_orders               |     6   |
| cat07_03_bpmn_dispatch             |     4.5 |
| cat07_04_causal_net                |     9.5 |
| cat07_05_proclets                  |     9.5 |
| cat07_06_perf_spectrum             |     9   |



### qwen-qwq-32b-nostepbystep   => 35.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     7.1 |
| cat01_06_system_logs               |     8.9 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     8.3 |
| cat02_01_conformance_textual       |     8.3 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     5.4 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     8.3 |
| cat03_01_process_tree_generation   |     7.7 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     7.1 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     8.9 |
| cat03_06_petri_net_generation      |     5.4 |
| cat03_07_process_tree_discovery    |     9.4 |
| cat03_08_powl_discovery            |     8.3 |
| cat04_01_pseudo_bpmn_description   |     7.7 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     1.4 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     9.4 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     9.4 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     8.3 |
| cat06_07_fair_unfair_powl          |     6.6 |



### deepseek-aiDeepSeek-R1   => 34.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     6.6 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     9.4 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     8.9 |
| cat01_08_tables_to_log             |     9.4 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     9.4 |
| cat02_03_anomaly_event_log         |     9.4 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     8.6 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     8.6 |
| cat03_07_process_tree_discovery    |     6.6 |
| cat03_08_powl_discovery            |     4.8 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.9 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     7.7 |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     8.3 |
| cat05_01_hyp_generation_log        |     4.9 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     6.6 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     8.3 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     8.3 |



### qwen-qwq-32b-stepbystep   => 34.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     8.9 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     7.7 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     7.7 |
| cat02_06_root_cause_1              |     8.6 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     7.7 |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     7.7 |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     6.6 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     8.9 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     7.7 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     7.1 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     7.1 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     8.3 |
| cat06_07_fair_unfair_powl          |     8.3 |



### nvidiallama-3.3-nemotron-super-49b-v1-thinkenab   => 33.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |    10   |
| cat01_02_activity_context          |     4.8 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     9.4 |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     3.7 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     9.4 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     9.4 |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     6.6 |
| cat03_03_log_skeleton_generation   |     6   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     7.1 |
| cat03_06_petri_net_generation      |     9.4 |
| cat03_07_process_tree_discovery    |     9.4 |
| cat03_08_powl_discovery            |     9.4 |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     8.9 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     8.3 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     7.7 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.1 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     8.3 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     8.3 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     6.6 |



### o3-mini-20250131-HIGH   => 33.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     9   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     8.8 |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     9.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     9.6 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     8.5 |
| cat02_08_underfitting_process_tree |     9.8 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     5.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     5   |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     8.8 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     8.5 |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     7.8 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8.8 |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     8.8 |
| cat06_04_bias_two_logs             |     8.5 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     7   |
| cat06_07_fair_unfair_powl          |     7   |
| cat07_01_ocdfg                     |     6   |
| cat07_02_bpmn_orders               |     3.5 |
| cat07_03_bpmn_dispatch             |     4.5 |
| cat07_04_causal_net                |     5.5 |
| cat07_05_proclets                  |     7.5 |
| cat07_06_perf_spectrum             |     8   |



### o1-pro-2024-12-17   => 33.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     9.2 |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     9   |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     6   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     8.8 |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     9   |
| cat02_06_root_cause_1              |     9.2 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     6.5 |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     9   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     8.7 |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     5   |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     8.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     8.8 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     9.5 |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |    10   |
| cat07_03_bpmn_dispatch             |     1   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     9.8 |
| cat07_06_perf_spectrum             |     9.8 |



### openrouterquasar-alpha   => 33.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     6.5 |
| cat01_03_high_level_events         |     8.5 |
| cat01_04_sensor_recordings         |     5.8 |
| cat01_05_merge_two_logs            |     6.5 |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     9   |
| cat01_08_tables_to_log             |     6.5 |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     9.8 |
| cat02_03_anomaly_event_log         |     9.8 |
| cat02_04_powl_anomaly_detection    |     9   |
| cat02_05_two_powls_anomalies       |     7.3 |
| cat02_06_root_cause_1              |     9   |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     4.5 |
| cat03_02_powl_generation           |    10   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     5.5 |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     8   |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |    10   |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     7.9 |
| cat05_03_hyp_gen_declare           |     7   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     8.8 |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     9.3 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     9.8 |
| cat06_03_bias_powl                 |     8.8 |
| cat06_04_bias_two_logs             |     8.5 |
| cat06_05_bias_two_logs_2           |     9.2 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     9   |



### o3-mini-2025-01-31   => 33.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     9.2 |
| cat01_03_high_level_events         |     9.5 |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     6.5 |
| cat01_08_tables_to_log             |     9   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     9.5 |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     7.5 |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     9.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     6   |
| cat03_07_process_tree_discovery    |     4.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     7.2 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     9.8 |
| cat05_01_hyp_generation_log        |     5.5 |
| cat05_02_hyp_gen_powl              |     8.8 |
| cat05_03_hyp_gen_declare           |     9   |
| cat05_04_hyp_gen_temp_profile      |     7   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     8.5 |
| cat06_05_bias_two_logs_2           |     5   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     6   |



### claude-3-7-sonnet-thinkhigh-20250219   => 33.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     4.5 |
| cat01_06_system_logs               |     8   |
| cat01_07_interv_to_pseudo_bpmn     |     6.5 |
| cat01_08_tables_to_log             |     6.5 |
| cat02_01_conformance_textual       |     9.8 |
| cat02_02_conf_desiderata           |     9   |
| cat02_03_anomaly_event_log         |     9.7 |
| cat02_04_powl_anomaly_detection    |     9   |
| cat02_05_two_powls_anomalies       |     8   |
| cat02_06_root_cause_1              |     8   |
| cat02_07_root_cause_2              |     7.8 |
| cat02_08_underfitting_process_tree |     9   |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     9   |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     1.5 |
| cat03_05_temp_profile_generation   |     7.9 |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     9.5 |
| cat03_08_powl_discovery            |     5   |
| cat04_01_pseudo_bpmn_description   |     9.5 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     3.5 |
| cat05_01_hyp_generation_log        |     8.5 |
| cat05_02_hyp_gen_powl              |     8   |
| cat05_03_hyp_gen_declare           |     6.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     2.5 |
| cat07_01_ocdfg                     |     5.5 |
| cat07_02_bpmn_orders               |     7   |
| cat07_03_bpmn_dispatch             |     6.5 |
| cat07_04_causal_net                |     7.5 |
| cat07_05_proclets                  |     7.5 |
| cat07_06_perf_spectrum             |     8.8 |



### gpt-4.5-preview   => 32.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     9.1 |
| cat01_05_merge_two_logs            |     7.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     8   |
| cat01_08_tables_to_log             |     6.5 |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     8.5 |
| cat02_07_root_cause_2              |     8.5 |
| cat02_08_underfitting_process_tree |     9   |
| cat02_09_fix_process_tree          |     9.2 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     5   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     7.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     8.5 |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     7.5 |
| cat05_03_hyp_gen_declare           |     4.5 |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     9.3 |
| cat06_02_bias_event_log            |     4.5 |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     9.2 |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8   |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |     6.5 |
| cat07_03_bpmn_dispatch             |     1   |
| cat07_04_causal_net                |     6.5 |
| cat07_05_proclets                  |     9.5 |
| cat07_06_perf_spectrum             |     8.8 |



### gemini-2.0-flash-thinking-exp-01-21   => 32.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.2 |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     9   |
| cat01_04_sensor_recordings         |     5   |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     9.2 |
| cat02_04_powl_anomaly_detection    |     9.2 |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     8.2 |
| cat02_07_root_cause_2              |     9.5 |
| cat02_08_underfitting_process_tree |     8.7 |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     6   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     1.5 |
| cat03_05_temp_profile_generation   |     8.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     9.5 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     4.5 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     9.5 |
| cat05_01_hyp_generation_log        |     8   |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     7.5 |
| cat05_04_hyp_gen_temp_profile      |     8.2 |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     9.6 |
| cat06_02_bias_event_log            |     8.8 |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     9   |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     6   |
| cat07_01_ocdfg                     |     9.7 |
| cat07_02_bpmn_orders               |     7.5 |
| cat07_03_bpmn_dispatch             |     6   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     9.5 |
| cat07_06_perf_spectrum             |     9.5 |



### o1-preview-2024-09-12   => 31.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     9   |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     9.2 |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     4.5 |
| cat01_08_tables_to_log             |     8.5 |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     9.4 |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     7.8 |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     9.8 |
| cat02_09_fix_process_tree          |     9.8 |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     4   |
| cat03_08_powl_discovery            |     5   |
| cat04_01_pseudo_bpmn_description   |     8.8 |
| cat04_02_pseudo_bpmn_open_question |     7   |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.2 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     7.5 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     8   |
| cat05_03_hyp_gen_declare           |     9   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     9.8 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     8.5 |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     6   |



### chatgpt-4o-latest-2025-03-26   => 30.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.2 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     5   |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     9.8 |
| cat02_01_conformance_textual       |     8.5 |
| cat02_02_conf_desiderata           |     8.3 |
| cat02_03_anomaly_event_log         |     9.2 |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     5.5 |
| cat02_06_root_cause_1              |     7.8 |
| cat02_07_root_cause_2              |     5.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     5.5 |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     5   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     7   |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     8.5 |
| cat04_07_sql_filt_top_k_vars       |     8.5 |
| cat05_01_hyp_generation_log        |     5   |
| cat05_02_hyp_gen_powl              |     6.9 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     9   |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     8.8 |
| cat06_05_bias_two_logs_2           |     8.5 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     7.5 |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |     6.5 |
| cat07_03_bpmn_dispatch             |     5.5 |
| cat07_04_causal_net                |    10   |
| cat07_05_proclets                  |     8   |
| cat07_06_perf_spectrum             |     9.5 |



### Grok-3-beta-20250220   => 30.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.2 |
| cat01_02_activity_context          |     5   |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     8.7 |
| cat01_08_tables_to_log             |     9   |
| cat02_01_conformance_textual       |     9.2 |
| cat02_02_conf_desiderata           |     9.2 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     5.5 |
| cat02_06_root_cause_1              |     6.5 |
| cat02_07_root_cause_2              |     7.8 |
| cat02_08_underfitting_process_tree |     6.5 |
| cat02_09_fix_process_tree          |     3   |
| cat03_01_process_tree_generation   |     5   |
| cat03_02_powl_generation           |     8   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     9.5 |
| cat05_03_hyp_gen_declare           |     7.5 |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |     9.2 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     4.5 |
| cat06_07_fair_unfair_powl          |     6.5 |
| cat07_01_ocdfg                     |     5.5 |
| cat07_02_bpmn_orders               |     9   |
| cat07_03_bpmn_dispatch             |     4   |
| cat07_04_causal_net                |     4.5 |
| cat07_05_proclets                  |     8   |
| cat07_06_perf_spectrum             |     7   |



### deepseek-aiDeepSeek-V3-0324   => 30.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     8.5 |
| cat01_04_sensor_recordings         |     8.5 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     5   |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     8.8 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     9.5 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     9   |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     3.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     6.5 |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     3.5 |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     9   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     9   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     5.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     9.2 |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     6.5 |



### DeepSeek-R1-Dynamic-Quant   => 30.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     8.3 |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     8.3 |
| cat01_07_interv_to_pseudo_bpmn     |     6.6 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     8.9 |
| cat02_02_conf_desiderata           |     9.8 |
| cat02_03_anomaly_event_log         |     5.4 |
| cat02_04_powl_anomaly_detection    |     6.6 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     7.7 |
| cat02_07_root_cause_2              |     8.9 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     5.4 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     4.8 |
| cat03_04_declare_generation        |     4.2 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     4.2 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     4.2 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     6.3 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     8.3 |
| cat05_03_hyp_gen_declare           |     7.7 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     8.3 |
| cat06_02_bias_event_log            |     6.6 |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     3.1 |
| cat06_06_bias_mitigation_declare   |     4.8 |
| cat06_07_fair_unfair_powl          |     6   |



### r1-1776   => 30.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.6 |
| cat01_02_activity_context          |     5.4 |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     7.1 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     8.9 |
| cat02_01_conformance_textual       |     9.8 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     8.3 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     8.9 |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     8.9 |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     5.4 |
| cat04_02_pseudo_bpmn_open_question |     7.7 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     6   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     3.7 |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     9.4 |
| cat05_07_question_interview        |     9.4 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     9.4 |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     4.8 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     8.3 |



### exaone-deep32b-fp16   => 29.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.4 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     8.3 |
| cat01_05_merge_two_logs            |     9.4 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     8.3 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     9.8 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     6   |
| cat03_03_log_skeleton_generation   |     8.3 |
| cat03_04_declare_generation        |     1.4 |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     7.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     5.4 |
| cat04_01_pseudo_bpmn_description   |     8.6 |
| cat04_02_pseudo_bpmn_open_question |     5.6 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     5.4 |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     9.4 |
| cat04_07_sql_filt_top_k_vars       |     4.8 |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     8.3 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     7.7 |
| cat06_01_bias_text                 |     9.4 |
| cat06_02_bias_event_log            |     8.3 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     7.7 |
| cat06_07_fair_unfair_powl          |     3.7 |



### claude-3-7-sonnet-20250219   => 29.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.8 |
| cat01_02_activity_context          |     9   |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     5.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     3.8 |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     5.5 |
| cat02_05_two_powls_anomalies       |     6.5 |
| cat02_06_root_cause_1              |     5   |
| cat02_07_root_cause_2              |     8.5 |
| cat02_08_underfitting_process_tree |     4.5 |
| cat02_09_fix_process_tree          |     9.8 |
| cat03_01_process_tree_generation   |     9.8 |
| cat03_02_powl_generation           |     7   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     5.5 |
| cat03_06_petri_net_generation      |     6.5 |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     4   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     8   |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     8   |
| cat05_05_question_gen_nlp          |     6.5 |
| cat05_06_question_pseudo_bpmn      |     8.8 |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     5.5 |
| cat06_07_fair_unfair_powl          |     6.5 |
| cat07_01_ocdfg                     |     8   |
| cat07_02_bpmn_orders               |     6.5 |
| cat07_03_bpmn_dispatch             |     6.5 |
| cat07_04_causal_net                |     6   |
| cat07_05_proclets                  |     8.5 |
| cat07_06_perf_spectrum             |     1   |



### claude-3-5-sonnet-20241022   => 28.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     5.5 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     5.5 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     7.5 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     7   |
| cat02_07_root_cause_2              |     5.5 |
| cat02_08_underfitting_process_tree |     9.5 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     9   |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     7   |
| cat04_03_declare_open_question     |     4.5 |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     8   |
| cat05_01_hyp_generation_log        |     5.5 |
| cat05_02_hyp_gen_powl              |     8.8 |
| cat05_03_hyp_gen_declare           |     7.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     6.5 |
| cat06_06_bias_mitigation_declare   |     4.5 |
| cat06_07_fair_unfair_powl          |     9   |
| cat07_01_ocdfg                     |     9.8 |
| cat07_02_bpmn_orders               |     1   |
| cat07_03_bpmn_dispatch             |    10   |
| cat07_04_causal_net                |     9.5 |
| cat07_05_proclets                  |     1   |
| cat07_06_perf_spectrum             |     1   |



### gemini-2.0-pro-exp-02-05   => 28.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     3.5 |
| cat01_04_sensor_recordings         |     7.6 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     6.5 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     3.5 |
| cat02_05_two_powls_anomalies       |     6.5 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     8   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     9   |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     5.5 |
| cat05_04_hyp_gen_temp_profile      |     5   |
| cat05_05_question_gen_nlp          |     8.8 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     9.6 |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     8.5 |
| cat06_07_fair_unfair_powl          |     7   |
| cat07_01_ocdfg                     |     7   |
| cat07_02_bpmn_orders               |     9.5 |
| cat07_03_bpmn_dispatch             |     7   |
| cat07_04_causal_net                |     9   |
| cat07_05_proclets                  |     9   |
| cat07_06_perf_spectrum             |     8   |



### gemini-1.5-pro-002   => 28.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.5 |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     7.8 |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     2.5 |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |     7.5 |
| cat02_02_conf_desiderata           |     6.5 |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     8.8 |
| cat02_07_root_cause_2              |     3.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     7.5 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     8   |
| cat05_02_hyp_gen_powl              |     4.5 |
| cat05_03_hyp_gen_declare           |     8   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9.8 |
| cat05_06_question_pseudo_bpmn      |     9.8 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     9.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     9.2 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     9   |
| cat07_01_ocdfg                     |     8.8 |
| cat07_02_bpmn_orders               |     8   |
| cat07_03_bpmn_dispatch             |     4.5 |
| cat07_04_causal_net                |     7   |
| cat07_05_proclets                  |     9.8 |
| cat07_06_perf_spectrum             |     8.8 |



### exaone-deep7.8b-fp16   => 28.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     8.9 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     7.7 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     5.4 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     8.9 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     7.7 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     9.4 |
| cat03_01_process_tree_generation   |     1.4 |
| cat03_02_powl_generation           |     3.1 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     7.7 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     4.2 |
| cat03_08_powl_discovery            |     4.8 |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     5.4 |
| cat04_03_declare_open_question     |     5.4 |
| cat04_04_declare_description       |     4.2 |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     3.1 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     4.2 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     4.8 |
| cat05_05_question_gen_nlp          |     7.1 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     4.2 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     9.4 |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     6.6 |



### DeepSeek-R1-Zero   => 28.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.1 |
| cat01_02_activity_context          |     7.7 |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     8.9 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     5.4 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     9.4 |
| cat02_01_conformance_textual       |     7.7 |
| cat02_02_conf_desiderata           |     3.3 |
| cat02_03_anomaly_event_log         |     7.7 |
| cat02_04_powl_anomaly_detection    |     2   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     8.3 |
| cat02_07_root_cause_2              |     8.3 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     3.1 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     9.4 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     3.1 |
| cat03_08_powl_discovery            |     8.9 |
| cat04_01_pseudo_bpmn_description   |     4.8 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     3.1 |
| cat04_04_declare_description       |     7.1 |
| cat04_05_sql_filt_num_events       |     8.3 |
| cat04_06_sql_filt_three_df         |     7.1 |
| cat04_07_sql_filt_top_k_vars       |     6.6 |
| cat05_01_hyp_generation_log        |     6.6 |
| cat05_02_hyp_gen_powl              |     8.9 |
| cat05_03_hyp_gen_declare           |     8.9 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     6.9 |
| cat06_02_bias_event_log            |     9.4 |
| cat06_03_bias_powl                 |     8.3 |
| cat06_04_bias_two_logs             |     7.7 |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     6.6 |
| cat06_07_fair_unfair_powl          |     2   |



### nvidiaLlama-3.1-Nemotron-70B-Instruct   => 27.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     5   |
| cat01_03_high_level_events         |     8.5 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     7.5 |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     6.5 |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     4   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     7.8 |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     6   |
| cat04_04_declare_description       |     4.5 |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     9.5 |
| cat05_01_hyp_generation_log        |     4.5 |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8.8 |
| cat05_06_question_pseudo_bpmn      |     9.2 |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     5.5 |
| cat06_03_bias_powl                 |     9.2 |
| cat06_04_bias_two_logs             |     7.5 |
| cat06_05_bias_two_logs_2           |     8.2 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     7   |



### claude-3-opus-20240229   => 27.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.5 |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     3.5 |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     7   |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     9   |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9.8 |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     1.5 |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     9   |
| cat03_06_petri_net_generation      |     6   |
| cat03_07_process_tree_discovery    |     4   |
| cat03_08_powl_discovery            |     5   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     5.8 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     4   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     5   |
| cat05_02_hyp_gen_powl              |     4.5 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     9   |
| cat05_05_question_gen_nlp          |     7   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     9.6 |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     9   |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     5.5 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     5   |
| cat06_07_fair_unfair_powl          |     9   |
| cat07_01_ocdfg                     |     4.5 |
| cat07_02_bpmn_orders               |     4   |
| cat07_03_bpmn_dispatch             |     3.5 |
| cat07_04_causal_net                |     5   |
| cat07_05_proclets                  |     3.5 |
| cat07_06_perf_spectrum             |     6.5 |



### o1-mini-2024-09-12   => 27.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.5 |
| cat01_02_activity_context          |     6.5 |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     8.8 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     8.5 |
| cat02_09_fix_process_tree          |     3.5 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     3.5 |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     8.5 |
| cat04_02_pseudo_bpmn_open_question |     7.8 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.7 |
| cat04_06_sql_filt_three_df         |     7.5 |
| cat04_07_sql_filt_top_k_vars       |     8.5 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     5   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     7   |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     6.5 |
| cat06_06_bias_mitigation_declare   |     4.5 |
| cat06_07_fair_unfair_powl          |     5   |



### QwenQwQ-32B-Preview   => 27.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.9 |
| cat01_02_activity_context          |     8.9 |
| cat01_03_high_level_events         |     8.6 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     4.2 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     8.3 |
| cat02_04_powl_anomaly_detection    |     4.2 |
| cat02_05_two_powls_anomalies       |     8.3 |
| cat02_06_root_cause_1              |     6.6 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     8.3 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     4.2 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     6.6 |
| cat04_02_pseudo_bpmn_open_question |     6.6 |
| cat04_03_declare_open_question     |     3.7 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     8.3 |
| cat05_02_hyp_gen_powl              |     6.6 |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     4.2 |
| cat05_05_question_gen_nlp          |     9.8 |
| cat05_06_question_pseudo_bpmn      |     8.6 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     7.7 |
| cat06_03_bias_powl                 |     8.9 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     2   |



### qwen-plus-2025-01-25   => 27.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.5 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     5   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     4.5 |
| cat02_01_conformance_textual       |     8.5 |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     7.8 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     5.5 |
| cat02_06_root_cause_1              |     5   |
| cat02_07_root_cause_2              |     5.5 |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     6   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     4.5 |
| cat04_02_pseudo_bpmn_open_question |     6.8 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     3.5 |
| cat04_07_sql_filt_top_k_vars       |     9   |
| cat05_01_hyp_generation_log        |     8   |
| cat05_02_hyp_gen_powl              |     7.5 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     8.4 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     7.8 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     9.5 |
| cat07_01_ocdfg                     |     4   |
| cat07_02_bpmn_orders               |     9   |
| cat07_03_bpmn_dispatch             |     5   |
| cat07_04_causal_net                |     4.5 |
| cat07_05_proclets                  |     3   |
| cat07_06_perf_spectrum             |     4.5 |



### deepseek-aiDeepSeek-V3   => 27.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     8   |
| cat02_01_conformance_textual       |     7.5 |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     8.5 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     8.8 |
| cat03_01_process_tree_generation   |     3.5 |
| cat03_02_powl_generation           |     5   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     4.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     7   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     9.8 |
| cat04_07_sql_filt_top_k_vars       |     3.5 |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     8   |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     5   |
| cat05_05_question_gen_nlp          |     9.8 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     8   |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     6.3 |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     6   |



### gpt-4o-2024-11-20   => 27.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     5.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     4.5 |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     5.5 |
| cat02_07_root_cause_2              |     7.5 |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     3.5 |
| cat03_02_powl_generation           |     9   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8.5 |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     5   |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     6.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     9   |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     9.2 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8   |
| cat07_01_ocdfg                     |     9.5 |
| cat07_02_bpmn_orders               |     6   |
| cat07_03_bpmn_dispatch             |     5   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     7   |
| cat07_06_perf_spectrum             |     9.5 |



### grok-2-1212   => 27.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     9.8 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     4.5 |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     5   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     3   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     8.9 |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     8.8 |



### qwen-max-2025-01-25   => 26.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.8 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     7.8 |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     4.5 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     4.5 |
| cat02_08_underfitting_process_tree |     6.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     7   |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     4.5 |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     4.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     4   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     4.5 |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     7.8 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     8.8 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8.8 |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     9   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     7.5 |
| cat07_01_ocdfg                     |     6   |
| cat07_02_bpmn_orders               |     5   |
| cat07_03_bpmn_dispatch             |     6   |
| cat07_04_causal_net                |     6.5 |
| cat07_05_proclets                  |     6.5 |
| cat07_06_perf_spectrum             |     7.5 |



### gemini-2.0-flash   => 26.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.8 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     9.8 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     8.5 |
| cat02_07_root_cause_2              |     5.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     5   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     8.2 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     1.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     8   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8.8 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     9   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     6   |
| cat07_01_ocdfg                     |     8.5 |
| cat07_02_bpmn_orders               |     9.2 |
| cat07_03_bpmn_dispatch             |     1   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     9.8 |
| cat07_06_perf_spectrum             |     1   |



### nvidiallama-3.3-nemotron-super-49b-v1   => 26.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     5   |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     4.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     6.5 |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     7   |
| cat02_06_root_cause_1              |     4.5 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     5.5 |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     7.5 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     7.5 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     6.8 |
| cat06_06_bias_mitigation_declare   |     5   |
| cat06_07_fair_unfair_powl          |     7.5 |



### gpt-4o-2024-05-13   => 26.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     8.5 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     5   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     5.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     4.5 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     4   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     5   |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     7.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     7   |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     7.5 |
| cat04_07_sql_filt_top_k_vars       |     6.5 |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     5.5 |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     4.5 |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     7.8 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     7   |
| cat07_01_ocdfg                     |     7   |
| cat07_02_bpmn_orders               |     6   |
| cat07_03_bpmn_dispatch             |     4   |
| cat07_04_causal_net                |     4   |
| cat07_05_proclets                  |     7   |
| cat07_06_perf_spectrum             |     7.5 |



### meta-llamaLlama-3.3-70B-Instruct   => 26.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.8 |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5.5 |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     8   |
| cat02_03_anomaly_event_log         |     8.3 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     5.5 |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     5.5 |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     5   |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     8.5 |
| cat04_07_sql_filt_top_k_vars       |     7.5 |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     7   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     5   |
| cat06_04_bias_two_logs             |     5.5 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     4.5 |
| cat06_07_fair_unfair_powl          |     7.5 |



### qwen2.5-72b-instruct   => 26.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     3.5 |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     4.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     6.5 |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     6.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     7.5 |
| cat04_07_sql_filt_top_k_vars       |     8.5 |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     5.5 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     5   |
| cat05_05_question_gen_nlp          |     7   |
| cat05_06_question_pseudo_bpmn      |     5   |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     8.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.8 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     9.5 |



### pixtral-large-2411   => 26.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.5 |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     8   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     6   |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     4.5 |
| cat02_07_root_cause_2              |     4   |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     9   |
| cat03_02_powl_generation           |     7   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     4.5 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     9.5 |
| cat04_07_sql_filt_top_k_vars       |     6.5 |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     7   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     8.8 |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     7.5 |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     8   |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     5.5 |
| cat06_07_fair_unfair_powl          |     2.5 |
| cat07_01_ocdfg                     |     3.5 |
| cat07_02_bpmn_orders               |    10   |
| cat07_03_bpmn_dispatch             |     9   |
| cat07_04_causal_net                |     8   |
| cat07_05_proclets                  |     7   |
| cat07_06_perf_spectrum             |     9.5 |



### gpt-4-turbo-2024-04-09   => 25.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.5 |
| cat01_02_activity_context          |     9   |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     3.5 |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     4.5 |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     3.5 |
| cat02_03_anomaly_event_log         |     7   |
| cat02_04_powl_anomaly_detection    |     8.7 |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     5.5 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     3.5 |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4.5 |
| cat03_06_petri_net_generation      |     1.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     6   |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     6.5 |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     8.7 |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     4   |
| cat07_01_ocdfg                     |     9.5 |
| cat07_02_bpmn_orders               |     4.5 |
| cat07_03_bpmn_dispatch             |     5.5 |
| cat07_04_causal_net                |     6   |
| cat07_05_proclets                  |     7.8 |
| cat07_06_perf_spectrum             |     8   |



### sonar-pro   => 25.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7   |
| cat01_02_activity_context          |     5   |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |     7   |
| cat01_05_merge_two_logs            |     4.5 |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     9   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     8   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |     3.5 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     7.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     5.5 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     8.8 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     9   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     4.5 |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     6.5 |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     5.5 |
| cat06_05_bias_two_logs_2           |     5   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     6.5 |



### deepseek-aiDeepSeek-R1-Distill-Qwen-32B   => 25.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     9.1 |
| cat01_03_high_level_events         |     7.7 |
| cat01_04_sensor_recordings         |     7.7 |
| cat01_05_merge_two_logs            |     5.4 |
| cat01_06_system_logs               |     4.8 |
| cat01_07_interv_to_pseudo_bpmn     |     4.2 |
| cat01_08_tables_to_log             |     4.2 |
| cat02_01_conformance_textual       |     7.1 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     7.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     6   |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     4.2 |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     4.2 |
| cat03_06_petri_net_generation      |     9.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     1.4 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     3.7 |
| cat04_07_sql_filt_top_k_vars       |     8.9 |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     3.1 |
| cat05_04_hyp_gen_temp_profile      |     3.7 |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     7.1 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     2.5 |
| cat06_04_bias_two_logs             |     7.1 |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     6   |
| cat06_07_fair_unfair_powl          |     7.1 |



### gemini-2.0-flash-lite   => 25.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     6.5 |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     7   |
| cat02_08_underfitting_process_tree |     8   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     5   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     7   |
| cat04_02_pseudo_bpmn_open_question |     9.2 |
| cat04_03_declare_open_question     |     5   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6.5 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     8.6 |
| cat06_01_bias_text                 |     7.8 |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     8.2 |
| cat06_04_bias_two_logs             |     5   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     5.5 |
| cat06_07_fair_unfair_powl          |     3   |
| cat07_01_ocdfg                     |     9.2 |
| cat07_02_bpmn_orders               |     5.5 |
| cat07_03_bpmn_dispatch             |     4   |
| cat07_04_causal_net                |     7   |
| cat07_05_proclets                  |     9.5 |
| cat07_06_perf_spectrum             |     7   |



### Sonus-1-Pro-Reasoning   => 24.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.5 |
| cat01_02_activity_context          |     8.5 |
| cat01_03_high_level_events         |     7   |
| cat01_04_sensor_recordings         |     5   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     7.5 |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     4.5 |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     4   |
| cat02_08_underfitting_process_tree |     6.5 |
| cat02_09_fix_process_tree          |     4   |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     9   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     4.5 |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     6.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     7.8 |
| cat05_06_question_pseudo_bpmn      |     8.7 |
| cat05_07_question_interview        |     9.5 |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     7.5 |



### mistral-large-2411   => 24.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     7   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     8.5 |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     5   |
| cat02_04_powl_anomaly_detection    |     8.8 |
| cat02_05_two_powls_anomalies       |     5   |
| cat02_06_root_cause_1              |     4.5 |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     8   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     6.5 |
| cat05_04_hyp_gen_temp_profile      |     3.5 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     5.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     7.8 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     7   |



### microsoftWizardLM-2-8x22B   => 24.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8   |
| cat01_02_activity_context          |     4.5 |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     5   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     9   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     7   |
| cat02_07_root_cause_2              |     4.5 |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     5.5 |
| cat03_06_petri_net_generation      |     3.5 |
| cat03_07_process_tree_discovery    |     2.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     5.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     9   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     9.5 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     4   |
| cat06_04_bias_two_logs             |     7   |
| cat06_05_bias_two_logs_2           |     4.8 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     9   |



### mistral-small-2503   => 24.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     9.3 |
| cat02_03_anomaly_event_log         |     4.5 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |     5   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     5.5 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     9   |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     8.8 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     9.6 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     6.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     8.5 |
| cat07_01_ocdfg                     |     7   |
| cat07_02_bpmn_orders               |     6   |
| cat07_03_bpmn_dispatch             |     5   |
| cat07_04_causal_net                |     7   |
| cat07_05_proclets                  |     6.5 |
| cat07_06_perf_spectrum             |     4.5 |



### deepseek-aiDeepSeek-R1-Distill-Llama-70B   => 24.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.3 |
| cat01_02_activity_context          |     3.1 |
| cat01_03_high_level_events         |     4.8 |
| cat01_04_sensor_recordings         |     6.3 |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     6.6 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     6.6 |
| cat02_03_anomaly_event_log         |     8.9 |
| cat02_04_powl_anomaly_detection    |     1   |
| cat02_05_two_powls_anomalies       |     5.4 |
| cat02_06_root_cause_1              |     5.4 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     8.9 |
| cat02_09_fix_process_tree          |     5.4 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     4.8 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4.2 |
| cat04_01_pseudo_bpmn_description   |     7.1 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     8.3 |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     4.8 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     4.2 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     7.1 |
| cat06_02_bias_event_log            |     5.4 |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     8.3 |
| cat06_05_bias_two_logs_2           |     7.7 |
| cat06_06_bias_mitigation_declare   |     5.4 |
| cat06_07_fair_unfair_powl          |     3.7 |



### microsoftphi-4   => 24.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     8   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     8.3 |
| cat02_03_anomaly_event_log         |     6.5 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     6.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     9   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     6   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     5.5 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     5.5 |
| cat05_02_hyp_gen_powl              |     5.5 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     7.8 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     4.5 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     6   |



### mistral-small-2501   => 24.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.5 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     3.5 |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     3.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     4.5 |
| cat01_08_tables_to_log             |     4.5 |
| cat02_01_conformance_textual       |     6.5 |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     8.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     4.5 |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     9.3 |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     7.5 |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     7   |
| cat05_06_question_pseudo_bpmn      |     9.7 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     5.5 |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     6   |



### open-mixtral-8x22b   => 23.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.5 |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     9.5 |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     4.5 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     8   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     6   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     7   |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     7   |
| cat06_02_bias_event_log            |     6.8 |
| cat06_03_bias_powl                 |     7   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     3.5 |



### gemma327b-it-q8_0   => 23.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     5   |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     4.5 |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     7.8 |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     2   |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     5.5 |
| cat05_01_hyp_generation_log        |     4.5 |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     7   |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     9.7 |
| cat06_02_bias_event_log            |     7.5 |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     5.5 |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     6   |
| cat07_01_ocdfg                     |     1   |
| cat07_02_bpmn_orders               |     6   |
| cat07_03_bpmn_dispatch             |     1   |
| cat07_04_causal_net                |     4   |
| cat07_05_proclets                  |     5.5 |
| cat07_06_perf_spectrum             |     4   |



### QwenQwen2.5-Coder-32B-Instruct   => 23.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     5   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     5.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     6   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     5.5 |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9.8 |
| cat03_01_process_tree_generation   |     5   |
| cat03_02_powl_generation           |     9.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     4.5 |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     6.5 |
| cat04_07_sql_filt_top_k_vars       |     7.7 |
| cat05_01_hyp_generation_log        |     3.5 |
| cat05_02_hyp_gen_powl              |     5.5 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     5   |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     7   |



### qwen2.5-32b-instruct   => 23.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |     6.8 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     7   |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     3.5 |
| cat05_02_hyp_gen_powl              |     5.5 |
| cat05_03_hyp_gen_declare           |     6.5 |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9.8 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     7.5 |
| cat06_04_bias_two_logs             |     8.5 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     5   |



### DeepSeek-R1-Distill-Qwen-14B   => 22.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     9.4 |
| cat01_02_activity_context          |     4.2 |
| cat01_03_high_level_events         |     2   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     3.1 |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     4.8 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     6.6 |
| cat02_04_powl_anomaly_detection    |     7.7 |
| cat02_05_two_powls_anomalies       |     7.1 |
| cat02_06_root_cause_1              |     3.1 |
| cat02_07_root_cause_2              |     4.2 |
| cat02_08_underfitting_process_tree |     9.4 |
| cat02_09_fix_process_tree          |     5.4 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     8.3 |
| cat03_03_log_skeleton_generation   |     5.4 |
| cat03_04_declare_generation        |     3.1 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     8.9 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2.5 |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     9.4 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     5.4 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     8.9 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     7.7 |
| cat06_02_bias_event_log            |     7.1 |
| cat06_03_bias_powl                 |     4.2 |
| cat06_04_bias_two_logs             |     3.1 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     4.2 |
| cat06_07_fair_unfair_powl          |     2.5 |



### MiniMax-01   => 22.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     3   |
| cat01_03_high_level_events         |     8.4 |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     6.5 |
| cat02_02_conf_desiderata           |     6.5 |
| cat02_03_anomaly_event_log         |     7   |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     4   |
| cat03_01_process_tree_generation   |     3.5 |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     2.5 |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     6.1 |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     9.2 |
| cat06_06_bias_mitigation_declare   |     1.5 |
| cat06_07_fair_unfair_powl          |     6   |



### gpt-4o-mini-2024-07-18   => 22.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     5   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     3.5 |
| cat02_01_conformance_textual       |     8   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     8   |
| cat02_04_powl_anomaly_detection    |     5   |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     5   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     7.5 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     7.5 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     6.5 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     9.2 |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     2   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     4   |
| cat06_07_fair_unfair_powl          |     7   |
| cat07_01_ocdfg                     |     7   |
| cat07_02_bpmn_orders               |     7.5 |
| cat07_03_bpmn_dispatch             |     5   |
| cat07_04_causal_net                |     6.5 |
| cat07_05_proclets                  |     7.5 |
| cat07_06_perf_spectrum             |     8.5 |



### codestral-2501   => 22.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     8.5 |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     9   |
| cat02_01_conformance_textual       |     5   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     4.5 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     2.5 |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     4.5 |
| cat04_01_pseudo_bpmn_description   |     4.5 |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |    10   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     5.5 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     9.2 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     6.5 |
| cat06_01_bias_text                 |     4.5 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     6.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     6   |



### gemma312b-it-q8_0   => 22.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     5.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5.5 |
| cat01_08_tables_to_log             |     5   |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     3   |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     3.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     4   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     6.5 |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     4.5 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     6   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     5.5 |
| cat05_03_hyp_gen_declare           |     3.5 |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     8.8 |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     9.5 |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     6.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     9   |
| cat07_01_ocdfg                     |     3.5 |
| cat07_02_bpmn_orders               |     4.5 |
| cat07_03_bpmn_dispatch             |     4.5 |
| cat07_04_causal_net                |     4.5 |
| cat07_05_proclets                  |     7.8 |
| cat07_06_perf_spectrum             |     4   |



### claude-3-5-haiku-20241022   => 22.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6.8 |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     9   |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     4.5 |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     6.5 |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     5.5 |
| cat02_04_powl_anomaly_detection    |     8.8 |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     4.5 |
| cat02_07_root_cause_2              |     4.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     4   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     1.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     4.5 |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     8.5 |
| cat04_06_sql_filt_three_df         |     6   |
| cat04_07_sql_filt_top_k_vars       |     7.5 |
| cat05_01_hyp_generation_log        |     3.5 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     4.5 |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     5   |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     2.5 |



### qwen2.5-14b-instruct   => 22.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.5 |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     5   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     5.5 |
| cat02_03_anomaly_event_log         |     5.5 |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     4   |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     5   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     1.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     4.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     6.5 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     5   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     7   |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     7   |
| cat06_03_bias_powl                 |     5   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     4   |



### qwen2.5-14b-instruct-1m   => 22.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     8   |
| cat01_03_high_level_events         |     5   |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     4   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     9   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     5.5 |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     4   |
| cat02_07_root_cause_2              |     6   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     4   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     3   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     7.5 |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     4   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     6.5 |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     9   |
| cat05_07_question_interview        |     7.8 |
| cat06_01_bias_text                 |     9   |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     8   |
| cat06_04_bias_two_logs             |     5.5 |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     3.5 |



### meta-llamaLlama-3.2-90B-Vision-Instruct   => 21.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.5 |
| cat01_02_activity_context          |     5   |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     5   |
| cat02_02_conf_desiderata           |     6   |
| cat02_03_anomaly_event_log         |     6   |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8   |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     6   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     4.5 |
| cat04_02_pseudo_bpmn_open_question |     5   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     8   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     8.2 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     5.5 |
| cat06_02_bias_event_log            |     3.5 |
| cat06_03_bias_powl                 |     4.5 |
| cat06_04_bias_two_logs             |     5.5 |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     2.5 |
| cat07_01_ocdfg                     |     5   |
| cat07_02_bpmn_orders               |     6.5 |
| cat07_03_bpmn_dispatch             |     4   |
| cat07_04_causal_net                |     3   |
| cat07_05_proclets                  |     3   |
| cat07_06_perf_spectrum             |     3.5 |



### falcon310b-instruct-q8_0   => 21.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5   |
| cat01_02_activity_context          |     7.5 |
| cat01_03_high_level_events         |     3.5 |
| cat01_04_sensor_recordings         |     6.5 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     4.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     9.5 |
| cat02_02_conf_desiderata           |     5   |
| cat02_03_anomaly_event_log         |     5   |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     6   |
| cat02_07_root_cause_2              |     4   |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     8.5 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     2.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3.5 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     5   |
| cat05_01_hyp_generation_log        |     4   |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     3.5 |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     9.7 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     9.2 |
| cat06_02_bias_event_log            |     3.5 |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     6.5 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     5   |
| cat06_07_fair_unfair_powl          |     6.5 |



### sonar-reasoning-pro   => 21.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     4.2 |
| cat01_02_activity_context          |     4.8 |
| cat01_03_high_level_events         |     3.1 |
| cat01_04_sensor_recordings         |     6.6 |
| cat01_05_merge_two_logs            |     6   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     3.1 |
| cat02_01_conformance_textual       |     5.4 |
| cat02_02_conf_desiderata           |     5.4 |
| cat02_03_anomaly_event_log         |     9.1 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     4.8 |
| cat02_06_root_cause_1              |     8.9 |
| cat02_07_root_cause_2              |     3.7 |
| cat02_08_underfitting_process_tree |     6   |
| cat02_09_fix_process_tree          |     6.6 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     2.5 |
| cat03_03_log_skeleton_generation   |     3.7 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     6   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     3.1 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.7 |
| cat04_06_sql_filt_three_df         |     4.2 |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     5.4 |
| cat05_02_hyp_gen_powl              |     7.2 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     3.1 |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     8.9 |
| cat05_07_question_interview        |     8.9 |
| cat06_01_bias_text                 |     4.8 |
| cat06_02_bias_event_log            |     6   |
| cat06_03_bias_powl                 |     4.2 |
| cat06_04_bias_two_logs             |     6.6 |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     3.1 |



### exaone-deep2.4b-fp16   => 21.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     1.4 |
| cat01_03_high_level_events         |     9.4 |
| cat01_04_sensor_recordings         |     5.4 |
| cat01_05_merge_two_logs            |     8.6 |
| cat01_06_system_logs               |     4.8 |
| cat01_07_interv_to_pseudo_bpmn     |     5.4 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     9.4 |
| cat02_02_conf_desiderata           |     7.7 |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     8.9 |
| cat02_05_two_powls_anomalies       |     8.9 |
| cat02_06_root_cause_1              |     4.8 |
| cat02_07_root_cause_2              |     3.1 |
| cat02_08_underfitting_process_tree |     3.1 |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     4.2 |
| cat03_03_log_skeleton_generation   |     3.7 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     3.1 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     9.4 |
| cat04_02_pseudo_bpmn_open_question |     3.1 |
| cat04_03_declare_open_question     |     3.7 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.1 |
| cat04_06_sql_filt_three_df         |     3.1 |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     5.4 |
| cat05_05_question_gen_nlp          |     8.3 |
| cat05_06_question_pseudo_bpmn      |     4.8 |
| cat05_07_question_interview        |     8.3 |
| cat06_01_bias_text                 |     5.4 |
| cat06_02_bias_event_log            |     3.7 |
| cat06_03_bias_powl                 |     7.1 |
| cat06_04_bias_two_logs             |     8.9 |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |



### googlegemma-2-9b-it   => 21.0 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     6.5 |
| cat01_04_sensor_recordings         |     3.5 |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     3.5 |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     3.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     7.5 |
| cat03_01_process_tree_generation   |     3   |
| cat03_02_powl_generation           |     8.5 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     6   |
| cat03_05_temp_profile_generation   |     2.5 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     4.5 |
| cat04_02_pseudo_bpmn_open_question |     6.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     4   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     9   |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     3.5 |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     4.5 |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     5.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     7.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     4   |



### qwen-turbo-2024-11-01   => 20.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2.5 |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     6   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     5   |
| cat02_03_anomaly_event_log         |     3   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     5   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     2.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2.5 |
| cat03_05_temp_profile_generation   |     3.5 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     5.5 |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     5.5 |
| cat05_01_hyp_generation_log        |     3.5 |
| cat05_02_hyp_gen_powl              |     5   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     8   |
| cat05_06_question_pseudo_bpmn      |     8.2 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     8.5 |
| cat06_02_bias_event_log            |     5.5 |
| cat06_03_bias_powl                 |     3   |
| cat06_04_bias_two_logs             |     5.5 |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     5   |



### pixtral-12b-2409   => 20.5 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     3.5 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     4.5 |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     4.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     7   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     5   |
| cat02_04_powl_anomaly_detection    |     6.5 |
| cat02_05_two_powls_anomalies       |     4.5 |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     4   |
| cat03_02_powl_generation           |     6.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     3   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     6   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     3.5 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     5.5 |
| cat05_05_question_gen_nlp          |     7   |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     8.2 |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     6.8 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     6.5 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     3   |
| cat07_01_ocdfg                     |     8.5 |
| cat07_02_bpmn_orders               |     6.5 |
| cat07_03_bpmn_dispatch             |     3.5 |
| cat07_04_causal_net                |     6   |
| cat07_05_proclets                  |    10   |
| cat07_06_perf_spectrum             |     6   |



### falcon37b-instruct-q8_0   => 20.4 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     6.5 |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |     5   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     8.5 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     5   |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     9.8 |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     4.5 |
| cat04_02_pseudo_bpmn_open_question |     5.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     8.5 |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     6   |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     2   |
| cat06_04_bias_two_logs             |     5.5 |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     5   |



### qwen2.5-omni-7b   => 18.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2.5 |
| cat01_02_activity_context          |     7   |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     4   |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     3.5 |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     3   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     4   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     9.5 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     4.5 |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     3.5 |
| cat05_05_question_gen_nlp          |     9.3 |
| cat05_06_question_pseudo_bpmn      |     9.2 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     6.5 |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     4   |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     3.5 |
| cat07_01_ocdfg                     |     3.5 |
| cat07_02_bpmn_orders               |     1   |
| cat07_03_bpmn_dispatch             |     3.5 |
| cat07_04_causal_net                |     3.5 |
| cat07_05_proclets                  |     3.5 |
| cat07_06_perf_spectrum             |     7.5 |



### qwen2.5-7b-instruct   => 18.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     7.5 |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     4.5 |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3   |
| cat02_04_powl_anomaly_detection    |     7.5 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     4.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     4   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     5.5 |
| cat04_02_pseudo_bpmn_open_question |     5   |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     7   |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     5.5 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     6.5 |
| cat06_02_bias_event_log            |     5   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     3   |



### gpt-3.5-turbo   => 18.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     5.5 |
| cat01_02_activity_context          |     8.3 |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1.5 |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2.3 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     3.5 |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     7.5 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     4   |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     7   |
| cat06_06_bias_mitigation_declare   |     3.5 |
| cat06_07_fair_unfair_powl          |     2.5 |



### ministral-3b-2410   => 18.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     6   |
| cat01_02_activity_context          |     2   |
| cat01_03_high_level_events         |     4.5 |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     4   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3.5 |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     7   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     5.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     4   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     6   |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     4   |
| cat05_04_hyp_gen_temp_profile      |     4   |
| cat05_05_question_gen_nlp          |     8.7 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     7   |
| cat06_02_bias_event_log            |     3   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     3   |



### DeepSeek-R1-Distill-Llama-8B   => 18.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     7.7 |
| cat01_02_activity_context          |     3.1 |
| cat01_03_high_level_events         |     3.7 |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     4.8 |
| cat01_06_system_logs               |     3.1 |
| cat01_07_interv_to_pseudo_bpmn     |     3.1 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     4.2 |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     3.1 |
| cat02_04_powl_anomaly_detection    |     4.8 |
| cat02_05_two_powls_anomalies       |     1   |
| cat02_06_root_cause_1              |     4.2 |
| cat02_07_root_cause_2              |     5.4 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     8.9 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     9.4 |
| cat03_03_log_skeleton_generation   |     1.4 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1.4 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     3.1 |
| cat04_01_pseudo_bpmn_description   |     6.6 |
| cat04_02_pseudo_bpmn_open_question |     4.2 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     8.9 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3.1 |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     7.1 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     9.1 |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     5.4 |
| cat06_01_bias_text                 |     5.4 |
| cat06_02_bias_event_log            |     8.9 |
| cat06_03_bias_powl                 |     7.7 |
| cat06_04_bias_two_logs             |     6.6 |
| cat06_05_bias_two_logs_2           |     8.9 |
| cat06_06_bias_mitigation_declare   |     3.1 |
| cat06_07_fair_unfair_powl          |     2   |



### granite3.28b-instruct-q4_K_M   => 17.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     4.5 |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     2.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     3.5 |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     7   |
| cat04_02_pseudo_bpmn_open_question |     3   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     2.5 |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     4.5 |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     9.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     8   |
| cat06_02_bias_event_log            |     3.5 |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     3   |



### gemma34b-it-q8_0   => 17.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2.5 |
| cat01_02_activity_context          |     3   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     2.5 |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3   |
| cat02_04_powl_anomaly_detection    |     9.2 |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     1   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     9   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     9.8 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1.5 |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     5   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     8.8 |
| cat05_07_question_interview        |     8.8 |
| cat06_01_bias_text                 |     7.5 |
| cat06_02_bias_event_log            |     3.5 |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     3.5 |
| cat06_05_bias_two_logs_2           |     8   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     1   |
| cat07_01_ocdfg                     |     3.5 |
| cat07_02_bpmn_orders               |     3   |
| cat07_03_bpmn_dispatch             |     2.5 |
| cat07_04_causal_net                |     4.5 |
| cat07_05_proclets                  |     4   |
| cat07_06_perf_spectrum             |     2.5 |



### qwen2.5-7b-instruct-1m   => 17.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     3   |
| cat01_02_activity_context          |     6   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     3.5 |
| cat01_05_merge_two_logs            |     1.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     4   |
| cat02_04_powl_anomaly_detection    |     3.5 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     5   |
| cat02_09_fix_process_tree          |     4   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     3   |
| cat04_03_declare_open_question     |     3.5 |
| cat04_04_declare_description       |     2.5 |
| cat04_05_sql_filt_num_events       |     8   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     3.5 |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     5.5 |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     6.5 |
| cat06_03_bias_powl                 |     4   |
| cat06_04_bias_two_logs             |     4.5 |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     3   |



### command-r7b7b-12-2024-q4_K_M   => 16.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2.5 |
| cat01_02_activity_context          |     2.5 |
| cat01_03_high_level_events         |     3.8 |
| cat01_04_sensor_recordings         |     3.5 |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     4   |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     4.5 |
| cat02_03_anomaly_event_log         |     3   |
| cat02_04_powl_anomaly_detection    |     5.5 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     2.5 |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     1.5 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     6.5 |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     6   |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     9   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2.5 |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     4   |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     7.5 |
| cat05_06_question_pseudo_bpmn      |     7   |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     6.8 |
| cat06_02_bias_event_log            |     4.5 |
| cat06_03_bias_powl                 |     5.5 |
| cat06_04_bias_two_logs             |     6   |
| cat06_05_bias_two_logs_2           |     6   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     1.5 |



### meta-llamaMeta-Llama-3.1-8B-Instruct   => 16.3 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1.5 |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     5.5 |
| cat01_04_sensor_recordings         |     2.5 |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     1.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     3   |
| cat02_01_conformance_textual       |     4   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     7   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     2.5 |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     3.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1.5 |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     4   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     7   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     8.8 |
| cat05_02_hyp_gen_powl              |     6   |
| cat05_03_hyp_gen_declare           |     3   |
| cat05_04_hyp_gen_temp_profile      |     3.5 |
| cat05_05_question_gen_nlp          |     7   |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     5.5 |
| cat06_04_bias_two_logs             |     3   |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     2.5 |



### falcon33b-instruct-q8_0   => 15.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     4   |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     4   |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     6.8 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     6.5 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     2.5 |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     2   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3.5 |
| cat04_05_sql_filt_num_events       |     6.5 |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     6.5 |
| cat05_06_question_pseudo_bpmn      |     8.5 |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     7.8 |
| cat06_02_bias_event_log            |     3   |
| cat06_03_bias_powl                 |     4.5 |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     2.5 |



### microsoftPhi-4-multimodal-instruct   => 14.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     2.5 |
| cat01_03_high_level_events         |     3.2 |
| cat01_04_sensor_recordings         |     2.5 |
| cat01_05_merge_two_logs            |     2.5 |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     2   |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3.5 |
| cat02_04_powl_anomaly_detection    |     5.5 |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     3   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     6   |
| cat03_01_process_tree_generation   |     1.5 |
| cat03_02_powl_generation           |     1.5 |
| cat03_03_log_skeleton_generation   |     1.5 |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     5   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     6.5 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     1.5 |
| cat05_01_hyp_generation_log        |     2.5 |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     3.5 |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9.5 |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     6.8 |
| cat06_02_bias_event_log            |     3.5 |
| cat06_03_bias_powl                 |     5.5 |
| cat06_04_bias_two_logs             |     3   |
| cat06_05_bias_two_logs_2           |     5.5 |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     2   |
| cat07_01_ocdfg                     |     6.5 |
| cat07_02_bpmn_orders               |     4   |
| cat07_03_bpmn_dispatch             |     2   |
| cat07_04_causal_net                |     3   |
| cat07_05_proclets                  |     9   |
| cat07_06_perf_spectrum             |     3.5 |



### meta-llamaLlama-3.2-11B-Vision-Instruct   => 14.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     2.5 |
| cat01_03_high_level_events         |     3   |
| cat01_04_sensor_recordings         |     6   |
| cat01_05_merge_two_logs            |     4   |
| cat01_06_system_logs               |     5   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     5   |
| cat02_03_anomaly_event_log         |     3   |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     3.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     2.5 |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     3   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     3   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     2   |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     3   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     4   |
| cat04_03_declare_open_question     |     1   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     6   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     3   |
| cat05_02_hyp_gen_powl              |     1   |
| cat05_03_hyp_gen_declare           |     2.5 |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     5   |
| cat05_07_question_interview        |     8.5 |
| cat06_01_bias_text                 |     6   |
| cat06_02_bias_event_log            |     3   |
| cat06_03_bias_powl                 |     1.5 |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     1.5 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |
| cat07_01_ocdfg                     |     2   |
| cat07_02_bpmn_orders               |     3.5 |
| cat07_03_bpmn_dispatch             |     3.5 |
| cat07_04_causal_net                |     5   |
| cat07_05_proclets                  |     3   |
| cat07_06_perf_spectrum             |     4   |



### olmo27b-1124-instruct-q8_0   => 14.6 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2.5 |
| cat01_02_activity_context          |     3   |
| cat01_03_high_level_events         |     3   |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     3.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     1.5 |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3   |
| cat02_04_powl_anomaly_detection    |     8   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     2.5 |
| cat02_07_root_cause_2              |     3.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     3   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     1.5 |
| cat03_06_petri_net_generation      |     1.5 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     4.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     2   |
| cat04_06_sql_filt_three_df         |     1.5 |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     6   |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     8.5 |
| cat05_06_question_pseudo_bpmn      |     1   |
| cat05_07_question_interview        |     8   |
| cat06_01_bias_text                 |     7.8 |
| cat06_02_bias_event_log            |     4   |
| cat06_03_bias_powl                 |     6   |
| cat06_04_bias_two_logs             |     3   |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     3   |
| cat06_07_fair_unfair_powl          |     1.5 |



### meta-llamaLlama-3.2-3B-Instruct   => 14.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     3.5 |
| cat01_04_sensor_recordings         |     3   |
| cat01_05_merge_two_logs            |     3.5 |
| cat01_06_system_logs               |     3   |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     3   |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     3   |
| cat02_04_powl_anomaly_detection    |     4   |
| cat02_05_two_powls_anomalies       |     3   |
| cat02_06_root_cause_1              |     3   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     3   |
| cat02_09_fix_process_tree          |     3   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     1.5 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3   |
| cat03_06_petri_net_generation      |     1.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     3   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     4   |
| cat04_06_sql_filt_three_df         |     3   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     1.5 |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9.3 |
| cat05_06_question_pseudo_bpmn      |     7.5 |
| cat05_07_question_interview        |     9   |
| cat06_01_bias_text                 |     5   |
| cat06_02_bias_event_log            |     3.5 |
| cat06_03_bias_powl                 |     2.5 |
| cat06_04_bias_two_logs             |     2.5 |
| cat06_05_bias_two_logs_2           |     4   |
| cat06_06_bias_mitigation_declare   |     2.5 |
| cat06_07_fair_unfair_powl          |     1.5 |



### qwen2.53b-instruct-q8_0   => 14.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     4   |
| cat01_03_high_level_events         |     4   |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     2   |
| cat01_06_system_logs               |     1.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     2.5 |
| cat02_01_conformance_textual       |     1.5 |
| cat02_02_conf_desiderata           |     3   |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     4   |
| cat02_05_two_powls_anomalies       |     2.5 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     2.5 |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     2   |
| cat03_01_process_tree_generation   |     2   |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     2   |
| cat03_04_declare_generation        |     4   |
| cat03_05_temp_profile_generation   |     1.5 |
| cat03_06_petri_net_generation      |     1.5 |
| cat03_07_process_tree_discovery    |     2   |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     4   |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     2.5 |
| cat04_06_sql_filt_three_df         |     2   |
| cat04_07_sql_filt_top_k_vars       |     3   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     2.5 |
| cat05_04_hyp_gen_temp_profile      |     3   |
| cat05_05_question_gen_nlp          |     9   |
| cat05_06_question_pseudo_bpmn      |     8   |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     6.8 |
| cat06_02_bias_event_log            |     5.5 |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     4   |
| cat06_05_bias_two_logs_2           |     3   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     2   |



### DeepSeek-R1-Distill-Qwen-7B   => 13.1 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     6   |
| cat01_04_sensor_recordings         |     3.1 |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     2.5 |
| cat01_08_tables_to_log             |     1.4 |
| cat02_01_conformance_textual       |     2.5 |
| cat02_02_conf_desiderata           |     2.5 |
| cat02_03_anomaly_event_log         |     1.4 |
| cat02_04_powl_anomaly_detection    |     6   |
| cat02_05_two_powls_anomalies       |     3.1 |
| cat02_06_root_cause_1              |     1.4 |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     6.6 |
| cat03_01_process_tree_generation   |     3.1 |
| cat03_02_powl_generation           |     2   |
| cat03_03_log_skeleton_generation   |     2.5 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     3.1 |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     4.8 |
| cat04_02_pseudo_bpmn_open_question |     4.8 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     6   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     3.1 |
| cat05_03_hyp_gen_declare           |     2.5 |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     9.4 |
| cat05_06_question_pseudo_bpmn      |     8.3 |
| cat05_07_question_interview        |     6   |
| cat06_01_bias_text                 |     3.7 |
| cat06_02_bias_event_log            |     4.8 |
| cat06_03_bias_powl                 |     1.4 |
| cat06_04_bias_two_logs             |     3.1 |
| cat06_05_bias_two_logs_2           |     4.2 |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     1   |



### qwen2.51.5b-instruct-q6_K   => 11.2 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1.5 |
| cat01_02_activity_context          |     2   |
| cat01_03_high_level_events         |     2   |
| cat01_04_sensor_recordings         |     2   |
| cat01_05_merge_two_logs            |     3   |
| cat01_06_system_logs               |     6   |
| cat01_07_interv_to_pseudo_bpmn     |     3.5 |
| cat01_08_tables_to_log             |     2   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     2.5 |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     2   |
| cat02_09_fix_process_tree          |     2   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     2   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1.5 |
| cat03_07_process_tree_discovery    |     1.5 |
| cat03_08_powl_discovery            |     1.5 |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     3.5 |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     3   |
| cat04_05_sql_filt_num_events       |     2   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     2   |
| cat05_01_hyp_generation_log        |     2   |
| cat05_02_hyp_gen_powl              |     3   |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     6   |
| cat05_06_question_pseudo_bpmn      |     6   |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     4   |
| cat06_02_bias_event_log            |     2.5 |
| cat06_03_bias_powl                 |     3   |
| cat06_04_bias_two_logs             |     2   |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     2   |
| cat06_07_fair_unfair_powl          |     1.5 |



### gemma31b-it-q8_0   => 10.7 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     1   |
| cat01_03_high_level_events         |     2   |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1.5 |
| cat01_07_interv_to_pseudo_bpmn     |     3   |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     1   |
| cat02_02_conf_desiderata           |     1.5 |
| cat02_03_anomaly_event_log         |     1.5 |
| cat02_04_powl_anomaly_detection    |     3   |
| cat02_05_two_powls_anomalies       |     1.5 |
| cat02_06_root_cause_1              |     2   |
| cat02_07_root_cause_2              |     2   |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     5.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1.5 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1.5 |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     3   |
| cat04_02_pseudo_bpmn_open_question |     2   |
| cat04_03_declare_open_question     |     2.5 |
| cat04_04_declare_description       |     2   |
| cat04_05_sql_filt_num_events       |     2   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     6.4 |
| cat05_02_hyp_gen_powl              |     2.5 |
| cat05_03_hyp_gen_declare           |     2.5 |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     6   |
| cat05_06_question_pseudo_bpmn      |     5.5 |
| cat05_07_question_interview        |     7.5 |
| cat06_01_bias_text                 |     6.5 |
| cat06_02_bias_event_log            |     3   |
| cat06_03_bias_powl                 |     3   |
| cat06_04_bias_two_logs             |     2   |
| cat06_05_bias_two_logs_2           |     3   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1.5 |



### meta-llamaLlama-3.2-1B-Instruct   => 8.9 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     2   |
| cat01_02_activity_context          |     1.5 |
| cat01_03_high_level_events         |     2.5 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1.5 |
| cat01_06_system_logs               |     2   |
| cat01_07_interv_to_pseudo_bpmn     |     1.5 |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     2   |
| cat02_03_anomaly_event_log         |     2   |
| cat02_04_powl_anomaly_detection    |     3   |
| cat02_05_two_powls_anomalies       |     2   |
| cat02_06_root_cause_1              |     1.5 |
| cat02_07_root_cause_2              |     1.5 |
| cat02_08_underfitting_process_tree |     1.5 |
| cat02_09_fix_process_tree          |     1.5 |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     1   |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     1   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     2.5 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     1   |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     1.5 |
| cat05_03_hyp_gen_declare           |     2   |
| cat05_04_hyp_gen_temp_profile      |     2   |
| cat05_05_question_gen_nlp          |     6.5 |
| cat05_06_question_pseudo_bpmn      |     4   |
| cat05_07_question_interview        |     7   |
| cat06_01_bias_text                 |     4   |
| cat06_02_bias_event_log            |     1.5 |
| cat06_03_bias_powl                 |     3.5 |
| cat06_04_bias_two_logs             |     2   |
| cat06_05_bias_two_logs_2           |     3.5 |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1   |



### DeepSeek-R1-Distill-Qwen-1.5B   => 7.8 points

| Question                           |   Score |
|:-----------------------------------|--------:|
| cat01_01_case_id_inference         |     1   |
| cat01_02_activity_context          |     2   |
| cat01_03_high_level_events         |     3.1 |
| cat01_04_sensor_recordings         |     1   |
| cat01_05_merge_two_logs            |     1   |
| cat01_06_system_logs               |     1   |
| cat01_07_interv_to_pseudo_bpmn     |     1   |
| cat01_08_tables_to_log             |     1   |
| cat02_01_conformance_textual       |     2   |
| cat02_02_conf_desiderata           |     1   |
| cat02_03_anomaly_event_log         |     1   |
| cat02_04_powl_anomaly_detection    |     5.4 |
| cat02_05_two_powls_anomalies       |     1   |
| cat02_06_root_cause_1              |     1.4 |
| cat02_07_root_cause_2              |     1.4 |
| cat02_08_underfitting_process_tree |     1   |
| cat02_09_fix_process_tree          |     2   |
| cat03_01_process_tree_generation   |     1   |
| cat03_02_powl_generation           |     1   |
| cat03_03_log_skeleton_generation   |     3.1 |
| cat03_04_declare_generation        |     1   |
| cat03_05_temp_profile_generation   |     2   |
| cat03_06_petri_net_generation      |     1   |
| cat03_07_process_tree_discovery    |     1   |
| cat03_08_powl_discovery            |     1   |
| cat04_01_pseudo_bpmn_description   |     2   |
| cat04_02_pseudo_bpmn_open_question |     1.4 |
| cat04_03_declare_open_question     |     2   |
| cat04_04_declare_description       |     1.4 |
| cat04_05_sql_filt_num_events       |     1   |
| cat04_06_sql_filt_three_df         |     1   |
| cat04_07_sql_filt_top_k_vars       |     1   |
| cat05_01_hyp_generation_log        |     1   |
| cat05_02_hyp_gen_powl              |     2   |
| cat05_03_hyp_gen_declare           |     1   |
| cat05_04_hyp_gen_temp_profile      |     1   |
| cat05_05_question_gen_nlp          |     6   |
| cat05_06_question_pseudo_bpmn      |     3.1 |
| cat05_07_question_interview        |     2.5 |
| cat06_01_bias_text                 |     4.8 |
| cat06_02_bias_event_log            |     2   |
| cat06_03_bias_powl                 |     1.4 |
| cat06_04_bias_two_logs             |     1   |
| cat06_05_bias_two_logs_2           |     2   |
| cat06_06_bias_mitigation_declare   |     1   |
| cat06_07_fair_unfair_powl          |     1.4 |

