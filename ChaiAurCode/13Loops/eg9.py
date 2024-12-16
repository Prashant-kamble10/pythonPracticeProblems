# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

uniqueItem =  set()

for item in items:
    if item in uniqueItem:
        print(item)
        break
    else:
        uniqueItem.add(item)