# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = 10
sumEvenNumber = 0

for nums in range(0, n+1):
    if nums%2 == 0:
        sumEvenNumber += nums

print(sumEvenNumber)
