import os
from pydantic import BaseModel
from typing import Optional
from src.database.database import Database

user_db = Database(os.environ.get('DETA'), 'users')
bucket_db = Database(os.environ.get('DETA'), 'bucket')

class Item(BaseModel):
    id: Optional[str]
    name: str
    value: str
    bucket_name: str 
    username: str