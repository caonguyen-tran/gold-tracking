from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class RoleBase(BaseModel):
    name: str

class Role(RoleBase):
    id: Optional[PyObjectId] = Field(alias="_id")

    class Config:
        from_attributes = True