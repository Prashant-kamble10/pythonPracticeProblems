cricket = {
    "opener" : "rohit",
    "middleOrder": "virat",
    "finisher" : "rinku"
}

print(cricket)       # {'opener': 'rohit', 'middleOrder': 'virat', 'finisher': 'rinku'}
print(cricket["opener"])    # rohit

print(cricket.get("finisher"))   # rinku


print(cricket.get("finisherrrrr"))    # None
# print(cricket["middleOrderrrrr"])        # KeyError: 'middleOrderrrrr'

cricket["opener"] = "yashavi"
print(cricket)                 # {'opener': 'yashavi', 'middleOrder': 'virat', 'finisher': 'rinku'}



for players in cricket:
    print(players)

# opener
# middleOrder
# finisher

for players in cricket:
    print(players, cricket[players])

# opener yashavi
# middleOrder virat
# finisher rinku

for key,value in cricket.items():
    print(key, value)

# opener yashavi
# middleOrder virat
# finisher rinku

