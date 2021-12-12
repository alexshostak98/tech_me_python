import datetime
import time
import random


class RandomMixin:

    def __init__(self, objects_count=0):
        self.count = objects_count
        self.rows_len = 0

    @staticmethod
    def random_date(start_time=datetime.date.fromtimestamp(10**5)):
        start_date = datetime.date.ctime(start_time)
        start = time.mktime(time.strptime(start_date))
        random_time = datetime.date.fromtimestamp(random.randint(int(start), int(time.time())))
        return random_time

    def random_text(self, file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            file.seek(self.rows_len)
            text = file.readline()
            self.rows_len += len(text)
        return text.strip('\n')
