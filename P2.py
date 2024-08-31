# taking input from the user

takeInput = input("enter your name:")
print(" your name:", takeInput)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# slicing on text 
# string[start:end:step]
name = "prashant"
output = name[5:8]      # ant
print(output)

# reverse string 
reverse = name[::-1]
print(reverse)      # tnahsarp

# concatentation of string
name1 = "prashant"
name2 = "kamble"
res = name1 +" "+ name2
print(res)

# finding length of string
name3 = "prashant"
result = len(name3)
print(result) 