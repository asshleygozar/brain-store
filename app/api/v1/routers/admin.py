from datetime import datetime, timedelta, timezone
import uuid
from fastapi import APIRouter, Header, Depends, HTTPException, status
from app.schemas.admin import IssueKeyRequest
from app.db.session import get_db
from app.db.models import AccessKeys
from app.core import settings
from app.util.generate_key import generate_access_key

admin_router = APIRouter()

@admin_router.post('/key')
async def issue_key(body: IssueKeyRequest, x_admin_secret: str = Header(...), db=Depends(get_db)):
    # Validate the admin secret
    if x_admin_secret != settings.ADMIN_SECRET.get_secret_value():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid admin secret")

    # Create a new access key
    key_id = uuid.uuid4()
    raw_key, hashed_key = generate_access_key(key_id)
    key = AccessKeys(
        id=key_id,
        key=hashed_key,
        note=body.note,
        activation_deadline=datetime.now(timezone.utc) + timedelta(days=7),
    )

    db.add(key) 
    await db.commit()
    
    return {"access_key": raw_key, "namespace": str(key.id)}



