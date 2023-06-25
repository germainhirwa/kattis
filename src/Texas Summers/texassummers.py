from heapq import *
import sys
input()
s = [[*map(int, l.split())] for l in sys.stdin]
D = [1e10]*len(s)
D[-2] = 0
pq, p = [(0, len(s)-2)], [-1]*len(s)
while pq:
    dd, vv = heappop(pq)
    if vv == len(s)-1: break
    if dd == D[vv]:
        x1, y1 = s[vv]
        for nn in range(len(s)):
            if nn == vv: continue
            x2, y2 = s[nn]
            dd2 = dd + (x1-x2)**2 + (y1-y2)**2
            if D[nn] > dd2:
                D[nn] = dd2
                heappush(pq, (D[nn], nn))
                p[nn] = vv
f = [p[len(s)-1]]
while f[-1] != -1: f.append(p[f[-1]])
if f[-1] == -1: f.pop()
if f[-1] == len(s)-2: f.pop()
if not f: print('-')
while f: print(f.pop())