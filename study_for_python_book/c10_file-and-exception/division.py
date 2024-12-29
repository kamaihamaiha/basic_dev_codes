try:
	print(5/0)
except ZeroDivisionError:
	print("you can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# 除法简单运算器
while True:
	first_num = input("First number:\n")
	if first_num == 'q':
		break		
	second_num = input("Second number:\n")
	if second_num == 'q':
		break
	
	try:
		answer = int(first_num) / int(second_num)
	except ZeroDivisionError:		
		print("you can't divide by zero!")
	else:	
		print(answer)		



