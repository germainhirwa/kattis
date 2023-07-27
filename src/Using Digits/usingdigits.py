import sys; input = sys.stdin.readline
from heapq import *
C, R = map(int, input().split())
K = int(input()[::-1]); F = K
M = [[*map(int, input().strip())] for _ in range(R)][::-1]

delta = ((1, 0), (0, 1)); D = {}
D[(0, 0, K)] = M[0][0]
pq = [(M[0][0], 0, 0, K)]
while pq:
    dd, rr, cc, kk = heappop(pq)
    if dd == D[(rr, cc, kk)]:
        hop = kk%10
        for dr, dc in delta:
            if 0<=rr+dr<R and 0<=cc+dc<C:
                nn = (rr+dr, cc+dc, kk)
                if nn not in D or D[nn] > dd+M[nn[0]][nn[1]]: D[nn] = dd+M[nn[0]][nn[1]]; heappush(pq, (D[nn], *nn))
            if hop and 0<=rr+dr*(hop+1)<R and 0<=cc+dc*(hop+1)<C:
                nn = (rr+dr*(hop+1), cc+dc*(hop+1), kk//10)
                if nn not in D or D[nn] > dd+M[nn[0]][nn[1]]: D[nn] = dd+M[nn[0]][nn[1]]; heappush(pq, (D[nn], *nn))
best = 1e9
while True:
    if (R-1, C-1, F) in D: best = min(best, D[(R-1, C-1, F)])
    if F == 0: break
    F //= 10
print(best)