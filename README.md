# 📄 Smart Document Assistant (GenAI Project)

An AI-powered assistant that reads, summarizes, and answers questions on user-uploaded documents (PDF/TXT). Powered by local LLMs like **TinyLlama via Ollama**.

---

## 🚀 Features
- 📤 Upload PDF/TXT documents
- 📝 Auto-summarization of the document
- 💬 Free-form Question Answering
- 🎯 "Challenge Me" Mode — generates logic-based questions & evaluates your answers
- 🔎 Answer justification with source snippet highlighting
- 🧠 Conversational memory for follow-up questions
- ✅ Runs fully locally with **TinyLlama** using **Ollama** — no OpenAI API key needed!

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-link>
cd smart-document-assistant


2️⃣ Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt




3️⃣ Install Ollama (for Local LLM Inference)
Download and install from:
👉 https://ollama.com/download

Once installed, pull TinyLlama:

bash
Copy
Edit
ollama pull tinyllama




4️⃣ Run the Ollama Server
bash
Copy
Edit
ollama serve
This starts the local API server at:

arduino
Copy
Edit
http://localhost:11434




🎯 Running the Streamlit App
Once Ollama is running, in a new terminal window:

bash
Copy
Edit
streamlit run main.py
The app will be available at:

arduino
Copy
Edit
http://localhost:8501


🔌 Optional: Postman Collection
The repository includes a Postman collection under:

bash
Copy
Edit
/postman/SmartDocAPI.postman_collection.json
Use this for testing if APIs are exposed via FastAPI or Flask.


🛠️ Tech Stack
Python

Ollama + TinyLlama (Local LLM Inference)

LangChain

FAISS for Document Embeddings

Streamlit for Frontend

HuggingFace Embeddings

Sentence Transformers

📄 License
MIT License

👨‍💻 Author
Nikhil Bhardwaj

GitHub: Bharnikhil

yaml
Copy
Edit

---

### ✅ Next Step:
1. Save this as `README.md` inside your project root.
2. Commit and push it:
```bash
git add README.md
git commit -m "Added complete README documentation"
git push origin main
<<<<<<< HEAD
👨‍💻 Author  
Nikhil Bhardwaj  

GitHub: Bharnikhil  

---

### 📺 Demo Video
👉 [Watch the Demo on YouTube](https://youtu.be/lsi4cex10sg)
=======


### 📺 Demo Video
Watch the complete demo of this project on YouTube:  
👉 [Watch the Demo on YouTube](https://www.youtube.com/watch?v=lsi4cex10sg)

This video provides a walkthrough of the features, functionality, and usage of the project.

>>>>>>> a75161bdf73c00dcf236f3be12a187a5e00c570d
