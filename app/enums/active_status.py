from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as SQL_ENUM


class ActiveStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)


active_status = SQL_ENUM(ActiveStatus, name="active_status", create_type=False)