# 一个函数就可以接收另一个函数作为参数
def add(x, y, fun):
    return fun(x) + fun(y)

# 应该输出 18
print(add(-9, 9, abs))
