from datetime import date
from pydantic import BaseModel


class AthleteSchema(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    event: str
    contact: int
    dob: date
    level: str
    heart_rate: str
    gender: str
    weight: float
    height: float
    personal_best: str

    class Config:
        from_attributes = True
