m = {}
for i in range(int(input())):
    a = [x for x in input().split()]

    if a[3].lower()=='in':
        id = 0
        if a[1]=='Xe_con':
            if a[2]=='5': id = 10000
            else : id = 15000
        elif a[1]=='Xe_tai':
            id = 20000
        elif a[1]=='Xe_khach':
            if a[2]=='29': id = 50000
            else: id = 70000
        if a[4] in m:
            m[a[4]]+=id
        else:
            m[a[4]]=id
    
for i in m :
    print(i + ': ' + str(m[i]))