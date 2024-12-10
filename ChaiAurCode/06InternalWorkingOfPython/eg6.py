n = [1,2,3]
print(n)      # [1, 2, 3]

m = n
print(m)       # [1, 2, 3]

res1 = m == n      # here it compare the value
print(res1)       # True
res2 = m is n      # here it compare the memory reference
print(res1)       # True

m = [1,2,3]

res3 = m == n
print(res3)        # True
res4 = m is n
print(res4)        # False