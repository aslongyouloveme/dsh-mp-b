#!/usr/bin/env python3
"""一个只使用 Python 标准库的命令行问候 demo。"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="简单的命令行问候 demo")
    parser.add_argument("--name", default="世界", help="要问候的名字（默认：世界）")
    args = parser.parse_args()
    print(f"你好，{args.name}！这是项目 B 的脚本 demo。")


if __name__ == "__main__":
    main()
