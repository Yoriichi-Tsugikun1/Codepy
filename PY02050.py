t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    st = []
    kq = []
    st.append(0)
    kq.append(1)
    for i in range(1,n):
        while len(st)!=0 and a[i]>=a[st[-1]]:
            del(st[-1])
        if len((st))==0 :
            kq.append(i+1)
        else:
            kq.append(i-st[-1])
        st.append(i)
    for i in kq:
        print(i,end=' ')
    print()