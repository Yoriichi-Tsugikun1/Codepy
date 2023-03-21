import math
def dem(n):
    lm = int(math.sqrt(n))
    prime = [int(x) for x in range(lm+1)]
    # tìm ước số nguyên tố nhỏ nhất
    i=2
    while i*i<=lm: 
        if prime[i]==i:
            for j in range(i*i,lm+1,i):
                if prime[j]==j:
                    prime[j]=i
        i=i+1
    d = 0 
    # dạng số có 9 chữ số là các số có dang (q*p)^2 trong đó p q là số nguyên tố hoặc
    # số i^8 <=n là  số có 9 chữ số  
    for i in range(2,lm+1):

        p = prime[i] 

        q = prime[i//prime[i]]

        if p*q==i and q!=1 and q!=p:
            d=d+1
        elif prime[i]==i:
            if i**8<=n:
                d=d+1

    return d

n = int(input())
print(dem(n))