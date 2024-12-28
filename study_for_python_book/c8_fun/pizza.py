def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with following toppings:")
	for topping in toppings:
		print("- " + topping)


# make_pizza(8, '香肠', '土豆', '牛肉')