def c(a,b):
    s=''
    while b > 0:
        k = b%a
        if k>=10:
            s = s + str(chr(k+55))
        else:
            s = s + str(k)
        b=b//a
    return s[::-1]

b = input()
b=int(b,2)
print(c(8,b))