from app.core import embeddings

def embedding_service(content: str):
    vector = embeddings.embed_query(content)
    return vector