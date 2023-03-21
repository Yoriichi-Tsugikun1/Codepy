t = int(input())
for _ in range(t):
    n = input()
    s = 0
    for i in n:
        s = s + int(i)
    
    a = str(s)
    if a == a[::-1] and len(a)>1: print("YES")
    else : print("NO")