#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/6/9 09:51

import requests


def down_file(down_url, file_name):
    response = requests.request("GET", down_url)
    with open(file_name, "wb") as f:
        f.write(response.content)


if __name__ == '__main__':
    down_file("a", "A")
