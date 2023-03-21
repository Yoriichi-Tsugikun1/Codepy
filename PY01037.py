'''
a = [0]*(10**7+1)
b = []
b.append(1)
b.append(2)
for i in range(1,10**7+1):
    for j in range(2*i,10**7,i):
        a[j]=a[j]+1

m = a[2]
for i in range(3,10**7):
    if a[i]>m:
        b.append(i)
        m=a[i]

for i in b:
    print(i,end=', ')
    '''
import sys
from bisect import bisect_left
b = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
t = int(input())
i = 0
for line in  sys.stdin:
    n = int(line)
    print(b[bisect_left(b, n)])
    i=i+1
    if i==t : break