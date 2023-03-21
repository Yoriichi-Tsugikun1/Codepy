a=[11]*11
n = 0
v = []
def out(i):
    b=[]
    for j in range(1,i+1):
        b.append(a[j])
    v.append(b)

def Try(i,s):
    for j in range(n,0,-1):
        if s -j>=0 and j<=a[i-1]:
            s=s-j
            a[i]=j
            if s==0:
                out(i)
            else:
                Try(i+1,s)
            s=s+j

for _ in range(int(input())):
    n=int(input())
    a = [11]*11
    v = []
    Try(1,n)
    print(len(v))
    for i in v:
        print("(",end='')
        print(*i,end='')
        print(")",end=' ')
    print()