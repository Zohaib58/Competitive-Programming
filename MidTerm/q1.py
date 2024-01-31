from sys import stdin
import math

lines = stdin.read().splitlines()

res = 1

for string in lines:
    for alpha in string:
        if alpha == 'A':
            if res == 1:
                res = 2
            elif res == 2:
                res = 1
            else:
                res = 3

        elif alpha == 'B':
            if res == 1:
                res = 1
            elif res == 2:
                res = 3
            else:
                res = 2

        elif alpha != 'B' and alpha != 'A':
            if res == 1:
                res = 3
            elif res == 2:
                res = 2
            else:
                res = 1

print(res)
