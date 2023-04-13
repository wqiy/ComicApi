from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/comics/{site}", response_model=list[schemas.Comic])
def read_comics(site: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comics = crud.get_comics(db, site=site, skip=skip, limit=limit)
    return comics


@app.get("/comics/{comic_name}", response_model=schemas.Comic)
def read_comic(comic_name: str, db: Session = Depends(get_db)):
    db_comic = crud.get_comic(db, comic_name=comic_name)
    return db_comic


@app.get("/comics/{comic_name}/chapters/", response_model=list[schemas.Chapter])
def read_chapters(comic_name: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    chapters = crud.get_chapters(db, comic_name=comic_name, skip=skip, limit=limit)
    return chapters
