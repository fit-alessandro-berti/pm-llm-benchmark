import os.path

import requests
import re
import json
import base64
import sys

from typing import Dict, Any

# the model used to respond to the questions
ANSWERING_MODEL_NAME = "gpt-4o-mini-2024-07-18" if len(sys.argv) < 3 else sys.argv[1]

# judge model
EVALUATING_MODEL_NAME = "chatgpt-4o-latest" if len(sys.argv) < 3 else sys.argv[2]


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
    SYSTEM_PROMPT = None
    # SYSTEM_PROMPT = "You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step."
    #SYSTEM_PROMPT = "You are a helpful and harmless assistant."
    TRIAL_CHANGE_EVALUATION_LRM = False
    CUSTOM_TEMPERATURE = None
    #CUSTOM_TEMPERATURE = 0.1


MODELS_DICT = {
    "openai": {
        "api_url": "https://api.openai.com/v1/",
        "api_key": "sk-",
        "models": {
            "o1-preview-2024-09-12", "o1-mini-2024-09-12", "gpt-4o-2024-11-20", "gpt-4o-2024-08-06",
            "gpt-4o-2024-05-13", "gpt-4o-mini-2024-07-18", "gpt-4-turbo-2024-04-09", "gpt-4-0613",
            "gpt-3.5-turbo"
        }
    },
    "google": {
        "api_url": "https://generativelanguage.googleapis.com/v1beta/",
        "api_key": "sk-",
        "models": {
            "gemini-1.5-pro-002", "gemini-1.5-flash-002", "gemini-1.5-flash-8b",
            "gemini-exp-1121", "gemini-exp-1206", "gemini-2.0-flash-exp"
        }
    },
    "claude": {
        "api_url": "https://api.anthropic.com/v1/",
        "api_key": "sk-",
        "models": {
            "claude-3-5-sonnet-20241022", "claude-3-5-sonnet-20240620", "claude-3-sonnet"
        }
    },
    "mistral": {
        "api_url": "https://api.mistral.ai/v1/",
        "api_key": "sk-",
        "models": {
            "pixtral-large-2411", "mistral-large-2411", "open-mixtral-8x22b", "mistral-small-2409", "open-mistral-nemo-2407", "codestral-2405",
            "open-mixtral-8x7b", "ministral-8b-2410", "ministral-3b-2410", "open-codestral-mamba"
        }
    },
    "grok": {
        "api_url": "https://api.x.ai/v1/",
        "api_key": "sk-",
        "models": {
            "grok-beta"
        }
    },
    "deepinfra": {
        "api_url": "https://api.deepinfra.com/v1/openai/",
        "api_key": "sk-",
        "models": {
            "meta-llama/Llama-3.3-70B-Instruct", "meta-llama/Meta-Llama-3.1-8B-Instruct",
            "meta-llama/Meta-Llama-3.1-405B-Instruct", "Qwen/Qwen2.5-Coder-32B-Instruct", "nvidia/Llama-3.1-Nemotron-70B-Instruct",
            "meta-llama/Llama-3.2-90B-Vision-Instruct", "meta-llama/Llama-3.2-11B-Vision-Instruct",
            "Qwen/QwQ-32B-Preview", "microsoft/WizardLM-2-8x22B", "microsoft/WizardLM-2-7B"
        }
    },
    "ollama_local": {
        "api_url": "http://137.226.117.70:11434/v1/",
        "api_key": "sk-",
        "models": {
            "mistral:7b-instruct-v0.3-q6_K", "gemma2:9b-instruct-q6_K", "qwen2.5:3b-instruct-q8_0", "llama3.2:1b-instruct-q6_K",
            "llama3.2:3b-instruct-q8_0", "qwen2.5:1.5b-instruct-q6_K", "nemotron:70b-instruct-q8_0", "qwen2.5:7b-instruct-q6_K",
            "qwen2.5:14b-instruct-q6_K", "qwen2.5:32b-instruct-q6_K", "gemma2:2b-instruct-q8_0", "smollm2:1.7b-instruct-q6_K"
        }
    }
}


