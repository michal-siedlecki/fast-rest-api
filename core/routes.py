import uuid

from typing import List
from fastapi import APIRouter, Body, Header, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from core.config import settings
from core import crud, utils, database, schemas

router = APIRouter(tags=["dates"], responses={404: {"description": "Not found"}})


# Dependency
def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/dates",
    response_model=List[schemas.DateFactSchema],
    status_code=status.HTTP_200_OK,
)
def read_dates(db: Session = Depends(get_db)):
    users = crud.get_dates(db)
    return users


@router.post(
    "/dates", response_model=schemas.DateFactSchema, status_code=status.HTTP_201_CREATED
)
def post_date(
    day: int = Body(..., title="The number day", ge=1, le=31),
    month: int = Body(..., title="Number of the month", ge=1, le=12),
    db: Session = Depends(get_db),
):
    if not utils.is_valid_day_month(day, month):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request"
        )
    date_fact = crud.create_date(month, day, db)
    return date_fact


@router.delete("/dates/{date_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_date(
    date_id: uuid.UUID,
    db: Session = Depends(get_db),
    X_API_HEADER: str = Header(None, convert_underscores=True),
):
    if X_API_HEADER != settings.APP_SECRET_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    if crud.delete_date(date_id, db):
        return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entry not found")


@router.get(
    "/popular",
    response_model=List[schemas.MonthRankSchema],
    status_code=status.HTTP_200_OK,
)
def get_popular(db: Session = Depends(get_db)):
    return list(crud.get_popular(db))
