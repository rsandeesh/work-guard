from datetime import timedelta
from typing import Annotated

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose.exceptions import JWTError
from sqlalchemy.orm import Session

from app.core import config
from app.core.logger_config import logger
from app.database.db_handler import get_db
from app.models.coach import Coach
from app.schemes.custom_types.token import Token

from app.schemes.requests.create_user_request import CreateUserRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix=f"{config.API_PREFIX}/auth", tags=["auth"])

auth_service = AuthService()
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


@router.post("/", tags=["User sign up"])
async def create_user(
    request: CreateUserRequest, db: Session = Depends(get_db)
) -> JSONResponse:
    try:
        await auth_service.create_user(request, db)
        return JSONResponse(
            content="User created successfully", status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        return JSONResponse(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/token", response_model=Token, tags=["User authentication"])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    try:
        user: Coach = await auth_service.authenticate_user(
            form_data.username, form_data.password, db
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate the user",
            )

        token = await auth_service.create_access_token(
            form_data.username, user.id, timedelta(minutes=20)
        )

        return Token(access_token=token, token_type="Bearer")
    except Exception as e:
        logger.exception(f"Exception occurred which authenticating: {str(e)}")


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        user_name: str = payload.get("sub")
        user_id: str = payload.get("id")
        if user_name is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user.",
            )

        return {"username": user_name, "id": user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user."
        )
