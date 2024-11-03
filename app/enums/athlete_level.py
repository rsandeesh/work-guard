from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as SQL_ENUM


class AthleteLevel(str, Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    EXPERT = "EXPERT"

    def __str__(self) -> str:
        return str(self.value)


level = SQL_ENUM(AthleteLevel, name="level", create_type=False)
