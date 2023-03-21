for _ in range(int(input())):
    x,y = [int(x) for x in input().split()]
    a = []
    b = []
    for i in map(int,input().split()):
        if i < 0 : 
            a.append(i)
        else:
            b.append(i)
    
    i = b.index(max(b))
    b.insert(i,y)
    for i in a :
        print(i,end=" ")
    for i in b :
        print(i,end=" ")
    print()