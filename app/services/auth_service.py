import datetime
import uuid

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.logger_config import logger
from app.enums.active_status import ActiveStatus
from app.exceptions.exception_handler import TransactionException
from app.models.coach import Coach
from app.schemes.requests.create_user_request import CreateUserRequest


class AuthService:
    def __init__(self):
        self.bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

    async def create_user(self, request: CreateUserRequest, db: Session):
        try:
            create_coach_model = Coach(
                id=uuid.uuid4(),
                first_name=request.first_name,
                last_name=request.last_name,
                email=request.email,
                password=self.bycrypt_context.hash(request.password),
                status=ActiveStatus.ACTIVE,
                created_at=datetime.datetime.now(),
                created_by=request.email,
                modified_by=request.email
            )
            db.add(create_coach_model)
            db.commit()
        except Exception as e:
            logger.exception(f"An exception occurred: {str(e)}")
            raise TransactionException(str(e))



