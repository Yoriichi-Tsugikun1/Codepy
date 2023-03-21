s = ' '+' '+input()
c = 1
for i in range(2,len(s)):
    if s[i]=='6' : continue
    elif s[i]=='8':
        if s[i-1]=='6': continue
        elif s[i-1]=='8' and s[i-2]=='6': continue
        else:
            c=0
            break
    else:
        c = 0
        break
if c==0:
    print("NO")
else : 
    print("YES")       