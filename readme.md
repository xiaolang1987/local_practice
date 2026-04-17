
## 虚拟环境创建和操作

### 创建虚拟环境
```
python3 -m venv .venv
```

### 激活虚拟环境

```
# mac/linux
source .venv/bin/activate

# win
.venv\Scripts\activate
```

### 管理
```
pip3 install <包名>
pip3 freeze > requirements.txt
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 退出
```
deactivate
```
