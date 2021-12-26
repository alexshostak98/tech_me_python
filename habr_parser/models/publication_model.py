from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from base_model import Base
from author_model import AuthorModel


class PublicationModel(Base):
    __tablename__ = "publications"
    id = Column(Integer, primary_key=True, autoincrement=True)
    release_date = Column(Date, unique=False)
    title = Column(String(200), unique=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship(AuthorModel, backref="publications")
