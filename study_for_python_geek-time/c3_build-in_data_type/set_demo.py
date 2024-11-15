# 集合

# 创建
second_names = {'赵', '钱', '孙', '李'}

# 应用： 去掉元组中的重复元素
colors = ('red', 'green', 'blue', 'green', 'blue', 'blue')
new_colors = set(colors)
print(new_colors)

# 再把set转成元组
colors_2 = tuple(new_colors)
print(colors_2)