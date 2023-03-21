import re
a = []
while True:
    try:
        a.append(input())
    except EOFError:
        break

for i in a:
    if i[-1]!='.' and i[-1]!='?' and i[-1]!='!':
        i=i+'.'
    m = re.split('\s+',i.lower())
    m[0]= m[0].title()
    
    s=''
    for j in range(len(m)-1):
        s=s+str(m[j])+' '
    if m[-1]=='?' or m[-1]=='!' or m[-1]=='.':
        s = s.strip()+str(m[-1])
    else:
        s= s + str(m[-1])
    print(s)