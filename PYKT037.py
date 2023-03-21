def chuyen(a,b):
    s=''
    while b!=0:
        k = int(b%a)
        if k >=10:
            s = s + str(chr(k+55))
        else:
            s = s + str(k)
        b =b//a
    
    return s[::-1]


for _ in range(int(input())):
    a , b = [int(x) for x in input().split()]

    print(chuyen(b,a))
