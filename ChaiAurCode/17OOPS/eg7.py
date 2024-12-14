# 7. static method =  a method belongs to class rather than an instance of  a class

# Add a static method to the Car class that returns a general description of a car

class Car:
    total_car = 0                   

    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def fuelType(self):
        return "petrol and diesel"
    
    def displayName(self):
        return f"{self.__brand + " " + self.model}"
    
    @staticmethod                                # static method
    def generalDescription():
        return "Cars are helpful"
    
class ElectriCar(Car):
    def __init__(self, userbrand, usermodel, batterySize):
        super().__init__(userbrand, usermodel)
        self.batterySize = batterySize

    def fuelType(self):
        return "Electric charfge"

prashantCar = Car("Tesla", "Model 5")

print(Car.generalDescription())     # Cars are helpful
    
        