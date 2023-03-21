
for _ in range(int(input())) :
    a = [int(x) for x in input().split()]
    
    A = complex(a[0], a[1])
    B = complex(a[2], a[3])

    C = (A + B) * A
    D = (A + B) ** 2

    print(str(int(C.real)) + ' + ' + str(int(C.imag)) + 'i,', end = ' ')
    print(str(int(D.real)) + ' + ' + str(int(D.imag)) + 'i')