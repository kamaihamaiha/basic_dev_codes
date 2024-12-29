import json

"""filename = "username.json"
try:
	with open(filename) as file_obj:
		username = json.load(file_obj)
except FileNotFoundError:
	# print("File" + filename + " not found!")
	username = input("What is your name?\n")
	with open(filename, 'w') as file_obj:
		json.dump(username, file_obj)
	print("I remember your when you come back, " + username + "!")
else:
	print("Welcom back, " + username + "!")
"""

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as file_obj:
			username = json.load(file_obj)
	except FileNotFoundError:
		return None
	else:
		return username			

def get_new_username():
	filename = 'username.json'
	with open(filename, 'w') as file_obj:
		username = input("What is your name?\n")
		json.dump(username, file_obj)
	return username

def greet_user():
	username = get_stored_username()
	if username:
		print("Welcom back, " + username + "!")
	else:
		username = get_new_username()	
		print("I remember your when you come back, " + username + "!")	


greet_user()



