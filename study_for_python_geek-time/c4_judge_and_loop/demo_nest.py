# 处理多重循环问题

# 找出100以内被 7 整除的数
list = [i for i in range(1, 100) if i % 7 == 0]
print(list)


# 二维数据
data = [
    ['a', 'b', 'c'],
    ['1', '2', '3'],
    ['甲', '乙', '丙']
]

for item in data:
    for name in item:
        print(name)


# 九九乘法表
for i in range(1, 10):
    #print(i)
    list = [j for j in range(1, i+1)]
    #print(list)
    for num in list:
        print(f"{num}*{len(list)}=", num * len(list), end=" ")
    print()        