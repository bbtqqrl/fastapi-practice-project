from typing import Annotated
from pydantic import BaseModel, ConfigDict, EmailStr
from annotated_types import MaxLen, MinLen

class CreateUser(BaseModel):
    username: Annotated[str, MinLen(2), MaxLen(20)]
    email: EmailStr

class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    username: str
    password: bytes
    email: EmailStr
    active: bool = True