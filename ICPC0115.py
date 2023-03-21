def gt(n):
    gth = int(1)
    for i in range(1,int(n)+1):
        gth=gth*int(i)
    return gth

t = int(input())
for _ in range(t):
    n = input()
    s= int(0)
    for i in range(len(n)):
        s = s + gt(n[i])
    if s == int(n): print("Yes")
    else: print("No")