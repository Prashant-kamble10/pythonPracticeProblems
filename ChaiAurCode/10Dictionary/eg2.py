cricket = {
    "opener" : "rohit",
    "middleOrder": "virat",
    "finisher" : "rinku"
}

if "opener" in cricket:
    print("opener exist")         # opener exist

print(len(cricket))          # 3

cricket["spiner"] = "axar"
print(cricket)  # {'opener': 'rohit', 'middleOrder': 'virat', 'finisher': 'rinku', 'spiner': 'axar'}

cricket.pop("finisher")
print(cricket)   # {'opener': 'rohit', 'middleOrder': 'virat', 'spiner': 'axar'}

del cricket["spiner"]
print(cricket)        # {'opener': 'rohit', 'middleOrder': 'virat'}





