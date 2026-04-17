import matplotlib.pyplot as plt
import json
import os

def percentile(data, p):
    """计算百分位数（纯Python实现）"""
    if not data:
        return None
    data_sorted = sorted(data)
    n = len(data_sorted)
    index = (p / 100) * (n - 1)
    
    if index.is_integer():
        return data_sorted[int(index)]
    else:
        lower = data_sorted[int(index)]
        upper = data_sorted[int(index) + 1]
        return lower + (upper - lower) * (index - int(index))

# 读取历史金价
with open("gold_price.json", "r", encoding="utf-8") as f:
    gold_prices = []
    for line in f:
        line = line.strip()
        if line:  # 跳过空行
            gold_prices.append(json.loads(line))

# 添加整理金价
for filename in os.listdir("his_daily/"):
    if filename.endswith('.json'):

        # 读取单个文件，获取最大值、最小值和90分位数
        with open("his_daily/%s" % filename, "r", encoding="utf-8") as f:
            p90_values = []
            for line in f:
                if line.strip():
                    data_line = json.loads(line)
                    p90_values.append(data_line['P90'])
        # 计算结果
        max_val = max(p90_values)
        p90_val = percentile(p90_values, 90)

        # 整理结果加入到数组
        get_date = int(filename.replace("his_daily_gold_price_", "").replace(".json", ""))
        new_dict = {"日期": get_date, "P90": p90_val, "max": max_val}
        
        # 添加或更新
        existing = next((item for item in gold_prices if item['日期'] == new_dict['日期']), None)
        if existing:
            existing.update(new_dict)
        else:
            gold_prices.append(new_dict)


# 保存新的数据
new_gold_prices = sorted(gold_prices, key=lambda x: x['日期'], reverse=True)
with open("gold_price.json", "w", encoding="utf-8") as f:
    for l in new_gold_prices:
        json.dump(l, f, ensure_ascii=False)
        f.write("\n")


# 准备展示趋势
sorted_data = sorted(gold_prices, key=lambda x: x['日期'])
plot_data = [f"{str(d['日期'])[:4]}/{str(d['日期'])[4:6]}/{str(d['日期'])[6:8]}" for d in sorted_data]
p90s = [d['P90'] for d in sorted_data]

plt.plot(plot_data, p90s, marker="o", label="P90")
plt.title("P90 Trend")
plt.xlabel("Date")
plt.ylabel("P90")
plt.xticks(rotation=45)


# 显示数值
for i, (x, y) in enumerate(zip(plot_data, p90s)):
    plt.text(x, y, f'{y}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

