import functools
def tong(n):
    s = 0
    while n!=0:
        s = s + n%10
        n=n//10
    return s

def cmp(a,b):
    if tong(a)== tong(b):
        if a > b : return 1
        else : return -1
    elif tong(a)>tong(b): return 1
    else: return -1
for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key = functools.cmp_to_key(cmp))
    print(*a)