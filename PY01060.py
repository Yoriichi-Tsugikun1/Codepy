t = int(input())
for _ in range(t):
    s = 0
    t = 1
    c = 0
    n = input()
    for i in range(len(n)):
        if i%2==1: s = s + int(n[i])
        else : 
            if n[i]=='0' : continue
            else:
                c = 1
                t = t * int(n[i])
    
    if c==0:
        print(0,end=' ')
        print(t)
    else:
        print(t,end=' ')
        print(s)