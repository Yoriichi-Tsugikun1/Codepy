a = []
for _ in range(int(input())):
    s = input()
    b = [x for x in s.split()]
    if len(b)==6 and (len(a)==0 or a[-1]==7):
        a.append(6)
    elif len(b)==7:
        a.append(7)    
    else : continue

d = 0
ans = []
for i in a :
    if i == 6 : ans.append(1)
    if i==7 and d == 0: 
        ans.append(2)
        d = d + 1
    elif i==7 and d!=0:
        d=d+1
    if d==4 : d=0

print(len(ans))
for i in ans:
    print(i)