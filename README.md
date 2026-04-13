<p align="center">
  <img src="assets/banner.png" alt="Mini RAG App Logo" width="200"/>
</p>

# 🧠 Mini RAG App

A local **Retrieval-Augmented Generation (RAG)** application that allows you to query your own documents using embeddings and a local language model.

---

## 🚀 Features

* 🔍 Semantic search with embeddings
* 🧠 Local LLM inference using `llama.cpp`
* 📄 PDF ingestion support
* 🗃️ Vector database powered by ChromaDB
* ⚡ Fast and fully offline

---

## 📁 Project Structure

```
mini_rag_app/
├── app/            # Main application logic
├── ingest/         # Data ingestion scripts
├── models/         # Local models (ignored in Git)
├── data/           # Input documents (ignored in Git)
├── chroma_db/      # Vector database
├── scripts/        # Utilities
├── assets/         # Static/UI files
└── dist/           # Executable build (optional)
```

---

## ⚙️ Requirements

* Python 3.10+
* pip

---

## 📦 Dependencies

```
chromadb
sentence-transformers
llama.cpp
pypdf
tqdm
```
---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/AndyAguilarJ/mini_rag_app.git
cd mini_rag_app
```

---

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Models Setup

⚠️ Models are **NOT included** in this repository.

Place your models inside:

```
models/
```

Example:

```
models/
└── all-MiniLM-L6-v2/
```

If using a `.gguf` model for `llama.cpp`, place it inside `models/` as well. You can use bigger models but that depends on the computer power you have, in this repo is recommended the deepseek-r1-distill-qwen-1.5b-q4_0.gguf for the minimal spec, as the proyect runs only in CPU power (you can modify anything to your liking)

---

## 📚 Adding Data

Add your documents (PDFs, etc.) to:

```
data/
```

Then run the ingestion process:

```bash
python ingest/ingest.py
```

---

## ▶️ Running the App

```bash
py app/main.py
```

Or run the built executable:

```bash
dist/run_app/run_app.exe
```
### 💬 What happens next?

* A command-line window will open
* The RAG system will load the models and database
* You will be prompted to enter a question

Example:

```
> Ask a question: What is this document about?
```

The app will:

1. Search relevant context from your data
2. Run the local LLM
3. Return an answer in the terminal

---

## 🧩 Tech Stack

* Embeddings: sentence-transformers
* Vector DB: chromadb
* LLM: llama.cpp
* PDF parsing: pypdf

---

## ⚠️ Notes

* Large model files (`*.gguf`) are not included
* First run may take time due to embedding generation
* Make sure `models/` and `chroma_db/` are properly set up
* Do not close the terminal while the model is loading
---

## 🛠️ Future Improvements

* Better UI
* Streaming responses
* Multi-file support
* Web interface

---
