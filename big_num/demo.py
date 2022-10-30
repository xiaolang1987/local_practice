#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2022/10/27 23:41

from openpyxl import load_workbook

wb = load_workbook('./demo.xlsx')
# https://zhuanlan.zhihu.com/p/409954748
print(wb.sheetnames)
