import uuid
from typing import List

from fastapi import APIRouter, Depends, status, Query, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core import config
from app.core.logger_config import logger
from app.database.db_handler import get_db
from app.schemes.requests.athlete_schema import AthleteSchema
from app.schemes.requests.create_athlete_request import CreateAthleteRequest
from app.schemes.requests.update_athlete_request import UpdateAthleteRequest
from app.services.athlete_service import AthleteService

router = APIRouter(prefix=f"{config.API_PREFIX}/athlete")

athlete_service = AthleteService()


@router.post("/", tags=["Save athlete"])
async def save_athlete(
    request: CreateAthleteRequest, db: Session = Depends(get_db)
) -> JSONResponse:
    try:
        await athlete_service.save_athlete(request, db)

        return JSONResponse(
            content="Athlete created successfully", status_code=status.HTTP_201_CREATED
        )

    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while saving athlete: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.put("/", tags=["Update athlete"])
async def update_athlete(
    request: UpdateAthleteRequest, db: Session = Depends(get_db)
) -> JSONResponse:
    try:
        await athlete_service.update_athlete(request, db)

        return JSONResponse(
            content="Athlete updated successfully", status_code=status.HTTP_200_OK
        )

    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while updating athlete: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.get("/", response_model=List[AthleteSchema], tags=["Get all athletes"])
async def get_athletes_by_coach(
    coach_id: str = Query(...), db: Session = Depends(get_db)
) -> JSONResponse:
    try:
        athletes = await athlete_service.get_athletes_by_coach(coach_id, db)
        athletes_data = [
            {
                **athlete.to_dict(),
                "id": str(athlete.id),
                "contact": str(athlete.contact),
            }
            for athlete in athletes
        ]
        return athletes_data
    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while retrieving athletes: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.get("/{id}", response_model=AthleteSchema, tags=["Get athlete by id"])
async def get_athletes_by_coach(id: str, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        athlete = await athlete_service.get_athlete_by_id(id, db)
        athlete = {
            **athlete.to_dict(),
            "id": str(athlete.id),
            "contact": str(athlete.contact),
        }
        return athlete
    except Exception as e:
        return JSONResponse(
            content=f"Error occurred while retrieving athlete: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.post("/count", tags=["Get athlete count"])
async def get_athlete_count(
    coach_id: uuid.UUID = Form(...), db: Session = Depends(get_db)
) -> JSONResponse:
    try:
        count = await athlete_service.get_athlete_count(coach_id, db)
        return JSONResponse(content=count, status_code=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error occurred while deleting the athlete: {str(e)}")
        return JSONResponse(
            content=f"Error occurred while deleting the athlete: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.delete("/{id}", tags=["Remove student"])
async def remove_athlete(id: str, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        await athlete_service.remove_athlete(id, db)
        return JSONResponse(
            content="Athlete deleted successfully", status_code=status.HTTP_200_OK
        )

    except Exception as e:
        logger.exception(f"Error occurred while deleting the athlete: {str(e)}")
        return JSONResponse(
            content=f"Error occurred while deleting the athlete: {str(e)}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
