from sys import stdin
from itertools import combinations

def outputs(line, p):
    length = len(p)
    toremove = set()

    for i in range(1, length + 1): # to generate combos - started from 1
        for combo in combinations(p, i):
            for pair in combo:
                toremove.add(pair[0])
                toremove.add(pair[1])

    print("avc")

line = input()

push = []
p = []

"""


"""
index = 0
for char in line:

    if char == '(':
        push.append(index)
    elif char == ')':
        p.append((push.pop(), index))

    index += 1

outputs(line, p)

