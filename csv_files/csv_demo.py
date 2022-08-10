#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2022/8/10 23:24

import csv

with open("data_file.csv", "r") as csvfile:
    content = csv.reader(csvfile)
    for row in content:
        print(row)  # 这里打印的是个列表

with open("new_data.csv", "r") as csvfile:
    content = csv.reader(csvfile)
    print(list(content))
    for row in content:
        print(row)  # 这里打印的是个列表
        continue

with open("new_data.csv", "a+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['小丽', '3', '女'])

