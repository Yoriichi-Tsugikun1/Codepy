ke = []

n = int(input())

for i in range(n+1): ke.append([])

for i in range(n-1):
    x,y=[int(x) for x in input().split()]
    ke[x].append(y)
    ke[y].append(x)
kt = 0
for i in ke:
    if len(i)==n-1:
        kt = 1
        print("Yes")
        break
if kt==0:
    print("No")