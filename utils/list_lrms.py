import os
from common import force_custom_evaluation_lrm


def read_co(file_path):
    ret = ""
    try:
        F = open(file_path, "r")
        ret = F.read()
        F.close()
    except:
        F = open(file_path, "r", encoding="utf-8")
        ret = F.read()
        F.close()
    return ret


llms = set(x.split("_")[0] for x in os.listdir("../answers"))
llms = {x.strip() for x in llms if x.strip()}
llms = {x for x in llms if force_custom_evaluation_lrm(x)}
llms1 = set()
for x in llms:
    answers = [os.path.join("../answers", y) for y in os.listdir("../answers") if y.startswith(x)]
    co = read_co(answers[0]).strip()
    if co.startswith("<"):
        llms1.add(x)
F = open("lrms_list.txt", "w")
F.write("\n".join(llms1))
F.close()
