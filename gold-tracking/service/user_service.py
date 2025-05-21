from repository.user_repository import UserRepository
from dto.user import UserCreate

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register_user(self, user: UserCreate):
        return await self.user_repo.create_user(user)

    async def get_user(self, user_id: str):
        return await self.user_repo.get_user_by_id(user_id)
