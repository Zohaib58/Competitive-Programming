from sys import stdin
from itertools import permutations
import heapq



#30th is 4,6,9, 11
def isValid(d, m, y):
    if (y < 2000):
        return False
    elif (m < 1 or m > 12):
        return False
    else:
        if (m == 2):
            if (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0) and (d > 29 or d < 1):                
                return False
            elif (d > 28 or d < 1):
                return False

        else:
            if (m == 4 or m == 6 or m == 9 or m == 11) and (d > 30 or d < 1):
                return False
            else:
                if (d > 31 or d < 1):
                    return False
        
        return True
    

lines = stdin.read().splitlines()

counter = int(lines[0])

for i in range(1, counter + 1):
    d, m, y = (lines[i].split(" "))
    
    s = d + m + y 

    d, m, y = int(d), int(m), int(y)

    all_permutations = permutations(s)

    count = 0

    a = []

    for perm in all_permutations:
        lperm = list(perm)
        
        d, m, y = int(''.join(lperm[:2])), int(''.join(lperm[2:4])), int(''.join(lperm[4:]))
        
        if (isValid(d, m, y)):
            count += 1

            heapq.heappush(a, int(str(d) + str(m) + str(y)))

    print(len(a))
