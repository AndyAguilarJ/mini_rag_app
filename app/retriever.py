from app.vector_store import collection
from app.embeddings import embed

def retrieve(query):
    # Ensure we don't crash if the collection is empty
    count = collection.count()
    if count == 0:
        return []

    q_emb = embed([query])
    results = collection.query(query_embeddings=q_emb, n_results=3)
    
    if not results["documents"] or len(results["documents"][0]) == 0:
        return []
        
    return results["documents"][0]