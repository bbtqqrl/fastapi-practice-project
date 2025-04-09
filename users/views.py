from fastapi import APIRouter
from users.schemas import CreateUser
from users import crud
router = APIRouter(prefix='/users', tags=['users'])

@router.post("/")
def hello_index(user: CreateUser):
    return crud.create_user(user_in=user)
