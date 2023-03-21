import math
class Point:
    def __init__(self,x,y): 
        self.x = x
        self.y = y
    
    def distance(self, tmp):
        x1 = self.x - tmp.x
        y1 = self.y - tmp.y
        kc = math.sqrt(x1 ** 2 + y1 ** 2)
        return float(kc)
class Triangle:
    def __init__(self, p1, p2, p3) :
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def xuLy(self) :
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        if a + b > c and a + c > b and b + c > a : 
            print('{:.3f}'.format(a + b + c))
        else :
            print('INVALID')
t = int(input())
a = []
for _ in range(t):
    a = a + [float(j) for j in input().split()]

for i in range(0,t*6,6):
    p1 = Point(a[i], a[i + 1])
    p2 = Point(a[i + 2], a[i + 3])
    p3 = Point(a[i + 4], a[i + 5])
    triangle = Triangle(p1, p2, p3)
    triangle.xuLy()