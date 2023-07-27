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

def post(url, data=None, cookie=None, header=None, is_json=False, files=None, params=None):
    data = data if data else {}
    cookie = cookie if cookie else {}
    header = header if header else {"Connection": "close"}
    files = files if files else {}
    params = params if params else {}
    try:
        # post_start_time = time.time()
        if is_json:
            res = requests.post(url, json=data, cookies=cookie, headers=header, verify=False, files=files,
                           params=params, timeout=10)
        else:
            res = requests.post(url, data=data, cookies=cookie, headers=header, verify=False, files=files,
                           params=params, timeout=10)
        # post_end_time = time.time()
        # post_time_used = post_end_time - post_start_time
        # print("\n【耗时：%s。接口返回数据：%s】" % (post_time_used, res))

    except Exception as e:
        res = {"error": str(e)}  # 如果接口调用出错的话，那么就返回一个有错误信息的字典
        print("\n异常信息：接口调用失败！ url 【%s】 data 【%s】 实际结果是 【%s】" % (url, data, res))

    return res


def get(url, data=None, cookie=None, header=None):
    data = data if data else {}
    data.update({"v": "istest_0.%s" % str(random.randint(0, 1000000)).zfill(7)})
    cookie = cookie if cookie else {}
    header = header if header else {}
    # print("【请求接口地址：%s】" % url)
    # print("【接口请求数据：%s】" % data)
    try:
        get_start_time = time.time()
        res = requests.get(url, params=data, cookies=cookie, headers=header, verify=False, timeout=10)
        # get_end_time = time.time()
        # get_time_used = get_end_time - get_start_time
        # print("【耗时：%s。接口返回数据：%s】" % (get_time_used, res))
    except Exception as e:
        res = {"error": str(e)}  # 如果接口调用出错的话，那么就返回一个有错误信息的字典
        print("异常信息：接口调用失败！ url 【%s】 data 【%s】 实际结果是 【%s】" % (url, data, res))
    return res


def down_file(down_url, file_name):
    response = requests.request("GET", down_url)
    with open(file_name, "wb") as f:
        f.write(response.content)


if __name__ == '__main__':
    down_file("a", "A")
