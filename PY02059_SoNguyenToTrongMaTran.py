def nto(n):
    if n < 2 : return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i==0:
            return False
    return True


n,m=[int(x) for x in input().split()]

a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
x = 0
for i in range(n):
    for j in range(m):
        if nto(a[i][j])==True and a[i][j]>x:
            x = a[i][j]
if x ==0 :
    print("NOT FOUND")
else:
    print(x)
    for i in range(n):
        for j in range(m):
            if a[i][j]==x:
                print('Vi tri ['+str(i)+ ']' + '[' + str(j) + ']')