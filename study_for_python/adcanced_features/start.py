# 构造一个 1, 3, 5, 7, ..., 99的列表，可以通过循环实现：
L = []
n = 1
while n < 100:
    L.append(n)
    n += 2


# 获取前n个元素 
        
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

# 使用高级特性，可以一行代码实现

