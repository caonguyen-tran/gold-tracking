from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from bson import ObjectId
from models.role import Role

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    username: str
    email: str
    password: str
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    google_id: Optional[str] = None
    provider: str = "local"
    is_active: bool = True
    is_verified: bool = False
    roles: List[Role] = []
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        arbitrary_types_allowed = True