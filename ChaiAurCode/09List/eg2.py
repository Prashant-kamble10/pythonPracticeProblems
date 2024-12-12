tea = ["ginger", "masala", "lemon", "black"]
print(tea[1:1])                   # []

tea[1:2] = "lemon"
print(tea)                      # ['ginger', 'l', 'e', 'm', 'o', 'n', 'lemon', 'black']

tea = ["ginger", "masala", "lemon", "black"]
tea[1:2] = ["lemon"]
print(tea)                     # ['ginger', 'lemon', 'lemon', 'black']

tea[1:3] = ["normal", "herbal"]
print(tea)                     # ['ginger', 'normal', 'herbal', 'black']


tea[2] = []
print(tea)              # ['ginger', 'normal', [], 'black']