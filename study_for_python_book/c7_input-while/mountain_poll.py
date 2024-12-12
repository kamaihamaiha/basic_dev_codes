# 民意调查
responses = {}
polling_active = True

while polling_active:
	name = input("What's your name?\n")
	mountain = input("Which mountain would you like to climb someday?\n")

	responses[name] = mountain

	# 是否继续
	repeat = input("Would you like to let another person respond?(yes/no)\n")
	if repeat == 'no':
		polling_active = False

# 输出调查结果
for name, mountain in responses.items():
	print(name + " would like to clime " + mountain + ".")		