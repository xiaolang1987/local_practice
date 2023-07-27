#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/7/27 23:37

import utils


class bili_station:

    def __int__(self):
        pass

    def get_av_list(self):
        """
        获取up主主页视频列表
        input up主id
        :return:
        视频id    $.data.list.vlist[*].bvid
        视频标题    $.data.list.vlist[*].title
        上传时间    $.data.list.vlist[1].created
        """
        get_av_list_url = "https://api.bilibili.com/x/space/wbi/arc/search?mid=6011141&ps=30&tid=0&pn=2"
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
        response = utils.get(url=get_av_list_url, header=get_av_list_headers, data=get_av_list_payload)
        print(response.json())


if __name__ == '__main__':
    # 待办
    # up主、id、存储目录的对应文件
    # 视频与下载状态的对应文件
    bili = bili_station()
    bili.get_av_list()
