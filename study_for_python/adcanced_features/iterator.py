# 迭代器

# 可以直接作用于for循环的数据类型有以下几种：
# 1- 集合数据类型: list, tuple, dict, set, str 等
# 2- generator，包括生成器和带 yield 的 generator function

# 可以直接作用于 for 循环的对象称为 可迭代对象: Iterable
# 可被 next() 调用并不断返回下一个值的对象称为 迭代器: Iterator

# 判断是否为迭代对象(集合数据类型)
from collections.abc import Iterable
isinstance([1, 2, 3], Iterable)

# 判断是否为迭代器对象(generator)
from collections.abc import Iterator
isinstance((x for x in range(10)), Iterator)


for x in ([1, 2, 3, 4, 5]):
    pass

# 等价于
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break        
