<p align="center">
  <img src="assets/banner.png" alt="Local RAG App Banner" width="700">
</p>

<h1 align="center">🧠 Local RAG App — Offline Document Chat</h1>

<p align="center">
  Chat with your PDFs using a fully local LLM (no cloud, no API keys).
</p>

<p align="center">
  🔒 Offline • 📄 PDF RAG • ⚡ Local LLM • 🖥️ CLI • 📦 EXE Buildable
</p>

---
A fully offline, private Retrieval-Augmented Generation (RAG) application. Chat with your PDFs using DeepSeek-R1-Distill-Qwen-1.5B and ChromaDB without an internet connection.
🌟 Overview

This project bundles a local LLM server (llama.cpp), a vector database (ChromaDB), and a PDF processing pipeline into a single, portable Windows executable. It is designed for users who need AI insights without compromising data privacy.
🛠️ Tech Stack

    LLM: DeepSeek-R1-Distill-Qwen-1.5B (GGUF)

    Engine: llama-server.exe (Llama.cpp)

    Embeddings: all-MiniLM-L6-v2 (Sentence-Transformers)

    Vector Store: ChromaDB

    PDF Engine: PyMuPDF (Fitz)

    Orchestration: LangChain

📥 Installation (Development Mode)
1. Clone & Setup Environment
Bash

git clone https://github.com/yourusername/mini_rag_app.git
cd mini_rag_app
conda create -n qwen_rag python=3.10
conda activate qwen_rag

2. Install Requirements
Bash

pip install langchain chromadb sentence-transformers pymupdf requests tqdm customtkinter

3. Model Preparation

    Create a models/ folder.

    Download the DeepSeek GGUF and place it in models/.

    Place the all-MiniLM-L6-v2 embedding model folder into models/.

🏗️ Building the Executable

Standard PyInstaller commands will fail due to the complex nature of AI dependencies. You must use the provided .spec file.
Critical Build Step:

The .spec file uses collect_all to grab dynamic hidden imports for LangChain, ChromaDB, and Sentence-Transformers. It also manually maps the pymupdf binary folder.

To build:
Bash

pyinstaller --clean run_app.spec

🚀 How to Use (EXE Mode)

    Launch: Run run_app.exe from the dist/run_app/ folder.

    Initialization: The app will load the embedding weights (100%) and then start the LLM server. Wait ~20 seconds for the "Engine Ready" message.

    Add Documents: - Type /add  (include the space).

        Drag and drop any PDF file directly into the console window.

        Press Enter.

    Chat: Ask questions based on the PDF content.

    Persistence: Your ingested documents are saved in the chroma_db/ folder and will be available the next time you open the app.

📂 Project Structure
Plaintext

├── app/                # Core logic (RAG, LLM API, Config)
├── llama/              # llama-server binaries and DLLs
├── models/             # LLM and Embedding models
├── ingest/             # PDF processing and chunking logic
├── scripts/            # CLI Chat loop
├── run_app.py          # Main entry point for PyInstaller
└── run_app.spec        # Custom build configuration

⚠️ Known Issues & Solutions

    RequestsDependencyWarning: A harmless warning regarding charset_normalizer. It does not affect RAG performance.

    ModuleNotFoundError (fitz/langchain): Usually caused by building without the --clean flag or missing the collect_all hooks in the .spec file.

    Connection Error: If the app cannot connect to Port 8080, check Task Manager and kill any lingering llama-server.exe processes.

📄 License

MIT License - See LICENSE for details.