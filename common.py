import os.path
import traceback

import requests
import re
import json
import base64
import sys

from typing import Dict, Any

# the model used to respond to the questions
ANSWERING_MODEL_NAME = "nvidia/llama-3.3-nemotron-super-49b-v1" if len(sys.argv) < 3 else sys.argv[1]

# judge model
EVALUATING_MODEL_NAME = "gpt-4o-2024-11-20" if len(sys.argv) < 3 else sys.argv[2]


class Shared:
    API_KEY = None
    MODEL_NAME = None
    MAX_REQUESTED_TOKENS = 16384
    API_URL = "https://api.openai.com/v1/"
    # API_URL = "http://137.226.117.70:11434/v1/"
    # API_URL = "https://api.deepinfra.com/v1/openai/"
    # API_URL = "https://api.x.ai/v1/"
    # API_URL = "https://api.mistral.ai/v1/"
    # API_URL = "https://generativelanguage.googleapis.com/v1beta/"
    # API_URL = "https://api.anthropic.com/v1/"
    # API_URL = "https://api.groq.com/openai/v1/"
    # API_URL = "https://api.deepseek.com/"
    # API_URL = "https://api.hyperbolic.xyz/v1/"
    # API_URL = "https://api.perplexity.ai/"
    # API_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/"
    # API_URL = "https://integrate.api.nvidia.com/v1/"
    SYSTEM_PROMPT = None
    # SYSTEM_PROMPT = "You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step."
    #SYSTEM_PROMPT = "You are a helpful and harmless assistant."
    TRIAL_CHANGE_EVALUATION_LRM = False
    CUSTOM_TEMPERATURE = None
    #CUSTOM_TEMPERATURE = 0.1
    TRIAL_SEVERE_EVALUATION = True
    ANTHROPIC_THINKING_TOKENS = 65536
    ANTHROPIC_THINKING_TOKENS = None


