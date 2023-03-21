import functools
class ThongTin:
    def __init__(self,name,ac,sub):
        self.name = name
        self.ac = ac
        self.sub = sub
    def __str__(self):
        return self.name+" "+str(self.ac)+" "+str(self.sub)
def cmp(a,b):
    if a.ac==b.ac:
        if a.sub==b.sub:
            if a.name<b.name: return -1
            else: return 1
        elif a.sub<b.sub: return -1
        else: return 1
    elif a.ac>b.ac: return -1
    else : return 1
a = []
for i in range(int(input())):
    s = input()
    m,n =[int(x) for x in input().split()]
    a.append(ThongTin(s,m,n))
a = sorted(a,key=functools.cmp_to_key(cmp))
for i in a:
    print(i)