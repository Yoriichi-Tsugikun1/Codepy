for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    d = 0
    for i in range(len(a)-2):
        x=a[i]
        l,r = i+1,len(a)-1

        while l < r:
            s = x+a[l]+a[r]
            if s==0: 
                d=d+1
                l=l+1
            elif s>0:
                r=r-1
            else:
                l=l+1
    print(d)