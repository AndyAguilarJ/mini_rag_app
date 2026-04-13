import os
import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
from app.config import DB_DIR, CHUNK_SIZE, CHUNK_OVERLAP, EMBED_MODEL_PATH

try:
    import fitz
except ImportError:
    # If fitz isn't found, try importing via the package name
    import pymupdf as fitz

# 1. Load resources globally (but inside the script)
embedder = SentenceTransformer(EMBED_MODEL_PATH)
client = chromadb.PersistentClient(path=DB_DIR)
collection = client.get_or_create_collection("docs")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

def process_single_file(file_path):
    """The function chat.py will call when you drag and drop"""
    if not os.path.exists(file_path) or not file_path.lower().endswith(".pdf"):
        print(f"Invalid file: {file_path}")
        return

    # Extract text
    doc = fitz.open(file_path)
    text = "".join([page.get_text() for page in doc])
    
    # Chunk and Embed
    chunks = splitter.split_text(text)
    embeddings = embedder.encode(chunks).tolist()
    
    # Use a unique ID for each session to avoid overwriting
    file_name = os.path.basename(file_path)
    ids = [f"{file_name}_{uuid.uuid4().hex[:6]}_{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )
    print(f"Successfully ingested: {file_name}")

def ingest_folder(pdf_folder):
    """Your original batch logic"""
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            process_single_file(os.path.join(pdf_folder, file))

if __name__ == "__main__":
    # If run manually, it still processes the default folder
    from app.config import PDF_FOLDER
    ingest_folder(PDF_FOLDER)