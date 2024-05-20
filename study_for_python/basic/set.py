# 一组key的集合，不存储 value
s = set([1, 2, 3])
print(s)

# 添加元素
s.add(4)
print(s)

# 移除元素
s.remove(2)
print(s)

# 交集和并集操作
s_1 = set([1, 2, 4])
s_2 = set([1, 2, 3])
print('交集: %s' % (s_1 & s_2))
print('并集: %s' % (s_1 | s_2))