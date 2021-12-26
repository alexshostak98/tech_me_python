from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from base_model import Base
from publication_model import PublicationModel


publication_tag = Table(
    "publication_tag",
    Base.metadata,
    Column("publication_id", Integer, ForeignKey("publications.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class TagModel(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), unique=True)
    publications = relationship(PublicationModel, secondary=publication_tag, backref="tags")
