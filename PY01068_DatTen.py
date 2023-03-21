import itertools

x , y = [int(x) for x in input().split()]

a = list(set([x for x in input().split()]))

a =sorted(a)

perm = list(itertools.combinations(a,y))

for i in perm:
    for j in i:
        print(j,end=" ")
    print()