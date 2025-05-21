from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGO_URL, DATABASE_NAME

client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]

def get_db():
    return db