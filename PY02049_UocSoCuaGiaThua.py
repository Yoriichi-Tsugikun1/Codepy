for _ in range(int(input())):
    x,y = [int(i) for i in input().split()]
    ans = 0 
    if x < y:
        print(0)
    else:
        for i in range(y,x+1,y):
            while i%y==0:
                ans = ans + 1
                i = int(i/y)
        
        print(ans)