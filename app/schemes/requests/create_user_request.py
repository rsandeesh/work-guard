from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
