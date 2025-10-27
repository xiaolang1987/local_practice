#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2025/10/23 14:53

import subprocess
import os


def scan_dir(directory):
    files = []
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():  # 直接判断是否为文件
                files.append(entry.name)
    return files


# 从MP4文件中提取MP3
def copy_mp3_from_mp4(input_file):
    # 判断能不能直接提取MP3
    audio_type = subprocess.run(["ffprobe", "-v", "quiet", "-select_streams", "a",
                                 "-show_entries", "stream = codec_name", "-of", "default=noprint_wrappers=1:nokey=1",
                                 input_file], capture_output=True, text=True, check=True)
    # print(audio_type.stdout.strip())

    # 开始提取
    if audio_type.stdout.strip() == "mp3":  # 如果是mp3，直接提取
        subprocess.run(["ffmpeg", "-i", input_file,
                        "-acodec", "copy", "-vn", input_file.replace(".mp4", ".mp3"),
                        "-y"])
        print("完成：" + input_file.replace(".mp4", ".mp3"))
    else:  # 如果不是mp3，先提取m4a，再转成mp3
        subprocess.run(["ffmpeg", "-i", input_file,
                        "-acodec", "copy", "-vn", input_file.replace(".mp4", ".m4a"),
                        "-y"])
        print("完成：" + input_file.replace(".mp4", ".m4a"))

        # 将m4a转成mp3
        subprocess.run(["ffmpeg", "-i", input_file.replace(".mp4", ".m4a"), "-c:a", "libmp3lame", "-b:a", "128k",
                        input_file.replace(".mp4", ".mp3"), "-y"])


# 切除指定时间段的音频
def cut_audio_remove(input_file, start_time, end_time, output_path):
    output_file = os.path.join(output_path, input_file.split("/")[-1])
    cut_time = "[0:a]atrim=0:%s[a1];[0:a]atrim=%s[a2];[a1][a2]concat=n=2:v=0:a=1" % (start_time, end_time)
    subprocess.run(["ffmpeg", "-i", input_file, "-filter_complex", cut_time, output_file, "-y"])


# 提取指定时间段的音频，不适合批量
def cut_audio_get(input_file, start_time, end_time, output_path):
    output_file = os.path.join(output_path, input_file.split("/")[-1])
    subprocess.run(
        ["ffmpeg", "-ss", start_time, "-t", end_time, "-i", input_file, "-acodec", "copy", "-avoid_negative_ts",
         "make_zero",
         output_file])


if __name__ == '__main__':
    file_path = "/Users/zhaopeng/Personal/bilibili/jinbo/temp"
    output_path = "/Users/zhaopeng/Personal/bilibili/jinbo/cut"
    # for i in scan_dir(file_path):
    #     copy_mp3_from_mp4(os.path.join(file_path, i))
    #     # cut_audio_remove(os.path.join(file_path, i), 0, 22, output_path)
    file_name = "/Users/zhaopeng/Personal/bilibili/jinbo/temp/%s.mp3" \
                "" % "放河灯的日子"
    st = "00:00:15"
    et = "00:05:49"
    cut_audio_get(file_name, st, et, output_path)
