#!/usr/bin/env python3
import os
import threading
import requests
import argparse
import json

# List of required category keys
CATEGORY_KEYS = [
    "1a_instruction_override",
    "1b_context_omission",
    "1c_prompt_contradiction",
    "2a_concept_fabrication",
    "2b_spurious_numeric",
    "2c_false_citation",
    "3a_unsupported_leap",
    "3b_self_contradiction",
    "3c_circular_reasoning",
    "4a_syntax_error",
    "4b_model_semantics_breach",
    "4c_visual_descr_mismatch"
]

PREFIX = """
## Task

I provide you the evaluation of an expert judge LLM over the answers of another LLM.
Detect every occurrence of hallucination according to the taxonomy defined in § “Hallucination taxonomy” (next section).  
For **each sub‑category** you must report:
1. **count**	– the number of distinct hallucinations of that type you found;  
2. **instances**	– an array where each element gives
   * `"snippet"` – a short excerpt (≤ 25 words) or JSON/code line number that shows the hallucination,
   * `"why"` – 1‑2 sentences explaining why it falls in this sub‑category,
   * `"severity"` – one of `"low" | "medium" | "high" | "critical"` following the scale in § “Severity scale”.

At the end provide the **overall total** across all sub‑categories.

## Hallucination taxonomy  *(copy for reference)*
```
1 Prompt‑faithfulness
  1a Instruction‑override | ignores an explicit constraint in the prompt
  1b Context‑omission   | silently drops prompt context needed for the answer
  1c Prompt‑contradiction | states the opposite of the prompt

2 Domain‑factual
  2a Concept fabrication   | invents a PM concept / method / KPI definition
  2b Spurious numeric      | uses numbers not supported by prompt or sources
  2c False citation        | attributes a statement to a non‑existent/ wrong source

3 Reasoning‑logic
  3a Unsupported leap      | conclusion not justified by preceding facts
  3b Self‑contradiction   | claims that conflict within the same answer
  3c Circular reasoning   | uses claim as its own proof

4 Structural / format
  4a Syntax error          | invalid JSON / code etc.
  4b Model‑semantics breach| violates modelling notation rules
  4c Visual/descr. mismatch| describes element not present in image/diagram
```  

## Severity scale
* **low**  Minor inconsistency; does not alter the main usefulness.
* **medium** Noticeable error; could mislead a non‑expert or require repair.
* **high**  Substantially wrong; invalidates a key part of the answer.
* **critical** Fatal; the answer cannot be used as‑is.

## Output format (JSON, no extra text)
```json
{
  "categories": {
    "1a_instruction_override": { "count": <int>, "instances": [] },
    "1b_context_omission":    { "count": <int>, "instances": [] },
    "1c_prompt_contradiction":{ "count": <int>, "instances": [] },
    "2a_concept_fabrication": { "count": <int>, "instances": [] },
    "2b_spurious_numeric":    { "count": <int>, "instances": [] },
    "2c_false_citation":      { "count": <int>, "instances": [] },
    "3a_unsupported_leap":    { "count": <int>, "instances": [] },
    "3b_self_contradiction":  { "count": <int>, "instances": [] },
    "3c_circular_reasoning":  { "count": <int>, "instances": [] },
    "4a_syntax_error":        { "count": <int>, "instances": [] },
    "4b_model_semantics_breach": { "count": <int>, "instances": [] },
    "4c_visual_descr_mismatch": { "count": <int>, "instances": [] }
  },
  "totals": { "hallucinations_overall": <int> }
}
```

> **Important:**
> • **Return only the JSON dictionary** exactly as above – no markdown fence, no commentary.
> • If an excerpt exceeds 25 words truncate with “…” at the end.
> • When no hallucinations of a sub‑category are present, use `"count": 0` and `"instances": []`.
> • Do not merge different hallucinations into one instance even if adjacent in the text.

## Judge report to evaluate:
"""


