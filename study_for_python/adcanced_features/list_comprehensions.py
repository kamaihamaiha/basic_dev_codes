## 列表生成式

# 生成 [1x1, 2x2, 3x3, ..., 10x10]
L = [x * x for x in range(1, 11)]

print(L)

# 还可以加上 if 判断
L = [ x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 两层循环
L = [m + n for m in '123' for n in 'ABC']
print(L)

# 列出当前目录下所有文件和目录名；需要导入 os 模块
import os
L = [dir for dir in os.listdir('.')]
print(L)

# for 循环同时使用多个变量，如 dict 的 items 可以同时迭代 key 和 value
d = {'x': 'a', 'y': 'b', 'z': 'c'}
for k, v in d.items():
    print(k, '=', v)


# 列生成式同时使用两个变量    
L = [k + '=' + v for k, v in d.items()]
print(L)

# 把list 所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
l = [s.lower() for s in L]
print(L)    
print(l)

# 练习: L1 = ['Hello', 'World', 18, 'Apple', None] , 转成小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L1)
print(L2)

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
