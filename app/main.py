import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from pinecone import Pinecone, ServerlessSpec
from app.core import settings, load_llm, load_llm_embeddings
from app.api import v1_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)
    app.state.pinecone_index = pc.IndexAsyncio(settings.PINECONE_INDEX_HOST)
    load_llm()
    load_llm_embeddings()
    yield

    await app.state.pinecone_index.close()

app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)


@app.get('/')
def main():
    return {"message": "Hello!"}

app.include_router(v1_router, prefix='/api/v1')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