MODELS_DICT = {
    "openai": {
        "api_url": "https://api.openai.com/v1/",
        "api_key": "sk-",
        "models": {
            "gpt-4o-2024-11-20", "gpt-3.5-turbo",
            "gpt-4-turbo-2024-04-09", "o1-mini-2024-09-12", "o1-preview-2024-09-12",
            "gpt-4.5-preview"
        }
    },
    "google": {
        "api_url": "https://generativelanguage.googleapis.com/v1beta/",
        "api_key": "sk-",
        "models": {
            "gemini-1.5-pro-002", "gemini-2.0-flash",
            "gemini-2.0-flash-thinking-exp-01-21", "gemini-2.0-flash-lite"
        }
    },
    "claude": {
        "api_url": "https://api.anthropic.com/v1/",
        "api_key": "sk-",
        "models": {
            "claude-3-5-sonnet-20241022", "claude-3-opus-20240229", "claude-3-7-sonnet-20250219",
            "claude-3-5-haiku-20241022"
        }
    },
    "mistral": {
        "api_url": "https://api.mistral.ai/v1/",
        "api_key": "sk-",
        "models": {
            "pixtral-large-2411", "pixtral-12b-2409", "ministral-3b-2410",
            "codestral-2501", "mistral-large-2411", "mistral-small-2501", "mistral-small-2503"
        }
    },
    "grok": {
        "api_url": "https://api.x.ai/v1/",
        "api_key": "sk-",
        "models": {
            "grok-2-1212"
        }
    },
    "deepinfra": {
        "api_url": "https://api.deepinfra.com/v1/openai/",
        "api_key": "sk-",
        "models": {
            "meta-llama/Llama-3.3-70B-Instruct", "meta-llama/Meta-Llama-3.1-8B-Instruct",
            "meta-llama/Llama-3.2-90B-Vision-Instruct", "meta-llama/Llama-3.2-11B-Vision-Instruct",
            "meta-llama/Llama-3.2-1B-Instruct", "meta-llama/Llama-3.2-3B-Instruct",
            "nvidia/Llama-3.1-Nemotron-70B-Instruct", "google/gemma-2-9b-it",
            "microsoft/phi-4", "microsoft/WizardLM-2-8x22B", "Qwen/QwQ-32B",
            "microsoft/Phi-4-multimodal-instruct", "microsoft/phi-4", "Qwen/Qwen2.5-Coder-32B-Instruct",
            "deepseek-ai/DeepSeek-V3-0324"
        }
    },
    "ollama_local": {
        "api_url": "http://137.226.117.70:11434/v1/",
        "api_key": "sk-",
        "models": {
            "qwen2.5:3b-instruct-q8_0",
            "falcon3:10b-instruct-q8_0", "falcon3:7b-instruct-q8_0",
            "falcon3:3b-instruct-q8_0", "command-r7b:7b-12-2024-q4_K_M",
            "olmo2:7b-1124-instruct-q8_0", "exaone-deep:32b-fp16",
            "exaone-deep:7.8b-fp16", "exaone-deep:2.4b-fp16",
            "gemma3:27b-it-q8_0", "gemma3:12b-it-q8_0", "gemma3:4b-it-q8_0",
            "gemma3:1b-it-q8_0", "granite3.2:8b-instruct-q4_K_M",
        }
    },
    "qwen": {
        "api_url": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/",
        "api_key": "sk-",
        "models": {
            "qwen-max-2025-01-25", "qwen-plus-2025-01-25", "qwen-turbo-2024-11-01",
            "qwen2.5-72b-instruct", "qwen2.5-32b-instruct", "qwen2.5-14b-instruct",
            "qwen2.5-7b-instruct", "qwen2.5-14b-instruct-1m", "qwen2.5-7b-instruct-1m",
            "qwen2.5:1.5b-instruct-q6_K", "qwen2.5:3b-instruct-q8_0"
        }
    },
    "nvidia": {
        "api_url": "https://integrate.api.nvidia.com/v1/",
        "api_key": "sk-",
        "models": {
            "nvidia/llama-3.3-nemotron-super-49b-v1"
        }
    },
    "manual": {
        "api_url": "http://0.0.0.0:1000/v1/",
        "api_key": "sk-",
        "models": {
            "DeepSeek-R1-Distill-Qwen-32B",
            "DeepSeek-V3", "o1-2024-12-17", "MiniMax-01",
            "gpt-4o-mini-2024-11-05", "Sonus-1-Pro-Reasoning",
            "o1-pro-2024-12-17", "DeepSeek-R1-Distill-Llama-70B",
            "DeepSeek-R1-Distill-Qwen-14B", "DeepSeek-R1-Distill-Llama-8B",
            "DeepSeek-R1-Distill-Qwen-1.5B", "DeepSeek-R1-Distill-Qwen-7B",
            "DeepSeek-R1-Zero", "DeepSeek-R1-671B-DS", "DeepSeek-R1-Dynamic-Quant",
            "DeepSeek-R1-671B-HB", "o3-mini-20250131-HIGH", "o3-mini-20250131-LOW",
            "Perplexity-R1-1776", "Perplexity-Sonar-Pro", "Perplexity-Sonar-Reasoning-Pro",
            "Grok-3-beta-thinking-20250221", "Grok-3-beta-20250220",
            "chatgpt-4o-latest-20250215"
        }
    }
}


def is_visual_model(model_name):
    patterns = ["qwen2-vl", "qwen2.5-vl", "qwen-vl", "pixtral", "gpt-4o", "gpt-4-turbo", "gpt-4.5", "Llama-3.2-11B", "Llama-3.2-90B", "gemini-", "claude-", "grok-vision-beta", "multimodal-", "gemma3:4b", "gemma-3-4b", "gemma3:12b", "gemma-3-12b", "gemma3:12b", "gemma3:27b", "mistral-small-2503"]

    for p in patterns:
        if p.lower() in model_name.lower():
            if "haiku" not in model_name.lower():
                return True

    return False


def is_open_source(m_name):
    m_name = m_name.lower()
    patterns = ["gpt-4", "gpt-3.5", "claude", "gemini", "o1-", "o3-", "ministral-3b", "grok", "sonus", "2.5-plus", "2.5-turbo", "2.5-max", "qwen-plus", "qwen-turbo", "qwen-max", "sonar-"]

    for p in patterns:
        if p in m_name:
            return False

    return True


def is_large_reasoning_model(m_name):
    m_name = m_name.lower()
    patterns = ["o1-", "o3-", "-thinking-", "qwq", "marco", "deepseek-r1", "reason", "r1-1776", "exaone"]

    for p in patterns:
        if p in m_name:
            return True

    return False


