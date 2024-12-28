# 9-6 冰淇淋小店

class Restaurant():
    def __init__(self, name, _type):
        self.name = name
        self.type = _type
        self.number_served = 0

    def describe(self):
        print("my restaurant name is " + self.name + ", and it is a " + self.type + ", " + str(self.number_served) + " people has 来过")

    def open(self):
        print("my restaurant " + self.name + " is opening")    

    def set_number_served(self, number):
        self.number_served = number 


class IceCreamStand(Restaurant):
	def __init__(self, name, _type):
		super().__init__(name, _type)
		self.flavors = ['apple', 'mango', 'strawbarry']

	def describe(self):
		print("My stand name is " + self.name + ", and it is a " + self.type + ", It has many flavors: ")
		for flavor in self.flavors:
			print(flavor)


my_cream_stand = IceCreamStand('蜜雪冰城', '饮料店')		
my_cream_stand.describe()		
