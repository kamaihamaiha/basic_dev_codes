# 列表
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1].title())

# 末尾添加元素
motobicycles = ['honda', 'yamaha', 'suzuki']
motobicycles.append('ducati')
print(motobicycles)

# 插入元素
motobicycles.insert(1, 'BMW')
print(motobicycles)

# 删除元素
del motobicycles[1]
print(motobicycles)

poped_moto = motobicycles.pop()
print(poped_moto)

# 弹出指定index的元素
print(motobicycles.pop(1))

# 根据value 删除
motobicycles.remove('suzuki')
print(motobicycles)

# 组织列表: sort() 永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorted() 临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)

# 反转列表
cars.reverse()
print(cars)
print("cars 种类: ", len(cars))








