#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/2/28 19:45

import json

# with open("apifox_template_LTV.json", "r") as f:
#     content = json.load(f)
# print(content["b"]["c"])
#
# with open("a.json", "w", encoding="utf-8") as file:
#     for i in range(10):
#         content["b"]["c"].append({"d%s" % i: i})
#     # print(content)
#     json.dump(content, file, indent=4, ensure_ascii=False)

case_id = 30
for i in range(4):
    print(int(case_id/10))
    step_id = int("19"+str(int(case_id/10)).zfill(4)+str(99-i))
    print(step_id)