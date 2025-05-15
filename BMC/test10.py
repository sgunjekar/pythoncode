import copy
import os
a = [[1, 2], [3, 4]]
b = copy.copy(a)      # shallow copy
c = copy.deepcopy(a)  # deep copy
b[1][1] = '8'
b.extend('5')
c.extend('6')
print(a)
print(b)
print(c)

import math
math.sqrt = lambda x: x**2
print(math.sqrt(6))  # 4

db_usr= os.environ.get("db_user")
print(db_usr)
