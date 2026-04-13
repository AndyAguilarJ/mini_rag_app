import os
import sys

def get_path(relative_path):
    """ Helper to find files inside the PyInstaller bundle or local dev """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# --- Folders ---
# This ensures ingest.py knows where to look for your documents
PDF_FOLDER = get_path("data")
DB_DIR = get_path("chroma_db")

# --- LLM Settings ---
MODEL_PATH = get_path("models/deepseek-r1-distill-qwen-1.5b-q4_0.gguf")
LLM_URL = "http://127.0.0.1:8080/v1/chat/completions"

# --- Embedding Settings ---
# Ensure 'all-MiniLM-L6-v2' is a folder inside your 'models' directory
EMBED_MODEL_PATH = get_path("models/all-MiniLM-L6-v2")
COLLECTION_NAME = "docs"
# --- RAG Constants ---
# These are now the ONLY places you change these numbers
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3