import sys; input = sys.stdin.readline
from array import array
n, c = int(input()), [*map(int, input().split())][::-1]
m = c[0]+c[1]
gdp = array('i', [0]*m); odp = array('i', [10**7]*m)
for i in c: odp[i] = 1
for i in range(1, m):
    for j in c:
        if i >= j: break
    gdp[i] = gdp[i-j] + 1
    for j in c:
        if i > j and odp[i] > (x:=odp[i-j]+1): odp[i] = x
    if odp[i] < gdp[i]: print('non-canonical'), exit(0)
print('canonical')