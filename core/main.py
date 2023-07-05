from fastapi import FastAPI
from core.config import settings
from core import models, routes
from .database import engine

models.BaseModel.metadata.create_all(bind=engine)


description = """

# Dates REST API

Dates REST API application implements a simple REST API using FastAPI. It is
a basic dates database interacting with an external API. 🚀

## Dates

You can **read dates facts**, but first you need to **post** a day and a month that you want read about.
You can find also the post **popular months** among dates that have been posted.
There is also way to **delete** date.

Source code is available [here](https://github.com/michal-siedlecki/fast-dates-api)

"""


app = FastAPI(
    title="Dates facts - REST API",
    openapi_url="/openapi.json",
    secret_key=settings.APP_SECRET_KEY,
    description=description,
    version="0.0.1",
    contact={
        "name": "Michał Siedlecki",
        "email": "siedlecki.michal@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/michal-siedlecki/fast-rest-api/blob/main/LICENCE",
    },
)

app.include_router(routes.router)
