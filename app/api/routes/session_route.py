from typing import List

from fastapi import APIRouter, Depends, status, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core import config
from app.database.db_handler import get_db
from app.schemes.requests.create_session_request import CreateSessionRequest
from app.schemes.requests.session_schema import SessionSchema
from app.services.session_service import SessionService

router = APIRouter(prefix=f"{config.API_PREFIX}/session")

session_service = SessionService()


@router.post("/", tags=["Create session"])
async def create_session(
    request: CreateSessionRequest, db: Session = Depends(get_db)
) -> JSONResponse:
    try:
        await session_service.create_session(request, db)
        return JSONResponse(
            content="Session created successfully", status_code=status.HTTP_201_CREATED
        )

    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while saving the session: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.post("/completed", tags=["Get session count"])
async def get_session_count( coach_id: str = Form(...),
    db: Session = Depends(get_db)
) -> JSONResponse:
    try:
        count = await session_service.get_session_count(coach_id, db)
        return count
    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while saving the session: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.get(
    "/completed", response_model=List[SessionSchema], tags=["Completed sessions"]
)
async def create_session(db: Session = Depends(get_db)) -> JSONResponse:
    try:
        sessions = await session_service.get_completed_sessions(db)
        return sessions
    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while saving the session: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.get(
    "/not-completed",
    response_model=List[SessionSchema],
    tags=["Not completed sessions"],
)
async def create_session(db: Session = Depends(get_db)) -> JSONResponse:
    try:
        sessions = await session_service.get_not_completed_sessions(db)
        return sessions
    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while saving the session: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.get("/{id}/athlete", tags=["Get sessions by athlete"])
async def get_sessions_by_athlete(
    id: str,
    db: Session = Depends(get_db),
) -> JSONResponse:
    try:
        sessions = await session_service.get_sessions_by_athlete(id, db)
        return sessions
    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while saving the session: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
