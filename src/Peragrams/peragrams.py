import sys

for line in sys.stdin:
    d = {}
    for l in line:
        d[l] = d.get(l,0)+1
    print(max(0,len(list(filter(lambda x: x % 2 == 1,d.values())))-1))