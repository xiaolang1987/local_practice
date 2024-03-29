#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/6/12 13:28

import requests
from bs4 import BeautifulSoup
import time
import random
import json
import urllib.parse
import re


def down_file(down_url, file_name):
    # 下载音频文件文件
    print("下载链接：%s" % down_url)
    print("下载地址：%s" % file_name)
    response = requests.request("GET", down_url)
    # print("文件大小：%s M" % str((len(response.content)/1024/1024)[:4]))
    with open(file_name, "wb") as f:
        f.write(response.content)


def get_audio_page_url(page_num):
    url_get_audio_id = "https://www.kugou.com/ts/album/14roqm24/p%s.html" % page_num
    print("获取音频列表，第%s页" % page_num)
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

    b = BeautifulSoup(response_get_audio_id.text, "html.parser")
    page_list = []
    for i in b.select("body div li span a"):
        # album_page_url = i.get("href")  # 音频页面链接
        album_id = i.get("href").split("/")[-1].split(".")[0]  # 音频id
        album_name = i.contents[0]  # 原文件名
        print([album_name, album_id])
        page_list.append([album_name, album_id])

    return page_list


def get_audio_download_url(page_id):
    print(page_id)
    domain = "https://www.kugou.com/"
    # audio_download_url = urllib.parse.urljoin(domain, path)
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
        'origin': 'https://www.kugou.com',
        'referer': 'https://www.kugou.com/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0'
    }
    # 'user-agent': '%s' % agent_list[random.randint(0, (len(agent_list) - 1))]

    # url_get_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery18007975900876100417_1687842587753&appid=1014&dfid=1twuST2NT6jC0r1mYJ0wSQMA&mid=0a3df919e29a5222c3a112fd0fcd91b3&platid=4&from=112&encode_album_audio_id=%s" % album_id
    # url_get_url = "https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1709015379646&mid=db5845faf9c8ce5dfbb70cb663a47616&uuid=db5845faf9c8ce5dfbb70cb663a47616&dfid=11S94t1t61n03kQIBr4VkM0f&appid=1014&platid=4&from=111&encode_album_audio_id=%s&token=&userid=0&signature=0526764811d9627cbcc079dfb8dd4972" % page_id
    url_get_url = "https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1709531874223&mid=0a3df919e29a5222c3a112fd0fcd91b3&uuid=0a3df919e29a5222c3a112fd0fcd91b3&dfid=1twuST2NT6jC0r1mYJ0wSQMA&appid=1014&platid=4&from=112&encode_album_audio_id=%s&token=&userid=0&signature=a808a2172f19edeb572b1ffef4dcde17" % page_id
    print("video ID：%s" % url_get_url)  # [-11:-1]

    response_get_url = requests.request("GET", url_get_url, headers=headers, data={})
    # print(headers['user-agent'])
    print(response_get_url.json())
    down_url = \
        json.loads(response_get_url.text.replace(response_get_url.text.split("(")[0] + "(", "").replace(");", ""))[
            "data"]["play_url"]
    return down_url


# album_id = input("输入酷狗链接的albumId：")
# save_path = input("输入本地保存路径：")

for i in get_audio_page_url(1):
    print(get_audio_download_url(i[1]))

# for num in range(1):
#     page_num = num + 1
#     url_get_audio_id = "https://www.kugou.com/ts/album/14roqm24/p%s.html" % page_num
#     print("下载页%s" % page_num)
#     headers_get_audio_id = {
#         'authority': 'www.kugou.com',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#         'cookie': 'kg_mid=0a3df919e29a5222c3a112fd0fcd91b3; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1686288424; kg_dfid=1twuST2NT6jC0r1mYJ0wSQMA; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22gzlogin-user.kugou.com%22%5D%5D%7D; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1686547582',
#         'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"macOS"',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'none',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
#     }
#
#     response_get_audio_id = requests.request("GET", url_get_audio_id, headers=headers_get_audio_id, data={})
#     # print(response_get_audio_id.text)
#
#     b = BeautifulSoup(response_get_audio_id.text, "html.parser")
#     for i in b.select("body div li span a"):
#         album_id = i.get("href").split("/")[-1].split(".")[0]  # 音频id
#         album_name = i.contents[0]  # 原文件名
#         print(album_name, album_id)
#
#         # 获取下载链接
#         agent_list = [
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
#             "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
#             "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo X9 Build/LMY49M)"
#         ]
#         headers = {
#             'authority': 'wwwapi.kugou.com',
#             'accept': '*/*',
#             'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#             'cookie': 'kg_mid=0a3df919e29a5222c3a112fd0fcd91b3; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1686288424; kg_dfid=1twuST2NT6jC0r1mYJ0wSQMA; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=0a3df919e29a5222c3a112fd0fcd91b3; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1687842297',
#             'referer': 'https://www.kugou.com/',
#             'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"macOS"',
#             'sec-fetch-dest': 'script',
#             'sec-fetch-mode': 'no-cors',
#             'sec-fetch-site': 'same-site',
#             'user-agent': '%s' % agent_list[random.randint(0, (len(agent_list) - 1))]
#         }
#
#         # url_get_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery18007975900876100417_1687842587753&appid=1014&dfid=1twuST2NT6jC0r1mYJ0wSQMA&mid=0a3df919e29a5222c3a112fd0fcd91b3&platid=4&from=112&encode_album_audio_id=%s" % album_id
#         url_get_url = "https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1709015379646&mid=db5845faf9c8ce5dfbb70cb663a47616&uuid=db5845faf9c8ce5dfbb70cb663a47616&dfid=11S94t1t61n03kQIBr4VkM0f&appid=1014&platid=4&from=111&encode_album_audio_id=%s&token=&userid=0&signature=0526764811d9627cbcc079dfb8dd4972" % album_id
#         print("video ID：%s" % url_get_url[-11:-1])
#
#         response_get_url = requests.request("GET", url_get_url, headers=headers, data={})
#         print(headers['user-agent'])
#         print(response_get_url.text)
#         down_url = \
#             json.loads(response_get_url.text.replace(response_get_url.text.split("(")[0] + "(", "").replace(");", ""))[
#                 "data"]["play_url"]
#
#         # 组装文件名
#         file_type = down_url.split(".")[-1]
#         edit_album_name = re.sub(r'^\d+', '', album_name)
#         album_num = re.search(r'^\d+', album_name)
#         if album_num:
#             file_name = album_num.group().zfill(3) + edit_album_name + file_type
#         else:
#             print("获取排序数字失败，暂时命名为000")
#             file_name = "000" + edit_album_name + "." + file_type
#         print("下载的文件名是：" + file_name)
#
#         # 下载并保存
#         down_file(down_url, "%s/%s" % ("/Users/zhaopeng/Personal/bilibili/魔兽有声剧/酷狗", file_name))
