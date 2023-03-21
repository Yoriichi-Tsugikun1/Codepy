import math
import re

n = input()
d4 = int(0)
d7 = int(0)
for i in n:
    if i=='4':
        d4 = d4+1
    if i=='7':
        d7 = d7 +1
if d4+d7==4 or d4+d7==7:
    print("YES")
else :
    print("NO")