def force_custom_evaluation_lrm(answering_model_name):
    model_name = answering_model_name.lower()
    for p in ["qwq", "qvq", "deepseek-r1-distill", "deepseek-ai", "deepseek-r1-zero", "grok-3-beta-thinking", "deepseek-r1-dynamic-quant", "r1-1776", "sonar-reasoning", "exaone"]:
        if p in model_name and not "deepseek-v3" in model_name:
            return True
    return False


def set_api_key(type_key):
    if type_key == "answer":
        answering_api_key_path = "answering_api_key.txt" if os.path.exists(
            "answering_api_key.txt") else "../answering_api_key.txt"
        Shared.API_KEY = open(answering_api_key_path, "r").read().strip()
        Shared.MODEL_NAME = ANSWERING_MODEL_NAME
    else:
        judge_api_key_path = "judge_api_key.txt" if os.path.exists("judge_api_key.txt") else "../judge_api_key.txt"
        Shared.API_KEY = open(judge_api_key_path, "r").read().strip()
        Shared.MODEL_NAME = EVALUATING_MODEL_NAME


def strip_non_unicode_characters(text):
    # Define a pattern that matches all valid Unicode characters.
    pattern = re.compile(r'[^\u0000-\uFFFF]', re.UNICODE)
    # Replace characters not matching the pattern with an empty string.
    cleaned_text = pattern.sub('', text)
    cleaned_text = cleaned_text.encode('cp1252', errors='ignore').decode('cp1252')

    return cleaned_text


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def callback_write(response_message, target_path):
    response_message = strip_non_unicode_characters(response_message)

    F = open(target_path, "w")
    F.write(response_message)
    F.close()


def get_llm_specific_settings() -> Dict[str, Any]:
    model_name = Shared.MODEL_NAME.lower()
    options = {}

    if "api.mistral" not in Shared.API_URL:
        if "mistral" in model_name:
            options["temperature"] = 0.3
            if "7b" in model_name:
                options["temperature"] = 1.0

    if "deepinfra" in Shared.API_URL:
        options["max_tokens"] = Shared.MAX_REQUESTED_TOKENS

    if Shared.CUSTOM_TEMPERATURE is not None:
        options["temperature"] = Shared.CUSTOM_TEMPERATURE

    return options


def dump_payload(payload, target_file):
    if "answers" in target_file:
        target_file = target_file.replace("answers", "json_payload")
        # print(target_file)

        try:
            json.dump(payload, open(target_file, "w"), indent=2)
        except:
            print("payload dumping failed")


def dump_response(response, target_file):
    if "answers" in target_file:
        target_file = target_file.replace("answers", "json_resp")
        # print(target_file)

        try:
            json.dump(response, open(target_file, "w"), indent=2)
        except:
            print("response dumping failed")


def query_text_simple_openai_new(question, api_url, target_file):
    complete_url = api_url
    if not complete_url.endswith("/"):
        complete_url += "/"
    complete_url += "responses"

    payload = {
        "model": Shared.MODEL_NAME,
        "input": question
    }

    if Shared.SYSTEM_PROMPT is not None:
        payload["instructions"] = Shared.SYSTEM_PROMPT

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    dump_payload(payload, target_file)

    response = requests.post(complete_url, headers=headers, json=payload)
    if response.status_code != 200:
        print(response)
        print(response.status_code)
        print(response.text)

    response = response.json()

    dump_response(response, target_file)

    return response["output"][-1]["content"][0]["text"]


