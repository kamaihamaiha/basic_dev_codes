import csv
from datetime import datetime
from matplotlib import pyplot as plt

class PopulationsWithAge():
    def __init__(self, file_name):
        with open(file_name) as f:
            reader = csv.reader(f)

            self.years = []
            self.youngs = []
            self.middles = []
            self.olders = []
            self.totals = []

            # 跳过title
            next(reader)

            year_column_index = 0
            young_column_index = 1
            middle_column_index = 2
            older_column_index = 3
            total_column_index = 4
            for row in reader:
                year = datetime.strptime(row[year_column_index][:-1], '%Y').year # [:-1]去掉最后一个汉字
                young = int(row[young_column_index])
                middle = int(row[middle_column_index])
                older = int(row[older_column_index])
                total = int(row[total_column_index])

                self.years.append(year)
                self.totals.append(total)
                self.youngs.append(young)
                self.middles.append(middle)
                self.olders.append(older)

            # 按照时间正序
            self.years.reverse()                
            self.totals.reverse()                
            self.youngs.reverse()                
            self.middles.reverse()                
            self.olders.reverse()                


    def draw_figure(self):
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(self.years, self.totals, c='gray')
        plt.plot(self.years, self.youngs, c='green')
        plt.plot(self.years, self.middles, c='blue')
        plt.plot(self.years, self.olders, c='black')
        plt.title('china past 34 year populations of different age groups')
        plt.xlim(min(self.years), max(self.years))
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel('population', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.xticks(self.years[::4]) #每4年一个
        plt.show()