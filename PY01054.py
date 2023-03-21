for _ in range(int(input())):
    n = input()
    if int(n)==0:
        print(0)
    else:
        t = 1 
        for i in n:
            if i=='0' : continue
            else :
                t = t * int(i)
        print(t)