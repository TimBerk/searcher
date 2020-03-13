# -*- coding:utf-8 -*-
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

from searcher.engines.engine_base import BaseSearcher


class Bing(BaseSearcher):

    def build_url(self, start):
        phrase = quote_plus(self.request)
        self.url = f"https://bing.com/search?q={phrase}&first={str(start)}"

    def parse_page(self):
        soup = BeautifulSoup(self.text, 'lxml')
        for block in soup.find_all(class_="b_algo"):
            if self.current_item < self.count and block.a is not None:
                link = block.a.get('href')
                link_name = block.a.text
                self.results.append({'Name': link_name, 'Link': link})
                self.current_item += 1

    def run(self):
        while self.current_item < self.count:
            if self.current_item < 10:
                start = 0
            else:
                start = (self.current_item // 10 + 1) * 10 + 1
            self.build_url(start)
            self.get_page()
            self.parse_page()
        return self.print_result()
