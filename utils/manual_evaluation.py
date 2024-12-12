import os
import common


ANSWERING_MODEL_NAME = "gpt-4o-mini-2024-07-18"
EVALUATING_MODEL_NAME = "o1-2024-12-05"

m_name = common.clean_model_name(ANSWERING_MODEL_NAME)
e_m_name = common.clean_model_name(EVALUATING_MODEL_NAME)

print(m_name)
print(e_m_name)
