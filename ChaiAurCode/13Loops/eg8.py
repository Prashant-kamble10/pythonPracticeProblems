# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = 20

isPrime =True

if number > 0:
    for num in range(2,number):
        if number%num == 0:
            isPrime = False
            break
        
print(isPrime)

