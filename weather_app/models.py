from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, index=True)
    country = Column(String, index=True)

class WeatherRecord(Base):
    __tablename__ = "weather_records"
    record_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    city_id = Column(Integer, ForeignKey("cities.city_id"))
    http_status_code = Column(Integer, index=True)
    time_stamp = Column(DateTime, default=func.now(), index=True)