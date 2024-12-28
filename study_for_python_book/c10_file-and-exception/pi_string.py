# 使用文件内容

filename = 'txt_files/pi_digits.txt'

def read_pi(filename, bit_count):
	with open(filename) as file_object:
		lines = file_object.readlines()

	pi_string = ''
	for line in lines:
		pi_string += line.strip()


	return pi_string[:bit_count]	

frag = read_pi(filename, 20)
print(frag)

# 读取包含1million位的文件
filename = 'txt_files/pi_million_digits.txt'
bit_count = 1000000
frag = read_pi(filename, bit_count)
print(frag)

# 圆周率是否包含自己的生日
birthday = input("Enter your birthday, in the form yymmdd:")
if birthday in frag:
	print("圆周率前" + str(bit_count) + "包含了你的生日: " + birthday)
else:
	print("没有找到")	

