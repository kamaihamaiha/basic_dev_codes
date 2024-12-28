# 9-11 练习
class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.login_attempts = 0

    def intro(self):
        print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")     

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0      

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