for _ in range(int(input())):
    a = sorted(input())
    b = sorted(input())
    print("Test " +str(_+1) + ": ",end='')
    if a==b:
        print("YES")
    else:
        print("NO")