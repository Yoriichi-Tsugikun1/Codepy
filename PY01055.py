def kt(s):
    if len(s)%2==0: return False
    if s[0]==s[1] : return False
    if s[0]!=s[-1]: return False
    for i in range(2,len(s),2):
        if s[i]!=s[i-2]: return False
    
    return True
for _ in range(int(input())):
    s = input()
    if kt(s)==True:
        print("YES")
    else:
        print("NO")