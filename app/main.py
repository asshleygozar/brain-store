from fastapi import FastAPI
from app.core import settings
import uvicorn

app = FastAPI(
    title=settings.APP_NAME
)


@app.get('/')
def main():
    return {"message": "Hello!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
