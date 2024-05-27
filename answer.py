import requests
import os
import traceback
import time
import re
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


API_URL = "https://api.openai.com/v1/"
#API_URL = "http://127.0.0.1:11434/v1/"
#API_URL = "https://api.deepinfra.com/v1/openai/"

MODEL_NAME = "gpt-4o"
API_KEY = open("api_key.txt", "r").read()

WAITING_TIME_RETRY = 60

questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]

for q in questions:
    question_path = os.path.join("questions", q)
    answer_path = os.path.join("answers", MODEL_NAME.replace("/", "").replace(":", "") + "_" + q).replace(".png", ".txt")

    if not os.path.exists(answer_path):
        print("Executing", question_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        payload = None
        if question_path.endswith(".txt"):
            question = open(question_path, "r", encoding="utf-8").read()
            messages = [{"role": "user", "content": question}]

            payload = {
                "model": MODEL_NAME,
                "messages": messages,
            }
        elif MODEL_NAME.startswith("gpt-4o") or MODEL_NAME.startswith("gpt-4-turbo") or MODEL_NAME.startswith("gpt-4-vision"):
            base64_image = encode_image(question_path)
            messages = [{"role": "user", "content": [{"type": "text", "text": "Can you describe the provided visualization?"}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image} "}}]}]

            payload = {
                "model": MODEL_NAME,
                "messages": messages,
                "max_tokens": 4096
            }

        if payload is not None:
            complete_url = API_URL + "chat/completions"

            response_message = ""
            response = None
            while not response_message:
                try:
                    response = requests.post(complete_url, headers=headers, json=payload).json()

                    response_message = strip_non_unicode_characters(response["choices"][0]["message"]["content"])

                    F = open(answer_path, "w")
                    F.write(response_message)
                    F.close()
                except:
                    print(response)

                    traceback.print_exc()

                    print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                    time.sleep(WAITING_TIME_RETRY)
