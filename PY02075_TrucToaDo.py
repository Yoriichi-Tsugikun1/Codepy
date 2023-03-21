import functools
class ThongTin:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def cmp(a,b):
    if a.y==b.y:
        if a.x<b.x: return -1
        else: return 1
    if a.y<b.y: return -1
    else : return 1
for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        x,y = [int(x) for x in input().split()]
        a.append(ThongTin(x,y))
    a = sorted(a,key=functools.cmp_to_key(cmp))
    ans = 1
    k = a[0].y
    for i in range(1,n):
        if a[i].x>=k:
            ans = ans + 1
            k = a[i].y 
    print(ans) 
        