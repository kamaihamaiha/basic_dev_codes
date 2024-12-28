# 1-4 练习 访客名单
filename = 'guest_book.txt'
while True:
	name = input("Enter your name and type 'q' to quit:\n")
	if name == 'q':
		break
	with open(filename, 'a') as file_object:
		print("Hello, " + name + "!")
		file_object.write(name + "\n")
	