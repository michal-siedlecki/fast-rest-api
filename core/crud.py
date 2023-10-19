import uuid
import requests
from sqlalchemy.orm import Session

from core import models
from sqlalchemy import func

from requests.exceptions import ConnectionError

from typing import Optional


class ApiResponseException(Exception):
    """The API did not return valid response code"""

    pass


def get_dates(db: Session) -> list:
    """Fetches models from database
    :param db:
    :return: list of the DatesFacts database models
    """
    return db.query(models.DateFactModel).all()


def create_date(month, day, db) -> Optional[models.DateFactModel]:
    """Create DateFact entry in database based on response from the external api.
    :param day: a day number
    :param month: a month number
    :param db: database context
    :return: DateFact model
    """
    valid_status_codes = [200, 301]
    url = f"http://numbersapi.com/{month}/{day}/date?format=json"
    try:
        response = requests.get(url)
    except ConnectionError as e:
        raise ApiResponseException(e)
    if response.status_code not in valid_status_codes:
        raise ApiResponseException(
            f"The API did not return valid response code {response.status_code}, "
            f'details {response.content.decode("utf-8")}'
        )
    date_fact = models.DateFactModel(
        id=uuid.uuid4(), day=day, month=month, fact=response.content.decode("utf-8")
    )
    db.add(date_fact)
    db.commit()
    return date_fact


def get_popular(db: Session) -> list:
    """Fetch DatesFacts models from the database and group them by month
    :param db: database context
    :return: list of DateFact database models
    """
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
    """Delete DateFact entry from the database
    :param date_id: a date id
    :param db: database context
    :return: True if deleted False if not
    """
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
