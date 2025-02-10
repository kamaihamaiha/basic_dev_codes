import pygal
from die import Die


die = Die()

results = []
for roll_num in range(1000000):
    results.append(die.roll())

# print(results)    
# 分析结果
frequencies = []
for point in range(1, die.num_sides + 1):
    frequency = results.count(point)
    frequencies.append(frequency)

print(frequencies)    

# 结果可视化
hist = pygal.Bar()
hist.title = "1000次掷骰子结果"
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = 'points'
hist.y_title = '次数'
hist.add('六面骰子', frequencies)
hist.render_to_file('die_test.svg')
