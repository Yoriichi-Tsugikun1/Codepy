def tang(a):
    for i in range(1,len(a)):
        if a[i]==a[i-1]: return False
    
    return True
def giam(a):

    for i in range(1,len(a)):
        if a[i-1]<=a[i]: return False
    return True
def tang_giam(n):
    if len(n)<3: return False
    c = 0
    for i in range(1,len(n)):
        if n[i]<n[i-1]:
            c = i-1
            break
    if c==0: return False
    x = n[:c]
    y = n[c:]
    if tang(x)==True and giam(y)==True: return True
    return False
for _ in range(int(input())):
    n = input()
    if tang_giam(n)==True:
        print("YES")
    else:
        print("NO")
    