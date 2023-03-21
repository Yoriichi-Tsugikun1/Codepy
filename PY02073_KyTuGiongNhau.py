for _ in range(int(input())):
    n = int(input())
    F=[0]*(n+1)
    
    x , y , z = [int(x) for x in input().split()]

    F[1]=x
    for i in range(2,n+1):
        if i%2==0:
            F[i] = min(F[i-1]+x,F[i//2]+z)
        else:
            F[i]=min(F[i-1]+x,F[i//2+1]+y+z)
    
    print(F[n])