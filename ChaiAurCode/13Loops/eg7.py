# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

number =  10

while True:
    if number >= 1 and number <= 10:
        print("valid")
        break
    else:
        print("Invalid")
        break