from tortoise.contrib.fastapi import register_tortoise
from config.Config import getSettings
from fastapi import FastAPI

settings = getSettings()

if settings.DB_URL:
    DATABASE_URL = settings.DB_URL

DATABASE_URL = f'postgres://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.SERVER_DATABASE_HOST}:5433/{settings.POSTGRES_DB}'

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": settings.MODELS,
            "default_connection": "default",
        },
    },
}

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app=app,
        db_url=DATABASE_URL,
        generate_schemas=settings.GENERATE_SCHEMAS,
        modules={"models": settings.MODELS},
        add_exception_handlers=True,
    )