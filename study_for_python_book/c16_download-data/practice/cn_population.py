import csv
import os
from datetime import datetime
from matplotlib import pyplot as plt

# change work dir
os.chdir('practice')
file_name = "cn_population.csv"
with open(file_name) as f:
    reader = csv.reader(f)

    years = []
    populations = []

    row_index = 0
    for row in reader:
        if row_index == 0:
            for year_str in row:
                years.append(year_str[:-1])
        if row_index == 1:
            for popu in row:
                populations.append(int(popu))
        row_index+=1        

# 按照时间正序
years.reverse()
populations.reverse()
# draw 
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(years, populations, c='red')
plt.title("china last 20 year population")
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('population', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.xticks(years[::2])
plt.show()


                 
