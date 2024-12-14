# 3. Inheritance

# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

    def displayFullName(self):
        return f"{self.brand + " " + self.model}"
    
class ElectriCar(Car):      # class ElectriCar Extends Car
    def __init__(self, userbrand, usermodel, batterySize):
        super().__init__(userbrand,usermodel)  # imp
        self.batterySize = batterySize


prashantTesla = ElectriCar("Tesla", "Model 5", "85KWH")
print(prashantTesla.displayFullName())
print(prashantTesla.brand)

# prashantCar =  Car("Toyota", "Fortuner")
# print(prashantCar.displayFullName())
# rupeshCar =  Car("TATA", "Safari")
# print(rupeshCar.displayFullName())






