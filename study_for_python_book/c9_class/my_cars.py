"""从一个模块中导入多个类"""
from car import Car, ElectricCar

my_bettle = Car('volkswagen', 'bettle', 2000)
print(my_bettle.get_descriptive())

my_tesla = ElectricCar('tesla', 'model Y', 2021)
print(my_tesla.get_descriptive())