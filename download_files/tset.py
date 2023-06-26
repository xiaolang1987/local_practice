#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/6/19 19:42

import json
import os

baseUrl = input("输入域名或ip：")

if baseUrl.split("://")[0] in "https:":
    host = baseUrl.split("://")[1]
    print(host.split("."))
else:
    host = baseUrl.split("://")[0]

with open("uba_api_p0_cases.json", "r",
          encoding="utf-8") as f:
    content = f.read().replace("[\"uat-cloud\",\"startdt\",\"com\"]", str(host.split(".")).replace("'", "\"")).replace(
        "uat-cloud.startdt.com", host)

with open("uba_api_p0_cases.json", "w",
          encoding="utf-8") as f:
    tmp_json = json.loads(content)
    j = 0
    for i in tmp_json["environment"]["variable"]["values"]:
        if i["key"] == "token":
            tmp_json["environment"]["variable"]["values"][j]["value"] = input("输入token：")
        elif i["key"] == "spaceId":
            tmp_json["environment"]["variable"]["values"][j]["value"] = input("输入spaceId：")
        elif i["key"] == "projectId":
            tmp_json["environment"]["variable"]["values"][j]["value"] = input("输入projectId：")
        j += 1
    json.dump(tmp_json, f, ensure_ascii=False, indent=2)

os.system("npx apifox run uba_api_p0_cases.json -r cli,html --verbose")
