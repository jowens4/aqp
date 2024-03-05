#data base operations
from sqlalchemy.orm import Session
from app import models, schemas


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

def create_dogbone(db: Session, dogbone: schemas.Dogbone):
    db_dogbone = models.Dogbone(
        number=dogbone.number, 
        note=dogbone.note, 
        length=dogbone.length,
        width=dogbone.width,
        thickness=dogbone.thickness,
        files=dogbone.files,
        timestamp=dogbone.timestamp)
    db.add(db_dogbone)
    db.commit()
    db.refresh(db_dogbone)
    return db_dogbone

def get_dogbone_by_id(db: Session, dogbone_id: int):
    return db.query(models.Dogbone).filter(models.Dogbone.id == dogbone_id).first()



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item