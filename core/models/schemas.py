import uuid
import calendar

from pydantic import BaseModel, Field, validator


class DateFactSchema(BaseModel):
    id: uuid.UUID
    day: int = Field(None, title="The number of the day")
    month: str = Field(None, title="The name of the month")
    fact: str = Field(None, title="The fun fact about the date")

    class Config:
        orm_mode = True

    @validator("month")
    def must_be_month_name(cls, v):
        try:
            x = int(v)
        except ValueError:
            raise ValueError("month number must be an integer")
        return calendar.month_name[x]


class MonthRankSchema(BaseModel):
    id: int
    month: str
    days_checked: int

    @validator("month")
    def must_be_month_name(cls, v):
        try:
            x = int(v)
        except ValueError:
            raise ValueError("month number must be an integer")
        return calendar.month_name[x]
