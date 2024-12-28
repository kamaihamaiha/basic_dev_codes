from car import Car

my_car = Car('Nio', 'ET5T', 2024)
print(my_car.get_descriptive())
my_car.read_odometer()

# 修改属性的value
my_car.odometer = 222
my_car.read_odometer()   

my_car.update_odometer(1888)
my_car.read_odometer()    

my_car.increment_odometer(200)
my_car.read_odometer()