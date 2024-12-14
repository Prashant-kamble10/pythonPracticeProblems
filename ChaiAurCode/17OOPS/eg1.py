# what data and what its type, in variable, is the main important thing in programming

# 1 Basic Class and Object

# Create a Car class with attributes (means variables) like brand and model. Then create an instance of this class.

# __init__ is a constructor
# self in python, this in JS
# self.brand is a attribute

class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

prashants_car = Car("Toyota", "Fortuner")   # creating a instance of a class / creating a object through the class
print(prashants_car.brand)
print(prashants_car.model)

rupeshs_car = Car("TATA", "Safari")
print(rupeshs_car.brand)
print(rupeshs_car.model)