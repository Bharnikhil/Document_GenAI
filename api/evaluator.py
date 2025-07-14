from langchain_community.llms import Ollama
from pathlib import Path

def load_eval_prompt():
    return Path("prompts/eval.txt").read_text()

def evaluate_answer(question, user_answer, reference_chunk):
    prompt = load_eval_prompt().replace("{{question}}", question)\
                               .replace("{{answer}}", user_answer)\
                               .replace("{{reference_chunk}}", reference_chunk)

    llm = Ollama(model="tinyllama")
    response = llm.predict(prompt)
    return response.strip()
