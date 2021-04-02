import sys

x = {}
y = {}
xi = []
yi = []

first_line = False
for line in sys.stdin:
    if not first_line:
        first_line = True
        n = int(line)
    else:
        a,b = list(map(int,line.split(" ")))
        x[a] = x.get(a,0)+1
        y[b] = y.get(b,0)+1
        xi.append(a)
        yi.append(b)

ans = 0
for i in range(n):
    ans += (x[xi[i]]-1)*(y[yi[i]]-1)

print(ans)