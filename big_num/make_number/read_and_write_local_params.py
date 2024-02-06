#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2024/2/6 22:14

import yaml


# 读取YAML文件
def read_yaml(file_name):
    with open(file_name, 'r') as file:
        return yaml.safe_load(file)


# 写入YAML文件
def write_yaml(data, file_name):
    with open(file_name, 'w') as file:
        yaml.safe_dump(data, file)


# 给YAML增加参数
def add_info_to_yaml(env, key, value, file_name):
    tmp_content = read_yaml(file_name)
    tmp_content[env]["params"][key] = value
    write_yaml(tmp_content, file_name)


if __name__ == '__main__':
    # write_yaml(a, "param_template.yml")
    add_info_to_yaml("qa-anl", "test001", "test001", "param_template.yml")
