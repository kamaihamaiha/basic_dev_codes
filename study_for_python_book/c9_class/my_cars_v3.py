from car_v3 import Car
from electric_car_v3 import ElectricCar

my_bettle = Car('volkswagen', 'bettle', 2000)
print(my_bettle.get_descriptive())

my_tesla = ElectricCar('tesla', 'model Y', 2021)
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() 