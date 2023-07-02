import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_SECRET_KEY: str = "1234qwer"  # os.getenv("SECRET_KEY")
    DATABASE_URL: str = (
        "postgresql://root:root@127.0.0.1:5432/facts"  #  os.getenv("DATABASE_URL")
    )


settings = Settings()
