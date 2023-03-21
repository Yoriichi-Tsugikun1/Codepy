t = int(input())

for i in range(t):
    n = input()
    kt = int(0)
    for i in n:
        if i!='4' and i!='7':
            kt=1
            break
    
    if kt==0: print("YES")
    else : print("NO")