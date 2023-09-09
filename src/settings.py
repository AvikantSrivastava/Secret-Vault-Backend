from pydantic import BaseSettings

class Config(BaseSettings):
    deta_api_key: str

config = Config()