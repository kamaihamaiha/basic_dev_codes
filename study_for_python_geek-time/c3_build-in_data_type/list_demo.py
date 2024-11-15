# 列表: 输出、访问元素、删除

list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'ab']
list_3 = [1, '2', 34, 'abc']
list_4 = [[1, 'a'], [2, 'ab']]

print(list_1)
print(list_2)
print(list_3)
print(list_4)

colors = ['red', 'blue', 'green']
print(colors)
# 输出 colors 类型
print(type(colors))

# 内置函数list() 可以把字符串创建成列表
print(list('hello'))

# 访问列表元素
print(colors[0])
print(colors[1])
print(colors[-1])

# 删除列表中的元素 / 删除列表
del colors[-1]
print(colors)
del colors