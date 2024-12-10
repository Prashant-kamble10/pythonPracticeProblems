list1 = [1,2,3]
print(list1)        # [1, 2, 3]

list2 = list1
print(list2)        # [1, 2, 3]

list1 = 'cricket'
print(list1)       # cricket

print(list2)         # [1, 2, 3]

list1 = [1,2,3]
print(list1)        # [1, 2, 3]

print(list2)        # [1, 2, 3]

list1[0] = 22
print(list1)        # [22, 2, 3]

print(list2)       # [1, 2, 3]