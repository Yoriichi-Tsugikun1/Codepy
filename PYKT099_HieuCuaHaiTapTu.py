import re
file = open('DATA1.in','r')
a = []
for i in file:
    if i[-1]=='\n':
        i = i[:-1]
    for j in re.split('\s+',i.lower()) :
        if j != '':
            if j not in a:
                a.append(j)
            else :continue
        else : continue

file1 = open('DATA2.in','r')
b=[]
for i in file1:
    if i[-1]=='\n':
        i = i[:-1]
    for j in re.split('\s+',i.lower()):
        if j !='':
            if j not in b:
                b.append(j)
            else :continue
        else : continue
a = sorted(a)
b = sorted(b)
for i in a:
    if i not in b:
        print(i,end=' ')
print()
for i in b:
    if i not in a:
        print(i,end=' ')