from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class PromoPage(Base):
    __tablename__ = "promo_page"
    id = Column(Integer, primary_key=True, autoincrement=True)
    promo_url = Column(String(200), unique=True)
    product_name = Column(String(200), unique=False)
