t = int((input()))
for _ in range(t):
    a = input().strip()
    s = ""
    s = s + a[len(a)-2] + a[len(a)-1]
    if int(s)==86:
        print("YES")
    else:
        print("NO")