filename = 'txt_files/learning_python.txt'

# 10-1 练习
def read_file(filename):
	with open(filename) as file_object:
		content = file_object.read()
		print(content)

def read_file_by_line(filename):
	with open(filename) as file_object:
		for line in file_object:
			print(line.strip())	

def read_file_by_line_v2(filename):
	with open(filename) as file_object:
		lines = []
		for line in file_object:
			lines.append(line.strip())
	
	for line in lines:
		print(line)			


read_file(filename)	
read_file_by_line(filename)	
print("\nv2:")
read_file_by_line_v2(filename)	


# 10-2 练习
def read_file_by_line_and_replace(filename):
	with open(filename) as file_object:
		lines = file_object.readlines()

	for line in lines:
		line = line.replace('Python', 'C')	
		print(line)


read_file_by_line_and_replace(filename)		



