a = list(input().lower().split())
b = list(input().lower().split())
m=set(a)
n=set(b)
ans=sorted(set(m|n))
for i in ans:
    print(i,end=' ')
print()
ans1 = sorted(set(m&n))
for i in ans1:
    print(i,end=' ')