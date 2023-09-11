#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/9/4 23:05

from utils import Req
from urllib import parse
import time
import random


class DownloadsOther:

    def __init__(self, down_path=None):
        self.down_path = down_path

    def get_download_info_ting55(self, book_name, bookId, max_page, folder_path, start_page=None):
        host = "https://m.ting55.com"
        get_audio_url_path = "/glink"
        start_page = int(start_page) if start_page else 1
        for i in range(int(max_page)):
            get_audio_url_payload = {"bookId": bookId, "isPay": 0, "page": i + int(start_page)}
            get_audio_url_headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'JSESSIONID=0A258D3B4B3E1A029A27AF4C10059CA9',
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
            try:
                r = Req(url=parse.urljoin(host, get_audio_url_path), header=get_audio_url_headers,
                        payload=get_audio_url_payload)
                response = r.post()
                print(response, response.json())
            except:
                r = Req(url=parse.urljoin(host, get_audio_url_path), header=get_audio_url_headers,
                        payload=get_audio_url_payload)
                response = r.post()
                print("第二次尝试", response)
                print("第二次尝试", response.json())

            audio_url = response.json()["url"] if response.json()["url"] != "" else response.json()["ourl"]
            audio_format = audio_url.split("/")[-1].split(".")[1]
            audio_number = audio_url.split("/")[-1].split(".")[0] if audio_url.split("/")[-1].split(".")[
                0].isdigit() else str(i + int(start_page))
            dr = Req(url=audio_url)
            dr.download_get(folder_path,
                            book_name + ".".join([audio_number.zfill(len(max_page)), audio_format]))

            time.sleep(random.randint(5, 10))


if __name__ == "__main__":
    down = DownloadsOther()
    down.get_download_info_ting55("庆余年", "13679", "751", "/Users/zhaopeng/Personal/有声书/庆余年", "706")
