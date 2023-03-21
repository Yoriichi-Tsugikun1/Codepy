a=[]
b = set()
while True:
    a = a + [int(x) for x in input().split()]
    for i in a:
        b.add(i%42)
    if len(a)==10: break
print(len(b))