import requests
import os
import traceback
import time
import re


def strip_non_unicode_characters(text):
    # Define a pattern that matches all valid Unicode characters.
    pattern = re.compile(r'[^\u0000-\uFFFF]', re.UNICODE)
    # Replace characters not matching the pattern with an empty string.
    cleaned_text = pattern.sub('', text)
    return cleaned_text


API_URL = "https://api.openai.com/v1/"
#API_URL = "http://127.0.0.1:11434/v1/"
#API_URL = "https://api.deepinfra.com/v1/openai/"

ANSWERING_MODEL_NAME = "gpt-4o"
EVALUATING_MODEL_NAME = "gpt-4o"
API_KEY = open("api_key.txt", "r").read()

WAITING_TIME_RETRY = 60

textual_questions = [x for x in os.listdir("questions") if x.endswith(".txt")]

for q in textual_questions:
    m_name = ANSWERING_MODEL_NAME.replace("/", "").replace(":", "")
    question_path = os.path.join("questions", q)
    answer_path = os.path.join("answers",  m_name + "_" + q)
    evaluation_path = os.path.join("evaluation", m_name + "_" + q)

    if os.path.exists(answer_path) and not os.path.exists(evaluation_path):
        print("Evaluating:", answer_path)

        question = open(question_path, "r", encoding="utf-8").read()
        answer = open(answer_path, "r").read()

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        inquiry = ["Given the following question:\n\n"]
        inquiry.append(question)
        inquiry.append("\n\nHow would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)?\n\n")
        inquiry.append(answer)

        messages = [{"role": "user", "content": "".join(inquiry)}]

        payload = {
            "model": EVALUATING_MODEL_NAME,
            "messages": messages,
        }

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
                print(response)

                traceback.print_exc()

                print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                time.sleep(WAITING_TIME_RETRY)
