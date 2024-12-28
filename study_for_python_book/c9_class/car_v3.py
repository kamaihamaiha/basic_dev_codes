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