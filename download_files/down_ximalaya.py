#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/8/31 22:36

from utils import req
from urllib import parse


class Downloads:

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
    xima = Downloads()
    down_info = xima.get_download_info_list("52843738")
    for info in down_info:
        down_url = xima.get_download_url(info[2])
        print(down_url.split(".")[-1])
        xima.download("bendi", "-".join([str(info[0]).zfill(4), ".".join([info[1], down_url.split(".")[-1]])]),
                      down_url)
