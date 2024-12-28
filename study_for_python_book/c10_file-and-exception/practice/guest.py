# 10-3 练习 访客
name = input("Enter your name, and I will save it to txt file guest.txt\n")

filename = 'guest.txt'
with open(filename, 'w') as file_object:
	file_object.write(name) 

