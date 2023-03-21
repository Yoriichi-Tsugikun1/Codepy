x,y = [int(x) for x in input().split()]

a = sorted(list(set([int(i) for i in input().split()])))
b = sorted(list(set([int(i) for i in input().split()])))
if a==b:
    print("YES")
else:
    print("NO")