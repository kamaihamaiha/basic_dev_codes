# for
for value in (1, 2, 3, 4):
    print(value)


for num in range(1, 20):
    print(num)    

# 遍历字典
movies = {
    "name": 'Friends',
    "lang": "En",
    "Sessions": 10,
    "Other name:": "Six of one"
} 

# 遍历字典的key
for key in movies.keys():
    print('key: ', key)

# 遍历key，valuye
for key, value in movies.items():
    print(f"{key}={value}")    

# 转成枚举类型，然后再遍历
for movie in enumerate(movies.items()):
    print(movie)    


# 使用 for 实现推导式
list1 = [i * i for i in range(1, 10)]
print(list1)      

# 加条件判断，奇数的平方
list2 = [i * i for i in range(1, 10) if i % 2 == 1]
print(list2)      
