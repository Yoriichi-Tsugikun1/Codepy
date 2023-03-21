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
file = open('DATA.in', 'r')
n = int(file.readline())
for _ in range(n):
    a = int(file.readline().strip())
    b = file.readline()
    b = int(b,2)
    print(c(a,b))