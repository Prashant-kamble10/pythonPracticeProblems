# 5. Polymorphism

# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectriCar classes, but with different behaviours

class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel

    def get_brand(self):
        return self.__brand + " !"
    
    def displayFullName(self):
        return f"{self.__brand + " " + self.model}"
    
    def fuelType(Self):                           # Polymorphism
        return "petrol or diesel"
    
    
class ElectriCar(Car):
    def __init__(self, userbrand, usermodel, batterySize):
        super().__init__(userbrand, usermodel)
        self.batterySize = batterySize

    def fuelType(Self):                         # Polymorphism
        return "Electric charge"

prashantTesla = ElectriCar("Tesla", "Model 5", "85KWH")
print(prashantTesla.fuelType())        # Electric charge

rupeshCar = Car("TATA", "SAfari")
print(rupeshCar.fuelType())           # petrol or diesel
     