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
