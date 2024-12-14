# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

animal = "cat"
age = 6

if animal == "dog":
    if age < 2:
       food =  "puppy food"

if animal == "cat":
    if age > 5:
        food = "senior cat food"

print(f"{age} old {animal} eats {food}")
    
