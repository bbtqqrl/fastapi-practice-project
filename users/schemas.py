from typing import Annotated
from pydantic import BaseModel, EmailStr
from annotated_types import MaxLen, MinLen

class CreateUser(BaseModel):
    username: Annotated[str, MinLen(2), MaxLen(20)]
    email: EmailStr