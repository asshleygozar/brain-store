from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from app.core import settings
llm = None

def load_llm():
    global llm
    llm = ChatGoogleGenerativeAI(
        api_key=settings.GEMINI_API_KEY,        
    )
    print('AI Loaded successfully!')