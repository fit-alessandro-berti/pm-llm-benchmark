import requests
import os
import traceback
import time
import re
import base64
import sys


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
#API_URL = "https://api.mistral.ai/v1/"

ANSWERING_MODEL_NAME = "gpt-4o" if len(sys.argv) < 3 else sys.argv[1]
EVALUATING_MODEL_NAME = "gpt-4o-2024-05-13" if len(sys.argv) < 3 else sys.argv[2]
INCLUDE_EVALUATING_MNAME_IN_EVALUATION = False if len(sys.argv) < 3 else True
CONTINUE_TRYING = True if len(sys.argv) < 3 else False

API_KEY = open("api_key.txt", "r").read()

WAITING_TIME_RETRY = 60

questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]

for q in questions:
    m_name = ANSWERING_MODEL_NAME.replace("/", "").replace(":", "")
    e_m_name = EVALUATING_MODEL_NAME.replace("/", "").replace(":", "")

    question_path = os.path.join("questions", q)

    answer_path = m_name + "_" + q
    answer_path = os.path.join("answers", answer_path)
    answer_path = answer_path.replace(".png", ".txt")

    if INCLUDE_EVALUATING_MNAME_IN_EVALUATION:
        evaluation_path = m_name + "__" + e_m_name + "__" + q
    else:
        evaluation_path = m_name + "_" + q

    if "gpt-4o" in e_m_name:
        base_evaluation_path = "evaluation"
    else:
        base_evaluation_path = "evaluation-"+e_m_name

    if not os.path.exists(base_evaluation_path):
        os.mkdir(base_evaluation_path)

    evaluation_path = os.path.join(base_evaluation_path, evaluation_path)
    evaluation_path = evaluation_path.replace(".png", ".txt")

    if os.path.exists(answer_path) and not os.path.exists(evaluation_path):
        print("Evaluating:", answer_path)

        answer = open(answer_path, "r").read()

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        payload = None

        if answer is not None and answer:
            if question_path.endswith(".txt"):
                question = open(question_path, "r", encoding="utf-8").read()

                inquiry = ["Given the following question:\n\n"]
                inquiry.append(question)
                inquiry.append("\n\nHow would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)?\n\n")
                inquiry.append(answer)
                messages = [{"role": "user", "content": "".join(inquiry)}]

                payload = {
                    "model": EVALUATING_MODEL_NAME,
                    "messages": messages,
                }
            elif EVALUATING_MODEL_NAME.startswith("chatgpt-4o") or EVALUATING_MODEL_NAME.startswith("gpt-4o") or EVALUATING_MODEL_NAME.startswith("gpt-4-turbo") or EVALUATING_MODEL_NAME.startswith("gpt-4-vision"):
                base64_image = encode_image(question_path)
                inquiry = ["Given the attached image, how would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)?\n\n"]
                inquiry.append(answer)
                messages = [{"role": "user", "content": [{"type": "text", "text": "".join(inquiry)}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image} "}}]}]

                payload = {
                    "model": EVALUATING_MODEL_NAME,
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

                    F = open(evaluation_path, "w")
                    F.write(response_message)
                    F.close()
                except:
                    if CONTINUE_TRYING:
                        print(response)

                        traceback.print_exc()

                        print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                        time.sleep(WAITING_TIME_RETRY)
                    else:
                        break
