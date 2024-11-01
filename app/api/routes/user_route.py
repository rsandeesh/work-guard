from fastapi import FastAPI, APIRouter, Form

from app.core import config

file_upload_route = FastAPI()
router = APIRouter(prefix=f"{config.API_PREFIX}/auth")
# file_service = FileService()

@router.post("/get-access-token", tags=["Authenticate user"])
async def get_access_token(user_name: str = Form(...), password: str = Form(...)):
    return "Hello World!"


# @router.post("/")