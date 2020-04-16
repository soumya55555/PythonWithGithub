import Demo.myModule as dm
import random
import math
import datetime
import calendar
import os
num=[10,20,30,40,100]
index=dm.find_index(num,30)
print(index)

# random_num=random.choice(num)
# print(random_num)

# sq_num=math.sqrt(8)
# print(sq_num)

today=datetime.date.today()
print(today)
print(calendar.isleap(2020))
print(os.getcwd())
print(os.__file__)

