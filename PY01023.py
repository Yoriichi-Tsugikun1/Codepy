import math
t = int(input())
for _ in range(t):
    s = int(input())
    ans = '1' 
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            ans = ans + ' * '
            d = 0
            while s%i==0:
                s=int(s/i)
                d=d+1
            ans = ans + str(i)+ '^' + str(d)
    if s > 1 :
        ans = ans + ' * ' + str(s) + '^' + str(1)
    print(ans)