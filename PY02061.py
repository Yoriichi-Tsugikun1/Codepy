for _ in range(int(input())):
    x,y = [int(x) for x in input().split()]
    a=[]
    for i in range(x):
        b=[int(x) for x in input().split()]
        a.append(b)
    c=[]
    for i in range(3):
        b=[int(x) for x in input().split()]
        c.append(b)

    ans = 0
    for i in range(x-2):
        for j in range(y-2):
            for k in range(0,3):
                for h in range(0,3):
                    ans = ans + a[i+k][j+h]*c[k][h]
                
    print(ans)