def query_text_simple_generic(question, api_url, target_file):
    """
    Generic function to query LLM endpoints:
      - OLLAMA (if "11434" is in api_url)
      - Otherwise, standard OpenAI /v1/chat/completions (optionally streaming)
    """

    # Usually OpenAI's Chat endpoint is /v1/chat/completions
    # If your base api_url doesn't already end with '/v1/',
    # you can do something like:
    complete_url = api_url
    if not complete_url.endswith("/"):
        complete_url += "/"
    complete_url += "chat/completions"  # might be /v1/chat/completions, depending on your setup

    messages = [{"role": "user", "content": question}]

    if Shared.SYSTEM_PROMPT is not None:
        messages = [{"role": "system", "content": Shared.SYSTEM_PROMPT}] + messages

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    # Base payload for OpenAI-like
    payload = {
        "model": Shared.MODEL_NAME,
        "messages": messages,
    }

    # Check if "11434" in api_url (OLLAMA case)
    if "11434" in api_url:
        # OLLAMA with streaming enabled
        options = {"num_ctx": Shared.MAX_REQUESTED_TOKENS}
        options.update(get_llm_specific_settings())

        # Include "stream": True in the payload
        payload = {
            "model": Shared.MODEL_NAME,
            "prompt": question,
            "options": options,
            "stream": True  # ask for a streamed response
        }

        # OLLAMA’s generate endpoint
        ollama_url = complete_url.replace("v1/chat/completions", "api/generate")

        response_message = ""
        chunk_count = 0

        # Use stream=True to process response chunks as they arrive
        with requests.post(ollama_url, headers=headers, json=payload, stream=True) as resp:
            # Iterate over each line in the streamed response
            for line in resp.iter_lines():
                if not line:
                    continue  # skip empty lines

                try:
                    # Each line should be a JSON-encoded object with a "response" field
                    data = json.loads(line.decode("utf-8"))
                except json.JSONDecodeError:
                    # If the line is not valid JSON, skip it
                    continue

                # Append the chunk's text to our overall response message
                chunk = data.get("response", "")
                response_message += chunk
                chunk_count += 1
                #print(chunk_count)

                if chunk_count % 10 == 0:
                    #print(chunk_count)
                    #print(chunk_count, len(response_message), response_message.replace("\n", " ").replace("\r", "").strip())
                    pass

    else:
        # Non-OLLAMA (OpenAI or OpenAI-compatible endpoint)
        payload.update(get_llm_specific_settings())

        # For debugging/logging
        dump_payload(payload, target_file)

        # Decide if we want streaming
        streaming_enabled = True

        if streaming_enabled:
            payload["stream"] = True
            response_message = ""
            chunk_count = 0

            # We add stream=True to requests so we can iterate over chunks
            with requests.post(complete_url, headers=headers, json=payload, stream=True) as resp:
                for line in resp.iter_lines():
                    if not line:
                        continue
                    decoded_line = line.decode("utf-8")

                    # OpenAI-style streaming lines begin with "data: "
                    if decoded_line.startswith("data: "):
                        data_str = decoded_line[len("data: "):].strip()
                        if data_str == "[DONE]":
                            # End of stream
                            break
                        try:
                            data_json = json.loads(data_str)
                            if "choices" in data_json:
                                # Each chunk has a delta with partial content
                                chunk_content = data_json["choices"][0]["delta"].get("content", "")
                                response_message += chunk_content
                                chunk_count += 1
                                #print(chunk_count)
                                if chunk_count % 10 == 0:
                                    #print(chunk_count, len(response_message), response_message.replace("\n", " ").replace("\r", "").strip())
                                    pass
                        except json.JSONDecodeError:
                            # Possibly a keep-alive or incomplete chunk
                            traceback.print_exc()

            # Optionally store the final result so you can debug
            final_response = {
                "choices": [
                    {"message": {"content": response_message}}
                ]
            }
            dump_response(final_response, target_file)

        else:
            # Non-streaming call
            response = requests.post(complete_url, headers=headers, json=payload)
            response = response.json()
            dump_response(response, target_file)
            try:
                response_message = response["choices"][0]["message"]["content"]
            except Exception as e:
                raise Exception(str(response))

    return response_message



