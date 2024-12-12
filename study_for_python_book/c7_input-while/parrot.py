# 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n"
msg = ""
while msg != 'quit':
	msg = input(prompt)
	if msg != 'quit':
		print(msg)
	