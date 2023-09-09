import os
from pydantic import BaseModel
from typing import Optional
from src.database.database import Database
from src.settings import config

user_db = Database(config.deta_api_key , 'users')
bucket_db = Database(config.deta_api_key, 'bucket')

class Item(BaseModel):
    id: Optional[str]
    name: str
    value: str
    bucket_name: str 
    username: str