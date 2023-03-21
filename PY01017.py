t = int(input())
for _ in range(t):
    s = input()
    l,r=0,0
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            print(i+1-l,end='')
            print(s[i],end='')
            l=i+1
    print(len(s)-l,end='')
    print(s[-1],end='')
    print()