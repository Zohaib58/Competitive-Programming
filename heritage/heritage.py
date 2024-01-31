from sys import stdin

def get_heritage(word, a, memo):
    if word in a:
        return a[word]
    else:
        

lines = stdin.read().splitlines()



a = {}
memo = {}

ctr, word = lines[0].split(" ")

ctr = int(ctr)

for i in range(1, ctr):
    ln = lines[i]

    key, val = ln.split(" ")
    val = int(val)

    a[key] = val

get_heritage(word, a, memo)

