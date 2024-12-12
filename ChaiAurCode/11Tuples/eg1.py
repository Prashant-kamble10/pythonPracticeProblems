#  list is mutuable

# Tuples is immutuable

players = ("rohit", "virat", "rinku")

print(players[0])   # rohit
print(players[-1])   # rinku
print(players[1:])   # ('virat', 'rinku')

# players[2] = "raina"
# print(players)        # TypeError: 'tuple' object does not support item assignment

print(len(players))    # 3

morePlayers = ("dhoni", "bumrah")

allPlayers = players + morePlayers
print(allPlayers)      # ('rohit', 'virat', 'rinku', 'dhoni', 'bumrah')


if "rohit" in players:
    print("rohit exist")         # rohit exist





