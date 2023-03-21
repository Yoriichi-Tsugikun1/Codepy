for _ in range(int(input())):
    s = input()
    a=""
    t=0
    for i in s:
        if i.isalpha():
            a = a+str(i)
        else :
            t = t + int(i)

    a = sorted(a)
    for i in a:
        print(i,end='')
    print(t)