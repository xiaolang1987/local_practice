#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author: zhaopeng
# @time: 2023/1/17 13:57

"""
{
    "name":"test_ltv",	// 单图名字
    "initialEvent":{	// 起始事件
        "type":"custom",
        "key":"$anyevent"
    },
    "revenueEvents":[	// 营收事件
        {
            "metric":{
                "alias":"访问的页面浏览数目",
                "id":"rRGoYQml",
                "key":"$visit",
                "type":"custom",
                "attributeKey":"$page_count"
            }
        }
    ],
    "timeRange":"day:8,1",	// 时间范围
    "targetUser":{
        "key":"uv"
    },
    "chartType":"LTV"
}
"""
