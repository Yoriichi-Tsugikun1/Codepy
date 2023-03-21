e = 10**9
for _ in range(int(input())):
    ind = int(input())
    s = input()
    n = int(len(s)/3)
    while s[n]!=' ':
        n=n-1
    a = s[:n]
    s=s[n:]
    x,y,z = e,e,e
    for i in map(int,a.split()):
        if i>=z : continue
        if i<=x:
            z,y,x=y,x,i
        if i > x and i <=y:
            z,y=y,i
        if i>y and i<z:
            z=i
    
    n = len(s)//2
    while s[n]!=' ':
        n=n-1
    for i in map(int,s[:n].split()):
        if i>=z : continue
        if i<=x:
            z,y,x=y,x,i
        if i > x and i <=y:
            z,y=y,i
        if i>y and i<z:
            z=i
    
    for i in map(int,s[n:].split()):
        if i>=z : continue
        if i<=x:
            z,y,x=y,x,i
        if i > x and i <=y:
            z,y=y,i
        if i>y and i<z:
            z=i
    
    print(x+y+z)