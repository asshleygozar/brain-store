from fastapi import Request, Header, Depends, HTTPException, status
from sqlalchemy import select
from pinecone.db_data.index_asyncio import IndexAsyncio
from app.db.session import get_db
from app.db.models import AccessKeys
from app.util.hash_value import HashManager
from datetime import datetime, timedelta, timezone

def get_pinecone_index(request: Request) -> IndexAsyncio:
    """Get the pinecone index with intellisense"""
    return request.app.state.pinecone_index


async def get_current_key(authorization: str = Header(...), db=Depends(get_db)) -> AccessKeys:
    """Get the current access key from the database for general user only!"""
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    
    token = authorization.removeprefix("Bearer ").strip()
    try:
        key_id, secret = token.split(".", 1)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    try:
        key = await db.scalar(select(AccessKeys).where(AccessKeys.id == key_id))
    except ValueError:
        key = None

    if key and not HashManager.verify_hash(secret, key.key):
        key = None
    if not key or not key.active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or revoked access key")

    now = datetime.now(timezone.utc)

    if key.first_used_at is None:
        if now > key.activation_deadline:
            raise HTTPException(401, "This link expired before it was used")
        # Establishes first use and sets expiration to 1 hour from now
        key.first_used_at, key.expires_at = now, now + timedelta(hours=1)
        await db.commit()
    elif now > key.expires_at:
        raise HTTPException(401, "Access key expired")

    return key