from collections import defaultdict
import sys
D, A = defaultdict(lambda: -1), [-1]
x, y = 0, 0
path = []
build, t = [(1, 1), (-1, 0)], 0
while len(path) < 10000:
    path.extend(build)
    nxt = [(a, -b) for a, b in build[::-1]]
    nxt.insert(len(nxt)//2, (0, -1)), path.extend(nxt)
    build = [(1, 1), *((-a, -b) for a, b in nxt), (-1, 0)]
ctr = {i:0 for i in range(1, 6)}
for dx, dy in path:
    s = set(range(1, 6))
    for nx, ny in ((x, y-1), (x, y+1), (x-1,y+1-x%2), (x-1, y-x%2), (x+1,y+1-x%2), (x+1, y-x%2)): s.discard(D[(nx, ny)])
    mv = min(ctr[i] for i in s); v = min(i for i in s if ctr[i]==mv)
    D[(x, y)] = v; A.append(v); ctr[v] += 1
    x += dx; y += dy
input()
for l in sys.stdin: print(A[int(l)])