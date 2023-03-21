n = input()

while len(n)!=1:
    m = len(n)//2
    s = int(n[:m:])
    s1 = int(n[m::])
    print(s+s1)
    n = str(s+s1)