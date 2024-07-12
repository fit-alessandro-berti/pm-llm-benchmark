import os

models = ["meta-llama/Meta-Llama-3-70B-Instruct", "Qwen/Qwen2-72B-Instruct", "mistralai/Mixtral-8x22B-Instruct-v0.1", "microsoft/WizardLM-2-8x22B", "mistralai/Mixtral-8x7B-Instruct-v0.1"]

os.chdir("..")

for i in range(len(models)):
    for j in range(i, len(models)):
        print("\n\n#### ", models[i], models[j])
        os.system("python evaluation.py "+models[i]+" "+models[j])
