import os
import traceback
import time
from common import ANSWERING_MODEL_NAME, EVALUATING_MODEL_NAME, query_text_simple, query_image_simple, callback_write, \
    encode_image, set_api_key

set_api_key("evaluation")

questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]
INCLUDE_EVALUATING_MNAME_IN_EVALUATION = False

while True:
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
            base_evaluation_path = "evaluation-" + e_m_name

        if not os.path.exists(base_evaluation_path):
            os.mkdir(base_evaluation_path)

        evaluation_path = os.path.join(base_evaluation_path, evaluation_path)
        evaluation_path = evaluation_path.replace(".png", ".txt")

        if os.path.exists(answer_path) and not os.path.exists(evaluation_path):
            print("Evaluating:", answer_path)

            answer = open(answer_path, "r").read()

            if answer is not None and answer:
                try:
                    if question_path.endswith(".txt"):
                        question = open(question_path, "r", encoding="utf-8").read()

                        inquiry = ["Given the following question:\n\n"]
                        inquiry.append(question)
                        inquiry.append(
                            "\n\nHow would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? Please put the grade at the beginning of the response.\n\n")
                        inquiry.append(answer)
                        inquiry = ",".join(inquiry)

                        query_text_simple(None, evaluation_path, callback_write, question=inquiry)
                    elif EVALUATING_MODEL_NAME.startswith("pixtral") or EVALUATING_MODEL_NAME.startswith(
                            "chatgpt-4o") or EVALUATING_MODEL_NAME.startswith(
                            "gpt-4o") or EVALUATING_MODEL_NAME.startswith(
                            "gpt-4-turbo") or EVALUATING_MODEL_NAME.startswith(
                            "gpt-4-vision") or EVALUATING_MODEL_NAME.startswith(
                            "meta-llama/Llama-3.2-11B") or EVALUATING_MODEL_NAME.startswith(
                            "meta-llama/Llama-3.2-90B") or EVALUATING_MODEL_NAME.startswith(
                            "gemini-") or EVALUATING_MODEL_NAME.startswith("claude-"):
                        base64_image = encode_image(question_path)
                        inquiry = [
                            "Given the attached image, how would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)?\n\n"]
                        inquiry.append(answer)
                        inquiry = "".join(inquiry)
                        query_image_simple(None, evaluation_path, callback_write, base64_image=base64_image,
                                           text=inquiry)
                except:
                    traceback.print_exc()

    #break
    time.sleep(15)
    # print("nextit")
