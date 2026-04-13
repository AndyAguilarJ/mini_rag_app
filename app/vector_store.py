import chromadb
from app.config import DB_DIR, COLLECTION_NAME

client = chromadb.Client(
    chromadb.config.Settings(persist_directory=DB_DIR)
)

collection = client.get_or_create_collection(COLLECTION_NAME)