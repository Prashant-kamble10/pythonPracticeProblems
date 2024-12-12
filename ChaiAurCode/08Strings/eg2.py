chai = "Masala Chai"

a = chai.lower()
print(a)           # masala chai

b = chai.upper()
print(b)            # MASALA CHAI

name = "    prashant  "
c = name.strip()
print(c)               # prashant


cricket = "Virat kohli"
d = cricket.replace("Virat", "Virraaaat") 
print(d)                  # Virraaaat kohli
print(cricket)            # Virat kohli


# convert string into list 
sports = "cricket, football, badminton, volleyball"
e = sports.split(",")
print(e)                            # ['cricket', ' football', ' badminton', ' volleyball']


dish = "masala Dosa"
f = dish.find("Dosa")
print(f)                       # 7

g = dish.find("dosa")
print(g)                       # -1


fastFood = "masala puri puri puri"
h = fastFood.count("puri")
print(h)                      # 3



