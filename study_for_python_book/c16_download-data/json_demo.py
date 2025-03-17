from MyJsonHelper import MyJsonHelper


# step1: download json file
json_file_download_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
file_name = 'docs/btc_close_2017_urllib.json'
json_helper = MyJsonHelper(json_file_download_url, file_name)
# json_data = json_helper.download_file_v2()
# print(json_data)

# step2: fill to format
json_helper.fill_to_format_data()

# step3 draw
img_line_day = json_helper.draw_line_chart()
img_line_day_log = json_helper.draw_line_chart(True)
# 取1-11月数据，因为12月数据不完整
idx_month = json_helper.dates.index('2017-12-01')
img_line_1 = json_helper.draw_line(json_helper.months[:idx_month], json_helper.close[:idx_month], '收盘价月日均值(¥)', '月日均值')

# 周日均图
idx_week = json_helper.dates.index('2017-12-11')
# 第一天是周日，是2016年最后一周，因此去掉,从 index 1 开始截取
img_line_2 = json_helper.draw_line(json_helper.week[1:idx_week], json_helper.close[1:idx_week], '收盘价周日均图(¥)', '周日均值')

# 每周各天的均值
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [weekdays.index(w) + 1 for w in json_helper.weekdays[1:idx_week]]

img_line_3 = json_helper.draw_line(weekdays_int, json_helper.close[1:idx_week], '收盘价星期均值(¥)', '星期日均值')


# 生成一个图 dashboard.html

dash_file = 'dashboard.html'
with open(dash_file, 'w', encoding='utf-8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [img_line_day, img_line_day_log, img_line_1, img_line_2, img_line_3]:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')


print('finish!')


