import os
from common import get_base_evaluation_path, EVALUATING_MODEL_NAME
from overall_table import write_evaluation


def do_deletion(base_path, original_name):
    if not os.path.exists(base_path):
        raise Exception("base_path %s does not exists!" % (base_path))

    files = [x for x in os.listdir(base_path) if x.startswith(original_name)]

    for f in files:
        original_path = os.path.join(base_path, f)
        print(original_path)
        os.remove(original_path)


if __name__ == "__main__":
    original_name = "gemini-2.5-flash-05-20-thinkhigh_"

    if not original_name.endswith("_"):
        raise Exception("original_name must terminate with _")

    do_deletion("../answers", original_name)
    do_deletion(os.path.join("..", get_base_evaluation_path(EVALUATING_MODEL_NAME)), original_name)

    write_evaluation("..", extra=True)
