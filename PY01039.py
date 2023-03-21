t = int(input())
for _ in range(t):
    n = input()
    c = 1
    for i in range(0,len(n)-2,1):
        if n[i]!=n[i+2]: 
            c=0
            break
    if c==1: print("YES")
    else : print("NO")