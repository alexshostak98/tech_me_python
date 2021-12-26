from base_model import Base
from sqlalchemy import Column, Integer, String


class AuthorModel(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    page = Column(String(200), unique=True)
    nickname = Column(String(200), unique=True)
