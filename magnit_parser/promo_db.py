from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from creator import DataCreator
import models


class PromoDB:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    @staticmethod
    def add_promo_pages(session):
        for pages in creator.create_dataset():
            session.add_all(pages)
            session.commit()  # возможно не нужен здесь

    def create_session(self):
        session = self.maker()
        try:
            self.add_promo_pages(session)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


if __name__ == "__main__":
    url = "https://magnit.ru/promo/"
    creator = DataCreator(url)
    db_url = "sqlite:///promo.db"
    db = PromoDB(db_url)
    db.create_session()
