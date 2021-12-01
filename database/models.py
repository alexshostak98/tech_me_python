from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, ForeignKey, Table
import time

Base = declarative_base()

publication_tag = Table(
    "publication_tag",
    Base.metadata,
    Column("publication_id", Integer, ForeignKey("publication.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
)


class Publication(Base):
    __tablename__ = "publication"
    id = Column(Integer, primary_key=True, autoincrement=True)
    release_date = Column(String, unique=False, default=time.asctime())
    title = Column(String(200), unique=False)
    content = Column(String())
    author_id = Column(Integer, ForeignKey("author.id"))
    author = relationship("Author", backref="publications")


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), unique=False)
    publications = relationship(Publication, secondary=publication_tag, backref="tags")


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(64), unique=False)
    nickname = Column(String(32), unique=True)
    b_date = Column(String, unique=False, default=time.asctime())
    reg_date = Column(String, unique=False, default=time.asctime())


# class Blog(Base):
#     __tablename__ = "blog"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     author_id = Column(Integer, ForeignKey("author.id"))
#     authors = relationship(Author)
#     publication_id = Column(Integer, ForeignKey("publication.id"))
#     publications = relationship(Publication)
