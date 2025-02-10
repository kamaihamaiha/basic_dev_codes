from die import Die


die = Die()

results = []
for roll_num in range(1000):
    results.append(die.roll())

# print(results)    
# 分析结果
frequencies = []
for point in range(1, die.num_sides + 1):
    frequency = results.count(point)
    frequencies.append(frequency)

print(frequencies)    