m={}
n = int(input())
a = [int(x) for x in input().split()]

for i in range(1,n+2):
    if i not in a:
        print(i)
        break