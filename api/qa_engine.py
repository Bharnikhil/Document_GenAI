from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from pathlib import Path
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    return vectorstore

def load_qa_prompt():
    prompt_template = Path("prompts/qa.txt").read_text(encoding='utf-8')
    return PromptTemplate(
        template=prompt_template,
        input_variables=["retrieved_chunks", "user_question"]
    )


def ask_question(vectorstore, user_question: str):
    retrieved_docs = vectorstore.similarity_search(user_question, k=1)
    top_chunk = retrieved_docs[0].page_content

    prompt = load_qa_prompt().format(
        retrieved_chunks=top_chunk,
        user_question=user_question
    )

    llm = Ollama(model="tinyllama")
    response = llm.predict(prompt)
    return response, top_chunk

def create_conversational_chain(vectorstore):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=Ollama(model="tinyllama"),
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return chain
