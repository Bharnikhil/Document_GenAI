from langchain_community.llms import Ollama
from pathlib import Path

def load_question_prompt():
    return Path("prompts/question_gen.txt").read_text()

def generate_questions(document_text: str):
    prompt = load_question_prompt() + "\n\nDocument:\n" + document_text[:3000]

    llm = Ollama(model="tinyllama")
    raw_output = llm.predict(prompt)

    questions = [q.strip("123456. ") for q in raw_output.strip().split("\n") if q.strip()]
    return questions[:3]
