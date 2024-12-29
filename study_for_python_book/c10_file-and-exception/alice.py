filename = 'txt_files/Alice.txt'

try:
	with open(filename) as file_object:
		contens = file_object.read()
except FileNotFoundError:
	print(filename + " not found!")
else:
	words = contens.split()
	print(filename + " has " + str(len(words)) + " words.")	