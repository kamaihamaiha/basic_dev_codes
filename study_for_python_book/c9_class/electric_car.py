from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive())   
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()







