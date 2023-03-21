class ThiSinh:
    def __init__(self,name,ns,d1,d2,d3):
        self.name = name.title()
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.t = d1+d2+d3
    def __str__(self):
        return f"{self.name} {self.ns} {'{:.1f}'.format(self.t)}"
namei = input()
nsi = input()
d1i = float(input())
d2i = float(input())
d3i = float(input())

a = ThiSinh(namei,nsi,d1i,d2i,d3i)
print(a)