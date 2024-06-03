# 迭代

# list

names = ['A', 'B', 'C', 'D']
for name in names:
    print(name)


# dict
infos = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key in infos:
    print(key)

for value in infos.values():
    print(value)
        

# 判断一个对象是否可迭代：使用 collections.abc 模块的 Iterable 类型的 isinstance() 判断

from collections.abc import Iterable
print('infos can inteation: %s' % isinstance(infos, Iterable))        
print('str can inteation: %s' % isinstance('this is str', Iterable))        
print('int can inteation: %s' % isinstance(123, Iterable))   


# 迭代时，同时输出下标信息
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


# 迭代，同时饮用两个变量
for x, y in [(1, 1), (2, 4), (3, 9), (4, 16)]:
    print(x, y)


# 练习： 使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if not L:
        return (None, None)
    min = L[0]
    max = min
    for value in L[1:]:
        if min > value:
            min = value
        if max < value:
            max = value
    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')                