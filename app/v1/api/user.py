from fastapi import APIRouter,Depends,status
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm
from app.servies.user_ser import UserService
from app.schemas.user import UserBase

router = APIRouter()

def get_user_service():
    return UserService

@router.post('/signup',status_code=status.HTTP_201_CREATED,response_model=UserBase)
async def signup(
    user : User,
    service : UserService=Depends(get_user_service)
):
    return await service.create_user_ser(user)

@router.post('/login',status_code=status.HTTP_202_ACCEPTED,response_model=UserBase)
async def login(
    user : OAuth2PasswordRequestForm = Depends(),
    service : UserService = Depends(get_user_service)
):
    return await service.verity_user_ser(user)

