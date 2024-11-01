from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as SQL_ENUM


class GenderEnum(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)


gender = SQL_ENUM(GenderEnum, name="gender", create_type=False)