import requests
import bs4


class Parser:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(self.response.text, "lxml")

    def get_data(self, pattern):
        return [self.soup.find_all(name, attrs) for name, attrs in pattern.items()]
        # for name, attrs in pattern.items():
        #     data_item = self.soup.find(name, attrs)
        #     return data_item
