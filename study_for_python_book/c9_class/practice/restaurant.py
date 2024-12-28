# 9.1 餐馆
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


my_resturant = Restaurant('兰州牛肉拉面', '面馆')        
my_resturant.describe()
my_resturant.open()


# 9.2 创建实例
my_resturant_1 = Restaurant('和平饭店', '大饭店')        
my_resturant_1.describe()

my_resturant_1.set_number_served(99)
my_resturant_1.describe()