MODELS_DICT = {
    "openai": {
        "api_url": "https://api.openai.com/v1/",
        "api_key": "sk-",
        "models": {
            "gpt-4o-mini-2024-07-18", "gpt-4o-2024-11-20"
        }
    },
    "google": {
        "api_url": "https://generativelanguage.googleapis.com/v1beta/",
        "api_key": "sk-",
        "models": {

        }
    },
    "claude": {
        "api_url": "https://api.anthropic.com/v1/",
        "api_key": "sk-",
        "models": {

        }
    },
    "mistral": {
        "api_url": "https://api.mistral.ai/v1/",
        "api_key": "sk-",
        "models": {
            "ministral-3b-2410", "ministral-8b-2410"
        }
    },
    "grok": {
        "api_url": "https://api.x.ai/v1/",
        "api_key": "sk-",
        "models": {

        }
    },
    "deepinfra": {
        "api_url": "https://api.deepinfra.com/v1/openai/",
        "api_key": "sk-",
        "models": {

        }
    },
    "ollama_local": {
        "api_url": "http://137.226.117.70:11434/v1/",
        "api_key": "sk-",
        "models": {

        }
    }
}


def is_visual_model(model_name):
    patterns = ["qwen2-vl", "pixtral", "gpt-4o", "gpt-4-turbo", "Llama-3.2-11B", "Llama-3.2-90B", "gemini-", "claude-", "grok-vision-beta"]

    for p in patterns:
        if p.lower() in model_name.lower():
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


def query_text_simple_generic(question, api_url, target_file):
    complete_url = api_url + "chat/completions"

    messages = [{"role": "user", "content": question}]

    if Shared.SYSTEM_PROMPT is not None:
        messages = [{"role": "system", "content": Shared.SYSTEM_PROMPT}] + messages

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    payload = {
        "model": Shared.MODEL_NAME,
        "messages": messages,
    }

    if "11434" in api_url:
        # OLLAMA
        options = {"num_ctx": 8192}
        options.update(get_llm_specific_settings())

        payload = {
            "model": Shared.MODEL_NAME,
            "prompt": question,
            "options": options
        }

        complete_url = complete_url.replace("v1/chat/completions", "api/generate")
        response0 = requests.post(complete_url, headers=headers, json=payload).text
        response0 = [x.strip() for x in response0.split("\n")]
        response = []
        for el in response0:
            try:
                response.append(json.loads(el))
            except:
                pass
        response_message = "".join(x["response"] for x in response)
    else:
        payload.update(get_llm_specific_settings())

        dump_payload(payload, target_file)

        response = requests.post(complete_url, headers=headers, json=payload).json()
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
        "x-api-key": Shared.API_KEY
    }

    payload = {
        "model": Shared.MODEL_NAME,
        "max_tokens": Shared.MAX_REQUESTED_TOKENS
    }

    payload["messages"] = messages
    dump_payload(payload, target_file)

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["content"][0]["text"]
    except Exception as e:
        raise Exception(str(response))

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

    if "googleapis" in Shared.API_URL:
        response_message = query_text_simple_google(question, Shared.API_URL, target_file)
    elif "anthropic" in Shared.API_URL:
        response_message = query_text_simple_anthropic(question, Shared.API_URL, target_file)
    else:
        response_message = query_text_simple_generic(question, Shared.API_URL, target_file)

    callback(response_message, target_file)


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
        "x-api-key": Shared.API_KEY
    }

    payload = {
        "model": Shared.MODEL_NAME,
        "max_tokens": Shared.MAX_REQUESTED_TOKENS
    }

    payload["messages"] = messages

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["content"][0]["text"]
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

    if "googleapis" in Shared.API_URL:
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
    MODELS_DICT["openai"]["api_key"] = open("api_openai.txt", "r").read().strip()
    MODELS_DICT["mistral"]["api_key"] = open("api_mistral.txt", "r").read().strip()
    MODELS_DICT["grok"]["api_key"] = open("api_grok.txt", "r").read().strip()
    MODELS_DICT["deepinfra"]["api_key"] = open("api_deepinfra.txt", "r").read().strip()
    MODELS_DICT["google"]["api_key"] = open("api_google.txt", "r").read().strip()
    MODELS_DICT["claude"]["api_key"] = open("api_anthropic.txt", "r").read().strip()

def check_all_models():
    insert_api_keys()

    for provider in MODELS_DICT:
        if provider not in {"google", "claude"}:
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
