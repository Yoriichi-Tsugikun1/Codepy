n = int(input())
a = [int(x) for x in input().split()]
ans = 0
def kt(x):
    for i in a:
        if int(i/x)==int(i/(x+1)):
            return False
    return True
for i in range(min(a),0,-1):
    if kt(i)==True:
        for j in range(n):
            ans = ans + int(a[j]/(i+1))+1
        break
print(ans)