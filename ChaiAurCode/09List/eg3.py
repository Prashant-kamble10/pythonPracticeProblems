sports = ["cricket", "football", "volleyball", "badminton"]

for i in sports:
    print(i)

# cricket
# football
# volleyball
# badminton


for i in sports:
    print(i, end="-")              # cricket-football-volleyball-badminton-

sports.append("table tennis")
print(sports)                         # ['cricket', 'football', 'volleyball', 'badminton', 'table tennis']

if "table tennis" in sports:
    print("True")                      # True

sports.remove("football")
print(sports)                          # ['cricket', 'volleyball', 'badminton', 'table tennis']

sports.insert(1, "boxing")
print(sports)                       # ['cricket', 'boxing', 'volleyball', 'badminton', 'table tennis']

