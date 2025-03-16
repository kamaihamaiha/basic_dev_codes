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
# json_helper.draw_line_chart(True)
# 取1-11月数据，因为12月数据不完整
# idx_month = json_helper.dates.index('2017-12-01')
# json_helper.draw_line(json_helper.months[:idx_month], json_helper.close[:idx_month], '收盘价月日均值(¥)', '月日均值')

# 周日均图
idx_week = json_helper.dates.index('2017-12-11')
# 第一天是周日，是2016年最后一周，因此去掉,从 index 1 开始截取
json_helper.draw_line(json_helper.week[1:idx_week], json_helper.close[1:idx_week], '收盘价周日均图(¥)', '周日均值')
print('finish!')


