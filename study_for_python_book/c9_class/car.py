"""一组用于表示燃油汽车和电动汽车的类"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")   

    def update_odometer(self, mileage):
        self.odometer = mileage         

    def increment_odometer(self, miles):
        self.odometer += miles     

    def fill_gas_tank(self):
        print('加 95# 汽油')



# 定义电池类，给  ElectricCar 当作属性用
class Battery():
    def __init__(self, battery_size = 60):
        self.battery_size = battery_size  

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")     

    # 续航计算
    def get_range(self):
        range = self.battery_size * 5
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)                              

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def upgrade_battery(self):
        if(self.battery.battery_size != 85):
            self.battery.battery_size = 85

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")        

    



