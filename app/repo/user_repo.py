from app.models.user import User


class UserRepo:

    @staticmethod
    async def create_user_repo(user):
        return await User.create(user)

    @staticmethod
    async def verify_username_repo(user):
        return await User.get_or_none(username=user.usernsme)