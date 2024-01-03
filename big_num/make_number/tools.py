#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/12/27 16:54


def read_all_txt():
    # 去读所有数据类型的值
    with open("./list_date.csv", "r") as datef:
        list_date = datef.readline()

    with open("list_float.csv", "r") as floatf:
        list_float = floatf.readline()

    with open("list_int.csv", "r") as intf:
        list_int = intf.readline()

    with open("list_list.csv", "r") as listf:
        list_list = listf.readline()

    with open("list_string.csv", "r") as strf:
        list_string = strf.readlines()

    return {"date": list_date, "list_float": list_float, "list_int": list_int, "list_list": list_list,
            "list_string": list_string}


if __name__ == '__main__':
    print(read_all_txt())
