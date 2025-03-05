import csv
from datetime import datetime
from matplotlib import pyplot as plt

class Populations():
    def __init__(self, file_name):
        with open(file_name) as f:
            reader = csv.reader(f)

            self.years = []
            self.totals = []
            self.citizens = []
            self.countries = []

            # 跳过title
            next(reader)

            year_column_index = 0
            country_column_index = 1
            citizen_column_index = 2
            total_column_index = 3
            for row in reader:
                year = datetime.strptime(row[year_column_index][:-1], '%Y').year # [:-1]去掉最后一个汉字
                citizen = int(row[citizen_column_index])
                country = int(row[country_column_index])
                total = int(row[total_column_index])

                self.years.append(year)
                self.totals.append(total)
                self.citizens.append(citizen)
                self.countries.append(country)

            # 按照时间正序
            self.years.reverse()                
            self.totals.reverse()                
            self.citizens.reverse()                
            self.countries.reverse()   


    def draw_figure(self):
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(self.years, self.totals, c='black')
        plt.plot(self.years, self.citizens, c='green')
        plt.plot(self.years, self.countries, c='red')
        plt.title('china last 74 year population')
        plt.xlim(min(self.years), max(self.years))
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel('population', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.xticks(self.years[::5]) #每5年一个
        plt.show()