def build_profile(first_name, last_name, **user_infos):
	"""创建一个字典，用于存放用户信息"""
	prifile = {}
	prifile['first_name'] = first_name
	prifile['last_name'] = last_name
	for key, value in user_infos.items():
		prifile[key] = value
	return prifile
	
user = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user)		