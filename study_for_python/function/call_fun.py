# 调用函数

# abs()
x = input('Please input num: ')
value = int(x)
print(f'{value} 的绝对值: {abs(value)}')

# max()
m = max(1,20)
print(m)

# int() 数据类型转换
print(int('123'))
print(int(12.34))

# float() 
print(float('12.34'))

# str() 
print(str(1.23))
print(str(123))

# bool()
print(bool(1))
print(bool(0))
print(bool(''))
print(bool('1'))

# 函数别名
a = abs
v = a(-100)
print(v)


# 练习: 把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
