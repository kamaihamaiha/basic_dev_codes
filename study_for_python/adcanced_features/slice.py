# Slice 切片操作符

# 构造一个 1, 3, 5, 7, ..., 99的列表，可以通过循环实现：
L = []
n = 1
while n < 100:
    L.append(n)
    n += 2

# 取前 3 个元素
print(L[0:3])  

# 等价于上面的
print(L[:3])

# 取倒数3个元素
print(L[-4:-1])
# 取倒数第3个元素
print(L[-3])

L_n = list(range(100))
print(L)

# 取前10个
print(L_n[:10])

# 取后10个
print(L_n[-10:])


# 前10个数，每2个取一个
print(L_n[:10:2])


# 所有数，每5个取一个
print(L_n[::5])

# 只写[:]就可以原样复制一个list：
print(L_n[:])


# tuple 的切片操作
print((1, 2, 3, 4, 5)[:3])

# 字符串的切片操作
print('abced'[:3])


# 练习: 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(str):
    if not str:
        return str
    # 切前面的空格
    while str[0] == ' ':
        str = str[1:]
        if len(str) == 1: # 还剩一个字符，是空格；则返回 ''
            return ''
    # 切后面的空格
    while str[-1] == ' ':
        str = str[0:-1]
        if len(str) == 1: # 还剩一个字符，是空格；则返回 ''
            return ''
    return str      

# 测试
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')             