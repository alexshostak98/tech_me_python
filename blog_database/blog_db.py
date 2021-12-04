import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from queries import Query

import objects
import models


class BlogDB:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    @staticmethod
    def add_authors(session):
        authors = author_gen.create_authors()
        session.add_all(authors)
        session.commit()
        return authors

    @staticmethod
    def add_publications(session, authors):
        publications = publications_gen.create_publications(authors)
        session.add_all(publications)
        session.commit()
        return publications

    @staticmethod
    def add_tags(session):
        tags = tags_gen.create_tags()
        session.add_all(tags)
        session.commit()
        return tags

    @staticmethod
    def create_link(tags, publications):
        for elem in publications:
            tags_count = random.randint(3, 7)
            while tags_count:
                random.choice(tags).publications.append(elem)
                tags_count -= 1

    def create_session(self):
        session = self.maker()
        try:
            authors = self.add_authors(session)
            publications = self.add_publications(session, authors)
            tags = self.add_tags(session)
            self.create_link(tags, publications)
            session.commit()
            query = Query(session)
            query.get_tags()
            query.get_authors()
        except:
            session.rollback()
            raise
        finally:
            session.close()


if __name__ == '__main__':
    db_url = "sqlite:///blog.db"
    db = BlogDB(db_url)
    author_gen = objects.AuthorsGen(objects_count=100)
    publications_gen = objects.PublicationGen()
    tags_gen = objects.TagsGen()
    db.create_session()
