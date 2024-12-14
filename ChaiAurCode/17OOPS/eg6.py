# 6. Class variable

# Add a class variable to Car that keeps track of the numbers of cars created

class Car:
    total_car = 0                       # creation of class variable

    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel
        # Car.total_car, self.total_car   # both syntax are same
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def fuelType(self):
        return "petrol and diesel"
    
    def displayName(self):
        return f"{self.__brand + " " + self.model}"
    
class ElectriCar(Car):
    def __init__(self, userbrand, usermodel, batterySize):
        super().__init__(userbrand, usermodel)
        self.batterySize = batterySize

    def fuelType(self):
        return "Electric charfge"

# prashantCar = ElectriCar("Tesla", "model 5", "85KWH")
rupeshCar = Car("TATA", "SAfari")
boomikCar = Car("TATA", "Nexo")
hashCar = Car("TATA", "Nano")

print(Car.total_car)          # 3
        