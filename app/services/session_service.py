import uuid

from sqlalchemy.orm import Session

from app.core.logger_config import logger
from app.enums.active_status import ActiveStatus
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
                    id=uuid.uuid4(), session_id=session_id, athlete_id=athlete.id
                )
                for athlete in athletes
            ]

            athlete_session = AthleteSession(
                id=session_id,
                name=request.name,
                session_date=request.sess_date,
                venue=request.venue,
                is_completed=False,
                status=ActiveStatus.ACTIVE,
                created_by=request.created_by,
                modified_by=request.created_by,
                session_details=sessions,
            )

            db.add(athlete_session)
            db.commit()

        except Exception as e:
            logger.exception(f"Error occurred while saving the session {str(e)}")
            raise e
