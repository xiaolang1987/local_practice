#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/6/9 09:52

import down_bilibili

bili = down_bilibili.Downloads()
bili.get_av_list()

# 对比需要下载的内从
# lista = ["a", "b", "d"]
# listb = ["a"]
# print(set(lista).difference(set(listb)))

# 开始下载
