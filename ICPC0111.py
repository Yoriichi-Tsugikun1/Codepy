t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().split()]
    s=input().split()
    for i in range(m,len(s)):
        print(s[i],end=' ')
    for i in range(m):
        print(s[i],end=' ')
    print()