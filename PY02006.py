for _ in range(int(input())):
    n = int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    a.sort()
    b.sort()
    c=0
    for i in range(n):
        if a[i]>b[i]:
            c=1
            break
    
    if c==0:
        print("YES")
    else:
        print("NO")