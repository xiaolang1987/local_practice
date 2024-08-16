#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2024/8/14 11:58

import pandas as pd
import json


# 获取并整理制作材料
def read_material():
    df = pd.read_csv("raw_material.csv")

    # 获取成品列表
    finished_list = []  # 初始化成品列表
    for a, b in df.iterrows():
        finished_list.append(b["成品"])

    # 初步整理材料字典
    metadata = {}
    for a, b in df.iterrows():
        # 材料列表转成字典表
        tmp_metadata = {}
        materials = b["材料"].split("&&")
        for material in materials:
            tmp_metadata.update(json.loads(material))
        finished_name = b["成品"]
        metadata.update({finished_name: tmp_metadata})
    # print(metadata)

    # 整理原材料数据
    material_dict = {}  # 初始化材料字典表
    for a, b in df.iterrows():
        # 材料列表转成字典表
        tmp_material_dict = {}
        materials = b["材料"].split("&&")
        for material in materials:
            material_json = json.loads(material)
            material_name = [key for key, value in material_json.items()][0]  # 获取key
            material_num = [value for key, value in material_json.items()][0]  # 获取值
            # 判断是不是半成品
            if material_name in finished_list:
                half_material_json = metadata[material_name]
                half_material_key = [key for key, value in half_material_json.items()][0]  # 获取key
                half_material_num = [value for key, value in half_material_json.items()][0]  # 获取值
                material_json[half_material_key] = half_material_num * material_num
                material_json[material_name] = 0
            tmp_material_dict.update(material_json)
        finished_name = b["成品"]
        material_dict.update({finished_name: tmp_material_dict})

    return material_dict


# 获取物品等级
def get_goods_level():
    df = pd.read_csv("raw_material.csv")
    level = {}
    for a, b in df.iterrows():
        level[b["成品"]] = b["物品等级"]

    return level


# 获取拍卖价格
def get_ah():
    df = pd.read_csv("ah_now.csv")
    ah = {}
    for a, b in df.iterrows():
        ah[b["名称"]] = b["价格"]

    # 增加商人售卖的材料
    businessman = [{"粗线": 10}, {"细线": 10}, {"丝线": 10}, {"符文线": 10}, {"盐": 10}, {"灰色染料": 10}, {"黑色染料": 10}]
    for i in businessman:
        ah.update(i)

    return ah


# 计算成本
def calculate_cost(materials, ah):
    cost = {}
    for finish, i in materials.items():
        gold = 0
        for material, num in i.items():
            gold += (ah[material] * num)
        cost[finish] = gold
    return cost


# 读取分解材料
def get_output():
    df = pd.read_csv("output.csv")
    output = {}
    for a, b in df.iterrows():
        # 整理概率
        ratio = b["分解概率"].split("&&")
        temp_ratio = {}
        for i in ratio:
            for key, value in json.loads(i).items():
                temp_ratio[key] = value

        # 整合个数
        levels = b["物品等级"]
        goods = b["分解材料"].split("&&")
        output[levels] = {}
        for i in goods:
            for key, value in json.loads(i).items():
                min_num = int(value.split("-")[0])
                max_num = int(value.split("-")[1])
                output[levels][key] = {}
                output[levels][key]["min"] = min_num
                output[levels][key]["max"] = max_num
                output[levels][key]["ratio"] = temp_ratio[key]

    return output


# 获取等级区间
def get_level_section(key, level):
    min_level = key.split("-")[0]
    max_level = key.split("-")[1]
    if level >= int(min_level):
        if level <= int(max_level):
            return True
        else:
            return False
    else:
        return False


# 整理和计算分解材料的价格。分解材料价格计算：个数 = 最小个数 + 个数差值 * 0.5；价格 = 材料A * 概率 + 材料B * 概率
def calculate_output_price(goods_level):
    all_level = get_output()
    all_price = get_ah()

    for key, value in all_level.items():
        final_price = 0
        if get_level_section(key, goods_level):
            for goods, item in value.items():
                final_num = item["min"] + (item["max"] - item["min"]) * 0.5
                price = final_num * all_price[goods] * item["ratio"]
                final_price += int(price)

            return final_price


if __name__ == '__main__':
    # print(get_ah())
    # todo 根据拍卖行导出的文件，展示出当前摆放的数量
    all_goods = [key for key, value in read_material().items()]  # 所有商品列表
    all_calculate_cost = calculate_cost(read_material(), get_ah())  # 所有商品的成本列表
    for goods in all_goods:
        goods_level = get_goods_level()[goods]
        # 等级为0，暂时表示中间产物，不统计收益
        if goods_level != 0:
            output_price = calculate_output_price(goods_level)
            input_price = all_calculate_cost[goods]
            profit = output_price - input_price  # 买出的材料 - 成本
            if profit > 0:
                print(goods, profit)
            # else:
            #     print(goods, profit)
