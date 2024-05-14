#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
# 字符串和编码: https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

str = '这是中文'
print(str)
str = 'this is English'
print(str)
str = '中文&English'
print(str)
print('A utf-8 code: ', ord('A'))
print('a utf-8 code: ',ord('a'))
print('中 utf-8 code: ',ord('中'))
print('utf-8 66 mapping char: ', chr(66))

# bytes 类型数据: b'xxx'
x = b'abc'
print(x)

# 以 Unicode表示的 str 通过 encode() 方法可以编码为指定的 bytes
x = 'abc'
x_b = x.encode('ascii')
print(x_b)

x = '你好'
x_b = x.encode('utf-8')
print(x_b)
# decode bytes
print(x_b.decode('utf-8'))

# len()
print(len('hello'))
print(len('你好'))
print(len(x_b))

# 格式化
print('hello, %s' % 'zkx')
print('Hi, %s, you have %d$ money!' % ('zkx', 99))

# 字符串中如何显示出 %s? 用 %% 转义

# 练习: 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2 / s1 - 1) * 100
# 使用了 f-string
print(f'小明成绩提升了: {r:.1f}%')