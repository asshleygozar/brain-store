import secrets
import uuid
from app.util.hash_value import HashManager

def generate_access_key(key_id: uuid.UUID) -> tuple[str, str]:
    """Return a public key id plus a bcrypt-hashed secret."""
    secret = secrets.token_urlsafe(32)
    return f"{key_id}.{secret}", HashManager.hash_value(secret)
