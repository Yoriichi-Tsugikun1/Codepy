for _ in range(int(input())):
    s = input()
    a ,kq = [],[]
    d = 1
    for i in s:
        if i=='(':
            a.append(d)
            kq.append(d)
            d = d + 1
        elif i==')':
            kq.append(a.pop())
        else: continue
    print(*kq)