# -*- coding:utf-8 -*-
from abc import ABC
from json import dump
from csv import DictWriter
import requests

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"


class BaseSearcher(ABC):

    def __init__(self, request, count, recurse, recurse_deep, format_result):
        self.request = request
        self.count = count
        self.recurse = recurse
        self.recurse_deep = recurse_deep
        self.format_result = format_result
        self.results = []
        self.current_item = 0
        self.url = ''
        self.text = ''

    def build_url(self, start):
        pass

    def get_page(self):
        headers = {"user-agent": USER_AGENT}
        response = requests.get(self.url, headers=headers, timeout=10)
        if response.status_code == 200:
            self.text = response.text

    def parse_page(self):
        pass

    def print_result(self):
        if self.format_result == 'json':
            self.to_json()
            return 'File json generate'

        if self.format_result == 'csv':
            self.to_csv()
            return 'File csv generate'

        return self.to_console()

    def to_console(self):
        console = [f"{data.get('Name')}: {data.get('Link')}" for data in self.results]
        return "\n".join(console)

    def to_json(self):
        try:
            with open('result.json', 'w', encoding='utf-8') as file:
                dump(self.results, file, indent=4, ensure_ascii=False)
        except IOError:
            print("I/O error")

    def to_csv(self):
        try:
            with open('result.csv', 'w', encoding='utf-8', newline='') as file:
                writer = DictWriter(file, fieldnames=self.results[0].keys())
                writer.writeheader()
                for data in self.results:
                    writer.writerow(data)
        except IOError:
            print("I/O error")

    def run(self):
        pass
