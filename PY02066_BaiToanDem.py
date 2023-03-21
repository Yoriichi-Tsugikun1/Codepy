n = int(input())
a = []
while True:
    a = a + [int(x) for x in input().split()]
    if len(a)==n:
        break
kt = 0
for i in range(1,max(a)):
    if i not in a:
        print(i)
        kt =1 
if kt==0:
    print("Excellent!") 