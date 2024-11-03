from typing import List

from pydantic import BaseModel
from datetime import date


class CreateSessionRequest(BaseModel):
    name: str
    sess_date: date
    venue: str
    athletes: List[str]
    created_by: str
