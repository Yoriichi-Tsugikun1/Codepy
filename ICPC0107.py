for _ in range(int(input())):
    x,y = [i for i in input().split()]
    s = input().strip()
    if ' ' in s:
        a,b=[i for i in s.split()]
    else:
        a=s
        b=input()
    maxx = max(x,y)
    minn = min(x,y)

    mi1 = a.replace(maxx,minn)
    mi2 = b.replace(maxx,minn)
    print(int(mi1)+int(mi2),end=' ')
    ma1 = a.replace(minn, maxx)
    ma2 = b.replace(minn, maxx)
    print(int(ma1)+int(ma2))
    