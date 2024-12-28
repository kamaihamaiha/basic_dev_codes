# 9-14 骰子 练习
from random import randint
class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		value = randint(1, self.sides)
		print("value is: " + str(value))		