import csv
import os
from datetime import datetime
from matplotlib import pyplot as plt

# change work dir
os.chdir('practice')
file_name = "cn_pop_last74_format.csv"
with open(file_name) as f:
    reader = csv.reader(f)

    years = []
    pop_toal = []
    pop_citizen = []
    pop_country = []

    row_index = 0
    skip_title = True

    next(reader) # 跳过第一个title
    for row in reader:
        year = datetime.strptime(row[0][:-1], '%Y').year
        citizen = int(row[1])
        country = int(row[2])
        total = int(row[3])
        years.append(year)
        pop_toal.append(total)
        pop_citizen.append(citizen)
        pop_country.append(country)

# 按照时间正序
years.reverse()
pop_toal.reverse()
pop_citizen.reverse()
pop_country.reverse()

# draw 
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(years, pop_toal, c='black')
plt.plot(years, pop_citizen, c='red')
plt.plot(years, pop_country, c='green')
plt.title("china last 74 year population")
plt.xlabel('', fontsize=16)
plt.xlim(min(years), max(years))
fig.autofmt_xdate()
plt.ylabel('population', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.xticks(years[::5]) 
plt.show()

                 
