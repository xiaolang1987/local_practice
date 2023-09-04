#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/9/4 23:05

from utils import Req
from urllib import parse


class DownloadsOther:

    def __init__(self, down_path=None):
        self.down_path = down_path

    def get_download_info_ting55(self, bookId):
        host = "https://m.ting55.com"
        path = "/glink"
        payload = {"bookId": bookId, "isPay": 0, "page": 99}
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'JSESSIONID=563DDDA05E922F84369B876B32FA195A; __bid_n=1889ef9d34ee06fb574207; FPTOKEN=sPDMXaJKNCgQguy7PFWL3CVYaRtAcRaz5Dc7AuKTyMnxM+RSIakC6p84ROvre//VN8xn2gupAq4sK6d/otG1JOCVkv0oUzDrhFoQEoo8F47jfLvWjQmBI5/i+YNCWuElwr2j3aXmXMATYr5K4tSXPks0GjdG4hV0yqJv/Z/zTWp1bDyZPhPccCS37XmpiokCdnCy074+PLIG3bqnsQqLvD3wfU2ZBVPZ3lxRQI5pk3jN46qG6bSkteJ7TvkHup8jBoT0rGLNwFHOH/iONyOSaDM4m17ewgVFOQHiEbHD9ILK71T+mUAgcLEFQMKhDsRvXhAK7G17ASVEFtIQsOqzhIr837d3pJP+AqVlKIHzv9ZVTXTBTzp0h/YvGu0of+XPZmGf9u+NsuBhPs0tHE+9zA==|BxHGUiv/kdoT4Q+3tjS6lobfQYVepJkEQSCAiax5DhA=|10|903ec84034ce319f3a75bbbfbbdd3769; mhting55=3b4e6a48e7ae40b2',
            'Origin': 'https://m.ting55.com',
            'Referer': 'https://m.ting55.com/book/13888-166',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'xt': 'c6177a5cb078df32ea13f6fa55b44636'
        }
        r = Req(url=parse.urljoin(host, path), header=headers, payload=payload)
        response = r.post()
        print(response.json())


if __name__ == "__main__":
    down = DownloadsOther()
    down.get_download_info_ting55("13888")
