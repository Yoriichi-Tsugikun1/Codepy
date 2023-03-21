n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [0] * (k + 1)
m = set(a)
a = sorted(list(m))
n = len(a)
def T(i):
    for j in range(b[i-1]+1,n+1):
        b[i]=j
        if i==k:
            for h in range(1,k+1):
                print(a[b[h]-1],end=' ')
            print()
        elif i<k:
            T(i+1)
T(1)