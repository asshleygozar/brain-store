from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core import settings


engine = create_async_engine(
    str(settings.async_database_url),
    connect_args={"ssl": "require"},
    pool_size=5, 
    max_overflow=5, # Limits pool size to 5 to prevent overpooling 
    pool_pre_ping=True, # My database is on free tier and suspends on inactivity (Neon specifically). This was implemented to ensure that first request will not throw connection closed error
    pool_recycle=1800, # Neon is serveless db so It will need this to established connection every 30 minutes just to ensure the connection is not dropped
)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
