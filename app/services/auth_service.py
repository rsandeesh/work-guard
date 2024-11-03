from datetime import datetime, timedelta
import uuid
from typing import Union

import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core import config
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
                created_by=request.email,
                modified_by=request.email
            )
            db.add(create_coach_model)
            db.commit()
        except Exception as e:
            logger.exception(f"An exception occurred: {str(e)}")
            raise TransactionException(str(e))

    async def authenticate_user(self, email: str, password: str, db: Session) -> Union[Coach | bool]:
        try:
            user = db.query(Coach).filter(Coach.email == email).first()
            if not user:
                return False
            if not self.bycrypt_context.verify(password, user.password):
                return False
            return user
        except Exception as e:
            raise TransactionException(str(e))

    async def create_access_token(self, username: str, user_id: uuid.UUID, expires_delta: timedelta):
        encode = {'sub': username, 'id': str(user_id)}
        expires = datetime.utcnow() + expires_delta
        encode.update({'exp': expires})
        return jwt.encode(encode, config.SECRET_KEY, algorithm=config.ALGORITHM)



