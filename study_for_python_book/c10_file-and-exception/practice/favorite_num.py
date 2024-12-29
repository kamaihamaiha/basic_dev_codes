# 保存用户喜欢的数字

import json

def get_new_num():
	filename = 'favorite_num.json'
	while True:
		try:
			num_str = input("What's your favorite number?\n")
			num = int(num_str)
		except ValueError:
			print('Please input number!')
		else:
			break

	with open(filename, 'w') as file_obj:
		json.dump(num, file_obj)
	return num	


def get_stored_num():
	filename = 'favorite_num.json'
	try:
		with open(filename) as file_obj:
			num = json.load(file_obj)
	except (FileNotFoundError, json.JSONDecodeError):
	    return None
	else:
		return num


def your_favorite():
	num = get_stored_num()
	if num:
		print('Wellcom back, Your favorite num is: ' + str(num))	
	else:
		num = get_new_num()
		print("I will remember your favorite num: " + str(num))
				

your_favorite()

