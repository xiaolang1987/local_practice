#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/7/27 23:37

from utils import Req
from urllib import parse
import yaml


class DownloadsBiLi:

    def __init__(self):
        pass

    def get_av_list(self):
        """
        获取up主主页视频列表
        input up主id
        :return:
        视频id    $.data.list.vlist[*].bvid
        视频标题    $.data.list.vlist[*].title
        上传时间    $.data.list.vlist[1].created
        合集  $.data.list.vlist[1].meta.title
        """
        av_list = []

        for i in range(60):
            get_av_list_url = "https://api.bilibili.com/x/space/wbi/arc/search?mid=6011141&ps=30&tid=0&pn=1"
            get_av_list_payload = {}
            get_av_list_headers = {
                'authority': 'api.bilibili.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'origin': 'https://space.bilibili.com',
                'referer': 'https://space.bilibili.com/6011141/video?tid=0&pn=1&keyword=&order=pubdate',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
            }
            r = Req(url=get_av_list_url, header=get_av_list_headers, payload=get_av_list_payload)
            response = r.get()
            vlist = response.json()["data"]["list"]["vlist"]
            if vlist == []:
                print("kongle")
                break
            else:
                for vinfo in vlist:
                    bvid = vinfo["bvid"]
                    title = vinfo["title"]
                    created = vinfo["created"]
                    albums = vinfo["meta"]["title"]
                    print([bvid, title, created, albums])
                    av_list.append([bvid, title, created, albums])
        return av_list

    def dif_need_download(self):
        net_list = ["a", "e", "f", "g", "i"]

        with open("download_info.yml", "r", encoding="utf-8") as f:
            con = yaml.load(f, Loader=yaml.FullLoader)
        a = con["bili"]["林霖心医"]
        need_down = set(net_list).difference(set(a["black_list"])).difference(set(a["downloaded_list"]))

        return need_down


if __name__ == '__main__':
    # 待办
    # up主、id、存储目录的对应文件
    # 视频与下载状态的对应文件
    bili = DownloadsBiLi()
    print(bili.dif_need_download())
