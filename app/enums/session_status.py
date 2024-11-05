from enum import Enum


class SessionStatus(str, Enum):
    COMPLETED = "COMPLETED"
    NOT_COMPLETED = "NOT_COMPLETED"

    def __str__(self):
        return self.value
