from app.repo.user_repo import UserRepo
from fastapi import HTTPException
from app.core.security import verify_hash_password,hash_password

class UserService:

    @staticmethod
    async def create_user_ser(user):
        exist_user = await UserRepo.verify_username_repo(user)
        if exist_user:
            raise HTTPException(status_code=409,detail='username must be unique')
        user.password = hash_password(user.password)
        return await UserRepo.create_user_repo(user,)

    @staticmethod
    async def verity_user_ser(user):
        db_user = await UserRepo.verify_username_repo(user)
        if not db_user:
            raise HTTPException(status_code=404,detail="user is None")
        if not verify_hash_password(user.password,db_user.password):
            raise HTTPException(status_code=401,detail='wroung password')
        return db_user
