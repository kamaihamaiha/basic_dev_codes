# 使用 json 存数据
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as file_obj:
	json.dump(numbers, file_obj)


	

