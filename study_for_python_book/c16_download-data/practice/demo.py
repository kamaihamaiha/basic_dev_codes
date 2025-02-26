import csv
import os
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

# change work dir
print(os.getcwd())
os.chdir('practice')
print(os.getcwd())
print(os.listdir(os.getcwd()))
old_file = 'cn_population_last74.csv'

# 读取原始 csv 文件
data = pd.read_csv(old_file, index_col=0)
# 转置数据，使每一行是年份，每一列是不同指标
data_transposd = data.T
# 重命名列名
data_transposd.columns = ['citizen', 'country', 'total']
# 保存为新的文件
data_transposd.to_csv('cn_pop_last74_format.csv')
print(data_transposd)