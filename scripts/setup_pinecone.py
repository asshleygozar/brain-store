import time
from pinecone import Pinecone, ServerlessSpec
from app.core import settings

def setup_pinecone():
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)
    index_name = settings.PINECONE_INDEX_NAME

    if not pc.has_index(index_name):
        print(f"Creating index {index_name}...")
        pc.create_index(
            name=index_name,
            dimension=1536,
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1' # Free tier only available this region I tried southeast asia but it's not free
            )
        )

        # Kept in timer state as long as the index is not yet ready for clear indicator
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)
        print(f"Index {index_name} is now ready")
    else:
        print(f"Index {index_name} already exists")

    host = pc.describe_index(index_name).host
    print(f"Set this in your .env: PINECONE_INDEX_HOST={host}")

if __name__ == "__main__":
    setup_pinecone()