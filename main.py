import streamlit as st
from api.doc_parser import extract_text_from_file
from api.utils import split_into_chunks
from api.qa_engine import create_vector_store, ask_question, create_conversational_chain
from api.summarizer import generate_summary
from api.question_gen import generate_questions
from api.evaluator import evaluate_answer
import re

# Helper: Highlight sentence in chunk
def highlight_snippet(snippet, sentence):
    highlighted = re.sub(
        re.escape(sentence.strip()),
        f"**:blue[{sentence.strip()}]**",
        snippet,
        flags=re.IGNORECASE
    )
    return highlighted

st.set_page_config(page_title="📄 Smart Document Assistant", layout="centered")
st.title("📄 Smart Document Assistant")

# 📤 Upload Document
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Step 1: Extract text
    with st.spinner("Extracting text from document..."):
        full_text = extract_text_from_file(uploaded_file)
        st.success("✅ Text successfully extracted!")

    # Step 2: Generate Summary
    with st.spinner("Generating summary..."):
        summary = generate_summary(full_text)
        st.session_state["summary"] = summary
        st.subheader("📝 Document Summary")
        st.write(summary)

    # Step 3: Chunking & Vector Store
    with st.spinner("Splitting and indexing document..."):
        chunks = split_into_chunks(full_text)
        vectorstore = create_vector_store(chunks)
        st.session_state["vectorstore"] = vectorstore
        st.session_state["doc_text"] = full_text
        st.session_state["conversation_chain"] = create_conversational_chain(vectorstore)
        st.success("✅ Document is ready for Q&A and reasoning.")

    # 🔄 UI Tabs
    tab1, tab2 = st.tabs(["💬 Ask Anything", "🎯 Challenge Me"])

    # ------------------ 💬 Tab 1: Ask Anything ------------------
    with tab1:
        st.subheader("💬 Ask Anything (with memory)")
        user_question = st.text_input("Ask a question or follow-up:")

        if user_question:
            with st.spinner("Searching for the answer..."):
                response, source_chunk = ask_question(st.session_state["vectorstore"], user_question)

                if "Justification:" in response:
                    answer_part, justification_part = response.split("Justification:", 1)
                    justification_text = justification_part.strip().strip("'\"")

                    st.markdown("### ✅ Answer")
                    st.markdown(answer_part.strip())

                    with st.expander("📌 Justification"):
                        st.markdown(justification_text)

                    highlighted_chunk = highlight_snippet(source_chunk, justification_text)
                    with st.expander("🔍 Highlighted Source"):
                        st.markdown(highlighted_chunk)
                else:
                    st.markdown("### ✅ Answer & Justification")
                    st.write(response)

    # ------------------ 🎯 Tab 2: Challenge Me ------------------
    with tab2:
        st.subheader("🎯 Comprehension Challenge")

        if st.button("🧠 Generate Questions"):
            with st.spinner("Generating 3 logic-based questions..."):
                questions = generate_questions(st.session_state["doc_text"])
                st.session_state["challenge_questions"] = questions
                st.session_state["user_answers"] = [""] * len(questions)
                st.session_state["evaluations"] = [""] * len(questions)

        # Show generated questions
        if "challenge_questions" in st.session_state:
            st.markdown("### 🖊️ Answer the following:")

            for i, question in enumerate(st.session_state["challenge_questions"]):
                st.markdown(f"**Q{i+1}: {question}**")
                st.session_state["user_answers"][i] = st.text_input(
                    f"Your answer to Q{i+1}", key=f"answer_{i}"
                )

            if st.button("📊 Evaluate My Answers"):
                for i, question in enumerate(st.session_state["challenge_questions"]):
                    user_ans = st.session_state["user_answers"][i]
                    reference = st.session_state["vectorstore"].similarity_search(question, k=1)[0].page_content

                    with st.spinner(f"Evaluating Q{i+1}..."):
                        feedback = evaluate_answer(question, user_ans, reference)
                        st.session_state["evaluations"][i] = feedback

        # Show feedback
        if "evaluations" in st.session_state:
            st.markdown("### 📋 Evaluation Results")
            for i, feedback in enumerate(st.session_state["evaluations"]):
                if feedback:
                    st.markdown(f"**Feedback for Q{i+1}:**")
                    st.markdown(feedback)

else:
    st.info("👈 Please upload a document to begin.")
