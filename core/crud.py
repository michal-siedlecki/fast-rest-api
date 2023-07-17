import uuid
import requests
from sqlalchemy.orm import Session
from typing import Optional

from core import models
from sqlalchemy import func


def get_dates(db: Session):
    return db.query(models.DateFactModel).all()


def try_get_response(url):
    accepted_status_codes = [200, 301]
    response = requests.get(url)
    if response.status_code in accepted_status_codes:
        return response

    retries = 3
    while retries:
        response = requests.get(url)
        if response.status_code in accepted_status_codes:
            return response
        retries -= 1


def create_date(month, day, db):
    url = f"http://numbersapi.com/{month}/{day}/date?format=json"
    response = try_get_response(url)
    if response:
        date_fact = models.DateFactModel(
            id=uuid.uuid4(), day=day, month=month, fact=response.content.decode("utf-8")
        )

        db.add(date_fact)
        db.commit()
        return date_fact


def get_popular(db: Session):
    result = (
        db.query(
            func.count(models.DateFactModel.id).label("days_checked"),
            models.DateFactModel.month,
        )
        .group_by(models.DateFactModel.month)
        .all()
    )
    return result


def delete_date(date_id: uuid.UUID, db: Session):
    date = (
        db.query(models.DateFactModel)
        .filter(models.DateFactModel.id == date_id)
        .first()
    )
    if not date:
        return False
    db.delete(date)
    db.commit()
    return True
