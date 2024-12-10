# library used in python regarding Numbers

import math
import random

# math.floor()
# math.trunc()

a = random.randint(1, 10)
print(a)

list = ["infosys", "accenture", "tcs", "parentpay"]
print(random.choice(list))

random.shuffle(list)
print(list)

set1 = {1,2,3,4}
print(type({}))       # <class 'dict'>