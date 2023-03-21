while True:
    n=int(input())
    if n==0 :
        break
    a=[]
    for i in range(n):
        a.append(int(input()))
    a=sorted(a)
    if a[0]==a[-1]:
        print("BANG NHAU")
    else:
        print(a[0],a[-1])