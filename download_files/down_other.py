#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/9/4 23:05

from utils import Req
from urllib import parse
import time
import random
from bs4 import BeautifulSoup


class DownloadsOther:

    # def __init__(self, down_path=None):
    #     self.down_path = down_path

    def ting55(self, book_name, bookId, max_page, folder_path, start_page=None):
        """
        :param book_name: 书名，存储音频文件命名用
        :param bookId: 书号
        :param max_page: 音频列表最大页数
        :param folder_path: 本地存储路径
        :param start_page: 音频列表开始下载的页数
        :return:
        """
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

    def kugou_web(self, book_name, bookId, max_page, folder_path):
        web_host = "https://www.kugou.com"
        for page_num in range(max_page):
            web_path = "ts/album/%s/p%s.html" % (bookId, page_num + 1)
            get_audio_id_headers = {
                'authority': 'www.kugou.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cookie': 'kg_mid=0a3df919e29a5222c3a112fd0fcd91b3; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1686288424; kg_dfid=1twuST2NT6jC0r1mYJ0wSQMA; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22gzlogin-user.kugou.com%22%5D%5D%7D; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1686547582',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
            }
            r = Req(url=parse.urljoin(web_host, web_path), header=get_audio_id_headers)
            get_audio_id_response = r.get()

            # 拆解返回的html
            b = BeautifulSoup(get_audio_id_response.text, "html.parser")
            for i in b.select("body div li span a"):
                album_id = i.get("href").split("/")[-1].split(".")[0]
                album_num = i.contents[0].replace("虚空凝剑行 第", "").replace("集", "").zfill(4)
                print(album_num, album_id)

                get_download_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery18007975900876100417_1687842587753&appid=1014&dfid=1twuST2NT6jC0r1mYJ0wSQMA&mid=0a3df919e29a5222c3a112fd0fcd91b3&platid=4&from=112&encode_album_audio_id=%s" % album_id
                print("video ID：%s" % get_download_url[-11:-1])
                get_download_url_headers = {
                    'authority': 'wwwapi.kugou.com',
                    'accept': '*/*',
                    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'cookie': 'kg_mid=0a3df919e29a5222c3a112fd0fcd91b3; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1686288424; kg_dfid=1twuST2NT6jC0r1mYJ0wSQMA; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=0a3df919e29a5222c3a112fd0fcd91b3; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1687842297',
                    'referer': 'https://www.kugou.com/',
                    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"macOS"',
                    'sec-fetch-dest': 'script',
                    'sec-fetch-mode': 'no-cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'someone'
                }
                # json.loads(response_get_url.text.split("(")[1].replace(");", ""))["data"]["play_url"]
                dr = Req(url=get_download_url, header=get_download_url_headers)
                dr.download_get(folder_path, )


if __name__ == "__main__":
    down = DownloadsOther()
    down.ting55("庆余年", "13679", "751", "/Users/zhaopeng/Personal/有声书/庆余年", "706")
