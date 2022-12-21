#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2022/12/21 12:44

from hashids import Hashids
hashids = Hashids(min_length=8, salt='0qDw6JujBPzPbAsr')
print(hashids.encode(7))
print(hashids.decode('wWDrwQML')[0])
