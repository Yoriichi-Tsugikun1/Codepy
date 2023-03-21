from collections import deque
n=int(input())

a = deque()
c = []
a.append('2')
a.append('3')
a.append('5')
a.append('7')
while True:
    s = a.popleft()
    
    if len(s)>n:
        break
    a.append(s+'2')
    a.append(s+'3')
    a.append(s+'5')
    a.append(s+'7')
    
    
    if len(set(list(s)))==4 and s[-1]!='2':
        c.append(s)

c = sorted(c, key=lambda x: len(x))
for i in c:
    print(i)