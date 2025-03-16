from __future__ import (absolute_import, division, print_function, unicode_literals)
import json
import certifi
import ssl
import requests
from urllib.request import urlopen
import pygal
import math
from itertools import groupby

class MyJsonHelper():
    """downlaod & parse json data"""
    def __init__(self, download_url, local_save_path):
        self.download_url = download_url
        self.local_save_path = local_save_path

        self.dates = []
        self.months = []
        self.week = []
        self.weekdays = []
        self.close = []

    def download_file_v1(self):
        ctx = ssl.create_default_context(cafile=certifi.where())
        reponse = urlopen(self.download_url, context=ctx)
        read_data = reponse.read()
        # 把数据写在文件中
        with open(self.local_save_path, 'wb') as f:
            f.write(read_data)
        # 返回保数据
        return json.loads(read_data)    

    def download_file_v2(self):
        req = requests.get(self.download_url)
        with open(self.local_save_path, 'w') as f:
            f.write(req.text)
        return req.json()            

    def get_json_data(self):
        with open(self.local_save_path) as f:
            json_data = json.load(f)
        return json_data   

    def print_info_peer_day(self, json_data):
        for btc_dict in json_data:
            date = btc_dict['date']
            month = int(btc_dict['month'])
            week = int(btc_dict['week'])
            weekday = btc_dict['weekday']
            close = int(float(btc_dict['close']))
            info = "{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close)
            print(info)

    def fill_to_format_data(self):
        original_data = self.get_json_data()
        for bean in original_data:
            self.dates.append(bean['date'])
            self.months.append(int(bean['month']))
            self.week.append(int(bean['week']))
            self.weekdays.append(bean['weekday'])
            self.close.append(int(float(bean['close'])))

    def draw_line_chart(self, convert_log = False):
        line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
        line_chart.title = '收盘价(¥)'
        line_chart.x_labels = self.dates
        N = 20 # x轴坐标每隔20天显示一次
        line_chart.x_labels_major = self.dates[::N]
        cur_close = [math.log10(_) for _ in self.close] if convert_log  else self.close
        title = "收盘价对数变化" if convert_log else '收盘价'
        line_chart.add(title, cur_close) 
        line_chart.render_to_file('docs/close_line_chart.svg')

    def draw_line(self, x_data, y_data, title, y_legend):
        xy_map = []
        for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):
            y_list= [v for _,v in y]    
            xy_map.append([x, sum(y_list) / len(y_list)])

        x_group,y_mean = [*zip(*xy_map)]
        line_chart = pygal.Line()
        line_chart.title = title
        line_chart.x_labels = x_group
        line_chart.add(y_legend, y_mean)
        line_chart.render_to_file('docs/' + title +'.svg')
        return line_chart                