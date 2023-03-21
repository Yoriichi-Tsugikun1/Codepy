import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def kc(self,a):
        return float(math.sqrt((self.x-a.x)**2+(self.y-a.y)**2))

class Triangle:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    
    def area(self):
        kc1 = self.a.kc(self.b)
        kc2 = self.a.kc(self.c)
        kc3 = self.b.kc(self.c)
        if kc1 + kc2 <= kc3 or kc1 + kc3 <= kc2 or kc2 + kc3 <= kc1:
            print("INVALID")
        else:
            s = math.sqrt((kc1+kc2+kc3)*(kc1+kc2-kc3)*(kc1-kc2+kc3)*(-kc1+kc2+kc3))/4
            print('{:.2f}'.format(s))
t = int(input())
a = []
for _ in range(t):
    a = a + [float(j) for j in input().split()]

for i in range(0,t*6,6):
    p1 = Point(a[i], a[i + 1])
    p2 = Point(a[i + 2], a[i + 3])
    p3 = Point(a[i + 4], a[i + 5])
    triangle = Triangle(p1, p2, p3)
    triangle.area()