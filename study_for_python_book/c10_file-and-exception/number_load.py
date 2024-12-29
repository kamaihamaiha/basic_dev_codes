import json

filename = 'numbers.json'
try:
	with open(filename) as file_obj:
		numbers = json.load(file_obj)	
except FileNotFoundError:
	print('file not found!')
else:
	print(numbers)

			
