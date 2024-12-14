#  4. Encapsulation

# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand  # __brand = pirvitisation of brand attribute, __brand is accessible in same class but as it pvt now it is not accessible outside class
        self.model = usermodel
    
    def get_brand(self):    # getter function
         return self.__brand + " !"
    
    def set_brand(self, new_brand):  # Setter function
        self.__brand = new_brand

    def displayFullName(self):
        return f"{self.__brand + " " + self.model}"
    
class ElectriCar(Car):
      def __init__(self, userbrand, usermodel, batterySize):
           super().__init__(userbrand, usermodel)
           self.batterySize = batterySize

PrashantTesla = ElectriCar("Tesla", "Model 5", "85KWH")

print(PrashantTesla.get_brand())      # Tesla !

# Modify brand using setter
PrashantTesla.set_brand("TeslaX")
print(PrashantTesla.get_brand())      # TeslaX !


print(PrashantTesla.__brand)       # AttributeError: 'ElectriCar' object has no attribute '__brand'.
