from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.core import config
from app.database.db_handler import get_db
from app.models.session import Session
from app.schemes.custom_types.token import Token

from app.schemes.requests.create_user_request import CreateUserRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix=f"{config.API_PREFIX}/auth", tags=["auth"])

auth_service = AuthService()


@router.post("/")
async def create_user(request: CreateUserRequest, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        await auth_service.create_user(request, db)
        return JSONResponse(content="User created successfully", status_code=status.HTTP_201_CREATED)
    except Exception as e:
        return JSONResponse(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)



