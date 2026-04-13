import os
import sys
from sentence_transformers import SentenceTransformer

def get_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(os.path.join(os.getcwd(), relative_path))

_model = None
MODEL_DIR = get_path("models/all-MiniLM-L6-v2")


if not os.path.exists(MODEL_DIR):
    print(f"CRITICAL ERROR: Embedding model folder not found at: {MODEL_DIR}")

else:
    _model = SentenceTransformer(MODEL_DIR)

def embed(texts):
    return _model.encode(texts).tolist()