from motor.motor_asyncio import AsyncIOMotorDatabase
from dto.user import UserCreate
from bson import ObjectId
from datetime import datetime
from core.utils import get_password_hash

class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["user"]

    async def create_user(self, user: UserCreate):
        # get current time
        current_time = datetime.now()

        user_dict = {
            "username": user.username,
            "email": user.email,
            "password": get_password_hash(password=user.password),
            "created_at": current_time,
            "updated_at": current_time,
            "is_active": True,
            "is_verified": False,
            "roles": [],
            "provider": "local"
        }

        result = await self.collection.insert_one(user_dict)
        obj_id = result.inserted_id
        user = await self.get_user_by_id(obj_id)
        return user

    async def get_user_by_id(self, user_id: str):
        return await self.collection.find_one({"_id": ObjectId(user_id)})
