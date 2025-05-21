import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = quote_plus(os.getenv('MONGO_PASSWORD'))
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
DATABASE_NAME = os.getenv("DATABASE_NAME", "fastapi_db")
MONGO_URL = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{DATABASE_NAME}?authSource=admin"
