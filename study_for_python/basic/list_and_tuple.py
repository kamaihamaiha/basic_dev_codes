# list
names = ['Bush', 'Tom', 'Bob']
print('the number of names is: %d' % len(names))

print('the last name is: %s' % names[-1])

# 添加到末尾
names.append('Jack')
print('the number of names is: %d' % len(names))
print('the last name is: %s' % names[-1])

# 添加到指定index
names.insert(1, 'Lucy')
print('the number of names is: %d' % len(names))
print('the 1 index name is: %s' % names[1])

# 删除(末尾元素)
names.pop()
print('the number of names is: %d' % len(names))
print('the last name is: %s' % names[-1])

# 删除指定index
names.pop(1)
print('the number of names is: %d' % len(names))
print('the 1 index name is: %s' % names[1])

# 修改某个元素的值
names[-1] = 'Trump'
print('the last index name is: %s' % names[-1])

# 元素也可以是 list
print('size of names is: %d' % len(names))
names.append(['A', 'B'])
print('size of names is %d' % len(names))

# 元组 tuple, 相当于数组
bodys = ('leg', 'head', 'arm', ['x', 'y'])
print(bodys[3][0])
bodys[3][0] = 'xx'
print(bodys[3][0])

# 练习: 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

