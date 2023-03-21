from collections import deque
a = deque()
n = 0
def check(s):
    i = s.count('2')
    if i > len(s)-i:
        return True
    return False

a.append('1')
a.append('2')
c = []
while True:
    s = a.popleft()
    if check(s)==True: c.append(s)
    a.append(s+'0')
    a.append(s+'1')  
    a.append(s+'2')
    if len(c)==1001:
        break
c = sorted(c,key=lambda x: len(x))
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        print(c[i],end=' ')
    print()