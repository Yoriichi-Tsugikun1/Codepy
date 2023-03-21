for _ in range(int(input())):
    n = int(input())
    m = {}
    for i in map(int, input().split()):
        if i in m:
            m[i]=m[i]+1
        else:
            m[i]=1
    
    for i in m:
        if m[i]%2==1:
            print(i)
            break