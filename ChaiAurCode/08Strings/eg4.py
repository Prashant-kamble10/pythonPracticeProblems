name = "prashant"

for letter in name:
    print(letter)

# p
# r
# a
# s
# h
# a
# n
# t


chai = "I love \"coffee\" "
print(chai)                       # I love "coffee"

playerName = "Virat\nkohli"
print(playerName)

# Virat
# kohli

# raw string I want 
playerName = r"Virat\nkohli"
print(playerName)                       # Virat\nkohli

path = r"c:\user\pwd"
print(path)                          # c:\user\pwd

path1 = "c:\\user\\pwd"
print(path1)                            # c:\user\pwd


fastFood = "masala puri"
print("masala" in fastFood)          # True
print("masalaaaa" in fastFood)       # False
