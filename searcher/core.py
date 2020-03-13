# -*- coding:utf-8 -*-
from searcher.engines.main import search_data


def parse(request, searcher, count, recurse, recurse_deep, format_result):
    searcher = search_data(searcher, request, count, recurse, recurse_deep, format_result)
    result = searcher.run()
    return result
