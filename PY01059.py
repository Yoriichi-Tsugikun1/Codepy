t = int(input())
for _ in range(t):
    s = 0
    t = 1
    c = 0
    n = input()
    for i in range(len(n)):
        if i%2==0: s = s + int(n[i])
        else : 
            if n[i]=='0' : continue
            else:
                c = 1
                t = t * int(n[i])
    
    if c==0:
        print(s,end=' ')
        print(0)
    else:
        print(s,end=' ')
        print(t)