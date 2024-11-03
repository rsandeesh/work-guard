import uuid
from datetime import datetime

from sqlalchemy import (
    String,
    Date,
    DateTime,
    DECIMAL,
    Integer,
    TIMESTAMP,
    UUID,
    ForeignKey,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.db_handler import Base
from app.models.session_detail import SessionDetail


class Athlete(Base):
    __tablename__ = "athlete"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    event: Mapped[str] = mapped_column(String(200), nullable=False)
    contact: Mapped[int] = mapped_column(Integer, nullable=False)
    dob: Mapped[Date] = mapped_column(Date, nullable=False)
    level: Mapped[str] = mapped_column(String(50), nullable=False)
    heart_rate: Mapped[str] = mapped_column(String(200), nullable=False)
    gender: Mapped[str] = mapped_column(String(50), nullable=False)
    weight: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2))
    height: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2))
    personal_best: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    coach_id: Mapped[UUID] = mapped_column(ForeignKey("coach.id"))
    created_by: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    modified_by: Mapped[str] = mapped_column(String(100))
    modified_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    coach: Mapped["Coach"] = relationship("Coach", back_populates="athletes")
    session_details: Mapped[list["SessionDetail"]] = relationship(
        "SessionDetail", back_populates="athlete"
    )

    def to_dict(self):
        return {
            column.name: str(getattr(self, column.name)) if isinstance(getattr(self, column.name), UUID)
            else getattr(self, column.name)
            for column in self.__table__.columns
        }
