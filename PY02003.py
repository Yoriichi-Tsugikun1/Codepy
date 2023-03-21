m = { 1 : 1 }
while True:
   a = []

   for i in m:
      if i < 10**18:
         if not((i*2) in m):
            a.append(i*2)
         if not((i*3) in m):
            a.append(i*3)
         if not((i*5) in m):
            a.append(i*5)
      
   if len(a)==0: break
   for i in a:
      m[i]=1

a = sorted(list(m))
d = 1
for i in a:
   m[i]=d
   d=d+1
for _ in range(int(input())):
   n = int((input()))
   if n in m:
      print(m[n])
   else:
      print("Not in sequence")