def kt(n):
    for i in n:
        if i<'0' or i>'3': return False
    return True
for _ in range(int(input())):
    n = input()
    if kt(n)==True:
        print("YES")
    else:
        print("NO")