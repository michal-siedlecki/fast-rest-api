import uuid
from sqlalchemy import Column, String, SmallInteger
from sqlalchemy.dialects.postgresql import UUID
from core.database import BaseModel


class DateFactModel(BaseModel):
    __tablename__ = "DatesFacts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    day = Column(SmallInteger)
    month = Column(SmallInteger)
    fact = Column(String)
