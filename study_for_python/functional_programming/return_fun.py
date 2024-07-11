# 返回函数

def lazy_sum(*args):
    def sum():
        ax = 0;
        for n in args:
            ax = ax + n
        return ax
    return sum

sum1 = lazy_sum(1, 2, 3)
# 调用的时候才会真正计算
print(sum1())
        
            
# 练习：利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    num = 0
    def counter():
        # nonlocal会把 num看成外层函数的局部变量
        nonlocal num
        num = num + 1
        return num
    return counter
            
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')            