from models.author_model import AuthorModel


class Author:

    def __init__(self, data):
        self.data = data

    def create_page(self):
        authors = []
        for url, name in self.data:
            author = AuthorModel(
                page=url,
                nickname=name,
            )
            authors.append(author)
        return authors
