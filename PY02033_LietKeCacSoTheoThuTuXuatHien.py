s = input()

if len(s)%2==1: 
    s = s[:len(s)-1]

a = []
for i in range(0,len(s),2):
    if int(s[i]+s[i+1]) in a :
        continue
    else:
        a.append(int(s[i]+s[i+1]))

for i in a :
    print(i,end= ' ')