#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/7/27 23:37

from utils import req
from urllib import parse
import yaml


class bili_station:

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
            r = req(url=get_av_list_url, header=get_av_list_headers, payload=get_av_list_payload)
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


class ximalaya_station:

    def __init__(self):
        self.host = "https://www.ximalaya.com"

    def get_download_info_list(self, album_id):
        """

        :param albumId:
        :return: [[音频编号，音频名，音频id]]
        """
        path = "/revision/album/v1/getTracksList"
        download_info_list = []
        page_num = 1
        for i in range(9999):
            get_info_params = {"albumId": album_id, "pageNum": page_num, "pageSize": "30"}
            r = req(url=parse.urljoin(self.host, path), params=get_info_params)
            response = r.get()
            tracks = response.json()["data"]["tracks"]
            if len(tracks) == 0:
                break
            for trank in tracks:
                download_info_list.append([trank["index"], trank["title"], trank["trackId"]])
            page_num += 1

        return download_info_list

    def get_download_url(self, sound_id):
        """

        :param sound_id:
        :return:
        """
        path = "/revision/play/v1/audio"
        get_download_url_params = {"id": sound_id, "ptype": "1"}
        r = req(url=parse.urljoin(self.host, path), params=get_download_url_params)
        response = r.get()

        return response.json()["data"]["src"]

    def download(self, floder_path, file_name, url):
        r = req(url=url)
        r.download_get(floder_path, file_name)


if __name__ == '__main__':
    # 待办
    # up主、id、存储目录的对应文件
    # 视频与下载状态的对应文件
    # bili = bili_station()
    # print(bili.dif_need_download())
    xima = ximalaya_station()
    down_info = xima.get_download_info_list("52843738")
    for info in down_info:
        down_url = xima.get_download_url(info[2])
        print(down_url.split(".")[-1])
        xima.download("bendi", "-".join([str(info[0]).zfill(4), ".".join([info[1], down_url.split(".")[-1]])]), down_url)
