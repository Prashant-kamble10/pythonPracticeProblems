list1 = [1,2,3]
print(list1)        # [1, 2, 3]

list2 = list1
print(list2)        # [1, 2, 3]

list1[0] = 44
print(list1)        # [44, 2, 3]

print(list2)        # [44, 2, 3]
# reason = list,sets,dict are mutuable.



