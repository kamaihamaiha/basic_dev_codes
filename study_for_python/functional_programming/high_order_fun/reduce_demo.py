# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

# 效果就是: reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


from functools import reduce

def f(x, y):
    return x + y

ret = reduce(f, list(range(101))[1:])

# 应该是 5050
print(ret)

# 实现 str => int 的函数

DIGITS = {'0': 0, '1': 1, '2': 2, '3':3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2Int(s):
    def char2Int(c):
        return DIGITS[c]
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(char2Int, s))

print(str2Int('12345')) # 12345


# 练习
# 1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)