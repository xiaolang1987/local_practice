#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/3/22 11:06

import requests
import json

url = "http://op211.growingio.cn/v3/graphql?op=createDashboard"
num = 1
for i in range(30):
    num += 1

    payload = json.dumps([
        {
            "operationName": "createDashboard",
            "variables": {
                "dashboard": {
                    "name": "多多(%s)" % num,
                    "components": [
                        {
                            "resourceType": "kpiAnalysis",
                            "resourceId": "rRGoYQml",
                            "layout": {
                                "x": 0,
                                "y": 0,
                                "w": 1,
                                "h": 6,
                                "minH": None,
                                "minW": 1,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "kpiAnalysis",
                            "resourceId": "ExQWOQ79",
                            "layout": {
                                "x": 1,
                                "y": 0,
                                "w": 1,
                                "h": 6,
                                "minH": None,
                                "minW": 1,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "eventAnalysis",
                            "resourceId": "ExQWOQ79",
                            "layout": {
                                "x": 2,
                                "y": 0,
                                "w": 2,
                                "h": 6,
                                "minH": None,
                                "minW": 2,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "eventAnalysis",
                            "resourceId": "AbQ3bDYe",
                            "layout": {
                                "x": 0,
                                "y": 6,
                                "w": 2,
                                "h": 6,
                                "minH": None,
                                "minW": 2,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "funnelAnalysis",
                            "resourceId": "rRGoYQml",
                            "layout": {
                                "x": 2,
                                "y": 6,
                                "w": 2,
                                "h": 6,
                                "minH": None,
                                "minW": 2,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "flowAnalysis",
                            "resourceId": "n1QVaDyR",
                            "layout": {
                                "x": 0,
                                "y": 12,
                                "w": 2,
                                "h": 6,
                                "minH": None,
                                "minW": 2,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "flowAnalysis",
                            "resourceId": "rRGoYQml",
                            "layout": {
                                "x": 2,
                                "y": 12,
                                "w": 2,
                                "h": 6,
                                "minH": None,
                                "minW": 2,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "retentionAnalysis",
                            "resourceId": "WlGk4Daj",
                            "layout": {
                                "x": 0,
                                "y": 18,
                                "w": 2,
                                "h": 6,
                                "minH": None,
                                "minW": 2,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "frequencyAnalysis",
                            "resourceId": "y9pm1pme",
                            "layout": {
                                "x": 2,
                                "y": 18,
                                "w": 2,
                                "h": 6,
                                "minH": None,
                                "minW": 2,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        },
                        {
                            "resourceType": "attributionAnalysis",
                            "resourceId": "WlGk4Daj",
                            "layout": {
                                "x": 0,
                                "y": 24,
                                "w": 2,
                                "h": 6,
                                "minH": None,
                                "minW": 2,
                                "moved": False,
                                "static": False,
                                "isDraggable": True,
                                "isResizable": True
                            }
                        }
                    ],
                    "filter": {
                        "op": "and",
                        "exprs": []
                    }
                },
                "projectId": "WlGk4Daj"
            },
            "query": "mutation createDashboard($dashboard: DashboardInput!, $projectId: HashId!) {\n  createDashboard(dashboard: $dashboard, projectId: $projectId) {\n    id\n    name\n    description\n    components {\n      resourceType\n      resourceId\n      layout {\n        x\n        y\n        w\n        h\n        minH\n        minW\n        moved\n        static\n        isDraggable\n        isResizable\n        __typename\n      }\n      __typename\n    }\n    creatorId\n    creator\n    editors {\n      id\n      name\n      email\n      __typename\n    }\n    readers {\n      id\n      name\n      email\n      __typename\n    }\n    createdAt\n    updatedAt\n    __typename\n  }\n}\n"
        }
    ])
    headers = {
        'Connection': 'keep-alive',
        'Cookie': 'gdp_user_id=9443f81e-aab4-4855-ac14-d86bb0dded2c; CDP_gdp_cs1=5; CDP_gdp_gio_id=5; internal_gdp_user_key=; internal_gdp_sequence_ids={%22globalKey%22:11%2C%22VISIT%22:3%2C%22PAGE%22:8%2C%22CUSTOM%22:3}; session=.eJwdjsFqwzAQRH9F6ByKtKu1pHxF7iWY1WoVm7pxsdxTyL9X9DQM8xjey85t475ot9fPlzXnCPutvfND7cXeNuWuZtsfZn2aczcsMkZzLms3P4P5sPf3_TJODu2LvTbeuo66Vnu1BOpInQvUamiJGaDEwKEqo8cGGrJwAWwiWMT5DBBzdcJeIDkqEHzJETnEFGVCaJAaRPFAEVGJiKfilQNDwlwpoELECgWIcosAw3_-7Xr82_iLlX60-dy_9DnkJMXmYUrRTZySIDEzhVSzdz4mVmicfc7Jvv8AkelU-g.ZBp1UQ.pGUna5u367iO9IA3_3-IbllWfqQ; growing_iam=M2I4YWIzYmItNDcyNS00ZjU5LWI3M2UtZmRjZGY0YjBmNzQ3; internal_gdp_session_id=446b0154-0078-487f-a539-9297f369b4ff; internal_gdp_cs1=5; internal_gdp_gio_id=5; internal_gdp_sequence_ids=%7B%22globalKey%22%3A12%2C%22VISIT%22%3A2%2C%22PAGE%22%3A10%2C%22CUSTOM%22%3A2%7D; internal_gdp_session_id_446b0154-0078-487f-a539-9297f369b4ff=true',
        'Origin': 'http://op211.growingio.cn',
        'Referer': 'http://op211.growingio.cn/projects/WlGk4Daj/dashboards/o8D03G7P',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'accept': '*/*',
        'accept-language': 'zh-CN',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
