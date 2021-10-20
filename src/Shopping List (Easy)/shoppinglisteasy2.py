import sys

d = {}
fl = True
sl = True
for line in sys.stdin:
    if fl:
        n,m = list(map(int,line.split()))
        fl = False
    elif sl:
        things = line.strip().split()
        for t in things:
            d[t] = 1
        sl = False
    else:
        things = line.strip().split()
        for t in things:
            if t in d:
                d[t] += 1
    
result = sorted(list(filter(lambda x:x[1]==n,d.items())))
print(len(result))
for r in result:
    print(r[0])