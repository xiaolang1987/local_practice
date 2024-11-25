1. 读取专业文件计算制作成本
2. 读取AH单价
   1. 读取ah_now文件
   2. 根据标签整理各类列表的物品，生成历史导入文件
   3. 根据价格存储历史价格
3. 计算收益


```
ah_now.csv  # 当前拍卖行价格
output.csv  # 附魔材料产出
raw_material.csv  # 制作材料表
item_list.csv  # 物品列表
test.py  # 计算收益
ah_import_file.txt  # 拍卖行导入文件
```
4. 统计历史价格