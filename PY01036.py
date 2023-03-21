t = int(input())
for _ in range(t):
    n = int(input())
    st = 0
    if n%2==0:
        st = 2
    else:
        st = 1
    s = 0 
    for i in range(st,n+1,2):
        s = s + float(1/i)
    
    print(format(s,".6f"))