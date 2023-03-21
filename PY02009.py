for _ in range(int(input())):
    a=[0]*1001
    b = []
    sl = int(input())
    for i in range(sl):
        n = int(input())
        if n in b:
            a[n]=a[n]+1
        else:
            b.append(n)
            a[n]=1
    
    m = sorted(a)
    d_a = m[len(m)-1]
    b = sorted(b)
    for i in b:
        if a[i]==d_a:
            print(i)
            break