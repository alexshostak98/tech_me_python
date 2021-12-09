from urllib.parse import urljoin

from my_parser import Parser
from page import Page


class DataCreator:

    templates = {"promo_pages": r"(/promo/\d+/)", "promo_title": r":title.+\"(.+)\""}

    def __init__(self, url):
        self.delim = 10
        self.url = url

    @staticmethod
    def get_parse_data(url, pattern):
        # return Parser(url, pattern).find_pattern()
        parser = Parser(url, pattern)
        return parser.find_pattern()

    def create_dataset(self):
        all_promo_pages = self.get_parse_data(self.url, self.templates["promo_pages"])
        pages_count = len(all_promo_pages)
        promo_data = {}
        for num, page in enumerate(all_promo_pages, 1):
            promo_url = urljoin(self.url, page)
            promo_title = " ".join(self.get_parse_data(promo_url, self.templates["promo_title"]))
            promo_data[promo_title] = promo_url
            if not num % self.delim or num == pages_count:
                page = Page(promo_data)
                yield page.create_page()
                promo_data.clear()
