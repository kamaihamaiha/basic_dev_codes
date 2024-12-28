# 9-3 用户
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


my_user = User('Bush', 88)
my_user.intro()  
print("User: " + my_user.name + " has login: " + str(my_user.login_attempts))
my_user.increment_login_attempts()   
my_user.increment_login_attempts()   
print("User: " + my_user.name + " has login: " + str(my_user.login_attempts))
my_user.reset_login_attempts()
print("User: " + my_user.name + " has login: " + str(my_user.login_attempts))