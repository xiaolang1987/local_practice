#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2022/9/4 21:47

import json


class YouTuBe():
    def first_page(self):
        with open("youtubebasejson.txt", "r") as f:
            contnet = f.readlines()[0]

        a = json.loads(contnet)["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][1]["tabRenderer"]["content"][
            "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["gridRenderer"]["items"]

        index = 1
        for i in a:
            print(str(index).zfill(3),
                  "you-get -i https://www.youtube.com/watch?v=" + i["gridVideoRenderer"]["videoId"])
            index += 1

    def other_page(self):
        with open("list/lf1.txt", "r") as f:
            content = f.readlines()[0]

        a = json.loads(content)["onResponseReceivedActions"][0]["appendContinuationItemsAction"]["continuationItems"]
        # print(a)
        index = 31
        for i in a:
            print(str(index).zfill(3),
                  "you-get -i https://www.youtube.com/watch?v=" + i["gridVideoRenderer"]["videoId"])
            index += 1


class BiBiLiLi():
    def
