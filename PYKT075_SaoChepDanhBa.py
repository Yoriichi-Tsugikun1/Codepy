import functools
class ThongTin:
    def __init__(self,name,sdt,date):
        self.name = name
        self.sdt = sdt
        self.date = date
        self.hd = ''
        m = name.split()
        for i in range(1,len(m)-1):
            self.hd = self.hd+m[i]+" "
        self.hd = self.hd.strip()
    def __str__(self):
        return self.name+": "+self.sdt+" "+self.date
def cmp(a,b):
    if a.name.split()[-1]==b.name.split()[-1]:
        if a.hd<b.hd: return -1
        else: return 1
    if a.name.split()[-1]<b.name.split()[-1]: return -1
    else: return 1
file = open('SOTAY.txt','r')
a = []
x = ''
x1 =''
for i in file :
    if i[-1]=='\n':
        i=i[:-1]
    m=i.split()
    if m[0]=='Ngay':
        x = m[1]
        continue
    elif i.isdigit() :
        a.append(ThongTin(x1,i,x))
    else:
        x1 = i
a = sorted(a,key=functools.cmp_to_key(cmp))
for i in a :
    print(i)