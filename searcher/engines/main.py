# -*- coding:utf-8 -*-

from searcher.engines.engine_google import Google
from searcher.engines.engine_rambler import Rambler
from searcher.engines.engine_bing import Bing
from searcher.engines.engine_yahoo import Yahoo
from searcher.engines.engine_yandex import Yandex
from searcher.engines.engine_mail import Mail


def search_data(searcher, request, count, recurse, recurse_deep, format_result):
    """Search data into different search engine"""
    searcher_map = {
        'google': Google,
        'rambler': Rambler,
        'bing': Bing,
        'yahoo': Yahoo,
        # 'yandex': Yandex,
        # 'mail': Mail,
    }

    if searcher not in searcher_map:
        return "Incorrect searcher"

    return searcher_map[searcher](request, count, recurse, recurse_deep, format_result)
