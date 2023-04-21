from typing import Union
from pydantic import BaseModel


class ChapterBase(BaseModel):
    comic_name: str


class ChapterCreate(BaseModel):
    pass


class Chapter(BaseModel):
    chapter_name: str
    chapter_url: str
    image_urls: str

    class Config:
        orm_mode = True


class ComicBase(BaseModel):
    comic_id: int
    site: str
    comic_name: str


class ComicCreate(BaseModel):
    pass


class Comic(BaseModel):
    comic_name: str
    comic_author: str
    comic_info: Union[str, None] = None
    tags: Union[str, None] = None
    img_url: str
    comic_url: str
    site: str
    status: str
    chapters: list[Chapter] = []

    class Config:
        orm_mode = True
