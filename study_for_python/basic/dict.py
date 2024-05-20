# 字典 dict, 类似 Java 的Map
d = {'A': 1, 'B': 2, 'C': 3}
print(d['A'])

d = {1: 'a', 2: 'ab', 3: 'abc'}
print(d[2])

keyState = 30 in d
if keyState:
    print('30 is in d')
else:    
    print('30 is not in d')

print(d.get(1))
print(d.get(10)) # 没有这个key，就返回 None
print(d.get(10, 'nothing...')) # 没有这个key，就返回自定义的值

# 删除一个key
d.pop(1)
print(d.get(1))