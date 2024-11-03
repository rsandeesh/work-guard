import uuid
from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy import String, TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.db_handler import Base
from app.models.athlete import Athlete


class Coach(Base):
    __tablename__ = "coach"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    created_by: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    modified_by: Mapped[str] = mapped_column(String(100))
    modified_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    athletes: Mapped[list["Athlete"]] = relationship("Athlete", back_populates="coach")
