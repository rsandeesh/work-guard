from datetime import date

from pydantic import BaseModel, PositiveFloat

from app.enums.athlete_level import AthleteLevel
from app.enums.gender import Gender


class UpdateAthleteRequest(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    event: str
    contact: str
    dob: date
    level: AthleteLevel
    heartRate: str
    gender: Gender
    weight: PositiveFloat
    height: PositiveFloat
    personalBest: str
