from pydantic_settings import BaseSettings
from decouple import config
from functools import lru_cache

class Settings(BaseSettings):
    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")
    POSTGRES_DB: str = config("POSTGRES_DB")
    DB_URL: str = config("DB_URL")
    SERVER_DATABASE_HOST: str = config("SERVER_DATABASE_HOST")
    GENERATE_SCHEMAS: bool = config("GENERATE_SCHEMAS", default=True)
    MODELS: list = [
        "aerich.models",
        "models.user.UserModel"
    ]

@lru_cache
def getSettings() -> Settings:
    return Settings()