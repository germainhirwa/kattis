import sys
from heapq import *

def transform(s):
    cvt = {
        'R': 64,
        'O': 32,
        'Y': 16,
        'G': 8,
        'B': 4,
        'I': 2,
        'V': 1
    }
    for i in cvt:
        s = s.replace(i, str(cvt[i]))
    return s

n, m = map(int, input().split())
g = {}
for line in sys.stdin:
    l1, l2, d, c = map(int, transform(line).split())
    l1 -= 1
    l2 -= 1
    for _ in range(2):
        for i in range(128):
            if 128*l1 + i not in g:
                g[128*l1 + i] = {}
            g[128*l1 + i][128*l2 + i|c] = d
        l1, l2 = l2, l1

D = [float('inf')] * (128 * n)
D[0] = 0
pq = [(0, 0)]

while pq:
    dd, vv = heappop(pq)
    if dd == D[vv] and vv in g:
        for nn in g[vv]:
            if D[nn] > dd + g[vv][nn]:
                D[nn] = dd + g[vv][nn]
                heappush(pq, (D[nn], nn))

print(D[127])