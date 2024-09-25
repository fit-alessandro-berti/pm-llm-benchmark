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


def query_text_simple(question_path, complete_url, target_file, callback):
    question = open(question_path, "r", encoding="utf-8").read()
    messages = [{"role": "user", "content": question}]

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
        print(response)
        raise Exception(e)
    callback(response_message, target_file)


def query_image_simple(question_path, complete_url, target_file, callback):
    base64_image = encode_image(question_path)
    messages = [{"role": "user", "content": [{"type": "text", "text": "Can you describe the provided visualization?"},
                                             {"type": "image_url",
                                              "image_url": {"url": f"data:image/png;base64,{base64_image}"}}]}]

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": 4096,
    }

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["choices"][0]["message"]["content"]
    except Exception as e:
        print(response)
        raise Exception(e)
    callback(response_message, target_file)


def query_text_chain_reasoning(question_path, complete_url, target_file, callback, max_steps=5):
    question = open(question_path, "r", encoding="utf-8").read()
    n_steps = 0

    messages = [
        {"role": "system", "content": """You are an expert AI assistant that explains your reasoning step by step. For each step, provide a title that describes what you're doing in that step, along with the content. Decide if you need another step or if you're ready to give the final answer. Respond in JSON format with 'title', 'content', and 'next_action' (either 'continue' or 'final_answer') keys. USE AS MANY REASONING STEPS AS POSSIBLE. AT LEAST 3. BE AWARE OF YOUR LIMITATIONS AS AN LLM AND WHAT YOU CAN AND CANNOT DO. IN YOUR REASONING, INCLUDE EXPLORATION OF ALTERNATIVE ANSWERS. CONSIDER YOU MAY BE WRONG, AND IF YOU ARE WRONG IN YOUR REASONING, WHERE IT WOULD BE. FULLY TEST ALL OTHER POSSIBILITIES. YOU CAN BE WRONG. WHEN YOU SAY YOU ARE RE-EXAMINING, ACTUALLY RE-EXAMINE, AND USE ANOTHER APPROACH TO DO SO. DO NOT JUST SAY YOU ARE RE-EXAMINING. USE AT LEAST 3 METHODS TO DERIVE THE ANSWER. USE BEST PRACTICES.

    Example of a valid JSON response:
    ```json
    {
        "title": "Identifying Key Information",
        "content": "To begin solving this problem, we need to carefully examine the given information and identify the crucial elements that will guide our solution process. This involves...",
        "next_action": "continue"
    }```
    """},
        {"role": "user", "content": question},
        {"role": "assistant",
         "content": "Thank you! I will now think step by step following my instructions, starting at the beginning after decomposing the problem."}
    ]

    while n_steps < max_steps:
        n_steps += 1

        payload = {
            "model": MODEL_NAME,
            "messages": messages,
        }
        response = requests.post(complete_url, headers=headers, json=payload).json()
        response_message = response["choices"][0]["message"]["content"]
        response_message = response_message.split("```json")[-1].split("```")[0]
        response = json.loads(response_message)

        print(n_steps, response_message)

        messages.append({"role": "assistant", "content": response_message})

        if response["next_action"] == "final_answer":
            break

    messages.append({"role": "user", "content": "Please provide the final answer based on your reasoning above."})
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
    }

    dump_payload(payload, target_file)
    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    response_message = response["choices"][0]["message"]["content"]
    response_message = response_message.split("```json")[-1].split("```")[0]
    response = json.loads(response_message)
    response_message = str(response["content"])

    callback(response_message, target_file)


API_URL = "https://api.openai.com/v1/"
#API_URL = "http://127.0.0.1:11434/v1/"
#API_URL = "https://api.deepinfra.com/v1/openai/"
#API_URL = "https://api.mistral.ai/v1/"

MODEL_NAME = "gpt-4o"
API_KEY = open("api_key.txt", "r").read()

WAITING_TIME_RETRY = 60

questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]
complete_url = API_URL + "chat/completions"

for q in questions:
    question_path = os.path.join("questions", q)
    answer_path = os.path.join("answers", MODEL_NAME.replace("/", "").replace(":", "") + "_" + q).replace(".png", ".txt")

    if not os.path.exists(answer_path):
        print("Executing", question_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        while not os.path.exists(answer_path):
            try:
                if question_path.endswith(".txt"):
                    #query_text_chain_reasoning(question_path, complete_url, answer_path, callback_write)
                    query_text_simple(question_path, complete_url, answer_path, callback_write)
                    break
                elif MODEL_NAME.startswith("pixtral") or MODEL_NAME.startswith("chatgpt-4o") or MODEL_NAME.startswith("gpt-4o") or MODEL_NAME.startswith("gpt-4-turbo") or MODEL_NAME.startswith("gpt-4-vision"):
                    try:
                        query_image_simple(question_path, complete_url, answer_path, callback_write)
                    except:
                        traceback.print_exc()
                    sys.exit(0)
                    break
                else:
                    break
            except SystemExit as e:
                sys.exit(0)
            except Exception as e:
                traceback.print_exc()

                print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                time.sleep(WAITING_TIME_RETRY)
