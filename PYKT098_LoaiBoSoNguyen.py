import re
file = open("DATA.in",'r')
b= []
for i in file:
    if i[-1]=='\n':
        i = i[:-1]
    a = re.split('\s+',i)
    for i in a:
        if i.isdigit()==False:
            b.append(i)
        else:
            if int(i)>-2147483647 and int(i)<2147483647:
                continue
            else:
                b.append(i)
file.close()
b = sorted(b)
print(*b)