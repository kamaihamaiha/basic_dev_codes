import pygal
from die import Die


die_1 = Die()
die_2 = Die()

count = 10000
results = []
for roll_num in range(count):
    results.append(die_1.roll() + die_2.roll())

# print(results)    
# 分析结果
frequencies = []
for point in range(2, die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(point)
    frequencies.append(frequency)

print(frequencies)    

# 结果可视化
hist = pygal.Bar()
hist.title = str(count) + "次掷骰子结果"
hist.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hist.x_title = 'points'
hist.y_title = '次数'
hist.add('2个六面骰子', frequencies)
hist.render_to_file('dual_die_test.svg')
