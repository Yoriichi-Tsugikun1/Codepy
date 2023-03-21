import re
lst = []
for _ in range(int(input())) : 
    for i in re.findall('\d+', input()) :
        lst.append(int(i))
for i in sorted(lst): print(i)