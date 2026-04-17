#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import time
import os


def get_page_content_from_dd373(page):
    """
    获取dd373页面数据
    """
    url = "https://www.dd373.com/s-aj0khw-0-axtk9f-pedqjd-0-0-tf85vg-0-0-recycle-0-0-%s-0-0-0.html" % page
    response = requests.get(url)
    
    return response.content


def get_total_item(html_content):
    """
    解析魔兽世界时光服游戏币交易数据
    返回总记录数
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 提取总记录数 "为您找到 条记录"
    pagination = soup.find('div', class_='footer-pagination')
    if pagination:
        total_span = pagination.find('span', class_='font12 colorFF5')
        if total_span and total_span.get_text(strip=True).isdigit():
            return int(total_span.get_text(strip=True))



def parse_trading_data(html_content):
    """
    提取单价、收货数量、交易均时、成交率
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    data_list = []
    prices = []

    for ul in soup.select('.platform-receive-content ul'):
        # 提取单价 (从 "0.0235元/金" 中提取)
        price_text = ul.select_one('.width198 .color666')
        if price_text:
            price_match = re.search(r'([\d.]+)元/金', price_text.text)
            if price_match:
                price = float(price_match.group(1))
                prices.append(price)
            else:
                price = None
        else:
            price = None
        
        # 提取收货数量
        quantity_text = ul.select_one('.width185 .colorFF5')
        quantity = quantity_text.text.strip() + '金' if quantity_text else None
        
        # 提取交易均时
        time_text = ul.select_one('.line-height14 .colorFF5')
        time_str = time_text.text.strip() if time_text else None
        
        # 提取成交率
        rate_text = ul.select('.line-height14 .colorFF5')[-1] if len(ul.select('.line-height14 .colorFF5')) >= 2 else None
        rate = rate_text.text.strip() if rate_text else None
        
        if price:
            data_list.append({
                '单价': price,
                '收货数量': quantity,
                '交易均时': time_str,
                '成交率': rate
            })
    
    return data_list


def get_90(content):
    prices = []
    for item in content:
        prices.append(item["单价"])
    prices_sorted = sorted(prices)
    index = int(len(prices_sorted) * 0.9)
    percentile_90 = prices_sorted[index] if index < len(prices_sorted) else prices_sorted[-1]

    return percentile_90



if __name__ == "__main__":
    # 单次获取金价
    page = 1
    content = []

    while True:
        page_content = get_page_content_from_dd373(page)
        result = parse_trading_data(page_content)
        content = content + result
        if len(result) > 0:
            page += 1
        else:
            break

    p_90 = get_90(content)

    line_content = {"time": time.strftime("%H:%M"), "P90": p_90, "count": len(content),"content": content}
    with open(time.strftime("his_daily/his_daily_gold_price_%Y%m%d.json"), "a", encoding="utf-8") as f:
        json.dump(line_content, f, ensure_ascii=False)
        f.write("\n")

    print("获取完毕%s" % line_content)