def validate_json_response(response_str):
    try:
        data = json.loads(response_str)
    except json.JSONDecodeError:
        return False

    # Top-level structure
    if not isinstance(data, dict):
        return False
    if "categories" not in data or "totals" not in data:
        return False

    # Validate categories
    categories = data["categories"]
    if not isinstance(categories, dict):
        return False
    for cat_key in CATEGORY_KEYS:
        if cat_key not in categories:
            return False
        cat = categories[cat_key]
        if not isinstance(cat, dict):
            return False
        if not isinstance(cat.get("count"), int):
            return False
        instances = cat.get("instances")
        if not isinstance(instances, list):
            return False
        for inst in instances:
            if not isinstance(inst, dict):
                return False
            if set(inst.keys()) != {"snippet", "why", "severity"}:
                return False
            if not isinstance(inst["snippet"], str):
                return False
            if not isinstance(inst["why"], str):
                return False
            if inst["severity"] not in ("low", "medium", "high", "critical"):
                return False

    # Validate totals
    totals = data["totals"]
    if not isinstance(totals, dict):
        return False
    if not isinstance(totals.get("hallucinations_overall"), int):
        return False

    return True


def process_file(input_path, output_path, semaphore):
    """
    Read the input file, send its contents to the OpenAI API, and write the response.
    Only saves if the JSON validation succeeds.
    Uses a semaphore to limit concurrent threads.
    """
    try:
        semaphore.acquire()

        # Read input with fallback for encoding
        try:
            with open(input_path, 'r') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

        # Get API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise EnvironmentError("OPENAI_API_KEY environment variable not set")

        # Build prompt
        prompt = PREFIX + "\n\n" + content
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': 'gpt-4.1-mini',
            'messages': [{'role': 'user', 'content': prompt}]
        }

        # API call
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            json=payload,
            headers=headers
        )
        response.raise_for_status()
        result = response.json()
        reply = result['choices'][0]['message']['content']

        # Validate JSON
        if validate_json_response(reply):
            with open(output_path, 'w', encoding='utf-8') as out_f:
                out_f.write(reply)
            print(f"[SUCCESS] {input_path} -> {output_path}")
        else:
            print(f"[ERROR] JSON validation failed for {input_path}, skipping save.")

    except Exception as e:
        print(f"[ERROR] Failed to process {input_path}: {e}")

    finally:
        semaphore.release()


def main(input_dir, output_dir, max_threads):
    os.makedirs(output_dir, exist_ok=True)

    while True:
        # Gather files that need processing
        to_process = []
        for fname in os.listdir(input_dir):
            if not fname.lower().endswith('.txt'):
                continue
            inp_path = os.path.join(input_dir, fname)
            out_path = os.path.join(output_dir, fname)
            if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
                print(f"[SKIP] {inp_path} already processed.")
            else:
                to_process.append((inp_path, out_path))

        # Session flag: True if attempting to create any files
        session = bool(to_process)
        print(f"[SESSION] Attempting to process files: {session}")

        # If nothing to do, exit loop
        if not session:
            break

        # Process queued files
        semaphore = threading.Semaphore(max_threads)
        threads = []
        for inp_path, out_path in to_process:
            thread = threading.Thread(
                target=process_file,
                args=(inp_path, out_path, semaphore),
                daemon=True
            )
            thread.start()
            threads.append(thread)

        # Wait for all threads in this session to finish
        for t in threads:
            t.join()

    print("[INFO] All files processed.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Process .txt files through OpenAI API with JSON validation"
    )
    parser.add_argument(
        '--input_dir', type=str, default='../evaluation-gemini-2.5-pro',
        help='Path to the input directory containing .txt files'
    )
    parser.add_argument(
        '--output_dir', type=str, default='output',
        help='Path to the directory for saving output .txt files'
    )
    parser.add_argument(
        '--max_threads', type=int, default=10,
        help='Maximum number of concurrent threads'
    )
    args = parser.parse_args()
    main(args.input_dir, args.output_dir, args.max_threads)
