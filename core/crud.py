import uuid

from sqlalchemy.orm import Session
from core import models
from sqlalchemy import func


def get_dates(db: Session):
    return db.query(models.DateFactModel).all()


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
