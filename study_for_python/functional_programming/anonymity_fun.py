# 匿名函数
mlist = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
print(mlist)

# 可以当作表达式
f = lambda x: x * x
print(f(3))

# 可以 return
def build(x, y):
    return lambda: x + y
# 第一种调用
f_add = build(3, 6)
print(f_add())

# 第二种调用
print(build(1, 8)())

# 练习  匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)