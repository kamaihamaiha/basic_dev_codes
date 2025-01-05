from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
	first = input("Please input your first name:\n")
	if first == 'q':
		break
	last = input("Please input your last name:\n")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print("\nNeatly formateed name: " + formatted_name + '.')		
