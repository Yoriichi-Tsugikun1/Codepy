def thapHN(n,a,b,c):
    if n==1 : print(a + ' -> ' + c)
    else:
        thapHN(n-1, a, c, b)
        thapHN(1, a, b, c)
        thapHN(n-1, b, a, c)

n = int(input())
thapHN(n, 'A', 'B', 'C')