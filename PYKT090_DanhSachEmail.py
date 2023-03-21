file = open("CONTACT.in", "r")

m = {}
for i in file:
    if i[-1]=='\n':
        i=i[:-1]
    else:
        i=i
    m[i.lower()]=1
m = sorted(m)
for i in m:
    print(i)