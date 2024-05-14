# 数据类型和变量

# 整数
int_1 = 1
int_2 = -2
int_3 = 0x11
int_4 = 1_234_333
int_5 = 0x1111_1111

print('0x11 = ', int_3)
print('1_234_333 = ', int_4)
print('0x1111_1111 = ', int_5)

# 浮点数
f_1 = 1.23
f_2 = 1.23e9
f_3 = 1.2e-3

print('f_1 = ', f_1)
print('f_2 = ', f_2)
print('f_3 = ', f_3)

# 字符串
str = 'I\'m \"OK\"'
str_1 = "I'm Ok"
print(str)
print(str_1)

# \ tab \
str = '\\\t\\'
print(str)
# 不转义
str = r'\\\t\\'
print(str)

# 多行字符串
str = '''line1
line2
line3'''
print(str)

# 布尔值
b = True
print(b)

b = False
print(b)

b = True and True
print(b)

b = True and False
print(b)

b = True or False
print(b)

b = not False
print(b)

# 空值 None
n = None
print(n)

