from __future__ import (absolute_import, division, print_function, unicode_literals)
from urllib.request import urlopen
import json
import certifi
import ssl
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
file_name = 'btc_close_2017_urllib.json'

# 方式1: 使用 urlopen 下载
def download_json_file_v1(json_url, file_name):
    # create an SSL context using certifi's certificates
    context = ssl.create_default_context(cafile=certifi.where())
    response = urlopen(json_url, context=context)
    # 读取数据
    req = response.read()
    # 把数据写入文件
    with open(file_name, 'wb') as f:
        f.write(req)
    # 返回 json 数据
    return json.loads(req)  

# 方式2: 使用 requests 下载；更简单
def download_json_file_v2(json_url, file_name):
    req = requests.get(json_url)
    with open(file_name, 'w') as f:
        f.write(req.text)
    return req.json()        
  
# 下载之后就不用再调用了
# download_json = download_json_file_v2(json_url, file_name)
# print(download_json)    

# 提取数据
with open(file_name) as f:
    btc_data = json.load(f)

# print data
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])    
    week = int(btc_dict['week'])    
    weekday = btc_dict['weekday']    
    close = int(float(btc_dict['close']))    
    print("{} is month {} week {},{}, the close price is {} RMB".format(date, month, week, weekday, close))

#     

