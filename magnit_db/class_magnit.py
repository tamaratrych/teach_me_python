import constance

import requests
import pathlib


class Magnit:
    def __init__(self):
        self.url = constance.url
        self.pattern_url = constance.pattern_url
        self.pattern_tittle = constance.pattern_tittle

    def write_to_file(self, file_path, message):
        with open(file_path, "wb") as file:
            file.write(message)

    def get_page(self, url, to_save=False):
        response = requests.get(url)
        if to_save:
            temporary = url.split("/")
            file_path = pathlib.Path(__file__).parent.joinpath(
                f"promo_links/{temporary[-1] or temporary[-2]}.html"
            )
            self.write_to_file(file_path, response.content)
            # with open(file_path, "wb") as file:
            #     file.write(response.content)
        return response


"""
ДЗ:
Написать программу, извлекающую данные
- Урл акции
- Название акции
и положить все в SQL БД (Посредством алхимии)
"""

