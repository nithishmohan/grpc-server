from app.meter_usage.database import Base
from sqlalchemy import Column, Integer, Float, DateTime
import datetime


class MeterUsage(Base):

    __tablename__ = "meter_usages"

    id = Column(Integer, primary_key=True)
    value = Column(Float)
    time = Column(DateTime, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


