import uuid

from sqlalchemy import String, Date, TIMESTAMP, Boolean, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.db_handler import Base
from app.enums.active_status import active_status


class Session(Base):
    __tablename__ = "session"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    session_date: Mapped[Date] = mapped_column(Date, nullable=False)
    venue_date: Mapped[Date] = mapped_column(Date, nullable=False)
    start_time: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    end_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    is_completed: Mapped[bool] = mapped_column(Boolean)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    created_by: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    modified_by: Mapped[str] = mapped_column(String(100))
    modified_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)

    session_details: Mapped[list["SessionDetail"]] = relationship(
        "SessionDetail", back_populates="session"
    )
