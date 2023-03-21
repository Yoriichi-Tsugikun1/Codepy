
n, m = [int(x) for x in input().split()]

a = [[]] * n

for i in range(n) :
    a[i] = [int(x) for x in input().split()]

x = 0
for i in range(n) :
    for j in range(m) :
        if a[i][j] > x and str((a[i][j])) == str((a[i][j]))[::-1]  and len(str(a[i][j])) > 1 :   
            x = a[i][j]

if x == 0 : print('NOT FOUND')
else : print(x)

for i in range(n) :
    for j in range(m) :
        if a[i][j] == x :
            print('Vi tri [' + str(i) + '][' + str(j) + ']')