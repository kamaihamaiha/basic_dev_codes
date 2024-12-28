with open('txt_files/pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)


# 逐行读取	
filename = 'txt_files/pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


# 在 with 代码块外面处理每一行的数据
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())	
