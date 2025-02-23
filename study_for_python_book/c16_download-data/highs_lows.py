import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # 遍历每一行的index=1的数据(最高温度)
    dates = []
    highs = []
    lows = []
    for row in reader:
        cur_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(cur_date)
        highs.append(int(row[1]))
        lows.append(int(row[2]))
    print(highs) 

    # 绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')      
    plt.plot(dates, lows, c='blue')      
    # 填充两个温度之间的颜色
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
    # 设置图形的格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    # 确保x轴从最开始日期开始，防止有留白部分
    plt.xlim(min(dates), max(dates))
    # 绘制斜的日期标签
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()     


