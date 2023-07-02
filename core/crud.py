import uuid

from sqlalchemy.orm import Session
from core.models import models
from sqlalchemy import func


def get_dates(db: Session):
    return db.query(models.DateFactModel).all()


def get_popular(db: Session):
    # sql = 'select ROW_NUMBER() OVER(order by month) as id, count(id) as days_checked, month from public."DatesFacts" group by month order by count(*) desc'
    # return engine.execute(sql)

    return (
        db.query(func.count(models.DateFactModel.id), models.DateFactModel.month)
        .group_by(models.DateFactModel.month)
        .all()
    )


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
