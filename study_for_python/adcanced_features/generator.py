# 一边循环一遍计算的机制; 即使元素很多，也不会占用大量的空间
g = (x * x for x in range(10))

# 一个个打印
print(next(g))    
print(next(g))    
print(next(g)) 


# 遍历打印出来; 上面调用了几次 next() 到这里，就会接着往后生成，而不是从头开始打印
for n in g:
    print(n)

   
# 斐波那契数列
def fib(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'ok'

print(fib(10))

# 这个函数为 generator 函数，因为包含了 yield 关键字

def fib_g(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'ok'

print(fib_g(10))