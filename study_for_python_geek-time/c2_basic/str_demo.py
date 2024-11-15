print('hello "python!')

print('''
赵
钱
孙
李
''')

age = 99
print(f"我的年龄是 {age}")

# 字符串基本操作
# 成员运算
x = 'a'
s = 'abc'
print(x in s)
print(x not in s)

# 连接运算 +, *
print('ab' + 'cd')
print('ab' * 3)

# 切片操作
s = 'abcdefg'
print(s[2])
print(s[2:5])
print(s[0:5:2])

# 字符串的常用方法
str = 'ababab'
sub = 'aba'
ret = str.count(sub[0])
print(f"非重叠次数:{ret}")

print("含有字母或者数字:", str.isalnum())
print("含有字母: ", "1234".isalpha())
print("含有字符a的个数: ", str.count("a"))

#abc每个字符间加上,
print("str join: ", ",".join("abc"))

print("str split: ", "a,b,c,d".split(','))
print("str startWiths: ", str.startswith('ab'))