# 9. class Inheritance and isInstance() function

# Demonstarte the use of isInstance() to check if prashantCar is an instance of Car and ElectiCar

class Car:
    total_car = 0                   

    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def fuelType(self):
        return "petrol and diesel"
    
    def displayName(self):
        return f"{self.__brand + " " + self.__model}"
    
    @staticmethod                               
    def generalDescription():
        return "Cars are helpful"
    
    @property                
    def model(self):
        return self.__model
    
class ElectriCar(Car):
    def __init__(self, userbrand, usermodel, batterySize):
        super().__init__(userbrand, usermodel)
        self.batterySize = batterySize

    def fuelType(self):
        return "Electric charfge"

prashantCar = ElectriCar("Tesla", "Model 5", "85KWH")

print(isinstance(prashantCar, Car))        # True
print(isinstance(prashantCar, ElectriCar))  # True

    
        