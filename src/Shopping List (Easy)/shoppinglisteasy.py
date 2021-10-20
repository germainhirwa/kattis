import sys

d = {}
for line in sys.stdin:
    try:
        n,m = list(map(int,line.split()))
    except:
        things = line.strip().split()
        for t in things:
            d[t] = d.get(t,0)+1
    
result = sorted(list(map(lambda x:x[0],filter(lambda x:x[1]==n,d.items()))))
print(len(result))
for r in result:
    print(r)