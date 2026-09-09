from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from app.core import settings
llm = None

def load_llm():
    global llm
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=settings.GEMINI_API_KEY,        
    )
    print('AI Loaded successfully!')

embeddings = None

def load_llm_embeddings():
    global embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        api_key=settings.GEMINI_API_KEY
    )
    print('Embeddings Loaded successfully!')