#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2022/11/11

from allpairspy import AllPairs
import json
import csv


def make_filter(filter_array):
    """
    filter_array: [属性id, 属性名, 数据类型, 表达式, 值]
    """
    if filter_array != []:
        var_id, var_name, var_type, filter_op, filter_values = filter_array[0], filter_array[1], filter_array[2], \
                                                               filter_array[3], filter_array[4]
        tem_filter = {
            "op": "and",
            "exprs": [
                {
                    "key": var_id,
                    "name": var_name,
                    "valueType": var_type,
                    "op": filter_op,
                    "values": [
                        filter_values
                    ]
                }
            ]
        }
        return tem_filter
    else:
        tem_filter = {
            "op": "and",
            "exprs": [

            ]
        }
        return tem_filter


def re_pairs(param):
    return_array = []
    for pairs in enumerate(AllPairs(param)):
        return_array.append(pairs[1])
        print(pairs[1])
    return return_array


def ltv_post_report(initial_array, revenue_array, time_range_and_len, target_users, global_filter):
    """

    :param initial_array: 0: 事件类型， 1：事件标识符
    :param revenue_array: 0：事件类型， 1：事件标识符， 2：度量
    :param time_range_and_len: 0：时间范围， 1：对应时间的断言
    :param target_users:： 目标用户
    :param global_filter: 全局过滤
    :return:
    """
    # initial_event_type, initial_event_key, initial_event_filter = 2, 3, 4
    # revenue_event_type, revenue_event_key, revenue_event_attributeKey, revenue_event_filter = 5, 6, 7, 8
    for i, pairs in enumerate(
            AllPairs([initial_array, revenue_array, time_range_and_len, target_users, global_filter])):
        body = {
            "name": "LTV分析" + str(i + 1),
            "initialEvent": {
                "type": pairs[0][0][0],
                "key": pairs[0][0][1],
                "filter": pairs[0][1]
            },
            "revenueEvents": [
                {
                    "metric": {
                        "alias": "接口自动化测试-LTV营收事件1",
                        "key": pairs[1][0][1],
                        "type": pairs[1][0][0],
                        "filter": pairs[1][1],
                        "attributeKey": pairs[1][0][2]
                    }
                }
            ],
            "timeRange": pairs[2][0],
            "targetUser": {
                "key": pairs[3]
            },
            "chartType": "LTV",
            "filter": pairs[4],
            "editStatus": "true"
        }
        print(json.dumps(body, ensure_ascii=False))
        with open("ltv_body.csv", "a", encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerow(["数据集-%s" % str(i + 1), json.dumps(body, ensure_ascii=False), pairs[2][1]])


def ltv_post_create():
    pass


def ltv_put_update():
    pass


if __name__ == '__main__':
    filter_values = [["b", "应用平台", "string", "=", "Web"], ["b", "应用平台", "string", "!=", "Web"],
                     ["b", "应用平台", "string", "in", "iOS", "Android"],
                     ["b", "应用平台", "string", "not in", "iOS", "Android"],
                     ["b", "应用平台", "string", "like", "iOS"], ["b", "应用平台", "string", "not like", "iOS"],
                     ["b", "应用平台", "string", "!=", " "], ["b", "应用平台", "string", "=", " "],
                     ["usr_$first_utm_campaign", "首次广告名称", "string", "=", "实用"],
                     ["usr_$first_utm_campaign", "首次广告名称", "string", "!=", "实用"],
                     ["usr_$first_utm_campaign", "首次广告名称", "string", "in", "实用", "保暖"],
                     ["usr_$first_utm_campaign", "首次广告名称", "string", "not in", "实用", "保暖"],
                     ["usr_$first_utm_campaign", "首次广告名称", "string", "like", "保暖"],
                     ["usr_$first_utm_campaign", "首次广告名称", "string", "not like", "保暖"],
                     ["usr_$first_utm_campaign", "首次广告名称", "string", "!=", " "],
                     ["usr_$first_utm_campaign", "首次广告名称", "string", "=", " "],
                     ["usr_$basic_birthday", "出生年月日", "date", "!=", "1675130471180"],
                     ["usr_$basic_birthday", "出生年月日", "date", "=", "1675130471180"],
                     ["usr_$basic_birthday", "出生年月日", "date", "<=", "1675134050711"],
                     ["usr_$basic_birthday", "出生年月日", "date", ">", "1675134050711"],
                     ["usr_$basic_birthday", "出生年月日", "date", "between", "abs:1672502400000,1675180799999"],
                     ["usr_$basic_birthday", "出生年月日", "date", "not between", "abs:1672502400000,1675180799999"],
                     ["usr_$basic_birthday", "出生年月日", "date", "relativeTime", "relativeTime:-100,0"],
                     ["usr_$basic_birthday", "出生年月日", "date", "relativeTime", "relativeTime:-100,-365"],
                     ["usr_$basic_birthday", "出生年月日", "date", "!=", " "],
                     ["usr_$basic_birthday", "出生年月日", "date", "=", " "], []]
    filter_list = []
    for i in filter_values:
        filter_list.append(make_filter(i))
    # print(filter_list)

    initial_array = [["custom", "$anyevent"]]
    revenue_array = [["custom", "$visit", "$duration"], ["custom", "$visit", "$page_count"],
                     ["custom", "$page", "$duration"]]
    time_range = ["day:8,1", "day:5,1", "day:31,1", "day:61,1", "day:91,1", "day:181,1"]
    target_users = ["uv", "nuv", "ruv"]

    # LTV分析-查询数据
    time_range_and_len = [[i, i.split(",")[0].replace("day:", "")] for i in time_range]
    with open("ltv_body.csv", "w", encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(["数据集名称", "ltv_query_body", "assert_data_len"])
    ltv_post_report(re_pairs([initial_array, filter_list]), re_pairs([revenue_array, filter_list]), time_range_and_len,
                    target_users, filter_list)
