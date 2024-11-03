from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as SQL_ENUM


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)


gender = SQL_ENUM(Gender, name="gender", create_type=False)
