import re
n=int(input())
for j in range(n):
    m = input()
    ans = 10**20
    kq = re.findall('\d{1,}',m)
    for _ in kq:
        if ans > int(_):
            ans = int(_)
    print(ans)