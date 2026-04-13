import os
from pypdf import PdfReader

def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf(path):
    reader = PdfReader(path)
    return "\n".join(p.extract_text() for p in reader.pages)

def load_file(path):
    if path.endswith(".txt"):
        return load_txt(path)
    elif path.endswith(".pdf"):
        return load_pdf(path)
    else:
        return None