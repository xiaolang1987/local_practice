#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/3/16 19:50

from allpairspy import AllPairs
import json


# 批量生成过滤条件组合，filter_array: [属性id, 属性名, 数据类型, 表达式, 值]
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


# 正则组合参数
def re_pairs(param):
    return_array = []
    for pairs in enumerate(AllPairs(param)):
        return_array.append(pairs[1])
        # print(pairs[1])
    return return_array


# 单图增删改查
def ltv_crdu(initial_array, revenue_array, time_range_and_len, target_users, global_filter):
    """

    :param initial_array: 0: 事件类型， 1：事件标识符
    :param revenue_array: 0：事件类型， 1：事件标识符， 2：度量
    :param time_range_and_len: 0：时间范围， 1：对应时间的断言
    :param target_users: 目标用户
    :param global_filter: 全局过滤
    :return: [[body_create, assert_new_name, assert_update_name], []]
    """
    crud_list = []
    for i, pairs in enumerate(
            AllPairs([initial_array, revenue_array, time_range_and_len, target_users, global_filter])):
        rule = "%s+%s%s" % (pairs[0][0][1], pairs[1][0][1], pairs[1][0][2])
        body_create = {
            "name": rule,
            "initialEvent": {
                "type": pairs[0][0][0],
                "key": pairs[0][0][1],
                "filter": pairs[0][1]
            },
            "revenueEvents": [
                {
                    "metric": {
                        "alias": "访问退出的分析组全局虚拟属性-float",
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
            "filter": pairs[4],
            "chartType": "LTV"
        }
        # print("查询LTV分析数据%s" % json.dumps(body_create, ensure_ascii=False))
        crud_list.append([body_create, rule, "更新LTV分析"])
    return crud_list


if __name__ == '__main__':
    # 参数整理
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
    initial_array = [["custom", "$anyevent"]]
    revenue_array = [["custom", "$visit", "$duration"], ["custom", "$visit", "$page_count"],
                     ["custom", "$page", "$duration"]]
    time_range = ["day:8,1", "day:5,1", "day:31,1", "day:61,1", "day:91,1", "day:181,1"]
    target_users = ["uv", "nuv", "ruv"]
    time_range_and_len = [[i, i.split(",")[0].replace("day:", "")] for i in time_range]

    # 生成增删改查的用例参数（body和断言）并组成用例 [[step1, step2, step3], []]
    crdu_parameter_list = ltv_crdu(re_pairs([initial_array, filter_list]), re_pairs([revenue_array, filter_list]),
                                   time_range_and_len,
                                   target_users,
                                   filter_list)  # [[body_create, assert_new_name, assert_update_name], []]

    # 读取apifox的用例模版，测试用例 $.apiTestCaseCollection[目录][子目录]
    with open("apifox_template_LTV.json", "r") as af:
        template_content = json.load(af)
    crdu_cases_list = template_content["apiTestCaseCollection"][1]["children"][0]["items"]
    print("已有%s个用例" % len(crdu_cases_list))
    case_id = len(crdu_cases_list)*10

    for parameter in crdu_parameter_list[:10]:
        case_id += 10
        # 读取用例模版
        with open("LTV_case_template.json", "r") as lf:
            curd_case_content = json.load(lf)[0]["content"][0]
            curd_case_content["name"] = "LTV-创建&打开&更新&删除单图-%s" % parameter[1]  # 用例名字
            curd_case_content["ordering"] = case_id
            steps = curd_case_content["steps"]  # 0是增删改查的步骤
        # 接口id对照
        for i in range(len(steps)):
            step_id = int("19"+str(int(case_id/10)).zfill(4)+str(99-i))
            print(step_id)

            if i == 0:  # 创建LTV分析
                steps[i]["httpApiCase"]["postProcessors"][0]["data"]["value"] = parameter[1]  # 断言新建的单图名字
                # steps[i]["httpApiCase"]["id"] = int("19"+str(int(case_id/10)).zfill(4)+str(99-i))  # 步骤id，唯一、倒序
                steps[i]["httpApiCase"]["name"] = "LTV-创建单图-%s" % parameter[1]  # 步骤名字
                steps[i]["httpApiCase"]["requestBody"]["data"] = json.dumps(parameter[0], ensure_ascii=False)  # 请求body

            elif i == 1:  # 获取LTV分析详情
                steps[i]["httpApiCase"]["postProcessors"][0]["data"]["value"] = parameter[1]  # 断言新建的单图名字
                # steps[i]["httpApiCase"]["id"] = int("19"+str(int(case_id/10)).zfill(4)+str(99-i))  # 步骤id，唯一、倒序
                steps[i]["httpApiCase"]["name"] = "LTV-打开单图-%s" % parameter[1]  # 步骤名字

            elif i == 2:  # 更新LTV分析，body固定
                steps[i]["httpApiCase"]["postProcessors"][0]["data"]["value"] = parameter[2]  # 断言更新的单图名字
                # steps[i]["httpApiCase"]["id"] = int("19"+str(int(case_id/10)).zfill(4)+str(99-i))  # 步骤id，唯一、倒序
                steps[i]["httpApiCase"]["name"] = "LTV-更新单图-%s" % parameter[1]  # 步骤名字

            elif i == 3:  # 获取LTV分析详情
                steps[i]["httpApiCase"]["postProcessors"][0]["data"]["value"] = parameter[2]  # 断言更新的单图名字
                # steps[i]["httpApiCase"]["id"] = int("19"+str(int(case_id/10)).zfill(4)+str(99-i))  # 步骤id，唯一、倒序
                steps[i]["httpApiCase"]["name"] = "LTV-打开单图-%s" % parameter[1]  # 步骤名字

            elif i == 4:  # 获取LTV分析详情
                steps[i]["httpApiCase"]["id"] = int("19"+str(int(case_id/10)).zfill(4)+str(99-i))  # 步骤id，唯一、倒序
                steps[i]["httpApiCase"]["name"] = "LTV-删除单图-%s" % parameter[1]  # 步骤名字
        crdu_cases_list.append(curd_case_content)
    # print(json.dumps(crdu_cases_list, ensure_ascii=False))

    # 写入
    with open("a.json", "w", encoding="utf-8") as file:
        json.dump(template_content, file, indent=4, ensure_ascii=False)

    # 插入用例
    # for case in cases:
    #     case_folder = case["name"]
    #     # 找到对应用例目录
    #     if case_folder == "LTV-创建&打开&更新&删除单图":
    #         print("用例列表 %s" % json.dumps(case["items"], ensure_ascii=False))
    #         # 实验
    #         for i in range(5):
    #             case["items"].append({"case": i, "steps": [i]})
    # 需要改动的字段
    # case_list.clear()
    # print(case_list)
    #
    # 获取步骤并替换对应的字段（body）
    # steps = case["items"]
    # elif case_folder == "LTV-查询数据":
    #     print(json.dumps(case, ensure_ascii=False))
    # elif case_folder == "LTV-获取LTV分析列表":
    #     print(json.dumps(case, ensure_ascii=False))
    # print(json.dumps(content, ensure_ascii=False))
