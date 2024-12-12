sports = {
    "cricket" : {
    "opener" : "rohit",
    "middleOrder": "virat",
    "finisher" : "rinku"
    },

    "pune" : "hinjewadi",
    "navi mumbai" : "airoli"
}

print(sports["cricket"]["opener"])    # rohit
print(sports["navi mumbai"])         # airoli

squaredNums = {x:x**2 for x in range(6)}
print(squaredNums)       # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squaredNums.clear()
print(squaredNums)      # {}