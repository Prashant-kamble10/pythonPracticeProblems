tea = ["ginger", "masala", "lemon", "black"]
print(tea[1:3])         # ['masala', 'lemon']
print(tea[:2])          # ['ginger', 'masala']
print(tea[2:])          # ['lemon', 'black']

a = len(tea)-1
print(tea[a])         # black

tea[1] = "normal"
print(tea)               # ['ginger', 'normal', 'lemon', 'black']