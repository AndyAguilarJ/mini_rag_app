from app.retriever import retrieve
from app.llm import generate

def answer(question: str) -> str:
    docs = retrieve(question)

    context = "\n".join(docs)

    prompt = f"""
Use the context to answer the question.

Context:
{context}

Question:
{question}
"""

    return generate(prompt)