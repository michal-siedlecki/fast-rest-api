import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Base settings for app.
    """

    APP_SECRET_KEY: str = os.getenv("SECRET_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")


settings = Settings()
