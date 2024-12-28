def formated_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print('\nPlease input your name:')
	print('\nEnter "q" at anytime to quit')
	f_name = input('First name:\n')
	if f_name == 'q':
		break
	l_name = input('Last name:\n')
	if l_name == 'q':
		break
	print("Hello, " + formated_name(f_name, l_name))	