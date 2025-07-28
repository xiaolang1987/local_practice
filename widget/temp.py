#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2024/12/12 11:41

import os
import mutagen
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC, TCON, TCOM, TPE2, COMM

dir = "/Users/zhaopeng/Desktop/士兵突击/"


def scan_dir(directory):
    files = []
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():  # 直接判断是否为文件
                files.append(entry.name)
    return files


print(scan_dir(dir))
for i in scan_dir(dir):
    file_name = i
    audio_file = dir + file_name
    audio = ID3(audio_file)
    # 通过文件名拆解歌名和歌手
    singer = audio_file.split("/")[-1].split("-")[0].replace(" ", "")
    name = audio_file.split("/")[-1].split("-")[1].split(".")[0].replace(" ", "")

    # 默认直接添加，暂无判断逻辑
    audio.add(TPE1(encoding=3, text="兰晓龙"))  # 添加艺术家
    audio.add(TIT2(encoding=3, text=file_name.replace(".mp3", "")))  # 添加歌曲名称
    audio.add(TALB(encoding=3, text="士兵突击"))  # 添加专辑名称
    # audio.delall("TCOM")
    audio.add(TCOM(encoding=3, text="士兵突击"))
    audio.delall("TPE2")
    audio.delall("TCON")
    audio.delall("COMM")
    audio.add(APIC(
                encoding=0,
                mime='image/jpeg',  # image/jpeg or image/png
                type=3,  # 3 is for the cover(front) image
                data=open("士兵突击.jpg", 'rb').read()
            ))

    audio.save()
    print("歌曲名称: ", audio["TIT2"])

print(audio.values())
print("艺术家: ", audio["TPE1"])
print("歌曲名称: ", audio["TIT2"])
print("专辑名称: ", audio["TALB"])
# print("音乐类型: ", audio["TCON"])
print("作曲者: ", audio["TCOM"])
# print("注释: ", audio["TPE2"])
# audio.delete()

# audio_file = "/Users/zhaopeng/Desktop/八路军冲锋号.mp3"
# audio = ID3(audio_file)
# print(audio.values())
# audio.add(TPE1(encoding=3, text="八路军"))  # 添加艺术家
# audio.add(TIT2(encoding=3, text="冲锋号"))  # 添加歌曲名称
# audio.add(TALB(encoding=3, text="军号"))  # 添加专辑名称
# # audio.delall("TCOM")
# # audio.add(TCOM(encoding=3, text="三体宇宙"))
# audio.delall("TPE2")
# audio.delall("TCON")
# audio.delall("COMM")
# print(audio.values())
# audio.save()
