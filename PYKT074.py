for _ in range(int(input())):
    s = input()
    if len(s)<=100:
        print(s)
    else:
        n=100
        while s[n]!=' ':
            n=n-1
        print(s[:n:])