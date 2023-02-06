#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/1/31 17:00

import csv

time_range = ["day:8,1", "day:5,1", "day:31,1", "day:61,1", "day:91,1", "day:181,1"]
print([[i, i.split(",")[0].replace("day:", "")] for i in time_range])
