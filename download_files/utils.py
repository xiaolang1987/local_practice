#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/6/9 09:51

import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import random
import time

# 禁用安全请求警告
disable_warnings(InsecureRequestWarning)


class req:
    ot = 10
    verify = False
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36 Edge/19.6",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
    ]

    def __init__(self, url, params=None, header=None, payload=None, files=None, cookie=None):
        self.url = url
        self.params = params if params else {}
        self.header = header if header else {}
        self.header["User-Agent"] = req.user_agent_list[random.randrange(len(req.user_agent_list))]
        self.payload = payload if payload else {}
        self.files = files if files else {}
        self.cookie = cookie if cookie else {}

    def get(self):
        try:
            res = requests.get(self.url, params=self.params, headers=self.header, data=self.payload,
                               cookies=self.cookie, verify=req.verify, timeout=req.ot)
        except Exception as e:
            res = {"error": str(e)}  # 如果接口调用出错的话，那么就返回一个有错误信息的字典
            print("异常信息：接口调用失败！ url 【%s】 data 【%s】 实际结果是 【%s】" % (self.url, self.params, res))

        return res

    def post(self):
        try:
            res = requests.post(self.url, params=self.params, headers=self.header, data=self.payload, files=self.files,
                                cookies=self.cookie, verify=req.verify, timeout=req.ot)
        except Exception as e:
            res = {"error": str(e)}  # 如果接口调用出错的话，那么就返回一个有错误信息的字典
            print("\n异常信息：接口调用失败！ url 【%s】 data 【%s】 实际结果是 【%s】" % (self.url, self.params, res))

        return res


def down_file(down_url, file_name):
    response = requests.request("GET", down_url)
    with open(file_name, "wb") as f:
        f.write(response.content)


if __name__ == '__main__':
    down_file("a", "A")
