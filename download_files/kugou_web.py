#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/6/12 13:28

import requests
from bs4 import BeautifulSoup
import time
import random
import json


def down_file(down_url, file_name):
    print("下载链接：%s" % down_url)
    print("下载地址：%s" % file_name)
    response = requests.request("GET", down_url)
    # print("文件大小：%s M" % str((len(response.content)/1024/1024)[:4]))
    with open(file_name, "wb") as f:
        f.write(response.content)


for page_num in range(62):
    url_get_audio_id = "https://www.kugou.com/ts/album/16kzygab/p%s.html" % (page_num + 62)
    print("下载页%s" % (page_num + 62))
    headers_get_audio_id = {
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

    response_get_audio_id = requests.request("GET", url_get_audio_id, headers=headers_get_audio_id, data={})
    # print(response_get_audio_id.text)

    b = BeautifulSoup(response_get_audio_id.text, "html.parser")
    for i in b.select("body div li span a"):
        album_id = i.get("href").split("/")[-1].split(".")[0]
        album_num = i.contents[0].replace("虚空凝剑行 第", "").replace("集", "").zfill(4)
        # print(album_num, album_id)

        url_get_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery18007975900876100417_1687842587753&appid=1014&dfid=1twuST2NT6jC0r1mYJ0wSQMA&mid=0a3df919e29a5222c3a112fd0fcd91b3&platid=4&from=112&encode_album_audio_id=%s" % album_id
        print(url_get_url[-11:-1])

        # 获取下载链接
        agent_list = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
            "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo X9 Build/LMY49M)"
        ]
        headers = {
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
            'user-agent': '%s' % agent_list[random.randint(0, (len(agent_list)-1))]
        }

        response_get_url = requests.request("GET", url_get_url, headers=headers, data={})
        print(headers['user-agent'])
        down_url = json.loads(response_get_url.text.split("(")[1].replace(");", ""))["data"]["play_url"]

        # 下载并保存
        down_file(down_url, "/Users/zhaopeng/Personal/bilibili/xukong/虚空凝剑行-%s.mp3" % album_num)
