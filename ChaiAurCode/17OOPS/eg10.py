# 9. multiple Inheritance 

# Create two classes Battery and Engine, and let the ElectriCar class inherit from both, demonstrating multiple inheritance

class Battery:
    def batteryInfo(self):
        return "This is battery Info"

class Engine:
    def engineInfo(self):
        return "This is Engine Info"

class ElecrtiCar(Battery, Engine):
    pass

newCar = ElecrtiCar()
print(newCar.batteryInfo())               # This is battery Info
print(newCar.engineInfo())                 # This is battery Info


    
        