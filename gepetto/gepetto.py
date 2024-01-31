from sys import stdin 

lines = stdin.read().splitlines()

N, M = (lines[0].split(" "))
N, M = (int(N)), (int(M)) 

pc = set()

for i in range(1, M + 1):
   f, s = lines[i].split(" ")
   f, s = int(f), int(s)
   
   pc.add((1 << (f - 1)) | (1 << (s - 1)))


res = 1
for i in range(1, 2**N):
   
   isPc = False   

   for p in pc:
      if ((p & i) == p):
        isPc = True
        break

   if (not isPc):
      res += 1
         
print(res)

