x,y = [int(x) for x in input().split()]

a = sorted(set([int(x) for x in input().split()]))
b = sorted(set([int(x) for x in input().split()]))

c = set(set(a)&set(b))
print(*sorted(c))
print(*sorted(set(a).difference(set(b))))
print(*sorted(set(b).difference(set(a))))