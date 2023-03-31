#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/3/6 14:22

import requests
import json
import time
import random


def create_event():
    url = "http://qa-anl.growingio.cn/v3/graphql?op=createDataCenterCustomEvent"

    for i in range(20):
        payload = json.dumps({
            "operationName": "createDataCenterCustomEvent",
            "variables": {
                "customEvent": {
                    "attributes": [
                        {
                            "type": "EVENT_VARIABLE",
                            "id": "0wDaJYQ1"
                        }
                    ],
                    "valueType": "counter",
                    "key": "flowhouxu%s" % str(i + 1),
                    "name": "事件流后续事件%s" % str(i + 1)
                }
            },
            "query": "mutation createDataCenterCustomEvent($customEvent: CustomEventInput!) {\n  createDataCenterCustomEvent(customEvent: $customEvent) {\n    name\n    __typename\n  }\n}\n"
        })
        headers = {
            'Connection': 'keep-alive',
            'Cookie': 'gdp_user_id=9443f81e-aab4-4855-ac14-d86bb0dded2c; CDP_gdp_sequence_ids=%7B%22globalKey%22%3A8349%2C%22VISIT%22%3A6%2C%22PAGE%22%3A35%2C%22CUSTOM%22%3A8310%7D; CDP_gdp_cs1=5; CDP_gdp_gio_id=5; internal_gdp_user_key=; internal_gdp_cs1=gioenc-3; internal_gdp_gio_id=gioenc-3; growing_portal=NjYxOTkyNTUtNTFhNi00MDQxLTg5MGEtN2UxMzdmNTQ2OTI4; internal_gdp_session_id=96211367-a4af-4f62-9be5-89598ab37b11; internal_gdp_session_id_96211367-a4af-4f62-9be5-89598ab37b11=true; internal_gdp_user_key=; internal_gdp_session_id=96211367-a4af-4f62-9be5-89598ab37b11; internal_gdp_cs1=gioenc-3; internal_gdp_gio_id=gioenc-3; internal_gdp_sequence_ids={%22globalKey%22:11%2C%22VISIT%22:3%2C%22PAGE%22:9%2C%22CUSTOM%22:3}; session=.eJwdjkFqxDAMRa9ivA7Flqw4zilmX4Yg29IkNJ2UOF0Nc_earv77SEjvZRfdua3S7Pz5subqYb-lNX6IHextF25i9uNhtqe5DsOl9KG51q2Zn77zYe_v-9CPnNJWOyvvTXrdqp0tgTgS5wJpDToxA-QYOFRh9KggIRXOgFoK5uJ8AoipusK-wOQoQ_A5ReQQp1hGBIVJIRYPFBGFiHjMXjgwTJgqBRSIWCEDUdII0P2X3ybnv40fbGmnLtfxJc8uh0ky1sBKgOQ9ayeKzP0XSugMfuSgYN9_oSBVcg.ZAWjbQ.ZlJUFC04mxnED6R3CrG5FnxLNGU; internal_gdp_sequence_ids={%22globalKey%22:11%2C%22VISIT%22:3%2C%22PAGE%22:9%2C%22CUSTOM%22:4}',
            'Origin': 'http://qa-anl.growingio.cn',
            'Referer': 'http://qa-anl.growingio.cn/dc/projects/1/event/custom-events',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'X-Product-Unique-Id': 'DC',
            'X-Project-Id': '1',
            'accept': '*/*',
            'accept-language': 'zh-CN, zh-CN',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)


