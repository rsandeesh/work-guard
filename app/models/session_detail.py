from sqlalchemy import String, DECIMAL, TEXT, TIMESTAMP, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.db_handler import Base
from app.enums.active_status import active_status


class SessionDetail(Base):
    __tablename__ = "session_detail"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    session_id: Mapped[UUID] = mapped_column(ForeignKey("session.id"), nullable=False)
    athlete_id: Mapped[UUID] = mapped_column(ForeignKey("athlete.id"), nullable=False)
    race_time: Mapped[str] = mapped_column(String(100), nullable=False)
    heart_rate_detail: Mapped[str] = mapped_column(TEXT)
    distance: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2))
    distance_type: Mapped[str] = mapped_column(String(20), nullable=False)
    status: Mapped[active_status] = mapped_column(active_status)
    created_by: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    modified_by: Mapped[str] = mapped_column(String(100))
    modified_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)

    session: Mapped["Session"] = relationship("Session", back_populates="session_details")
    athlete: Mapped["Athlete"] = relationship("Athlete", back_populates="session_details")