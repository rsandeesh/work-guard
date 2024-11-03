from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core import config
from app.database.db_handler import get_db
from app.schemes.requests.create_session_request import CreateSessionRequest
from app.services.session_service import SessionService

router = APIRouter(prefix=f"{config.API_PREFIX}/session")

session_service = SessionService()


@router.post("/", tags=["Create session"])
async def create_session(request: CreateSessionRequest, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        await session_service.create_session(request, db)
        return JSONResponse(content="Session created successfully", status_code=status.HTTP_201_CREATED)

    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while saving the session: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )