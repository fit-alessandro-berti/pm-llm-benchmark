import requests
import os
import traceback
import time


API_URL = "https://api.openai.com/v1/"
#API_URL = "http://127.0.0.1:11434/v1/"
#API_URL = "https://api.deepinfra.com/v1/openai/"

MODEL_NAME = "gpt-4o"
API_KEY = open("api_key.txt", "r").read()

WAITING_TIME_RETRY = 60

textual_questions = [x for x in os.listdir("questions") if x.endswith(".txt")]

for q in textual_questions:
    question_path = os.path.join("questions", q)
    answer_path = os.path.join("answers", MODEL_NAME.replace("/", "").replace(":", "") + "_" + q)

    if not os.path.exists(answer_path):
        print("Executing", question_path)

        question = open(question_path, "r").read()

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        messages = [{"role": "user", "content": question}]

        payload = {
            "model": MODEL_NAME,
            "messages": messages,
        }

        complete_url = API_URL + "chat/completions"

        response_message = ""
        response = None
        while not response_message:
            try:
                response = requests.post(complete_url, headers=headers, json=payload).json()

                response_message = response["choices"][0]["message"]["content"]

                F = open(answer_path, "w")
                F.write(response_message)
                F.close()
            except:
                print(response)

                traceback.print_exc()

                print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                time.sleep(WAITING_TIME_RETRY)
