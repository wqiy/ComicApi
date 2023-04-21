from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class Comic(Base):
    __tablename__ = "comics"
    comic_name = Column(Text, primary_key=True, index=True)
    comic_author = Column(Text)
    comic_info = Column(Text)
    tags = Column(Text, index=True)
    img_url = Column(Text)
    comic_url = Column(Text)
    site = Column(Text, index=True)
    status = Column(Text)

    chapters = relationship("Chapter", back_populates="owner")


class Chapter(Base):
    __tablename__ = "chapters"
    comic_name = Column(Text, ForeignKey("comics.comic_name"))
    chapter_name = Column(Text, primary_key=True)
    chapter_url = Column(Text)
    image_urls = Column(Text)

    owner = relationship("Comic", back_populates="chapters")
