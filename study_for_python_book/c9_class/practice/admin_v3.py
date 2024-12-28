from user_v3 import User
class Privileges():
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can be user']

class Admin(User):
	def __init__(self, name, age):
		super().__init__(name, age)
		self.privileges = Privileges()

	def show_privileges(self):
		print("My name is " + self.name + " and I'm a administrator, My privileges: ")
		for privilege in self.privileges.privileges:
			print(privilege)