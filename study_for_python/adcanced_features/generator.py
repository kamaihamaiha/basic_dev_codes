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

print("==================\n")
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


g = fib_g(10)
print(next(g))
print(next(g))
print(next(g))

# 练习 杨辉三角定义如下：

def triangles():
    n = 1
    line = [1]
    while True:
        yield line
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')