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

all_permutations = permutations(lines[1:])

minimum = math.inf 

for p in all_permutations:
  count = 0

  for i in range(counter - 1):
    a = p[i] & p[i + 1]


    while a:
      count += a & 1
      a >>= 1

minimum = min(count, minimum)



print(minimum)

