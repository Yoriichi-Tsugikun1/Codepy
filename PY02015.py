import math
while True:
    a=[int(x) for x in input().split()]
    if a[0]==0 and a[1]==0 and a[2]==0 and a[3]==0:
        break
    else:
        b=a
        d = 0
        while True:
            if b[0]==b[1] and b[1]==b[2] and b[2]==b[3]:
                print(d)
                break
            else:
                x=b[0]
                y=b[3]
                for i in range(0,3):
                    b[i]=abs(b[i]-b[i+1])
                b[3]=abs(x-y)
                d=d+1
                