def query_text_simple_anthropic(question, api_url, target_file):
    complete_url = api_url + "messages"

    messages = [{"role": "user", "content": question}]

    headers = {
        "content-type": "application/json",
        "anthropic-version": "2023-06-01",
        "anthropic-beta": "output-128k-2025-02-19",
        "x-api-key": Shared.API_KEY
    }

    payload = {
        "model": Shared.MODEL_NAME,
        "max_tokens": Shared.MAX_REQUESTED_TOKENS,
        "messages": messages
    }

    if Shared.ANTHROPIC_THINKING_TOKENS is not None:
        payload["thinking"] = {"type": "enabled", "budget_tokens": Shared.ANTHROPIC_THINKING_TOKENS}
        payload["max_tokens"] += Shared.ANTHROPIC_THINKING_TOKENS
        payload["max_tokens"] = min(128000, payload["max_tokens"])

    dump_payload(payload, target_file)

    response_message = ""

    streaming_enabled = False

    if streaming_enabled:
        payload["stream"] = True
        chunk_count = 0

        # Make a streaming POST request
        with requests.post(complete_url, headers=headers, json=payload, stream=True) as resp:
            for line in resp.iter_lines():
                if not line:
                    continue
                # Decode the line
                decoded_line = line.decode("utf-8").strip()

                # Optionally check for a stream end marker (Anthropic may send "[DONE]")
                if "message_stop" in decoded_line:
                    break

                if "message_start" in decoded_line:
                    continue

                try:
                    decoded_line = decoded_line.split("data: ")[-1].strip()
                    if "text" in decoded_line:
                        chunk = decoded_line.split('"text":"')[-1].split('"')[0].replace("\\n", "\n")
                        response_message += chunk
                        chunk_count += 1
                        #print(chunk_count)

                        # You could add logging or progress updates here if desired
                        if chunk_count % 10 == 0:
                            #print(chunk_count, len(response_message), response_message)
                            pass

                except json.JSONDecodeError:
                    # Skip any malformed lines
                    traceback.print_exc()
                    continue
    else:
        with requests.post(complete_url, headers=headers, json=payload) as resp:
            respj = resp.json()
            response_message = respj["content"][-1]["text"]

    # Optionally, dump the final aggregated response for debugging
    final_response = {"content": [{"text": response_message}]}
    dump_response(final_response, target_file)

    return response_message


def query_text_simple_google(question, api_url, target_file):
    complete_url = api_url + "models/" + Shared.MODEL_NAME + ":generateContent?key=" + Shared.API_KEY

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {"parts": [
                {"text": question}
            ]}
        ]
    }
    dump_payload(payload, target_file)

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        raise Exception(str(response))

    return response_message


def query_text_simple(question_path, target_file, callback, question=None):
    if question is None:
        question = open(question_path, "r", encoding="utf-8").read()

    if "api.openai" in Shared.API_URL:
        response_message = query_text_simple_openai_new(question, Shared.API_URL, target_file)
    elif "googleapis" in Shared.API_URL:
        response_message = query_text_simple_google(question, Shared.API_URL, target_file)
    elif "anthropic" in Shared.API_URL:
        response_message = query_text_simple_anthropic(question, Shared.API_URL, target_file)
    else:
        response_message = query_text_simple_generic(question, Shared.API_URL, target_file)

    if response_message:
        callback(response_message, target_file)


def query_image_simple_openai_new(base64_image, api_url, target_file, text):
    complete_url = api_url
    if not complete_url.endswith("/"):
        complete_url += "/"
    complete_url += "responses"

    payload = {
        "model": Shared.MODEL_NAME,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": text},
                    {"type": "input_image", "image_url": f"data:image/png;base64,{base64_image}"}
                ]
            }
        ]
    }

    if Shared.SYSTEM_PROMPT is not None:
        payload["instructions"] = Shared.SYSTEM_PROMPT

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    dump_payload(payload, target_file)

    response = requests.post(complete_url, headers=headers, json=payload)
    if response.status_code != 200:
        print(response)
        print(response.status_code)
        print(response.text)

    response = response.json()

    dump_response(response, target_file)

    return response["output"][-1]["content"][0]["text"]


def query_image_simple_generic(base64_image, api_url, target_file, text):
    complete_url = api_url + "chat/completions"

    messages = [{"role": "user", "content": [{"type": "text", "text": text},
                                             {"type": "image_url",
                                              "image_url": {"url": f"data:image/png;base64,{base64_image}"}}]}]

    if Shared.SYSTEM_PROMPT is not None:
        messages = [{"role": "system", "content": Shared.SYSTEM_PROMPT}] + messages

    payload = {
        "model": Shared.MODEL_NAME,
        "messages": messages,
        "max_tokens": Shared.MAX_REQUESTED_TOKENS,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    payload.update(get_llm_specific_settings())

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["choices"][0]["message"]["content"]
    except Exception as e:
        print(response)
        raise Exception(e)

    return response_message


def query_image_simple_anthropic(base64_image, api_url, target_file, text):
    complete_url = api_url + "messages"

    messages = [
        {"role": "user", "content": [
            {"type": "text", "text": text},
            {"type": "image", "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": base64_image
            }}
        ]}
    ]

    headers = {
        "content-type": "application/json",
        "anthropic-version": "2023-06-01",
        "anthropic-beta": "output-128k-2025-02-19",
        "x-api-key": Shared.API_KEY
    }

    payload = {
        "model": Shared.MODEL_NAME,
        "max_tokens": Shared.MAX_REQUESTED_TOKENS
    }

    if Shared.ANTHROPIC_THINKING_TOKENS is not None:
        payload["thinking"] = {"type": "enabled", "budget_tokens": Shared.ANTHROPIC_THINKING_TOKENS}
        payload["max_tokens"] += Shared.ANTHROPIC_THINKING_TOKENS
        payload["max_tokens"] = min(128000, payload["max_tokens"])

    payload["messages"] = messages

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["content"][-1]["text"]
    except Exception as e:
        raise Exception(str(response))

    return response_message


