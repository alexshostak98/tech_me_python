from urllib.parse import urljoin

import my_parser
import patterns


class Creator:

    def __init__(self, url):
        self.url = url

    def get_page_url(self):
        for page in parser.get_data(patterns.page_link):
            page_link = page.attrs['href']
            page_url = urljoin(self.url, page_link)
            yield page_url

    def get_next_page(self):
        for page in parser.get_data(patterns.pagination_link):
            page_link = page.attrs['href']
            page_url = urljoin(self.url, page_link)
            yield page_url

    def get_page_data(self):
        for page_url in self.get_page_url():
            author_name = parser.get_data(patterns.author_name)
            author_link = parser.get_data(patterns.author_link)
            publication_title = parser.get_data(patterns.publication_title)
            release_date = parser.get_data(patterns.release_date)
            tags = parser.get_data(patterns.tags)


if __name__ == "__main__":
    start_url = "https://habr.com/ru/all/"
    creator = Creator(start_url)
    parser = my_parser.Parser(start_url)


