class Employee():
	def __init__(self, name, annual_salary):
		self.name = name
		self.annual_salary = annual_salary

	def give_rise(self, rise_salary = 5000):
		self.annual_salary += rise_salary

				