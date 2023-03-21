for _ in range(int(input())):
    x,y,z = [int(i) for i in input().split()]

    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    
    i = 0
    i1 =0
    i2 =0
    ok = 0
    while i < x and i1 < y and i2 < z:
        if a[i]==b[i1]==c[i2]:
            ok=1
            print(a[i],end=' ') 
            i=i+1
            i1=i1+1
            i2=i2+1
        elif a[i]<b[i1] or a[i]<c[i2]: i=i+1
        elif b[i1]<c[i2] or b[i1]<a[i]: i1 = i1 +1 
        elif c[i2]<a[i] or c[i2]<b[i1]: i2 = i2 + 1
    if ok==0:
        print("NO",end=' ')
    print()