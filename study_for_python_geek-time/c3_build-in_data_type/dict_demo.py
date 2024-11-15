# 字典
d_1 = {'one':1, 'two': 2}
d_2 = dict(one=1, two=2)
d_3 = {x: x**2 for x in range(5)}

print(d_1)
print(d_2)
print(d_3)


# 练习: 两个列表组成字典
list_1 = [ 'name1', 'name2', 'name3' ]
list_2 = [ '1111', '2222', '3333']
my_d = {list_1[0]: list_2[0], list_1[1]: list_2[1], list_1[2]: list_2[2]}
print(my_d)

# 或者
my_d2 = {list_1[i]: list_2[i] for i in range(len(list_1))}
print(my_d2)

# 常见操作
# 1.访问所有元素/key/value
print(my_d2.items())
print(my_d2.keys())
print(my_d2.values())
# 2.访问指定元素
print(my_d2.get('name1'))
print(my_d2['name2'])
# 3.遍历
for key, value in my_d2.items():
    print(key, value)

# 4. 添加新的key,value
my_d2['name4'] = '4'
print(my_d2)

# 5. 字典项数
print("字典项数: ", len(my_d2))

# 6. 判断 key 是否在字典中
print("name is in key: ", 'name' in my_d2)

# 7. 移除改键, 返回 key/item
print(my_d2.pop('name1'))
print(my_d2.popitem()) #popitem() 不需要参数，移除的是最后一个
print(my_d2)

# 高级用法
# 8. 字典默认值: 如果字典存在键key,返回它对应的值; 如果不存在，插入 default 的键 key, 并返回 default
name1 = my_d2.setdefault('name1', 'this is name 1 value') # 第二个参数不传，则为 None
print(name1)
print(my_d2)

# 9. 用新字典的key/value 更新旧的字典, 新字典的key/value 优先; Pyhton3.9 以上版本支持
my_d3 = {'word: ': 'this is word value'}
my_d2 |= my_d3
print(my_d2)

# 课后练习: 设计一个字典数据类型用于存储通讯录，通讯录中包含：必须填写的姓名、可以为空的备注名、1 个邮箱，至少 2 个手机号码，并尝试增加和删除联系人
contacts = {
    '张三': {
        "comment": "",
        'E-mail': "xxx@gmail.com",
        'phone_1': "110",
        'phone_2': "120"
    },
   '李四': {
        "comment": "",
        'E-mail': "1xxx@gmail.com",
        'phone_1': "1101",
        'phone_2': "1201"
    } 
    }

# 添加练习人
contacts.setdefault('王五', {
   "comment": "",
        'E-mail': "2xxx@gmail.com",
        'phone_1': "1102",
        'phone_2': "1202" 
})

print(contacts)

# 删除张三
contacts.pop('张三')

print(contacts)