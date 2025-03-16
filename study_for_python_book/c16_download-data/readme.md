## 下载数据

处理2种常见的数据: CSV, JSON

### CSV文件格式

如，下面的天气数据:
```
2014-1-5,61,44,26,18,7
```
- 这个项目使用过的天气数据从 http://www.wunderground.com/history 下载

### csv文件转换 列为行

- 用到 pandas 库
- 安装: `python3 -m pip install pandas --trusted-host mirrors.aliyun.com`
- 注意，如果是在虚拟环境运行代码，则需要在 terminal 先激活虚拟环境: `source /Users/kk/myenv/bin/activate`

### JSON格式

- 制作交易收盘价走势图
- 先用代码下载数据: btc_close_2017.py
- 用 Pygal 绘制折线图(line chart)