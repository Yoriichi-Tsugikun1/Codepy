s = input()
dt = 0
dh = 0
for i in s:
    if i >= 'a' and i <= 'z': dt=dt+1
    elif i>='A' and i<='Z' : dh=dh+1
if dt>=dh:
    print(s.lower())
else:
    print(s.upper())