filename = 'txt_files/programming.txt'

# 新建/覆盖
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# 附加
with open(filename, 'a') as file_object:
	file_object.write("I also love programming.\n")
	file_object.write("I love creating apps that can run in a browser.\n")