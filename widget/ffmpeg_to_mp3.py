#!/usr/bin/env python3
"""
批量将目录下所有 mp4 转换为 mp3。
优先直接转 mp3；如果失败，则先转 m4a 再转 mp3。
依赖：系统中已安装 ffmpeg（命令行可调用）。
兼容 macOS / Linux / Windows。
"""

import os
import sys
from pathlib import Path
import subprocess


def run_ffmpeg(args: list[str]) -> bool:
    """执行 ffmpeg 命令，stdout/stderr 直接继承终端，实时显示 ffmpeg 原始输出。"""
    try:
        result = subprocess.run(args, check=False)  # 不捕获 → 直接显示到终端
        return result.returncode == 0
    except FileNotFoundError:
        print("错误：未找到 ffmpeg，请先安装并确保在 PATH 中。")
        sys.exit(1)
    except Exception as e:
        print(f"  [异常] {e}")
        return False


def mp4_to_mp3_direct(mp4: Path, mp3: Path) -> bool:
    """直接 mp4 -> mp3"""
    print("  尝试直接转换为 mp3 ...")
    cmd = [
        "ffmpeg", "-y", "-hide_banner",
        "-i", str(mp4),
        "-vn",              # 去掉视频
        "-acodec", "libmp3lame",
        "-q:a", "2",        # 音质（0~9，越小越好）
        str(mp3),
    ]
    return run_ffmpeg(cmd)


def mp4_to_m4a(mp4: Path, m4a: Path) -> bool:
    """mp4 -> m4a（提取音轨，不重新编码）"""
    print("  尝试提取音轨为 m4a ...")
    cmd = [
        "ffmpeg", "-y", "-hide_banner",
        "-i", str(mp4),
        "-vn",
        "-acodec", "copy",  # 直接复制音频流，速度快
        str(m4a),
    ]
    return run_ffmpeg(cmd)


def m4a_to_mp3(m4a: Path, mp3: Path) -> bool:
    """m4a -> mp3"""
    print("  尝试将 m4a 转为 mp3 ...")
    cmd = [
        "ffmpeg", "-y", "-hide_banner",
        "-i", str(m4a),
        "-acodec", "libmp3lame",
        "-q:a", "2",
        str(mp3),
    ]
    return run_ffmpeg(cmd)


def convert_one(mp4: Path) -> bool:
    """转换单个文件，返回是否成功。"""
    mp3 = mp4.with_suffix(".mp3")
    if mp3.exists():
        print(f"跳过（mp3 已存在）：{mp3.name}")
        return True

    print(f"\n处理：{mp4}")

    # 1) 直接转 mp3
    if mp4_to_mp3_direct(mp4, mp3) and mp3.exists() and mp3.stat().st_size > 0:
        print(f"  ✓ 直接转换成功：{mp3.name}")
        return True

    # 清理可能生成的空文件
    if mp3.exists():
        mp3.unlink()

    # 2) 先转 m4a，再转 mp3
    m4a = mp4.with_suffix(".m4a")
    if mp4_to_m4a(mp4, m4a) and m4a.exists() and m4a.stat().st_size > 0:
        if m4a_to_mp3(m4a, mp3) and mp3.exists() and mp3.stat().st_size > 0:
            print(f"  ✓ 经 m4a 转换成功：{mp3.name}")
            m4a.unlink(missing_ok=True)  # 删除中间文件
            return True
        else:
            print("  ✗ m4a 转 mp3 失败")
            return False
    else:
        print("  ✗ 提取 m4a 失败")
        return False


def main():
    # 目录：默认当前目录，可通过命令行参数指定
    target_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    if not target_dir.is_dir():
        print(f"错误：{target_dir} 不是有效目录")
        sys.exit(1)

    # 递归查找所有 .mp4（不区分大小写）
    mp4_files = sorted(
        p for p in target_dir.rglob("*")
        if p.is_file() and p.suffix.lower() == ".mp4"
    )

    if not mp4_files:
        print(f"在 {target_dir} 下未找到 mp4 文件。")
        return

    print(f"找到 {len(mp4_files)} 个 mp4 文件。")

    ok, fail = 0, 0
    for mp4 in mp4_files:
        try:
            if convert_one(mp4):
                ok += 1
            else:
                fail += 1
        except Exception as e:
            print(f"  [异常] {e}")
            fail += 1

    print(f"\n完成：成功 {ok} 个，失败 {fail} 个。")


if __name__ == "__main__":
    main()