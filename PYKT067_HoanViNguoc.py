import itertools

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in range(n,0,-1)]
    
    per = itertools.permutations(a)
    per = list(per)
    print(len(per))
    for i in per:
        for j in i:
            print(j,end='')
        print(end=' ')
    print()