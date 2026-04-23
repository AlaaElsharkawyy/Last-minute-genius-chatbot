import streamlit as st
import tempfile
import requests

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="📚 Last Minute Genius", layout="wide")
st.title("📚 Last Minute Genius AI")

TOP_K = 3

# =========================
# EMBEDDINGS (Compatible with your version)
# =========================
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

embeddings = load_embeddings()

# =========================
# SESSION STATE
# =========================
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================
# OLLAMA FUNCTION
# =========================
def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["response"]

# =========================
# SIDEBAR - PDF UPLOAD
# =========================
with st.sidebar:
    st.header("📄 Upload PDF")

    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

    if uploaded_file and st.session_state.vector_db is None:
        with st.spinner("Processing PDF..."):

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                path = tmp.name

            loader = PyPDFLoader(path)
            docs = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=600,
                chunk_overlap=100
            )

            chunks = splitter.split_documents(docs)

            st.session_state.vector_db = FAISS.from_documents(
                chunks,
                embeddings
            )

            st.success(f"✅ Indexed {len(chunks)} chunks")

# =========================
# CHAT DISPLAY
# =========================
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"🧑‍💻 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")

# =========================
# RAG FUNCTION
# =========================
def get_answer(question):
    docs = st.session_state.vector_db.similarity_search(question, k=TOP_K)
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
Use the context to answer the question.

Context:
{context}

Question:
{question}

Answer in simple and clear English.
"""

    return ask_ollama(prompt)

# =========================
# CHAT INPUT
# =========================
question = st.chat_input("Ask anything about your PDF...")

if question:
    st.session_state.chat_history.append(("user", question))

    if st.session_state.vector_db:
        answer = get_answer(question)
    else:
        answer = "⚠️ Please upload a PDF first."

    st.session_state.chat_history.append(("bot", answer))

# =========================
# ACTION BUTTONS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🧠 Summarize"):
        if st.session_state.vector_db:
            ans = get_answer("Summarize the PDF in simple bullet points")
            st.session_state.chat_history.append(("bot", ans))

with col2:
    if st.button("📝 Quiz Me"):
        if st.session_state.vector_db:
            ans = get_answer("Generate 5 quiz questions with answers")
            st.session_state.chat_history.append(("bot", ans))

with col3:
    if st.button("💡 Explain"):
        if st.session_state.vector_db:
            ans = get_answer("Explain the main ideas in a very simple way")
            st.session_state.chat_history.append(("bot", ans))