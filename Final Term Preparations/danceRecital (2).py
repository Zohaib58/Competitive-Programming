from sys import stdin
from itertools import permutations
import math

lines = stdin.read().splitlines()

counter = int(lines[0])

for i in range(1, counter + 1):   
  strc = lines[i]
  bitVal = 0b0 
  for char in strc:
    bitVal |= (1 << (ord(char) - ord('A'))) 

  lines[i] = bitVal



minimum = math.inf 

for p in permutations(lines[1:]):
  if p[0] <= p[-1]:
    count = 0

    for i in range(counter - 1):
      a = p[i] & p[i + 1]

      
      while a:
        a &= (a - 1)
        count += 1

    minimum = min(count, minimum)



print(minimum)

