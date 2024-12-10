# 操作列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

# 创建数值列表
nums = list(range(0, 9))
for num in nums:
	print(num)	


# 存放平方数
squares = []
for value in range(1, 10):
	squares.append(value ** 2)
print(squares)	


# 对数字列表进行简单的统计运算: min(), max(), sum()
digits = list(range(1, 10))
print("min value: ", min(digits))
print("max value: ", max(digits))
print("sum value: ", sum(digits))

# 列表解析
squares = [value ** 2 for value in range(1, 100)]
print(squares)

# 使用列表的一部分: 切片
values = list(range(1, 21))
print(values[0:3])
print(values[:3])
print(values[3:])
print(values[-3:])

# 用切片复制列表
my_values = values[:]
print(my_values)






