import time
from datetime import datetime
from urllib.parse import urljoin

import requests
import bs4


class HabrParser:
    def __init__(self, start_url):
        self.start_url = start_url
        self.done_urls = set()
        self.tasks = []
        self.tasks.append(self.get_task(self.start_url, self.rows_parse))
        self.__parse_time = time.time()
        self.delay = 1


    def get_task(self, url: str, callback):
        def task():
            return callback(url)

        return task


    def run(self):
        while self.tasks:
            task = self.tasks.pop(0)
            data = task()
            if data:
                self.save(data)


    def save(self, data):
        pass


    def _get_response(self, url, complete_statuses):
        while True:
            next_time = self.__parse_time + self.delay
            now_time = time.time()
            if next_time > now_time:
                time.sleep(next_time - now_time)
            response = requests.get(url)
            if response in complete_statuses:
                return response


    def get_soup(self, url):
        response = self._get_response(url, ["200"])
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
        print(1)


    def article_parse(self, url):
        soup = self.get_soup(url)
        title = soup.find("h1", attrs={"class": "m-article-snippet__title tm-article-snippet__title_h1"}).text
        published_date = datetime.fromisoformat(soup.find("time").attrs.get('datetime')[:-1])
        author_tag = soup.find('a', attrs={'class': "tm-user-info__username"})
        author_name = author_tag.text
        autor_url = urljoin(url, author_tag.attrs.get("href"))
    print(1)


if __name__ == '__main__':
    start_url = "https://habr.com/ru/all/"
    parser = HabrParser(start_url)
    parser.run()
    print(1)