# -*- coding:utf-8 -*-
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

from searcher.engines.engine_base import BaseSearcher


class Yahoo(BaseSearcher):

    def build_url(self, start):
        phrase = quote_plus(self.request)
        self.url = f"https://search.yahoo.com/search?p={phrase}&b={str(start)}"

    def parse_page(self):
        soup = BeautifulSoup(self.text, 'lxml')
        list_results = soup.find('ol', class_='searchCenterMiddle')
        for block in list_results.find_all(class_='algo'):
            if self.current_item < self.count and block.a is not None:
                link = block.a.get('href')
                link_name = block.a.text
                self.results.append({'Name': link_name, 'Link': link})
                self.current_item += 1

    def run(self):
        while self.current_item < self.count:
            if self.current_item < 10:
                start = 10 if self.current_item >= 7 else 0
            else:
                start = (self.current_item // 10 + 1) * 10 + 1
            self.build_url(start)
            self.get_page()
            self.parse_page()
        return self.print_result()
