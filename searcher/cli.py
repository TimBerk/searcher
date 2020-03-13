# -*- coding:utf-8 -*-

import argparse
from searcher.core import parse


def main():
    access_searches = ['google', 'rambler', 'bing', 'yahoo']
    parser = argparse.ArgumentParser(description='Console searcher')
    parser.add_argument('request', type=str, help="Text of request")
    parser.add_argument('searcher', choices=access_searches, type=str, help="Search system")
    parser.add_argument('count', type=int, help="Result count")
    parser.add_argument('-r', type=bool, dest='recurse', nargs='*', default=False, help="Used recurse search")
    parser.add_argument('-d', type=int, dest='recurse_deep', default=1, help="Deep recurse search")
    parser.add_argument('-f', type=str, dest='format', default='console',
                        help="Set format of output(console, json, csv)")

    args = parser.parse_args()
    print(parse(args.request, args.searcher, args.count, args.recurse, args.recurse_deep, args.format))


# if __name__ == '__main__':
#     main()
