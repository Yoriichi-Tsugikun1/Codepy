t = int(input())

for _ in range(t):
    n = int(input())
    kt = int(0)
    for i in range(1000):
        if n % 7 == 0: 
            print(n)
            kt=1
            break
        n = n + int(str(n)[::-1])
    if kt == 0: print(-1)