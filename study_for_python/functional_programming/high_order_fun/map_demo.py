# 有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上
def f(x):
    return x * x

ret = map(f, [1,2, 3, 4, 5, 6, 7, 8, 9])
print(list(ret))

# 也可以这么写
ret = map(f, list(range(10))[1:])
print(list(ret))
