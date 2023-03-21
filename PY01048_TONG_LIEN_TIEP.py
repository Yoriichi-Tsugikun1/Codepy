import math
for i in range(int(input())):
    n = 2*int(input())

    s = 0 
    for i in range(2,int(math.sqrt(n))+1):
        if n % i==0:
            x = int(n/i)
            y = i-1
            if (x-y)%2==0:
                l=(x-y)/2
                r =x-l
                if r>l: s= s+1
            
    
    print(s)
