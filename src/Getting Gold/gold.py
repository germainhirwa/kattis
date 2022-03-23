import sys

c, r = map(int, input().split())
m = []
for line in sys.stdin:
    m.append(list(line.strip()))

g = {}
gold = set()
deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))
for i in range(1, r - 1):
    for j in range(1, c - 1):
        pos = c*i + j
        if m[i][j] == 'P':
            s = pos
        if m[i][j] not in ['#', 'T']:
            sense = False
            for dr, dc in deltas:
                if m[i + dr][j + dc] == 'T':
                    sense = True
                    break
            if not sense:
                for dr, dc in deltas:
                    dest = c*(i + dr) + (j + dc)
                    if m[i + dr][j + dc] not in ['#', 'T']:
                        if pos not in g:
                            g[pos] = set()
                        g[pos].add(dest)

from collections import deque
q = deque([s])
vis = {s}
while q:
    u = q.popleft()
    if u in g:
        for v in g[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
                if m[v // c][v % c] == 'G':
                    gold.add(v)
print(len(gold))