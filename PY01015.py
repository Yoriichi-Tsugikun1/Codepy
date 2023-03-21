def kg(n):
    for i in range(1,len(n)):
        if n[i-1]>n[i] : return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    if kg(n)==True: print("YES")
    else : print("NO")