def query_image_simple_google(base64_image, api_url, target_file, text):
    complete_url = api_url + "models/" + Shared.MODEL_NAME + ":generateContent?key=" + Shared.API_KEY

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {"parts": [
                {"text": text},
                {"inline_data": {
                    "mime_type": "image/png",
                    "data": base64_image
                }}
            ]}
        ]
    }

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        raise Exception(str(response))

    return response_message


def query_image_simple(question_path, target_file, callback, base64_image=None, text=None):
    if text is None:
        text = "Can you describe the provided visualization?"

    if base64_image is None:
        base64_image = encode_image(question_path)

    if "api.openai" in Shared.API_URL and False:
        response_message = query_image_simple_openai_new(base64_image, Shared.API_URL, target_file, text)
    elif "googleapis" in Shared.API_URL:
        response_message = query_image_simple_google(base64_image, Shared.API_URL, target_file, text)
    elif "anthropic" in Shared.API_URL:
        response_message = query_image_simple_anthropic(base64_image, Shared.API_URL, target_file, text)
    else:
        response_message = query_image_simple_generic(base64_image, Shared.API_URL, target_file, text)

    callback(response_message, target_file)


def get_models():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    complete_url = Shared.API_URL+"models"

    models = requests.get(complete_url, headers=headers).json()

    return models


def insert_api_keys():
    MODELS_DICT["openai"]["api_key"] = open("../api_openai.txt", "r").read().strip()
    MODELS_DICT["mistral"]["api_key"] = open("../api_mistral.txt", "r").read().strip()
    MODELS_DICT["grok"]["api_key"] = open("../api_grok.txt", "r").read().strip()
    MODELS_DICT["deepinfra"]["api_key"] = open("../api_deepinfra.txt", "r").read().strip()
    MODELS_DICT["qwen"]["api_key"] = open("../api_qwen.txt", "r").read().strip()
    MODELS_DICT["nvidia"]["api_key"] = open("../api_nvidia.txt", "r").read().strip()
    MODELS_DICT["google"]["api_key"] = open("../api_google.txt", "r").read().strip()
    MODELS_DICT["claude"]["api_key"] = open("../api_anthropic.txt", "r").read().strip()


def check_all_models():
    insert_api_keys()

    for provider in MODELS_DICT:
        if provider not in {"google", "claude", "grok", "qwen", "manual"}:
            print(provider)
            info = MODELS_DICT[provider]
            Shared.API_URL = info["api_url"]
            Shared.API_KEY = info["api_key"]
            models = get_models()
            models = {x["id"] for x in models["data"]}
            models_specified = set(info["models"])
            diff = models_specified.difference(models)
            if len(diff) > 0:
                print("ERROR")
                print(diff)
                print(models_specified)
                print(models)
                input()


def check_missing_models():
    responding_models = set(x.split("_cat")[0] for x in os.listdir("answers") if not x.startswith("__init"))
    catalogue_models = set()
    for provider in MODELS_DICT:
        info = MODELS_DICT[provider]
        for model in info["models"]:
            catalogue_models.add(clean_model_name(model))
    diff = set(catalogue_models).difference(responding_models)
    if diff:
        raise Exception("catalogue_models outdated: "+str(diff))
    diff = set(responding_models).difference(catalogue_models)
    print(diff)


def clean_model_name(m_name):
    return m_name.replace("/", "").replace(":", "")


def get_base_evaluation_path(model_name):
    return "evaluation" if "gpt-4o" in model_name else "evaluation-" + clean_model_name(model_name)


if __name__ == "__main__":
    check_all_models()
    check_missing_models()
    #set_api_key("answer")
    #models = get_models()
    #print(models)
