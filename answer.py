import requests
import os
import traceback
import time
import re
import json
import sys
import base64


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


def callback_write(response_message, answer_path):
    response_message = strip_non_unicode_characters(response_message)

    F = open(answer_path, "w")
    F.write(response_message)
    F.close()


def dump_payload(payload, target_file):
    target_file = target_file.replace("answers", "json_payload")
    #print(target_file)

    try:
        json.dump(payload, open(target_file, "w"), indent=2)
    except:
        print("payload dumping failed")


def dump_response(response, target_file):
    target_file = target_file.replace("answers", "json_resp")
    #print(target_file)

    try:
        json.dump(response, open(target_file, "w"), indent=2)
    except:
        print("response dumping failed")


def query_text_simple_generic(question, api_url, target_file):
    complete_url = api_url + "chat/completions"

    messages = [{"role": "user", "content": question}]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
    }
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
        "x-api-key": API_KEY
    }

    payload = {
        "model": MODEL_NAME,
        "max_tokens": 8192
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
    complete_url = api_url + "models/" + MODEL_NAME + ":generateContent?key=" + API_KEY

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


def query_text_simple(question_path, api_url, target_file, callback):
    question = open(question_path, "r", encoding="utf-8").read()

    if "googleapis" in api_url:
        response_message = query_text_simple_google(question, api_url, target_file)
    elif "anthropic" in api_url:
        response_message = query_text_simple_anthropic(question, api_url, target_file)
    else:
        response_message = query_text_simple_generic(question, api_url, target_file)

    callback(response_message, target_file)


def query_image_simple_generic(base64_image, api_url, target_file):
    complete_url = api_url + "chat/completions"

    messages = [{"role": "user", "content": [{"type": "text", "text": "Can you describe the provided visualization?"},
                                             {"type": "image_url",
                                              "image_url": {"url": f"data:image/png;base64,{base64_image}"}}]}]

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": 4096,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["choices"][0]["message"]["content"]
    except Exception as e:
        print(response)
        raise Exception(e)

    return response_message


def query_image_simple_anthropic(base64_image, api_url, target_file):
    complete_url = api_url + "messages"

    messages = [
        {"role": "user", "content": [
            {"type": "text", "text": "Can you describe the provided visualization?"},
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
        "x-api-key": API_KEY
    }

    payload = {
        "model": MODEL_NAME,
        "max_tokens": 8192
    }

    payload["messages"] = messages

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["content"][0]["text"]
    except Exception as e:
        raise Exception(str(response))

    return response_message


def query_image_simple_google(base64_image, api_url, target_file):
    complete_url = api_url + "models/" + MODEL_NAME + ":generateContent?key=" + API_KEY

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {"parts": [
                {"text": "Can you describe the provided visualization?"},
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


def query_image_simple(question_path, api_url, target_file, callback):
    base64_image = encode_image(question_path)

    if "googleapis" in api_url:
        response_message = query_image_simple_google(base64_image, api_url, target_file)
    elif "anthropic" in api_url:
        response_message = query_image_simple_anthropic(base64_image, api_url, target_file)
    else:
        response_message = query_image_simple_generic(base64_image, api_url, target_file)

    callback(response_message, target_file)


API_URL = "https://api.openai.com/v1/"
#API_URL = "http://127.0.0.1:11434/v1/"
#API_URL = "https://api.deepinfra.com/v1/openai/"
#API_URL = "https://api.mistral.ai/v1/"
#API_URL = "https://generativelanguage.googleapis.com/v1beta/"
#API_URL = "https://api.anthropic.com/v1/"

MODEL_NAME = "gpt-4o"
API_KEY = open("api_key.txt", "r").read().strip()

WAITING_TIME_RETRY = 60

questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]

for q in questions:
    question_path = os.path.join("questions", q)
    answer_path = os.path.join("answers", MODEL_NAME.replace("/", "").replace(":", "") + "_" + q).replace(".png", ".txt")

    if not os.path.exists(answer_path):
        print("Executing", question_path)

        while not os.path.exists(answer_path):
            try:
                if question_path.endswith(".txt"):
                    #query_text_simple(question_path, API_URL, answer_path, callback_write)
                    break
                elif MODEL_NAME.startswith("pixtral") or MODEL_NAME.startswith("chatgpt-4o") or MODEL_NAME.startswith("gpt-4o") or MODEL_NAME.startswith("gpt-4-turbo") or MODEL_NAME.startswith("gpt-4-vision") or MODEL_NAME.startswith("meta-llama/Llama-3.2-11B") or MODEL_NAME.startswith("meta-llama/Llama-3.2-90B") or MODEL_NAME.startswith("gemini-")  or MODEL_NAME.startswith("claude-"):
                    try:
                        query_image_simple(question_path, API_URL, answer_path, callback_write)
                    except:
                        traceback.print_exc()
                    break
                else:
                    break
            except SystemExit as e:
                sys.exit(0)
            except Exception as e:
                if "context length" in str(e):
                    break

                traceback.print_exc()

                print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                time.sleep(WAITING_TIME_RETRY)
