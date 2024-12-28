class Dog():

    """定义一个类，小狗"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now seting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " is rolled over!")


my_doy = Dog('willie', 3)
print("My dog's name is " + my_doy.name.title())                        
print("My dog's age is " + str(my_doy.age) + " years old.")     
my_doy.sit()
my_doy.roll_over()                
