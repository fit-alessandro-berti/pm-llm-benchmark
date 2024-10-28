import os
import traceback
import time
import sys
from common import ANSWERING_MODEL_NAME, query_text_simple, query_image_simple, callback_write, set_api_key

set_api_key("answer")
WAITING_TIME_RETRY = 60

questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]

for q in questions:
    question_path = os.path.join("questions", q)
    answer_path = os.path.join("answers", ANSWERING_MODEL_NAME.replace("/", "").replace(":", "") + "_" + q).replace(".png", ".txt")

    if not os.path.exists(answer_path):
        print("Executing", question_path)

        while not os.path.exists(answer_path):
            try:
                if question_path.endswith(".txt"):
                    query_text_simple(question_path, answer_path, callback_write)
                    break
                elif ANSWERING_MODEL_NAME.startswith("pixtral") or ANSWERING_MODEL_NAME.startswith("chatgpt-4o") or ANSWERING_MODEL_NAME.startswith("gpt-4o") or ANSWERING_MODEL_NAME.startswith("gpt-4-turbo") or ANSWERING_MODEL_NAME.startswith("gpt-4-vision") or ANSWERING_MODEL_NAME.startswith("meta-llama/Llama-3.2-11B") or ANSWERING_MODEL_NAME.startswith("meta-llama/Llama-3.2-90B") or ANSWERING_MODEL_NAME.startswith("gemini-")  or ANSWERING_MODEL_NAME.startswith("claude-"):
                    try:
                        query_image_simple(question_path, answer_path, callback_write)
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
