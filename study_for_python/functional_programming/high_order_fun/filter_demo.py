#filter 函数

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
def is_odd(n):
    return n % 2 == 1

# 保留奇数
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 定义一个匿名函数
def not_divisible(n):
    return lambda x: x % n > 0

# 不能被2整除
not_divisible_2 = not_divisible(2)
print(not_divisible_2(1)) # True
print(not_divisible_2(2)) # False


# 生成器: 从3开始的奇数序列
def old_iter():
    n = 1
    while True:
        n += 2
        yield n

# 生成器：不断返回下一个素数(埃拉托斯特尼筛法)
def primes():
    yield 2 # 第一个素数
    it = old_iter() # 初始序列
    while True:
       n = next(it) # 返回序列第一个数

       yield n
       not_div_n = not_divisible(n) # 判断是否可以不被n整除
       it = filter(not_div_n, it) # 把序列 it的可以整除n的数过滤掉，然后生成一个新的序列

# 打印素数，max 最大素数范围
def printPrims(max = 10):
    rowNum = 10
    count = 0
    for num in primes():
        if(num < max):
            count += 1
            print(num, end = ", ")
            if(count % rowNum == 0):
                print() # 换行
        else:
            print()
            break;    

printPrims()
printPrims(999)
