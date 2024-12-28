"""导入整个 car 模块"""
import car

my_bettle = car.Car('volkswagen', 'bettle', 2000)
print(my_bettle.get_descriptive())

my_tesla = car.ElectricCar('tesla', 'model Y', 2021)
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()