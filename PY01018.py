p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    n = input()
    if n=='0': break;
    x = n.split()
    a=int(x[0])
    b=x[1]
    res = ""
    for i in b:
        for j in range (28):
            if i==p[j]:
                res = res + p[int(j+a)%28]
    res=res[::-1]
    print(res)