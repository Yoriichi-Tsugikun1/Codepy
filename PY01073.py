import itertools 
  
listA = list(input())
perm = itertools.permutations(listA) 
  
for i in list(perm): 
    for j in i:
        print(j,end='')
    print()