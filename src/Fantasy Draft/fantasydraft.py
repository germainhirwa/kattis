import sys; input = sys.stdin.readline
from heapq import *
n, k = map(int, input().split()); pm = []
for _ in range(n):
    _, *p = input().strip().split()
    pm.append({e:70000*(i-len(p)) for i,e in enumerate(p)})
t = [input().strip() for _ in range(int(input()))]; r = {e:i for i,e in enumerate(t)}
ans = [[] for _ in range(n)]; h = [False]*len(t); tbl = [[] for _ in range(n)]
for i in range(n):
    for j in range(len(t)):
        tbl[i].append(((pm[i][t[j]] if t[j] in pm[i] else 0)+j, r[t[j]]))
    heapify(tbl[i])
for _ in range(k):
    for i in range(n):
        while True:
            _, b = heappop(tbl[i])
            if h[b]: continue
            h[b] = True; ans[i].append(t[b]); break
for s in ans: print(*s)