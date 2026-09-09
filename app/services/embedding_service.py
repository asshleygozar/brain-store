from app.core import genai

def embedding_service(contents: list[str]) -> list[list[float]]:
    """Embed multiple chunks in a single provider request."""
    vectors = genai.embeddings.embed_documents(contents)
    print(f'Embedded {len(vectors)} chunks')
    return vectors