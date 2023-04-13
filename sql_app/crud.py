from sqlalchemy.orm import Session
from . import models, schemas


def get_comic(db: Session, comic_name: str):
    return db.query(models.Comic).filter(models.Comic.comic_name == comic_name).first()


def get_comics(db: Session, site: str, skip: int = 0, limit: int = 100):
    return db.query(models.Comic).filter(models.Comic.site == site).offset(skip).limit(limit).all()


def get_chapters(db: Session, comic_name: str, skip: int = 0, limit: int = 100):
    return db.query(models.Chapter).filter(models.Chapter.comic_name == comic_name).offset(skip).limit(limit).all()