#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2024/1/11 19:16

from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC
import requests
import sys


def add_mp3_info(audio_file, album, pic_url=None):
    # 打开音频文件
    audio = ID3(audio_file)
    # 通过文件名拆解歌名和歌手
    name = audio_file.split("/")[-1].split("-")[0].replace(" ", "")
    singer = audio_file.split("/")[-1].split("-")[1].split(".")[0].replace(" ", "")

    # 默认直接添加，暂无判断逻辑
    audio.add(TIT2(encoding=3, text=singer))  # 添加艺术家
    audio.add(TPE1(encoding=3, text=name))  # 添加歌曲名称
    audio.add(TALB(encoding=3, text=album))  # 添加专辑名称
    if pic_url:
        success = download_cover(pic_url)
        if success:
            print("封面下载成功开始添加")
            audio.add(APIC(
                encoding=0,
                mime='image/jpeg',  # image/jpeg or image/png
                type=3,  # 3 is for the cover(front) image
                data=open("temp.jpg", 'rb').read()
            ))
        else:
            print("封面下载失败，未替换封面")
    audio.save(v2_version=3)
    print("艺术家: ", audio["TIT2"])
    print("歌曲名称: ", audio["TPE1"])
    print("专辑名称: ", audio["TALB"])
    # print("发布日期: ", audio["TDRC"])


def download_cover(pic_url):
    try:
        response = requests.get((pic_url))
        with open("temp.jpg", "wb") as f:
            f.write(response.content)
        return True
    except:
        return False


# audio_file = sys.argv[1]
# album = sys.argv[2]
# pic_url = sys.argv[3]
while True:
    audio_file = input("输入文件地址")
    album = input("输入专辑名")
    pic_url = input("输入封面下载地址")
    if pic_url:
        add_mp3_info(audio_file, album, pic_url)
    else:
        add_mp3_info(audio_file, album)
    print("完成\n")
