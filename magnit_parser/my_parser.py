import requests
import re


class Parser:

    def __init__(self, url, pattern):
        self.url = url
        self.pattern = re.compile(pattern)
        self.response = requests.get(self.url)

    def find_pattern(self):
        return set(re.findall(self.pattern, self.response.text))
