# 函数参数：位置参数、默认参数、可变参数、关键字参数；参数组合


# 位置参数

def power(x, n):
    s = 1
    while n >= 1:
        s = s * x;
        n = n - 1;
    return s;

x_v = input('type x: ')
n_v = input('type n: ')

x_int_v = int(x_v)
n_int_v = int(n_v)
print('power(%s, %s) = %d' % (x_v, n_v, power(x_int_v, n_int_v)))


# 默认参数
def add_end(L=None):
    if L is None:
        L = [];
    L.append('End...')
    return L

   
print(add_end())
print(add_end())
print(add_end([1,2]))

# 可变参数
def calc(*nums):
        s = 0;
        for n in nums:
            s = s + (n * n)
        return s

print(calc())
print(calc(1, 2))
scores = [100, 1, 2]
print(calc(*scores))
print(calc(scores[0], scores[1]))

# 关键字参数
def person(name, age, **kw):
     print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)     
person('Bob', 31, city='HongKong')     
person('Messi', 36, city='Shanghai', gender='Male')

info = {'city': 'Beijing', 'job': "Engineer"}
person('Jack', 24, **info)

# 命名关键字参数；上面的参数名可以随便输入，不受限制；如果想限制的话看下面的
def person(name, age, *, city, job):
     print(name, age, city, job)

person('Jack', 25, city='NY', job='Teacher')     

# 如果参数有可变参数，命名关键字参数的前面不用加 * 分割了
def person(name, age, *args, city, job):
     print(name, age, args, city, job)


# 参数组合： 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
     
def f1(a, b, c = 0, *args, **kw):
     print('a=', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)

f1(1,2)
f1(1,2,3)
f1(1,2,3,'arg1')          
f1(1,2,3,'arg1','arg2')          
f1(1,2,3,'arg1','arg2', city='shagnhai')          
f1(1,2,3,'arg1','arg2', city='shagnhai', gender='m')

def f2(a,b,c=0, *, d, **kw):
     print('a=',a, 'b=',b,'c=',c, 'd=',d, 'kw=',kw)

args = (1, 2, 3, 4)
kw = {'age': 22, 'height': 177}
f1(1,2,3,*args, **kw)

args = (1,2,3)
kw = {'d': 100, 'x': 99}
f2(*args, **kw) # 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


# 练习: 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def mul(x, y):
    return x * y

def mul(x, *y):
    ret = x
    for item_y in y:
        ret = ret * item_y
    return ret


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
