import requests
import re
import json
import base64


API_URL = "https://api.openai.com/v1/"
#API_URL = "http://127.0.0.1:11434/v1/"
#API_URL = "https://api.deepinfra.com/v1/openai/"
#API_URL = "https://api.mistral.ai/v1/"
#API_URL = "https://generativelanguage.googleapis.com/v1beta/"
#API_URL = "https://api.anthropic.com/v1/"

# the model used to respond to the questions
ANSWERING_MODEL_NAME = "gpt-4o-2024-05-13"

# judge model
EVALUATING_MODEL_NAME = "gpt-4o-2024-08-06"


class Shared:
    API_KEY = None

def set_api_key(type_key):
    if type_key == "answer":
        Shared.API_KEY = open("answering_api_key.txt", "r").read().strip()
    else:
        Shared.API_KEY = open("judge_api_key.txt", "r").read().strip()


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


def dump_payload(payload, target_file):
    if "answers" in target_file:
        target_file = target_file.replace("answers", "json_payload")
        #print(target_file)

        try:
            json.dump(payload, open(target_file, "w"), indent=2)
        except:
            print("payload dumping failed")


def dump_response(response, target_file):
    if "answers" in target_file:
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
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    payload = {
        "model": ANSWERING_MODEL_NAME,
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
        "x-api-key": Shared.API_KEY
    }

    payload = {
        "model": ANSWERING_MODEL_NAME,
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
    complete_url = api_url + "models/" + ANSWERING_MODEL_NAME + ":generateContent?key=" + Shared.API_KEY

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

    if "googleapis" in API_URL:
        response_message = query_text_simple_google(question, API_URL, target_file)
    elif "anthropic" in API_URL:
        response_message = query_text_simple_anthropic(question, API_URL, target_file)
    else:
        response_message = query_text_simple_generic(question, API_URL, target_file)

    callback(response_message, target_file)


def query_image_simple_generic(base64_image, api_url, target_file, text):
    complete_url = api_url + "chat/completions"

    messages = [{"role": "user", "content": [{"type": "text", "text": text},
                                             {"type": "image_url",
                                              "image_url": {"url": f"data:image/png;base64,{base64_image}"}}]}]

    payload = {
        "model": ANSWERING_MODEL_NAME,
        "messages": messages,
        "max_tokens": 4096,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

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
        "model": ANSWERING_MODEL_NAME,
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


def query_image_simple_google(base64_image, api_url, target_file, text):
    complete_url = api_url + "models/" + ANSWERING_MODEL_NAME + ":generateContent?key=" + Shared.API_KEY

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

    if "googleapis" in API_URL:
        response_message = query_image_simple_google(base64_image, API_URL, target_file, text)
    elif "anthropic" in API_URL:
        response_message = query_image_simple_anthropic(base64_image, API_URL, target_file, text)
    else:
        response_message = query_image_simple_generic(base64_image, API_URL, target_file, text)

    callback(response_message, target_file)
