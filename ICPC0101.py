n=int(input())
a=[]
for i in map(int,input().split()):
    if len(a)==0: a.append(i)
    elif (a[-1]+i)%2==0:
        del(a[-1])
    else : a.append(i)
print(len(a))