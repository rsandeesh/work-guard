import uuid

from app.core.logger_config import logger
from app.enums.active_status import ActiveStatus
from app.exceptions.exception_handler import TransactionException
from app.models.athlete import Athlete
from app.models.coach import Coach
from app.models.session import Session
from app.schemes.requests.create_athlete_request import CreateAthleteRequest
from app.schemes.requests.update_athlete_request import UpdateAthleteRequest


class AthleteService:
    def __init__(self):
        pass

    async def save_athlete(self, request: CreateAthleteRequest, db: Session):
        try:
            coach = db.query(Coach).filter(Coach.email == request.createdBy).first()
            if not coach:
                raise TransactionException("Coach not found in the current data")

            athlete = Athlete(
                id=uuid.uuid4(),
                first_name=request.firstName,
                last_name=request.lastName,
                email=request.email,
                event=request.event,
                contact=int(request.contact),
                dob=request.dob,
                level=request.level,
                heart_rate=request.heartRate,
                gender=request.gender,
                weight=request.weight,
                height=request.height,
                personal_best=request.personalBest,
                status=ActiveStatus.ACTIVE,
                coach_id=coach.id,
                created_by=coach.email,
                modified_by=coach.email,
            )
            db.add(athlete)
            db.commit()

        except Exception as e:
            logger.exception(f"Error occurred while saving athlete: {str(e)}")
            raise e

    async def update_athlete(self, request: UpdateAthleteRequest, db: Session):
        try:
            athlete = db.query(Athlete).filter(Athlete.id == request.id).first()
            if not athlete:
                raise TransactionException("Athlete not found in the current data")

            athlete.first_name = request.firstName
            athlete.last_name = request.lastName
            athlete.email = request.email
            athlete.event = request.event
            athlete.contact = int(request.contact)
            athlete.dob = request.dob
            athlete.level = request.level
            athlete.heart_rate = request.heartRate
            athlete.gender = request.gender
            athlete.weight = request.weight
            athlete.height = request.height
            athlete.personal_best = request.personalBest

            db.commit()

        except Exception as e:
            logger.exception(f"Error occurred while updating athlete: {str(e)}")
            raise e

    async def get_athletes_by_coach(self, coach_id: str, db: Session):
        try:
            athletes = db.query(Athlete).where(Athlete.coach_id == coach_id)
            return athletes.all()
        except Exception as e:
            logger.exception(f"Error occurred while fetching athletes: {str(e)}")
            raise e

    async def get_athlete_by_id(self, id: str, db: Session):
        try:
            return db.query(Athlete).filter(Athlete.id == id).first()
        except Exception as e:
            logger.exception(f"Error occurred while fetching athletes: {str(e)}")
            raise e

    async def get_athlete_count(self, coach_id: str, db: Session):
        try:
            count = db.query(Athlete).filter(Athlete.coach_id == coach_id).count()
            return count
        except Exception as e:
            logger.exception(f"Error occurred while fetching athletes: {str(e)}")
            raise e

    async def remove_athlete(self, athlete_id: str, db: Session):
        try:
            athlete = db.query(Athlete).filter_by(id=athlete_id).first()
            if not athlete:
                raise TransactionException("Athlete not found in the current data")

            db.delete(athlete)
            db.commit()

        except Exception as e:
            logger.exception(f"Error occurred while updating athlete: {str(e)}")
            raise e
