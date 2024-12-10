h1 = [1,2,3]
print(h1)      # [1, 2, 3]

h2 = h1[:]      # here it is not referencing to same memory location, h2 has made a seperate copy
print(h2)       # [1, 2, 3]

h1[0] = 88
print(h1)       # [88, 2, 3]

print(h2)       # [1, 2, 3]
# reason = here it is not referencing to same memory location, h2 has made a seperate copy