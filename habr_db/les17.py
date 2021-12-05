import time
import typing
from datetime import datetime
from urllib.parse import urljoin

from constants import COMPLETE_STATUSES
from control_decoration import num_wrong_tries

import requests
import bs4

# TODO: Логирование ошибок в БД
# TODO: Общая декомпозиция и универсализация подхода
# TODO: Предусмотреть повторный запуск без обхода дубликатов
class HabrParser:

    def __init__(self, start_url, delay=1.0):
        self.start_url = start_url
        self.done_urls = set()
        self.tasks = []
        self.tasks.append(self.get_task(self.start_url, self.rows_parse))
        self.__parse_time = 0
        self.delay = delay

    def get_task(self, url: str, callback: typing.Callable):
        def task():
            return callback(url)

        return task

    def run(self):
        while self.tasks:
            task = self.tasks.pop(0)
            data = task()
            if data:
                self.save(data)
            print(1)

    # TODO: Сохранять данные в БД посредством SQLALCHEMY
    def save(self, page_data):
        """
        - Модель публикации
        - Модель автора
        - Модель Тега
        """
        pass

    # TODO: Ретрай при недоступности с контролем количества
    # TODO: Предусмотреть количество плохих повторений циклов
    @num_wrong_tries
    def _get_response(self, url):
        while True:
            next_time = self.__parse_time + self.delay
            now_time = time.time()
            if next_time > now_time:
                time.sleep(next_time - now_time)
            response = requests.get(url)
            self.__parse_time = now_time
            if response.status_code in COMPLETE_STATUSES:
                return response

    # TODO: Реализовать набор статусов не хардкодно и гибко
    # TODO: Обработка ошибки создания Супа
    def get_soup(self, url):
        response = self._get_response(url)
        soup = bs4.BeautifulSoup(response.text, "lxml")
        return soup

    def __links_parse(self, url, soup, class_name, callback):
        links = soup.find_all("a", attrs={"class": class_name})
        for itm in links:
            href = itm.attrs.get("href")
            if href:
                link = urljoin(url, href)
                self.tasks.append(self.get_task(link, callback))

    def rows_parse(self, url):
        soup = self.get_soup(url)
        # self.__links_parse(url, soup, "tm-pagination__page", self.rows_parse)
        self.__links_parse(url, soup, "tm-article-snippet__title-link", self.article_parse)

    def article_parse(self, url):
        soup = self.get_soup(url)
        title = soup.find("h1", attrs={'class': 'tm-article-snippet__title'}).text
        published_date = datetime.fromisoformat(soup.find('time').attrs.get('datetime')[:-1])
        author_tag = soup.find('a', attrs={'class': "tm-user-info__username"})
        tags = [link.text for link in soup.find_all('li', attrs={'class': 'tm-separated-list__item'})]
        print(1)


if __name__ == '__main__':
    start_url = "https://habr.com/ru/all/"
    parser = HabrParser(start_url, 0.2)
    parser.run()
    print(1)