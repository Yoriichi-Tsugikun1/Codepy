t = int(input())
for i in range(t):
    n=input()
    ans = ""
    m = int(len(n)-1)
    a=n[m]
    while m>0:
        if a>='5':
            ans='0'+ans
            a=chr(int(n[m-1])+1+48)
        else :
            ans='0'+ans
            a=n[m-1]
        m=m-1
    if a>'9':
        ans='10'+ans
    else:
        ans=a+ans
    print(ans)