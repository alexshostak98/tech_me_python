import random
from models import Author, Publication, Tag
from mixins import RandomMixin


def while_deco(func):
    def wrapper(self):
        objects = []
        while self.count:
            instance = func(self)
            objects.append(instance)
            self.count -= 1
        return objects

    return wrapper


class AuthorsGen(RandomMixin):

    @while_deco
    def create_authors(self):
        b_date = self.random_date()
        author = Author(
            fullname=self.random_text("names.txt"),
            nickname=self.random_text("names.txt"),
            b_date=b_date,
            reg_date=self.random_date(b_date)
        )
        return author


class PublicationGen(RandomMixin):

    def create_publications(self, authors):
        publications = []
        for elem in authors:
            publics_count = self.count if self.count else random.randint(50, 100)
            while publics_count:
                content = self.random_text("1984.txt")
                publication = Publication(
                    title=content[:content.find(" ")],
                    release_date=self.random_date(elem.reg_date),
                    content=content,
                    author_id=elem.id
                )
                publications.append(publication)
                publics_count -= 1
        return publications


class TagsGen:

    def __init__(self):
        self.count = random.randint(450, 500)

    @while_deco
    def create_tags(self):
        tag = Tag(
            title=''.join([chr(random.randint(97, 122)) for _ in range(random.randint(5, 7))])
        )
        return tag
