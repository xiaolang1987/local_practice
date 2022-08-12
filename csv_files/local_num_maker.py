#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2022/8/11 23:08

import random
import csv


def maker_str(base_str, many: int):
    """
    生成字符串列表
    :param base_str: 前置字符
    :param many: 要生成字符串的个数
    :return: list
    """
    list_str = []
    for i in range(many):
        list_str.append(base_str+str(random.randint(1, many)))
    return list_str


def maker_int(many: int):
    """
    生成整数列表
    :param many:
    :return:
    """
    base_int = [1, 5, 10, 333, 6666, 99999, 299998]
    list_int = []
    for i in range(many):
        list_int.append(random.choice(base_int))
    return list_int


def maker_float(many: int):
    """
    生成小数列表
    :param many:
    :return:
    """
    base_float = [0.0001, 0.05, 0.04, 3.33, 0, 1, 10086.005]
    list_float = []
    for i in range(many):
        list_float.append(random.choice(base_float))
    return list_float


def maker_date(many: int):
    """
    生成日期列表
    :param many:
    :return:
    """
    base_date = ["0000-01-01", "1977-02-02", "2021-03-03", "2022-04-04", "2030-05-05", "2022-02-31"]
    list_date = []
    for i in range(many):
        list_date.append(random.choice(base_date))
    return list_date


def maker_user(base_user, many: int):
    """
        生成用户列表
        :param base_user: 前置字符
        :param many: 要生成字符串的个数
        :return: list
        """
    list_user = []
    for i in range(many):
        list_user.append(base_user + str(i+1).zfill(4))
    return list_user


def integrated_data():
    user_list = maker_user("analysis_", 20)
    str_list = maker_str("abv", 6)
    int_list = maker_int(6)
    for i in range(len(user_list)):
        with open("new_data.csv", "a+") as csvfile:
            writer = csv.writer(csvfile)
            print(user_list[i])
            writer.writerow([user_list[i], "event", "time", random.choice(str_list), random.choice(int_list)])


if __name__ == "__main__":
    # print(maker_user("analysis_", 5))
    integrated_data()
