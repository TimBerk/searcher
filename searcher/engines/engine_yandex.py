# -*- coding:utf-8 -*-
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

from searcher.engines.engine_base import BaseSearcher


class Yandex(BaseSearcher):

    def build_url(self, start):
        phrase = quote_plus(self.request)
        self.url = f"https://yandex.ru/search?text={phrase}&p={str(start)}"

    def parse_page(self):
        soup = BeautifulSoup(self.text, 'lxml')
        print(soup.findAll('li', class_="serp-item"))
        for block in soup.findAll('li', class_="serp-item"):
            if self.current_item < self.count:
                link = block.a.get('href')
                link_name = block.find("div", {"class": 'organic__url-text'}).text
                self.results.append({'Name': link_name, 'Link': link})
                self.current_item += 1

    def run(self):
        while self.current_item < self.count:
            if self.current_item < 11:
                start = 1
            else:
                start = self.current_item // 10
            self.build_url(start)
            self.get_page()
            self.parse_page()
        return self.print_result()
