import sys; input = sys.stdin.readline
from bisect import *
n = int(input())
c = []
for _ in range(n): a, b = map(int, input().split()); c.append(a), c.append(b-0.5)
c.append(b), c.append(1e10)
p, x = int(input()), {*map(int, input().split())}
u = [0]*(n+1)
for i in x:
    b = bisect_left(c, i)
    if b == 0 and c[0] != i: continue
    if b % 2: u[b//2] += 1
    elif b == 0: u[0] += 1
    else:
        if c[b-1] == i-0.5: u[b//2-1] += 1
        if c[b] == i: u[b//2] += 1
ans = []
for i in range(n-1):
    pc1, pc2 = int(c[2*i+1]+0.5), c[2*i+2]
    if pc1 == pc2 and pc1 not in x and u[i] < 2 and u[i+1] < 2: u[i] += 1; u[i+1] += 1; ans.append(pc1), x.add(pc1)
for i in range(n):
    if u[i] > 1: continue
    for j in range(c[2*i]+1, int(c[2*i+1]+0.5)):
        if j not in x: ans.append(j), x.add(j); u[i] += 1; break
    if u[i] > 1: continue
    for j in range(j, int(c[2*i+1]+0.5)):
        if j not in x: ans.append(j), x.add(j); u[i] += 1; break
u.pop()
if min(u) == max(u) == 2: print(len(ans), *ans)
else: print('impossible')