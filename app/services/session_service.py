import uuid

from sqlalchemy.orm import Session

from app.core.logger_config import logger
from app.enums.active_status import ActiveStatus
from app.enums.session_status import SessionStatus
from app.exceptions.exception_handler import TransactionException
from app.models.athlete import Athlete
from app.models.session import Session as AthleteSession
from app.models.session_detail import SessionDetail
from app.schemes.requests.create_session_request import CreateSessionRequest


class SessionService:
    def __init__(self):
        pass

    async def create_session(self, request: CreateSessionRequest, db: Session):
        try:
            athletes = db.query(Athlete).filter(Athlete.id.in_(request.athletes)).all()
            if not athletes:
                raise TransactionException("Athletes not found for the relevant ids")

            session_id = uuid.uuid4()

            sessions = [
                SessionDetail(
                    id=uuid.uuid4(),
                    session_id=session_id,
                    athlete_id=athlete.id,
                    status=ActiveStatus.ACTIVE,
                    created_by=request.created_by,
                    modified_by=request.created_by,
                )
                for athlete in athletes
            ]

            athlete_session = AthleteSession(
                id=session_id,
                name=request.name,
                session_date=request.sess_date,
                venue=request.venue,
                is_completed=False,
                status=SessionStatus.COMPLETED,
                created_by=request.created_by,
                modified_by=request.created_by,
                session_details=sessions,
            )

            db.add(athlete_session)
            db.commit()

        except Exception as e:
            logger.exception(f"Error occurred while saving the session {str(e)}")
            raise e

    async def get_completed_sessions(self, db: Session):
        try:
            athletes = db.query(AthleteSession).filter(
                AthleteSession.status == SessionStatus.COMPLETED
            )
            return athletes.all()

        except Exception as e:
            logger.exception(f"Error occurred while saving the session {str(e)}")
            raise e

    async def get_not_completed_sessions(self, db: Session):
        try:
            athletes = db.query(AthleteSession).filter(
                AthleteSession.status == SessionStatus.NOT_COMPLETED
            )
            return athletes.all()

        except Exception as e:
            logger.exception(f"Error occurred while saving the session {str(e)}")
            raise e

    async def get_sessions_by_athlete(self, id: str, db: Session):
        try:
            athletes = (
                db.query(AthleteSession)
                .join(SessionDetail)
                .filter(SessionDetail.athlete_id == id)
                .limit(5)
            )
            return athletes.all()

        except Exception as e:
            logger.exception(f"Error occurred while saving the session {str(e)}")
            raise e

    async def get_session_count(self, coach_id: str, db: Session):
        try:
            count = db.query(AthleteSession).join(AthleteSession.session_details).join(SessionDetail.athlete).filter(
                Athlete.coach_id == coach_id
            ).count()
            return count
        except Exception as e:
            logger.exception(f"Error occurred while saving the session {str(e)}")
            raise e
