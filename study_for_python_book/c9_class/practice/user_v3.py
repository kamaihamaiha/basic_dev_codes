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