from common import encode_image
from common import Shared as CommonShared


def forge(question_path, answer):
    if question_path.endswith(".txt"):
        question = open(question_path, "r", encoding="utf-8").read()

        inquiry = ["Given the following question:\n\n"]
        inquiry.append(question)
        inquiry.append(
            "\n\nHow would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)? Please put the grade at the beginning of the response. ")
        if CommonShared.TRIAL_CHANGE_EVALUATION_LRM:
            inquiry.append(
                "Please ignore the initial part of the answer, as it contains the 'flow of thought' and it can be verbose and repetitive. Only the final part/conclusions should be considered for the grade!")
        if CommonShared.TRIAL_SEVERE_EVALUATION:
            inquiry.append(
                "Please evaluate with the utmost strictness. Be hypercritical of any inaccuracies, "
                "unclarities, or logical flaws. Even minor issues should result in a significantly "
                "lower score. Only award a very high score if the answer is nearly flawless."
            )

        inquiry.append("\n\n")

        inquiry.append(answer)
        inquiry = ",".join(inquiry)

        base64_image = None
    else:
        base64_image = encode_image(question_path)
        inquiry = [
            "Given the attached image, how would you grade the following answer from 1.0 (minimum) to 10.0 (maximum)?\n\n"]
        inquiry.append(answer)
        inquiry = "".join(inquiry)

    return inquiry, base64_image
