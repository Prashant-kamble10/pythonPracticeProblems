# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

totalPostive = 0

for nums in numbers:
    if nums > 0:
        totalPostive += 1

print(totalPostive)   # 6