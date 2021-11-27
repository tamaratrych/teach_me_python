from urllib.parse import urljoin, urlparse
import requests
import re
import time


def parse_page(source, response, products):
    for link in re.findall(source.pattern_url, response.text):
        base = urlparse(response.url)
        url = urljoin(response.url, link)
        if base.netloc == urlparse(url).netloc:
            if url not in products:
                _ = source.get_page(url, to_save=True)
            products.add(url)
           #time.sleep(0.001)


def parse_data(source, products):
    promo_dict = {}
    for url in products:
        response = requests.get(url)
        promo_title = re.findall(source.pattern_tittle, response.text)
        if promo_title:
            promo_dict[url] = promo_title[0]
    return promo_dict


