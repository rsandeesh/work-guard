from sqlalchemy import String, TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.db_handler import Base
from app.enums.active_status import active_status


class Coach(Base):
    __tablename__ = "coach"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    user_name: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[active_status] = mapped_column(nullable=False)
    created_by: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    modified_by: Mapped[str] = mapped_column(String(100))
    modified_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)

    athletes: Mapped[list["Athlete"]] = relationship("Athlete", back_populates="coach")
