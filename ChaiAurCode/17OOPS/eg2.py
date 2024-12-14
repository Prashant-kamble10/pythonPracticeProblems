# 2. Class Method and self

# Add a method to the Car class that displays the full name of the car(brand and model)

class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

    def displayFullName(self):
         return f"{self.brand +" "+ self.model}"

prashants_car = Car("Toyota", "Fortuner")  
print(prashants_car.displayFullName())
rupeshs_car = Car("TATA", "Nano")
print(rupeshs_car.displayFullName())







