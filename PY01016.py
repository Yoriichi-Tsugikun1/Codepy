t = int(input())
for _ in range(t):
    s = input()
    for i in range(len(s)):
        if s[i]>='1' and s[i]<='9':
            for j in range(int(s[i])):
                print(s[i-1],end='')
    
    print()