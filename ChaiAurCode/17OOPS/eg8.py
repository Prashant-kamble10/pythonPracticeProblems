# 8. property Decorators

# use a property decorator in the Car class to make the model attribute read-only

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
    
    @property                   # property decorator
    def model(self):
        return self.__model
    
class ElectriCar(Car):
    def __init__(self, userbrand, usermodel, batterySize):
        super().__init__(userbrand, usermodel)
        self.batterySize = batterySize

    def fuelType(self):
        return "Electric charfge"

prashantCar = Car("Toyota", "Fortuner")

# prashantCar.model = "Tesla"   

print(prashantCar.model)         # Fortuner
print(prashantCar.model())       # TypeError: 'str' object is not callable

    
        