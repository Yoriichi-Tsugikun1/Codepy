for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a=sorted(a)
    minn = a[0]
    maxx = a[-1]

    d = 0
    for i in range(minn,maxx):
        if i not in a:
            d = d + 1

    print(d)