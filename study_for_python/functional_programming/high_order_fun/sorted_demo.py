# sorted

list = sorted([1, -2, 3, -4, 5, -6])
print(list)

nums = [1, -2, 3, -4, 5, -6]
# 按照绝对值大小排序
list = sorted(nums, key=abs)
print(list)

# 对字符串排序：忽略字母大小写
names = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(names, key=str.lower))

# 反向排序
print(sorted(names, key=str.lower, reverse=True))


# 练习: 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 按名字排序
print(sorted(L, key=lambda x: x[0]))

# 按成绩排序: 升序
print(sorted(L, key=lambda x: x[1]))

# 按成绩排序: 降序
print(sorted(L, key=lambda x: x[1], reverse=True))