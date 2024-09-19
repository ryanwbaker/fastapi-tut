from sqlalchemy.orm import Session
from . import models, schemas
from dotenv import load_dotenv

load_dotenv()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_cities(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.City).offset(skip).limit(limit).all()

def get_city_by_name_country(db: Session, city: str, country: str):
    return db.query(models.City).filter(models.City.city == city and models.City.country == country).first()

def create_city(db: Session, city: schemas.CityOut):
    db_city = models.City(city=city.city, country=city.country)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return [db_city]
