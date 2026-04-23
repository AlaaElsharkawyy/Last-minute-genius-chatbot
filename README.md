<div align="center">

# 🧠 Last Minute Genius Chatbot
**Your Local-First AI Study Assistant**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)](https://langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-White?style=flat&logo=ollama&logoColor=black)](https://ollama.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*An intelligent, private, and highly accurate study companion powered by local Large Language Models and Retrieval-Augmented Generation (RAG).*

[Features](#-features) • [Tech Stack](#%EF%B8%8F-tech-stack) • [Architecture](#%EF%B8%8F-architecture) • [Getting Started](#-getting-started) • [Usage](#-usage) • [Roadmap](#-roadmap)

</div>

---

## 💡 Overview

**Last Minute Genius Chatbot** is a powerful web application designed to help students and professionals digest complex documents in record time. By leveraging local LLMs through Ollama, it provides a completely private ChatGPT-like experience that strictly answers questions based on the exact PDF materials you provide. 

No internet required for inference. No data sent to third-party APIs. Just you and your study materials.

---

## ✨ Features

- **📄 Seamless PDF Ingestion**: Upload dense textbooks, research papers, or lecture slides with a single click.
- **💬 Conversational UI**: A beautiful, intuitive ChatGPT-style interface with chat bubbles and conversation history.
- **🔍 Context-Aware Q&A**: Employs advanced Retrieval-Augmented Generation (RAG) to fetch precise answers from your documents.
- **🔒 100% Privacy**: Runs entirely on your local machine using Ollama—zero data leakage.
- **⚡ Blazing Fast Retrieval**: Utilizes FAISS vector databases for sub-second document similarity searches.

---

## 🛠️ Tech Stack

This project is built using modern AI engineering tools:

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | `Streamlit` | Rapid, interactive, and responsive web UI |
| **Framework** | `LangChain` | Orchestration of the LLM pipeline and RAG chain |
| **LLM Engine** | `Ollama` | Local inference engine running **LLaMA 3** |
| **Embeddings** | `HuggingFace` | Open-source sentence transformers for text vectorization |
| **Vector Store** | `FAISS` | Facebook AI Similarity Search for high-speed retrieval |

---

## 🏗️ Architecture

How **Last Minute Genius** processes your data:

1. **Document Loading**: Uploaded PDFs are parsed and split into manageable, overlapping text chunks.
2. **Vectorization**: HuggingFace embeddings convert these chunks into high-dimensional mathematical vectors.
3. **Storage**: Vectors are indexed in a local FAISS database for near-instant retrieval.
4. **Retrieval**: When you ask a question, your query is vectorized and compared against the FAISS index to find the most relevant document chunks.
5. **Generation**: The retrieved context + your question are sent to the local LLaMA 3 model, which generates a highly accurate, context-bound response.

---

## 🚀 Getting Started

Follow these steps to get your local environment set up.

### Prerequisites

1. **Python 3.9 or higher**: [Download here](https://www.python.org/downloads/)
2. **Ollama**: Must be installed and running on your machine.
   - Download from [ollama.com](https://ollama.com/download)
   - Once installed, open your terminal and pull the LLaMA 3 model:
     ```bash
     ollama run llama3
     ```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/last-minute-genius-chatbot.git
   cd last-minute-genius-chatbot
   ```

2. **Create a virtual environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### 🏃‍♂️ Running the App

Once everything is installed, spin up the Streamlit server:

```bash
streamlit run app.py
```
The application will automatically open in your default browser at `http://localhost:8501`.

---

## 🎯 Example Usage

1. **Upload**: Drag and drop your `Machine_Learning_Syllabus.pdf` into the sidebar.
2. **Process**: Click the "Process Documents" button to generate embeddings.
3. **Ask**: Type your question in the chat bar:
   > *"What are the key differences between Supervised and Unsupervised learning according to chapter 2?"*
4. **Learn**: The local LLaMA 3 model will instantly generate a summarized explanation based purely on the uploaded PDF text!

---

## 🗺️ Future Improvements (Roadmap)

- [ ] **Document Summarization**: Add a 1-click button to generate an executive summary of the uploaded document.
- [ ] **"Explain Like I'm 5" Toggle**: Introduce a feature to dynamically simplify complex technical explanations.
- [ ] **Multi-Document Support**: Chat across entire folders of PDFs simultaneously.
- [ ] **Source Citations**: UI updates to show exactly which page/paragraph the AI pulled the answer from.
- [ ] **Conversation Export**: Save your Q&A sessions as markdown or PDF notes.

---

## 👨‍💻 Author

**Last Minute Genius** was built to make studying smarter, not harder.

* Developed by **[Your Name/Username]**
* GitHub: [@yourusername](https://github.com/AlaaElsharkawyy)
* LinkedIn: [Your Profile](linkedin.com/in/alaa-elsharkawy)

If you find this project helpful, please consider giving it a ⭐ on GitHub!

---
<p align="center">
  <i>"Genius is 1% inspiration, 99% perspiration... and a really good RAG pipeline."</i>
</p>