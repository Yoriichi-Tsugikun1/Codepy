def s_u_m(a):
    n=int(a)
    s = 0
    while(n!=0):
        s=s+n%10
        n=int(n/10)
    if s%10==0 : return True
    return False
def c_(n):
    for i in range(1,len(n)):
        if abs ( int(n[i]) - int(n[i-1])) != 2 : return False
    return True
t = int(input())
for _ in range(t):
    n=input()
    if c_(n)==True and s_u_m(n)==True:
        print("YES")
    else:
        print("NO")