def shishidaoshu():
    # url = "http://106.75.103.15:8080/v3/projects/91eaf9b283361032/collect"
    url = "http://117.50.84.75:8080/v3/projects/edf08c66697d2d37/collect"
    # p = [["0", 1677902401, 1677902401, 1677902401, 1677902401, 1677902401, 1677902401, 1677902401, 1677902401],
    #      ["1", 1677902403, 1677902462, 1677906001, 1677906062, 1677909602, 1677985202, 1677992402, 1678075202],
    #      ["2", 1677902405, 1677902642, 1677906003, 1677906238, 1677913452, 1677985561, 1677996542, 1678886081],
    #      ["3", 1677902407, 1677902822, 1677906005, 1677906414, 1677917302, 1677985920, 1678000682, 1679696960],
    #      ["4", 1677902409, 1677903002, 1677906007, 1677906590, 1677921152, 1677986279, 1678004822, 1680507839],
    #      ["5", 1677902411, 1677903182, 1677906009, 1677906766, 1677925002, 1677986638, 1678008962, 1681318718],
    #      ["6", 1677902413, 1677903362, 1677906011, 1677906942, 1677928852, 1677986997, 1678013102, 1682129597],
    #      ["7", 1677902415, 1677903542, 1677906013, 1677907118, 1677932702, 1677987356, 1678017242, 1682940476],
    #      ["8", 1677902417, 1677903722, 1677906015, 1677907294, 1677936552, 1677987715, 1678021382, 1683751355],
    #      ["9", 1677902419, 1677903902, 1677906017, 1677907470, 1677940402, 1677988074, 1678025522, 1684562234],
    #      ["10", 1677902421, 1677904082, 1677906019, 1677907646, 1677944252, 1677988433, 1678029662, 1685373113],
    #      ["11", 1677902423, 1677904262, 1677906021, 1677907822, 1677948102, 1677988792, 1678033802, 1686183992],
    #      ["12", 1677902425, 1677904442, 1677906023, 1677907998, 1677951952, 1677989151, 1678037942, 1686994871],
    #      ["13", 1677902427, 1677904622, 1677906025, 1677908174, 1677955802, 1677989510, 1678042082, 1687805750],
    #      ["14", 1677902429, 1677904802, 1677906027, 1677908350, 1677959652, 1677989869, 1678046222, 1688616629],
    #      ["15", 1677902431, 1677904982, 1677906029, 1677908526, 1677963502, 1677990228, 1678050362, 1689427508],
    #      ["16", 1677902433, 1677905162, 1677906031, 1677908702, 1677967352, 1677990587, 1678054502, 1690238387],
    #      ["17", 1677902435, 1677905342, 1677906033, 1677908878, 1677971202, 1677990946, 1678058642, 1691049266],
    #      ["18", 1677902437, 1677905522, 1677906035, 1677909054, 1677975052, 1677991305, 1678062782, 1691860145],
    #      ["19", 1677902439, 1677905702, 1677906037, 1677909230, 1677978902, 1677991664, 1678066922, 1692671024],
    #      ["20", 1677902441, 1677905882, 1677906039, 1677909406, 1677982752, 1677992023, 1678071062, 1693481903]]
    p = [["0", 1678420801, 1678420801, 1678420801, 1678420801, 1678420801, 1678420801, 1678420801, 1678420801],
         ["1", 1678420803, 1678420862, 1678424401, 1678424462, 1678428002, 1678503602, 1678510802, 1678593602],
         ["2", 1678420805, 1678421042, 1678424403, 1678424638, 1678431852, 1678503961, 1678514942, 1679404481],
         ["3", 1678420807, 1678421222, 1678424405, 1678424814, 1678435702, 1678504320, 1678519082, 1680215360],
         ["4", 1678420809, 1678421402, 1678424407, 1678424990, 1678439552, 1678504679, 1678523222, 1681026239],
         ["5", 1678420811, 1678421582, 1678424409, 1678425166, 1678443402, 1678505038, 1678527362, 1681837118],
         ["6", 1678420813, 1678421762, 1678424411, 1678425342, 1678447252, 1678505397, 1678531502, 1682647997],
         ["7", 1678420815, 1678421942, 1678424413, 1678425518, 1678451102, 1678505756, 1678535642, 1683458876],
         ["8", 1678420817, 1678422122, 1678424415, 1678425694, 1678454952, 1678506115, 1678539782, 1684269755],
         ["9", 1678420819, 1678422302, 1678424417, 1678425870, 1678458802, 1678506474, 1678543922, 1685080634],
         ["10", 1678420821, 1678422482, 1678424419, 1678426046, 1678462652, 1678506833, 1678548062, 1685891513],
         ["11", 1678420823, 1678422662, 1678424421, 1678426222, 1678466502, 1678507192, 1678552202, 1686702392],
         ["12", 1678420825, 1678422842, 1678424423, 1678426398, 1678470352, 1678507551, 1678556342, 1687513271],
         ["13", 1678420827, 1678423022, 1678424425, 1678426574, 1678474202, 1678507910, 1678560482, 1688324150],
         ["14", 1678420829, 1678423202, 1678424427, 1678426750, 1678478052, 1678508269, 1678564622, 1689135029],
         ["15", 1678420831, 1678423382, 1678424429, 1678426926, 1678481902, 1678508628, 1678568762, 1689945908],
         ["16", 1678420833, 1678423562, 1678424431, 1678427102, 1678485752, 1678508987, 1678572902, 1690756787],
         ["17", 1678420835, 1678423742, 1678424433, 1678427278, 1678489602, 1678509346, 1678577042, 1691567666],
         ["18", 1678420837, 1678423922, 1678424435, 1678427454, 1678493452, 1678509705, 1678581182, 1692378545],
         ["19", 1678420839, 1678424102, 1678424437, 1678427630, 1678497302, 1678510064, 1678585322, 1693189424],
         ["20", 1678420841, 1678424282, 1678424439, 1678427806, 1678501152, 1678510423, 1678589462, 1694000303]]
    for i in p:
        print(i)
        userid = 0
        for timestamp in i[1:]:
            userid += 1
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)), userid)
            payload = json.dumps([
                {
                    "deviceId": "deviceid%s" % str(userid),
                    "userId": "fl1%s" % str(userid),
                    "sessionId": "sessionid%s" % str(userid),
                    "eventType": "PAGE",
                    "sendTime": timestamp * 1000,
                    "timestamp": timestamp * 1000,
                    "dataSourceId": "92ceb8f57d860d68",
                    "domain": "analysisWeChat1",
                    "urlScheme": "analysisWeChat1",
                    "appState": "FOREGROUND",
                    "globalSequenceId": 99,
                    "eventSequenceId": 3,
                    "path": "/b/page%s" % i[0],
                    "orientation": "PORTRAIT",
                    "title": "页面%s" % str(random.randint(1, 4)),
                    "networkState": "4G",
                    "appChannel": "微信小程序",
                    "screenHeight": 1920,
                    "screenWidth": 1080,
                    "deviceBrand": "google",
                    "deviceModel": "Nexus %s" % str(userid),
                    "deviceType": "PHONE",
                    "platform": "Android",
                    "platformVersion": "7.1.2",
                    "appName": "222看数小助手",
                    "appVersion": "1.2.4",
                    "language": "zh_CN",
                    "latitude": 39.988518,
                    "longitude": 116.478797,
                    "sdkVersion": "3.3.6"
                }
            ])
            headers = {
                'Content-Type': 'application/json'
            }

            requests.request("POST", url, headers=headers, data=payload)
            # time.sleep(0.05)
            # print(response.text)


if __name__ == '__main__':
    # create_event()
    shishidaoshu()
