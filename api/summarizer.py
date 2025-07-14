from langchain_community.llms import Ollama
from pathlib import Path

def load_summary_prompt(text: str) -> str:
    template = Path("prompts/summary.txt").read_text()
    return template.replace("{{full_text}}", text)

def generate_summary(document_text: str) -> str:
    prompt = load_summary_prompt(document_text[:3000])

    llm = Ollama(model="tinyllama")
    response = llm.predict(prompt)
    return response.strip()
