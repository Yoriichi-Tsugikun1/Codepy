class Rectangle:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color.title()
    def output(self):
        if self.w <= 0 or self.h <= 0: 
            print("INVALID")
        else:
            perimeter = (self.w + self.h) * 2
            area = self.w * self.h
            print(perimeter, area, self.color)

a = input().split()
tmp = Rectangle(int(a[0]), int(a[1]), a[2])
tmp.output()