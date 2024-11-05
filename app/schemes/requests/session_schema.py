from datetime import date

from pydantic import BaseModel


class SessionSchema(BaseModel):
    name: str
    session_date: date
    venue: str
    status: str
