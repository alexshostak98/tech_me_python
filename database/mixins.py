import time
import random


class RandomMixin:

    def __init__(self, objects_count=0):
        self.count = objects_count
        self.rows_len = 0

    @staticmethod
    def random_date(start_time=time.ctime(0)):
        start = time.mktime(time.strptime(start_time))
        random_time = time.ctime(random.randint(int(start), int(time.time())))
        return random_time

    def random_text(self, file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            file.seek(self.rows_len)
            text = file.readline().strip('\n')
            self.rows_len = self.rows_len + len(text) + 1
        return text
