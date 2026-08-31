import uuid
import datetime
from typing import Optional
from sqlalchemy import String, Integer, Boolean, DateTime, text, func, Uuid
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


# Access key model
class AccessKeys(Base):
    __tablename__ = "access_keys"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    key: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    note: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.current_timestamp(), nullable=False
    )
    activation_deadline: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    first_used_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True)
    )
    expires_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True)
    )
    active: Mapped[bool] = mapped_column(
        Boolean, server_default=text("true"), nullable=False
    )
    upload_count: Mapped[int] = mapped_column(
        Integer, server_default=text("0"), nullable=False
    )
    query_count: Mapped[int] = mapped_column(
        Integer, server_default=text("0"), nullable=False
    )
